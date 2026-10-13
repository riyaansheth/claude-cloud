"""Builder: listings + crawl/social/people/LinkedIn evidence -> CSVs + REPORT.md.

Order of operations (all inside this script, never a manual pass):
  1. kill-list pass #2 on every listing (+ site check), segment or drop
  2. per-listing evidence assembly (email, people, LinkedIn, tel: numbers)
  3. union-find dedupe on email / phone digits / website domain / name+market
     (shared platform hosts and shared switchboards excluded as keys)
  4. merge: keep the most complete row, fill blanks, write columns 23-25
  5. qualification (2 of 3), Signals, Match Type, Flags (column 26)
  6. kill-list pass #3 immediately before the row is written; schema asserts
Deterministic: same DB in, byte-identical CSVs out (Found At = discovery time).
"""
import csv
import json
import re
from collections import Counter, defaultdict

from . import config, db, scope
from .util import (LOW_VALUE_LOCALS, domain_of, is_us_number, email_relates, email_status, fmt_phone, is_role_email,
                   is_shared_host, is_toll_free, name_tokens, now_iso, parse_city_state,
                   phone_digits, state_from_zip)

ROLE_ORDER = ["Owner", "President", "Founder", "Partner", "Member", "Manager",
              "Featured On About Page"]
METHOD_ORDER = ["bbb-profile", "site-jsonld", "agent-about", "site-regex"]
CORE_FIELDS = ["Phone", "Email", "LinkedIn Profile", "Contact Person", "Website",
               "Address", "Real City", "Real State", "Rating", "Reviews"]


def norm_name(n):
    n = (n or "").lower().replace("&", " and ")
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = re.sub(r"\b(the|inc|llc|ltd|co|corp|company)\b", " ", n)
    n = re.sub(r"\bjewell?ers?\b|\bjewell?ery\b|\bjewelry\b", "jewelry", n)
    return re.sub(r"\s+", " ", n).strip()


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)


def _load(con):
    listings = [dict(r) for r in con.execute("SELECT * FROM listings ORDER BY bkey")]
    crawls = {r["root"]: json.loads(r["result"]) for r in
              con.execute("SELECT root, result FROM crawls WHERE status='ok'")}
    socials = {r["url"]: json.loads(r["result"]) for r in
               con.execute("SELECT url, result FROM socials WHERE status='ok'")}
    people = defaultdict(list)
    from .util import plausible_name
    for r in con.execute("SELECT * FROM people ORDER BY bkey, name"):
        # Names stored by an older crawl are re-checked with the current rule.
        if r["method"] == "site-regex" and not plausible_name(r["name"], need_given=True):
            continue
        people[r["bkey"]].append(dict(r))
    linked = defaultdict(list)
    for r in con.execute("SELECT * FROM linkedin WHERE status='match'"):
        linked[r["bkey"]].append(dict(r))
    return listings, crawls, socials, people, linked


def _pick_email(lst, crawl, socials_res, site_dom):
    """Return (email, source_url, placeholder_seen)."""
    cands = []  # (rank, email, src)
    extra = json.loads(lst.get("extra") or "{}")
    if extra.get("email") and email_status(extra["email"]) == "ok":
        cands.append((1, extra["email"].lower(), lst["source_url"]))
    for e, src in (crawl or {}).get("emails", {}).items():
        cands.append((0, e, src))
    for sres in socials_res:
        for e, src in sres.get("emails", {}).items():
            cands.append((2, e, src))
    good = []
    toks = [t for t in name_tokens(lst["name"]) if len(t) >= 3]
    # Own-domain mail counts only when that domain is recognisably this business's
    # (a retailer page about a designer brand carries the retailer's inbox).
    trust_dom = site_dom if (not toks or domain_relates(site_dom, toks)) else ""
    for rank, e, src in cands:
        if email_status(e) != "ok" or not email_relates(e, trust_dom, lst["name"]):
            continue
        if e.rsplit("@", 1)[-1] in ASSOCIATION_DOMAINS:
            continue
        own = site_dom and e.endswith("@" + site_dom)
        # Prefer own-domain named inbox, then own-domain role inbox, then others.
        low = e.split("@")[0] in LOW_VALUE_LOCALS
        good.append(((1 if low else 0), (0 if own else 1), (1 if is_role_email(e) else 0), rank, e, src))
    placeholder = bool((crawl or {}).get("placeholder_emails"))
    if not good:
        return "", "", placeholder
    good.sort()
    return good[0][4], good[0][5], placeholder


def _pick_person(plist, links):
    """Contact = the person with a verified LinkedIn if any, else best role/method."""
    if links:
        lk = sorted(links, key=lambda x: x["person"])[0]
        p = next((p for p in plist if p["name"] == lk["person"]), None)
        return lk["person"], (p or {}).get("role", ""), lk["url"], lk["search_url"]
    if not plist:
        return "", "", "", ""
    best = sorted(plist, key=lambda p: (
        ROLE_ORDER.index(p["role"]) if p["role"] in ROLE_ORDER else 9,
        METHOD_ORDER.index(p["method"]) if p["method"] in METHOD_ORDER else 9, p["name"]))[0]
    return best["name"], best["role"] or "Featured On About Page", "", ""


def site_is_business(lst, crawl):
    """The listed website must actually be this business's own site. Directory or
    association pages (e.g. a trade group's member page) carry someone else's
    emails and phone numbers. Trusted when the domain or the homepage title/h1
    carries a distinctive token of the business name, or the name has none."""
    dom = domain_of(lst["website"])
    if dom in ASSOCIATION_DOMAINS:
        return False
    toks = [t for t in name_tokens(lst["name"]) if len(t) >= 3]
    if not toks or not crawl:
        return True
    if domain_relates(dom, toks):
        return True
    m = crawl.get("meta") or {}
    head = f"{m.get('title', '')} {m.get('h1', '')}".lower()
    return all(re.search(rf"\b{re.escape(t)}", head) for t in toks)


ASSOCIATION_DOMAINS = {"agta.org", "plumbclub.com", "jewelers.org", "americangemsociety.org",
                       "gia.edu", "jbt.org", "jvclegal.org", "ijo.com", "rjoonline.com",
                       "centurionjewelry.com", "jckonline.com", "nationaljeweler.com"}


def domain_relates(dom, toks):
    label = dom.split(".")[0] if dom else ""
    return any(t in label for t in toks)


def assemble(lst, crawl, socials_map, plist, links):
    if crawl and not site_is_business(lst, crawl):
        crawl = None
        plist = [p for p in plist if not p["method"].startswith("site")]
    site_dom = domain_of(lst["website"]) if lst["website"] else ""
    soc_urls = list((crawl or {}).get("socials", []))
    extra = json.loads(lst.get("extra") or "{}")
    for s in extra.get("socials") or []:
        if s.startswith("http") and s not in soc_urls:
            soc_urls.append(s.rstrip("/"))
    soc_res = [socials_map[u] for u in soc_urls if u in socials_map]
    email, email_src, placeholder = _pick_email(lst, crawl, soc_res, site_dom)
    person, role, li_url, li_src = _pick_person(plist, links)
    tels = dict((crawl or {}).get("tels", {}))
    for sres in soc_res:
        for t, src in sres.get("tels", {}).items():
            tels.setdefault(t, src)
    city, state = lst.get("city") or "", (lst.get("state") or "").upper()
    if not city and lst.get("address"):
        city, state2 = parse_city_state(lst["address"])
        state = state or state2
    if (not city or not lst.get("address")) and crawl:
        for d in crawl.get("jsonld", []):
            a = d.get("address")
            if isinstance(a, list):
                a = a[0] if a else {}
            if isinstance(a, dict) and a.get("addressLocality"):
                city = city or a.get("addressLocality", "")
                state = state or (a.get("addressRegion") or "")[:2].upper()
                if not lst.get("address") and a.get("streetAddress"):
                    lst["address"] = ", ".join(x for x in (a["streetAddress"], a["addressLocality"],
                                               f"{a.get('addressRegion', '')} {a.get('postalCode', '')}".strip()) if x)
                break
    if not state and lst.get("zip"):
        state = state_from_zip(lst["zip"])
    tags = list((crawl or {}).get("signals", []))
    if extra.get("trade") == "ags" and "ags" not in tags:
        tags.append("ags")
    if extra.get("trade") == "ja" and "ja" not in tags:
        tags.append("ja")
    since = (crawl or {}).get("since") or extra.get("bbb_years") or ""
    return {
        "_bkey": lst["bkey"], "_site_dom": site_dom, "_tels": tels, "_tags": tags,
        "_since": since, "_placeholder": placeholder, "_socials": soc_urls,
        "Business": lst["name"], "Segment": lst["segment"],
        "Category (as listed)": lst["category"], "Phone": lst["phone"] or "",
        "Email": email, "LinkedIn Profile": li_url, "Contact Person": person, "Role": role,
        "Website": lst["website"] or "", "Address": lst.get("address") or "",
        "Real City": city, "Real State": state, "Market": lst["market"],
        "Lead Origin": lst["origin"], "Rating": lst.get("rating") or "",
        "Reviews": lst.get("reviews") or "", "Source": lst["source_url"],
        "Email Source": email_src, "LinkedIn Source": li_src,
        "Found At": lst["discovered_at"],
    }


def dedupe(rows):
    """Union-find over reachable-contact keys. Returns list of groups (lists of rows)."""
    phone_names = defaultdict(set)
    phone_doms = defaultdict(set)
    for r in rows:
        d = phone_digits(r["Phone"])
        if d:
            phone_names[d].add(norm_name(r["Business"]))
            if r["_site_dom"]:
                phone_doms[d].add(r["_site_dom"])
    # Same number on 3+ differently named businesses with 2+ different websites:
    # a building/mall switchboard, not a business identity.
    shared_phones = {d for d in phone_names
                     if len(phone_names[d]) >= 3 and len(phone_doms[d]) >= 2}
    uf = UF(len(rows))
    first = {}
    for i, r in enumerate(rows):
        keys = []
        if r["Email"]:
            keys.append("e:" + r["Email"].lower())
        d = phone_digits(r["Phone"])
        if d and d not in shared_phones:
            keys.append("p:" + d)
        if r["_site_dom"] and not is_shared_host(r["_site_dom"]):
            keys.append("d:" + r["_site_dom"])
        nn = norm_name(r["Business"])
        if nn:
            keys.append(f"n:{nn}|{r['Market']}")
        for k in keys:
            if k in first:
                uf.union(first[k], i)
            else:
                first[k] = i
    groups = defaultdict(list)
    for i, r in enumerate(rows):
        groups[uf.find(i)].append(r)
    return list(groups.values()), shared_phones


def completeness(r):
    return sum(1 for f in CORE_FIELDS if r.get(f))


def merge(group):
    group = sorted(group, key=lambda r: (-completeness(r), r["Found At"], r["_bkey"]))
    base = dict(group[0])
    for other in group[1:]:
        for f in CORE_FIELDS + ["Email Source", "LinkedIn Source", "Role"]:
            if not base.get(f) and other.get(f):
                # Keep email/LinkedIn paired with their sources and person with role.
                if f == "Email":
                    base["Email"], base["Email Source"] = other["Email"], other["Email Source"]
                elif f == "LinkedIn Profile":
                    for g in ("LinkedIn Profile", "LinkedIn Source", "Contact Person", "Role"):
                        base[g] = other[g]
                elif f == "Contact Person":
                    base["Contact Person"], base["Role"] = other["Contact Person"], other["Role"]
                elif f in ("Email Source", "LinkedIn Source", "Role"):
                    continue
                else:
                    base[f] = other[f]
        for t, src in other["_tels"].items():
            base["_tels"].setdefault(t, src)
        base["_tags"] = sorted(set(base["_tags"]) | set(other["_tags"]))
        base["_socials"] = base["_socials"] + [s for s in other["_socials"] if s not in base["_socials"]]
        base["_since"] = min(x for x in (base["_since"], other["_since"]) if x) if (base["_since"] or other["_since"]) else ""
        base["_placeholder"] = base["_placeholder"] or other["_placeholder"]
    seen_names = {base["Business"].lower()}
    also = []
    for o in group[1:]:
        if o["Business"].lower() not in seen_names:
            seen_names.add(o["Business"].lower())
            also.append(o["Business"])
    base["Also Listed As"] = ", ".join(also)
    base["Other Markets"] = ", ".join(sorted({o["Market"] for o in group} - {base["Market"]}))
    base["Merged Listings"] = len(group) - 1
    base["_group_phones"] = {phone_digits(o["Phone"]) for o in group if phone_digits(o["Phone"])}
    base["_addresses"] = {re.sub(r"\W", "", o["Address"].lower())[:20] for o in group if o["Address"]}
    base["_markets"] = {o["Market"] for o in group}
    base["_members"] = [o["_bkey"] for o in group]
    return base


def compute_flags(r, shared_phones):
    flags = []
    if not r["Address"]:
        flags.append("no-address")
    if is_toll_free(r["Phone"]):
        flags.append("toll-free")
    if len(r["_addresses"]) >= 3 or (len(r["_markets"]) >= 3 and len(r["_addresses"]) >= 2):
        flags.append("chain")
    if r["_placeholder"] and not r["Email"]:
        flags.append("placeholder-email")
    if phone_digits(r["Phone"]) in shared_phones:
        flags.append("shared-switchboard")
    return flags


DIRECTORY_PHONES = set()   # every directory-listed number in the run (set by build)


def qualify(r):
    main = phone_digits(r["Phone"])
    # A number that is some listing's directory phone (e.g. the same owner's other
    # store) is a published main line, not a private/direct one.
    directory = r["_group_phones"] | ({main} if main else set()) | DIRECTORY_PHONES
    mobiles = sorted(t for t in r["_tels"]
                     if t not in directory and not is_toll_free(t) and is_us_number(t))
    r["Mobile Candidates"] = ", ".join(fmt_phone(t) for t in mobiles)
    has_email = bool(r["Email"])
    has_li = bool(r["LinkedIn Profile"]) and "/in/" in r["LinkedIn Profile"]
    has_direct = bool(mobiles)
    n = has_email + has_li + has_direct
    tags = [f"{n} of 3"]
    if has_email and is_role_email(r["Email"]):
        tags.append("role-email")
    if has_direct:
        tags.append("direct-line")
    for t in ("gia", "ags", "ja", "bench", "custom-design"):
        if t in r["_tags"]:
            tags.append(t)
    if r["_since"]:
        tags.append(f"since-{r['_since']}")
    r["Signals"] = ", ".join(tags)
    if has_email and has_li:
        r["Match Type"] = "Both"
    elif has_email:
        r["Match Type"] = "Email"
    elif has_li:
        r["Match Type"] = "LinkedIn"
    else:
        r["Match Type"] = "None"
    r["Socials"] = ", ".join(r["_socials"])
    return n


def assert_schema(out_rows, shared_phones):
    for r in out_rows:
        assert list(r.keys()) == config.COLUMNS, "column order drift"
        assert r["Business"], "Business required"
        assert r["Source"].startswith("http"), f"missing Source for {r['Business']}"
        assert r["Segment"] in config.SEGMENTS, f"bad segment {r['Segment']}"
        assert r["Lead Origin"] in config.ORIGINS, f"bad origin {r['Lead Origin']}"
        assert not r["LinkedIn Profile"] or "linkedin.com/in/" in r["LinkedIn Profile"]
        assert "/company/" not in r["LinkedIn Profile"]
        assert not r["Email"] or email_status(r["Email"]) == "ok"
        assert not r["Email"] or r["Email Source"].startswith("http"), "email without source"
        assert not r["LinkedIn Profile"] or r["Contact Person"], "LinkedIn without a named human"
        for f in (r["Flags"].split(", ") if r["Flags"] else []):
            assert f in config.FLAG_VALUES, f"unknown flag {f}"
        assert "out-of-scope" not in r["Flags"], "out-of-scope row reached the writer"
        # Flags column must reflect reality — it has silently come out empty before.
        if not r["Address"]:
            assert "no-address" in r["Flags"], f"no-address flag missing: {r['Business']}"
        if is_toll_free(r["Phone"]):
            assert "toll-free" in r["Flags"], f"toll-free flag missing: {r['Business']}"
        if phone_digits(r["Phone"]) in shared_phones:
            assert "shared-switchboard" in r["Flags"]
        assert isinstance(r["Merged Listings"], int)


def build(log=print):
    con = db.connect()
    listings, crawls, socials_map, people, linked = _load(con)
    drops = Counter()
    rows = []
    pending = 0
    crawl_tried = {r["root"] for r in con.execute("SELECT root FROM crawls")}
    for lst in listings:
        crawl = crawls.get(lst["website"]) if lst["website"] else None
        extra = json.loads(lst.get("extra") or "{}")
        reason = scope.kill_reason(lst["name"], lst["category"], lst["address"], lst["market"],
                                   osm_tags=extra.get("tags"))
        if not reason and crawl:
            m = crawl.get("meta") or {}
            reason = scope.site_kill_reason(m.get("title", ""), m.get("desc", ""), m.get("h1", ""))
        site_text = ""
        if crawl:
            m = crawl.get("meta") or {}
            site_text = " ".join([m.get("title", ""), m.get("desc", ""), m.get("h1", ""),
                                  crawl.get("about_text", "")[:2000]])
        seg = None if reason else scope.classify_segment(lst["name"], lst["category"], site_text,
                                                         extra.get("tags"))
        if not reason and not seg:
            if lst["website"] and lst["website"] not in crawl_tried:
                pending += 1  # site may still settle the segment; decide after its crawl
                continue
            reason = "no-segment"
        if reason:
            db.drop(con, lst["bkey"], lst["name"], lst["category"], lst["market"], lst["origin"],
                    reason, "builder", lst["source_url"])
            drops[reason] += 1
            continue
        lst["segment"] = seg
        rows.append(assemble(lst, crawl, socials_map, people.get(lst["bkey"], []),
                             linked.get(lst["bkey"], [])))
    DIRECTORY_PHONES.clear()
    DIRECTORY_PHONES.update(phone_digits(x["phone"]) for x in listings if phone_digits(x["phone"]))
    groups, shared_phones = dedupe(rows)
    out_all, out_q = [], []
    for g in groups:
        r = merge(g)
        # Final kill-list pass immediately before writing, over every merged name.
        names = [r["Business"]] + [n for n in r["Also Listed As"].split(", ") if n]
        reason = next((rs for rs in (scope.kill_reason(n, r["Category (as listed)"], r["Address"], r["Market"])
                                     for n in names) if rs), None)
        if reason:
            drops[reason] += 1
            for bkey in r["_members"]:
                db.log_event(con, "builder", "final-kill", f"{bkey}: {reason}")
            continue
        n = qualify(r)
        r["Flags"] = ", ".join(compute_flags(r, shared_phones))
        row = {c: r.get(c, "") for c in config.COLUMNS}
        out_all.append(row)
        if n >= 2:
            out_q.append(row)
    assert_schema(out_all, shared_phones)
    if len(out_all) >= 50:
        assert any(r["Flags"] for r in out_all), \
            "Flags column is empty on every row — builder flag logic is broken"
    order = {config.market_label(c, s): i for i, (c, s, _) in enumerate(config.MARKETS)}
    key = lambda r: (order.get(r["Market"], 99), r["Business"].lower(), r["Source"])
    out_all.sort(key=key)
    out_q.sort(key=key)
    for path, data in ((config.ALL_CSV, out_all), (config.QUALIFIED_CSV, out_q)):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=config.COLUMNS)
            w.writeheader()
            w.writerows(data)
    log(f"[build] {len(listings)} listings -> {len(out_all)} businesses, "
        f"{len(out_q)} qualified; dropped this pass: {dict(drops)}; "
        f"{pending} awaiting crawl for segment")
    from . import report
    report.write(con, out_all, out_q, len(listings))
    return {"listings": len(listings), "businesses": len(out_all), "qualified": len(out_q)}
