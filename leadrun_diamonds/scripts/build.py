"""Stage 2: build diamonds_all.csv / diamonds_qualified.csv / REPORT.md from progress.sqlite3.

- kill-list gate #2 right before a row is written
- union-find dedupe on email / phone / website domain / normalised name+market, with the
  shared-building guard (address never merges; a phone or email shared by listings in
  different suites or with different websites is a switchboard and does not merge)
- 2-of-3 qualification (email, personal LinkedIn, direct/mobile tel: from own site/socials)
Pure function of the DB: re-running produces identical output (no duplicate rows).
"""
import csv
import json
import re
import sqlite3
from collections import Counter, defaultdict

from common import (COLUMNS, CORE_COLUMNS, DB_PATH, LEAD_ORIGINS, RUN_DIR, SEGMENT, classify_email,
                    clean_linkedin, host_of, is_role_email, is_toll_free, kill_reason,
                    linkedin_is_personal, norm_name, phone_digits, root_url, site_domain)

SOCIAL_HOSTS = ("facebook.com", "instagram.com", "x.com", "twitter.com", "tiktok.com",
                "linkedin.com", "youtube.com", "pinterest.com")
FREE_MAIL = ("gmail.com", "yahoo.com", "hotmail.com", "aol.com", "outlook.com", "icloud.com",
             "msn.com", "live.com", "me.com", "verizon.net", "optonline.net", "comcast.net")
MEMBERSHIP_CANON = [
    ("DDC", r"\bddc\b|diamond dealers club"), ("DMIA", r"\bdmia\b|manufacturers (&|and) importers"),
    ("JBT", r"\bjbt\b|jewelers board of trade"), ("RapNet", r"rapnet|rapaport"), ("IDEX", r"\bidex\b"),
    ("AGS", r"\bags\b|american gem society"), ("AGTA", r"\bagta\b"), ("GIA", r"\bgia\b"),
    ("IGI", r"\bigi\b"), ("HRD", r"\bhrd\b"), ("Bourse", r"bourse|wfdb"), ("JA", r"jewelers of america"),
    ("Polygon", r"polygon"), ("NDC", r"natural diamond council"), ("DCA", r"diamond council of america"),
    ("MJSA", r"\bmjsa\b"), ("JVC", r"\bjvc\b|jewelers vigilance"), ("IJO", r"\bijo\b"),
    ("Kimberley Process", r"kimberley"), ("RJC", r"\brjc\b|responsible jewellery council"),
]


def canon_memberships(items):
    out = []
    for it in items:
        for name, rx in MEMBERSHIP_CANON:
            if re.search(rx, str(it), re.I) and name not in out:
                out.append(name)
    return out


def as_list(v):
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    return [x.strip() for x in str(v or "").split(",") if x.strip()]


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


def load(con):
    rows = con.execute("SELECT listing_key, data, status, drop_reason, drop_stage, found_at FROM listings "
                       "ORDER BY listing_key").fetchall()
    crawl = {}
    if con.execute("SELECT 1 FROM sqlite_master WHERE name='crawl'").fetchone():
        for key, emails, tels, socials in con.execute(
                "SELECT listing_key, emails, tels, socials FROM crawl WHERE status='ok'"):
            crawl[key] = (json.loads(emails), json.loads(tels), json.loads(socials))
    keep, dropped, invalid = [], [], []
    for key, data, status, reason, stage, found_at in rows:
        rec = json.loads(data)
        rec["_key"], rec["_found_at"] = key, found_at
        # site-crawl results (scripts/crawl.py): harvested from the business's own pages only
        c_emails, c_tels, c_socials = crawl.get(key, ({}, [], []))
        rec["_own_tels"] = c_tels
        rec["socials"] = as_list(rec.get("socials")) + c_socials
        if classify_email(rec.get("email", ""))[1] != "ok" and c_emails:
            best = sorted(c_emails, key=lambda e: (is_role_email(e), e))[0]
            rec["email"], rec["email_source"] = best, c_emails[best]
        if status == "keep":
            # kill-list gate #2 (builder) — catches anything that slipped past discovery
            r2 = kill_reason(rec.get("business", ""), rec.get("category_as_listed", ""))
            site = (rec.get("website") or "") + " " + rec.get("business", "")
            if not r2 and re.search(r"pearl", site, re.I) and not re.search(r"diamond", site, re.I):
                r2 = "gemstone-only"  # pearl house with no diamond line in its name/domain
            if r2:
                dropped.append((rec, r2, "builder"))
                continue
            keep.append(rec)
        elif status == "dropped":
            dropped.append((rec, reason, stage or "discovery"))
        else:
            invalid.append((rec, reason))
    return keep, dropped, invalid


def prep(rec):
    """Normalise one listing in place."""
    rec["_name_n"] = norm_name(rec.get("business", ""))
    rec["_market"] = (rec.get("market") or "").strip()
    rec["_phone_d"] = phone_digits(rec.get("phone", ""))
    email, est = classify_email(rec.get("email", ""))
    rec["_email"], rec["_email_status"] = email, est
    rec["_domain"] = site_domain(rec.get("website", ""))
    rec["_suite"] = re.sub(r"\W", "", (rec.get("suite") or "").lower())
    rec["_building"] = norm_name(rec.get("building") or "")


def shared_values(recs, field):
    """Values of `field` that appear on listings with conflicting suites or website domains."""
    groups = defaultdict(list)
    for r in recs:
        if r[field]:
            groups[r[field]].append(r)
    shared = set()
    for val, rs in groups.items():
        if len(rs) < 2:
            continue
        doms = {r["_domain"] for r in rs if r["_domain"]}
        names = {r["_name_n"] for r in rs}
        suites = {(r["_building"], r["_suite"]) for r in rs if r["_suite"]}
        if len(doms) > 1 or (len(suites) > 1 and len(names) > 1):
            shared.add(val)
    return shared


def dedupe(recs):
    uf = UF(len(recs))
    shared_phone = shared_values(recs, "_phone_d")
    shared_email = {e for e in shared_values(recs, "_email")}
    index = defaultdict(list)
    for i, r in enumerate(recs):
        if r["_email"] and r["_email_status"] == "ok" and r["_email"] not in shared_email:
            index[("e", r["_email"])].append(i)
        if r["_phone_d"] and r["_phone_d"] not in shared_phone:
            index[("p", r["_phone_d"])].append(i)
        if r["_domain"]:
            index[("d", r["_domain"])].append(i)
        if r["_name_n"]:
            index[("n", r["_name_n"], r["_market"].lower())].append(i)
    for idxs in index.values():
        for j in idxs[1:]:
            uf.union(idxs[0], j)
    clusters = defaultdict(list)
    for i in range(len(recs)):
        clusters[uf.find(i)].append(recs[i])
    return list(clusters.values()), shared_phone


def completeness(r):
    fields = ["phone", "email", "linkedin_url", "contact_person", "website", "address", "category_as_listed",
              "suite", "role"]
    return (sum(bool(str(r.get(f) or "").strip()) for f in fields)
            + len(as_list(r.get("tel_numbers"))) * 0.1 + len(as_list(r.get("trade_memberships"))) * 0.1)


def own_source(src, website, socials):
    """True only if EVERY URL cited as the tel source is the business's own site or a social page."""
    urls = re.findall(r"https?://[^\s,;()]+", src or "")
    return bool(urls) and all(_own_host(u, website) for u in urls)


def _own_host(url, website):
    h = host_of(url)
    if not h:
        return False
    dom = site_domain(website)
    if dom and (h == dom or h.endswith("." + dom)):
        return True
    return any(h == s or h.endswith("." + s) for s in ("facebook.com", "instagram.com", "x.com",
                                                        "twitter.com", "tiktok.com"))


def merge_cluster(cluster, shared_phone):
    cluster = sorted(cluster, key=lambda r: (-completeness(r), r["_key"]))
    base = dict(cluster[0])
    others = cluster[1:]
    for o in others:
        for f in ("category_as_listed", "phone", "website", "address", "city", "state", "rating", "reviews",
                  "building", "suite"):
            if not str(base.get(f) or "").strip() and str(o.get(f) or "").strip():
                base[f] = o[f]
        if base["_email_status"] != "ok" and o["_email_status"] == "ok":
            base["email"], base["email_source"] = o["email"], o.get("email_source", "")
            base["_email"], base["_email_status"] = o["_email"], "ok"
        if not clean_linkedin(base.get("linkedin_url")) and clean_linkedin(o.get("linkedin_url")):
            for f in ("linkedin_url", "linkedin_source", "contact_person", "role", "contact_source"):
                base[f] = o.get(f, "")
        elif not base.get("contact_person") and o.get("contact_person"):
            for f in ("contact_person", "role", "contact_source"):
                base[f] = o.get(f, "")
    # union list fields; tel numbers only count when harvested from the business's own site/socials
    tels, socials, mems, hooks = [], [], [], []
    for r in [base] + others:
        rs = as_list(r.get("socials"))
        socials += rs
        if own_source(r.get("tel_source", ""), r.get("website", "") or base.get("website", ""), rs):
            tels += as_list(r.get("tel_numbers"))
        tels += r.get("_own_tels", [])
        mems += as_list(r.get("trade_memberships"))
        hooks += [h.lower() for h in as_list(r.get("hooks"))]
    base["_tels"], base["_socials"] = tels, list(dict.fromkeys(socials))
    base["_mems"], base["_hooks"] = canon_memberships(mems + hooks), list(dict.fromkeys(hooks))
    base["_others"] = others
    base["_shared_phone"] = base["_phone_d"] in shared_phone if base.get("_phone_d") else False
    return base


def mobile_candidates(main_d, tels):
    seen, cands = set(), []
    for t in tels:
        d = phone_digits(t)
        if d and d != main_d and d not in seen:
            seen.add(d)
            cands.append(d)
    # most-likely-mobile first: not toll-free, not on the main line's exchange, then the rest
    cands.sort(key=lambda d: (is_toll_free(d), bool(main_d) and d[:6] == main_d[:6]))
    return cands


def fmt(d):
    return f"({d[:3]}) {d[3:6]}-{d[6:]}"


def build_row(b):
    email_ok = b["_email_status"] == "ok"
    li = clean_linkedin(b.get("linkedin_url"))
    person = " ".join((b.get("contact_person") or "").split())
    li_ok = bool(li) and linkedin_is_personal(li, b.get("business", ""), person)
    cands = mobile_candidates(b["_phone_d"], b["_tels"])
    phone_from_site = False
    if not b["_phone_d"] and cands:
        # no directory-listed main line: the site's first local number IS the main line, not a direct one
        main = next((d for d in cands if not is_toll_free(d)), cands[0])
        b["_phone_d"], b["phone"], phone_from_site = main, fmt(main), True
        cands = [d for d in cands if d != main]
    # a number on the main line's exchange within a few digits of it is a fax / rollover, not a direct line
    def adjacent(d):
        m = b["_phone_d"]
        return bool(m) and d[:6] == m[:6] and abs(int(d[6:]) - int(m[6:])) <= 5
    direct_ok = any(not is_toll_free(d) and not adjacent(d) for d in cands)
    score = email_ok + li_ok + direct_ok

    signals = [f"{score} of 3"]
    if email_ok and is_role_email(b["_email"]):
        signals.append("role-email")
    if direct_ok:
        signals.append("direct-line")
    hooks, mems = b["_hooks"], b["_mems"]
    if "GIA" in mems or any("gia" in h for h in hooks):
        signals.append("gia")
    if "AGS" in mems:
        signals.append("ags")
    for h in hooks:
        m = re.search(r"since[- ]?(1[89]\d\d|20[0-2]\d)", h)
        if m and f"since-{m.group(1)}" not in signals:
            signals.append(f"since-{m.group(1)}")
    for tag in ("3rd-generation", "4th-generation", "2nd-generation", "family-owned", "lab-grown", "natural",
                "melee", "large-stones", "manufacturer", "importer", "cutter", "broker", "rough"):
        if any(tag in h for h in hooks):
            signals.append(tag)
    for m in mems:
        if m in ("DDC", "DMIA", "RapNet", "IDEX", "JBT", "Bourse", "AGTA") and m.lower() not in signals:
            signals.append(m.lower())

    match = "Both" if email_ok and li_ok else "Email" if email_ok else "LinkedIn" if li_ok else "Neither"

    flags = []
    if not (b.get("address") or "").strip():
        flags.append("no-address")
    if b["_phone_d"] and is_toll_free(b["_phone_d"]):
        flags.append("toll-free")
    if kill_reason(b.get("business", "")) == "chain":
        flags.append("chain")
    if b["_email_status"] in ("placeholder", "invalid"):
        flags.append("placeholder-email")
    if b["_shared_phone"]:
        flags.append("shared-switchboard")
    if phone_from_site:
        flags.append("phone-from-site")
    if b.get("lead_origin") == "YellowPages" and not b.get("verified"):
        flags.append("scope-unverified")  # in scope on YP's self-assigned category only
    if li and not li_ok:
        flags.append("linkedin-rejected")
    if email_ok and b["_email"].split("@")[1] in FREE_MAIL:
        flags.append("freemail")

    others = b["_others"]
    also = list(dict.fromkeys(o["business"] for o in others if norm_name(o["business"]) != b["_name_n"]))
    other_mk = list(dict.fromkeys(o["_market"] for o in others if o["_market"] and o["_market"] != b["_market"]))
    origin = b.get("lead_origin") or ""
    if origin not in LEAD_ORIGINS:
        origin = "Web Search"
    bs = ", ".join(x for x in [b.get("building", "").strip(),
                               (b.get("suite") or "").strip()] if x)

    row = {
        "Business": b["business"].strip(), "Segment": SEGMENT,
        "Category (as listed)": b.get("category_as_listed", ""),
        "Phone": (b.get("phone") or "").strip(),
        "Email": b["_email"] if email_ok else "",
        "LinkedIn Profile": li if li_ok else "",
        "Contact Person": person, "Role": b.get("role", "") if person else "",
        "Website": root_url(b.get("website", "")),
        "Address": (b.get("address") or "").strip(),
        "Real City": b.get("city", ""), "Real State": (b.get("state") or "").upper()[:2],
        "Market": b["_market"], "Lead Origin": origin,
        "Rating": b.get("rating", ""), "Reviews": re.sub(r"\D", "", str(b.get("reviews") or "")),
        "Source": b["source_url"], "Signals": ", ".join(signals), "Match Type": match,
        "Email Source": b.get("email_source", "") if email_ok else "",
        "LinkedIn Source": (b.get("linkedin_source") or li) if li_ok else "",
        "Found At": b["_found_at"],
        "Also Listed As": ", ".join(also), "Other Markets": ", ".join(other_mk),
        "Merged Listings": len(others), "Flags": ", ".join(flags),
        "Mobile Candidates": ", ".join(fmt(d) for d in cands),
        "Socials": ", ".join(s for s in b["_socials"] if any(h in s for h in SOCIAL_HOSTS)),
        "Building / Suite": bs, "Trade Memberships": ", ".join(mems),
    }
    # Flags must be populated whenever a condition holds — assert, don't trust.
    assert ("no-address" in row["Flags"]) == (not row["Address"]), row["Business"]
    assert ("shared-switchboard" in row["Flags"]) == b["_shared_phone"], row["Business"]
    assert row["Source"].startswith("http"), row["Business"]
    return row, score, (email_ok, li_ok, direct_ok)


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)


def main():
    con = sqlite3.connect(DB_PATH)
    keep, dropped, invalid = load(con)
    for r in keep:
        prep(r)
    clusters, shared_phone = dedupe(keep)
    built = []
    for c in clusters:
        b = merge_cluster(c, shared_phone)
        built.append((b,) + build_row(b))
    built.sort(key=lambda t: (-t[2], t[1]["Market"], t[1]["Business"].lower()))
    all_rows = [t[1] for t in built]
    qual_rows = [t[1] for t in built if t[2] >= 2]
    write_csv(RUN_DIR / "diamonds_all.csv", all_rows)
    write_csv(RUN_DIR / "diamonds_qualified.csv", qual_rows)
    with open(RUN_DIR / "dropped_out_of_scope.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Business", "Market", "Reason", "Stage", "Source", "Why"])
        for rec, reason, stage in sorted(dropped, key=lambda t: (t[1], t[0].get("business", ""))):
            w.writerow([rec.get("business", ""), rec.get("market", ""), reason, stage,
                        rec.get("source_url", ""), rec.get("scope_reason", "")])

    if all_rows:
        flagged = sum(bool(r["Flags"]) for r in all_rows)
        need = sum((not r["Address"]) or bool(r["Flags"]) for r in all_rows)
        assert flagged == need, "Flags column came out empty where conditions hold"
    assert list(all_rows[0].keys())[:26] == CORE_COLUMNS if all_rows else True

    write_report(keep, dropped, invalid, built, all_rows, qual_rows)
    print(f"listings kept={len(keep)} dropped={len(dropped)} invalid={len(invalid)} "
          f"unique={len(all_rows)} qualified={len(qual_rows)}")


def pct(n, d):
    return f"{(100 * n / d):.0f}%" if d else "—"


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def write_report(keep, dropped, invalid, built, all_rows, qual_rows):
    n_all, n_q = len(all_rows), len(qual_rows)
    L = ["# Diamond trade lead run — REPORT", ""]
    L.append(f"Generated by `scripts/build.py` at {built[0][0]['_found_at'][:10] if built else ''}; "
             "numbers below are computed from `progress.sqlite3`, not typed in.\n")
    L.append("## Headline\n")
    L.append(table(["Metric", "Count"], [
        ["Listings researched (raw records ingested)", len(keep) + len(dropped) + len(invalid)],
        ["…in scope after kill-list (both gates)", len(keep)],
        ["…dropped out of scope", len(dropped)],
        ["…invalid (no name / no source URL)", len(invalid)],
        ["Unique businesses after dedupe (diamonds_all.csv)", n_all],
        ["Listings folded in by dedupe", sum(r["Merged Listings"] for r in all_rows)],
        ["Qualified 2-of-3 (diamonds_qualified.csv)", n_q],
        ["…of which 3 of 3", sum(t[2] == 3 for t in built)],
        ["Pass rate (qualified / unique)", pct(n_q, n_all)],
    ]))
    tri = Counter()
    for t in built:
        e, l, d = t[3]
        tri["email"] += e
        tri["linkedin"] += l
        tri["direct"] += d
    L.append("\n## Qualification criteria hit (unique businesses)\n")
    L.append(table(["Criterion", "Businesses", "Rate"], [
        ["Real email", tri["email"], pct(tri["email"], n_all)],
        ["Personal LinkedIn (/in/, named human)", tri["linkedin"], pct(tri["linkedin"], n_all)],
        ["Direct/mobile tel: ≠ main line, own site/socials", tri["direct"], pct(tri["direct"], n_all)],
    ]))
    L.append("\n## Fill rate per field\n")
    fr = []
    for c in COLUMNS:
        a = sum(bool(str(r[c]).strip()) and str(r[c]) != "0" for r in all_rows)
        q = sum(bool(str(r[c]).strip()) and str(r[c]) != "0" for r in qual_rows)
        fr.append([c, f"{a}/{n_all} ({pct(a, n_all)})", f"{q}/{n_q} ({pct(q, n_q)})"])
    L.append(table(["Column", "all.csv", "qualified.csv"], fr))

    def breakdown(title, keyf):
        ca, cq = Counter(), Counter()
        for r in all_rows:
            ca[keyf(r)] += 1
        for r in qual_rows:
            cq[keyf(r)] += 1
        L.append(f"\n## {title}\n")
        L.append(table([title.split(" ")[-1].title(), "Researched", "Qualified"],
                       [[k or "(none)", v, cq[k]] for k, v in ca.most_common()]))

    breakdown("Per market", lambda r: r["Market"])
    breakdown("Per city", lambda r: f"{r['Real City']}, {r['Real State']}".strip(", "))
    breakdown("Per building", lambda r: r["Building / Suite"].split(",")[0].strip())
    breakdown("Per source", lambda r: r["Lead Origin"])

    mem = Counter()
    for r in all_rows:
        for m in as_list(r["Trade Memberships"]):
            mem[m] += 1
    L.append("\n## Trade-membership counts (unique businesses)\n")
    L.append(table(["Membership", "Businesses"], mem.most_common()) if mem else "None captured.")

    dr = Counter((reason, stage) for _, reason, stage in dropped)
    L.append("\n## dropped_out_of_scope (by reason)\n")
    L.append(table(["Reason", "Gate", "Dropped"], [[r, s, n] for (r, s), n in dr.most_common()])
             if dr else "None.")
    L.append("\nPer-business detail: `dropped_out_of_scope.csv`.")
    if invalid:
        L.append("\n## Invalid worker records (not shipped)\n")
        L.append(table(["Listing", "Reason"], [[r.get("business", "?"), why] for r, why in invalid]))
    flags = Counter(f for r in all_rows for f in as_list(r["Flags"]))
    L.append("\n## Flags\n")
    L.append(table(["Flag", "Rows"], flags.most_common()) if flags else "No flags.")

    notes = RUN_DIR / "RUN_NOTES.md"
    if notes.exists():
        L.append("\n" + notes.read_text())
    (RUN_DIR / "REPORT.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
