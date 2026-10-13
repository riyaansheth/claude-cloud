"""Site crawl — concurrent plain-HTTP workers, one job per website domain.

For each domain fetch /, /about, /about-us, /contact, /team, /our-story (+ a few
jeweler-specific paths and any same-site link whose text says about/team/story/
meet). Extract: mailto + regex + Cloudflare-obfuscated emails, ALL tel: numbers,
social URLs, names near owner/founder/president/gemologist/master jeweler,
JSON-LD founder/address, and jewelry signals (GIA/AGS/JA, since-19xx, on-site
bench, custom design). Results are stored per domain in progress.sqlite3.
"""
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from . import config, db, scope
from .http import fetch, Blocked
from .util import (EMAIL_RX, abs_url, clean_email, decode_cfemail, domain_of,
                   email_status, extract_people, jsonld_blocks, now_iso, norm_social,
                   phone_digits, SOCIAL_RX, visible_text)

SIGNAL_RX = {
    "gia": re.compile(r"\bGIA\b|Gemological Institute of America|Graduate Gemologist|\bG\.G\.", re.I),
    "ags": re.compile(r"American Gem Society|\bAGS\b", re.I),
    "ja": re.compile(r"Jewelers of America", re.I),
    "bench": re.compile(r"on[- ]site (?:bench|jeweler|goldsmith|repair|workshop)|in[- ]house (?:jeweler|goldsmith|repair|workshop|bench)|bench jeweler|master jeweler|goldsmith on (?:site|premises)", re.I),
    "custom-design": re.compile(r"custom (?:design|jewelry|engagement|made)|bespoke|CAD design|design your own", re.I),
}
SINCE_RX = re.compile(r"\b(?:since|est\.?|established(?: in)?|founded(?: in)?|serving [\w\s]{0,30} since)\s*(19\d{2}|20[0-2]\d)\b", re.I)
SUBPAGE_HINT = re.compile(r"about|our[- ]story|team|meet|staff|owner|history|contact|who[- ]we[- ]are", re.I)
FAX_CONTEXT = re.compile(r"fax", re.I)


def parse_page(html, url):
    soup = BeautifulSoup(html, "lxml")
    out = {"emails": [], "placeholders": [], "tels": [], "socials": [], "links": [],
           "title": "", "desc": "", "h1": "", "jsonld": []}
    out["title"] = (soup.title.get_text(" ").strip() if soup.title else "")[:300]
    md = soup.find("meta", attrs={"name": "description"})
    out["desc"] = (md.get("content", "") if md else "")[:500]
    h1 = soup.find("h1")
    out["h1"] = h1.get_text(" ").strip()[:200] if h1 else ""
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        low = href.lower()
        if low.startswith("mailto:"):
            out["emails"].append(clean_email(href))
        elif low.startswith("tel:"):
            # Only the link text and the text immediately before it ("Fax: <a>").
            prev = a.find_previous(string=True)
            label = a.get_text(" ") + " " + (str(prev)[-20:] if prev else "")
            if not FAX_CONTEXT.search(label):
                d = phone_digits(href)
                if d:
                    out["tels"].append(d)
        elif low.startswith("http") or low.startswith("/"):
            full = abs_url(url, href)
            if SOCIAL_RX.match(full):
                out["socials"].append(norm_social(full))
            elif SUBPAGE_HINT.search(href + " " + a.get_text(" ")):
                out["links"].append(full)
    for el in soup.select("[data-cfemail]"):
        e = decode_cfemail(el["data-cfemail"])
        if e:
            out["emails"].append(clean_email(e))
    for d in jsonld_blocks(soup):
        keep = {k: d.get(k) for k in ("@type", "name", "email", "telephone", "address",
                                       "founder", "foundingDate", "sameAs", "employee")
                if d.get(k)}
        if keep:
            out["jsonld"].append(keep)
            for k in ("email",):
                if isinstance(d.get(k), str):
                    out["emails"].append(clean_email(d[k]))
            same = d.get("sameAs") or []
            for s in same if isinstance(same, list) else [same]:
                if isinstance(s, str) and SOCIAL_RX.match(s):
                    out["socials"].append(norm_social(s))
    text = visible_text(soup)
    raw_emails = set(EMAIL_RX.findall(text)) | set(EMAIL_RX.findall(html))
    out["emails"].extend(clean_email(e) for e in raw_emails)
    out["text"] = text
    return out


def crawl_domain(root, business_name, max_extra=4):
    """Crawl one site. Returns the result dict stored in crawls.result."""
    res = {"root": root, "pages": {}, "emails": {}, "placeholder_emails": [],
           "tels": {}, "socials": [], "people": [], "signals": [], "since": "",
           "meta": {}, "about_text": "", "about_url": "", "jsonld": [], "errors": []}
    host = urlparse(root).hostname
    queue = [root.rstrip("/") + p for p in config.CRAWL_PATHS]
    seen = set()
    extra_added = 0
    while queue:
        url = queue.pop(0)
        key = url.rstrip("/").lower()
        if key in seen:
            continue
        seen.add(key)
        try:
            status, final, html = fetch(url, min_gap=0.8, timeout=20, retries=1)
        except Blocked:
            raise
        except Exception as e:  # noqa: BLE001
            res["errors"].append(f"{url}: {type(e).__name__}")
            if url.rstrip("/") == root.rstrip("/"):
                break  # site down: don't hammer sub-paths
            continue
        if status != 200 or domain_of(final) != domain_of(root):
            res["pages"][url] = status
            continue
        res["pages"][url] = 200
        p = parse_page(html, final)
        if url.rstrip("/") == root.rstrip("/"):
            res["meta"] = {"title": p["title"], "desc": p["desc"], "h1": p["h1"]}
        for e in p["emails"]:
            st = email_status(e)
            if st == "ok":
                res["emails"].setdefault(e, final)
            elif st == "placeholder" and e not in res["placeholder_emails"]:
                res["placeholder_emails"].append(e)
        for t in p["tels"]:
            res["tels"].setdefault(t, final)
        for s in p["socials"]:
            if s not in res["socials"]:
                res["socials"].append(s)
        res["jsonld"].extend(p["jsonld"])
        for name, role, snippet in extract_people(p["text"], business_name):
            if name not in [x["name"] for x in res["people"]]:
                res["people"].append({"name": name, "role": role, "url": final,
                                      "evidence": snippet})
        for tag, rx in SIGNAL_RX.items():
            if tag not in res["signals"] and rx.search(p["text"]):
                res["signals"].append(tag)
        m = SINCE_RX.search(p["text"])
        if m and (not res["since"] or m.group(1) < res["since"]):
            res["since"] = m.group(1)
        if re.search(r"about|story|meet|team|owner", url, re.I) and len(p["text"]) > len(res["about_text"]):
            res["about_text"], res["about_url"] = p["text"][:6000], final
        for link in p["links"]:
            if (urlparse(link).hostname == host and extra_added < max_extra
                    and link.rstrip("/").lower() not in seen):
                queue.append(link.split("#")[0])
                extra_added += 1
    for d in res["jsonld"]:
        f = d.get("founder")
        for item in f if isinstance(f, list) else [f]:
            nm = item.get("name") if isinstance(item, dict) else item
            if isinstance(nm, str) and nm.strip() and nm not in [x["name"] for x in res["people"]]:
                res["people"].append({"name": nm.strip(), "role": "Founder",
                                      "url": root, "evidence": "JSON-LD founder"})
    return res


def run(workers=16, limit=None, log=print):
    con = db.connect()
    rows = con.execute("""
        SELECT l.website, MIN(l.name) AS name FROM listings l
        LEFT JOIN crawls c ON c.domain = l.website
        WHERE l.website != '' AND c.domain IS NULL
        GROUP BY l.website""").fetchall()
    todo = [(r["website"], r["name"]) for r in rows]
    if limit:
        todo = todo[:limit]
    log(f"[crawl] {len(todo)} sites to crawl with {workers} workers")
    done = blocked = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(crawl_domain, root, name): root for root, name in todo}
        for fut in as_completed(futs):
            root = futs[fut]
            try:
                res = fut.result()
                status = "ok" if any(v == 200 for v in res["pages"].values()) else "unreachable"
            except Blocked as e:
                blocked += 1
                db.log_event(con, "crawl", "egress-blocked", f"{root}: {e}")
                continue  # leave uncrawled so a later run retries it
            except Exception as e:  # noqa: BLE001
                res, status = {"errors": [str(e)]}, "error"
            con.execute("INSERT OR REPLACE INTO crawls VALUES (?,?,?,?,?,?)",
                        (root, root, status, json.dumps(res.get("pages", {})),
                         json.dumps(res, ensure_ascii=False), now_iso()))
            _apply_site_scope(con, root, res)
            _store_people(con, root, res)
            done += 1
            if done % 100 == 0:
                log(f"[crawl] {done}/{len(todo)} done ({blocked} blocked)")
    log(f"[crawl] finished: {done} crawled, {blocked} blocked")
    return {"crawled": done, "blocked": blocked}


def _apply_site_scope(con, root, res):
    """Kill-list on what the site plainly sells (title / meta description / h1)."""
    meta = res.get("meta") or {}
    reason = scope.site_kill_reason(meta.get("title", ""), meta.get("desc", ""), meta.get("h1", ""))
    if not reason:
        return
    for r in con.execute("SELECT * FROM listings WHERE website=?", (root,)).fetchall():
        db.drop(con, r["bkey"], r["name"], r["category"], r["market"], r["origin"],
                reason, "site-check", root)


def _store_people(con, root, res):
    for r in con.execute("SELECT bkey FROM listings WHERE website=?", (root,)).fetchall():
        for p in res.get("people", []):
            db.add_person(con, r["bkey"], p["name"], p["role"], p["url"],
                          "site-regex" if p["evidence"] != "JSON-LD founder" else "site-jsonld",
                          p["evidence"])
