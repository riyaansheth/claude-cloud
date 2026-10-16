"""Discovery sources 2-5, browser-driven: Google Maps, YellowPages, BBB (with
profile pages — the best owner-name source), Jewelers of America / AGS member
directories.

Selectors target the live DOM as of 2026 and are deliberately defensive: if a
page shape changes the parser yields nothing and the run logs it, it never
guesses. Every listing carries the URL it was read from.
"""
import json
import re
import time
from urllib.parse import quote_plus, urljoin

from bs4 import BeautifulSoup

from . import config, db, scope
from .http import Blocked

# Seconds between BBB profile fetches; BBB 403s bursts, so a slower pace means fewer cooldowns.
import os as _os
BBB_GAP = float(_os.environ.get("BBB_GAP", "3"))
from .util import (domain_of, fmt_phone, parse_city_state, phone_digits, root_url, sha,
                   state_from_zip, plausible_name)


def ingest(con, rec, stats, stage="discovery"):
    if not rec.get("name") or db.is_dropped(con, rec["bkey"], stage_not="builder"):
        return
    reason = scope.kill_reason(rec["name"], rec.get("category", ""),
                               rec.get("address", ""), rec["market"])
    if reason:
        db.drop(con, rec["bkey"], rec["name"], rec.get("category", ""), rec["market"],
                rec["origin"], reason, stage, rec["source_url"])
        stats["dropped"] += 1
        return
    if rec.get("address") and not rec.get("city"):
        rec["city"], rec["state"] = parse_city_state(rec["address"])
    stats["new" if db.upsert_listing(con, rec) else "seen"] += 1


def _txt(el):
    return re.sub(r"\s+", " ", el.get_text(" ")).strip() if el else ""


# ---------------------------------------------------------------- Google Maps
def parse_gmaps_place(html, url, market):
    s = BeautifulSoup(html, "lxml")
    name = _txt(s.select_one("h1.DUwDvf, h1"))
    cat = _txt(s.select_one("button.DkEaL, button[jsaction*='category']"))
    addr_el = s.select_one("button[data-item-id='address']")
    address = (addr_el.get("aria-label", "").replace("Address:", "").strip()
               if addr_el else "")
    ph_el = s.select_one("button[data-item-id^='phone:tel:']")
    phone = ph_el["data-item-id"].split("tel:")[-1] if ph_el else ""
    web_el = s.select_one("a[data-item-id='authority']")
    website = web_el.get("href", "") if web_el else ""
    rating, reviews = "", ""
    rbox = s.select_one("div.F7nice")
    if rbox:
        m = re.search(r"(\d\.\d)", _txt(rbox))
        rating = m.group(1) if m else ""
        m = re.search(r"\(([\d,]+)\)", _txt(rbox))
        reviews = m.group(1).replace(",", "") if m else ""
    rating = rating[:-2] if rating.endswith(".0") else rating
    return {"bkey": "gmaps:" + sha(url.split("?")[0].split("/data=")[0]),
            "name": name, "category": cat, "phone": fmt_phone(phone) or phone,
            "website": root_url(website) if website and "google." not in website else "",
            "address": address, "market": market, "origin": "Google Maps",
            "rating": rating, "reviews": reviews, "source_url": url.split("?")[0]}


def run_gmaps(br, markets, log=print, max_places=120):
    con = db.connect()
    stats = {"new": 0, "seen": 0, "dropped": 0}
    for city, st, _ in markets:
        market = config.market_label(city, st)
        for q in config.GMAPS_QUERIES:
            task = f"gmaps:{market}:{q}"
            if db.task_done(con, task):
                continue
            url = f"https://www.google.com/maps/search/{quote_plus(q + ' ' + market)}?hl=en"
            try:
                html = br.get_html(url, wait_selector="a.hfpxzc", scroll=12)
            except Blocked as e:
                db.log_event(con, "gmaps", "blocked", e)
                log(f"[gmaps] blocked: {e}")
                return stats
            if br.last_status != 200:
                db.log_event(con, "gmaps", f"soft-block-{br.last_status}", url)
                continue
            links = []
            soup = BeautifulSoup(html, "lxml")
            for a in soup.select("a.hfpxzc[href*='/maps/place/']"):
                href = a["href"]
                if href not in links:
                    links.append(href)
            if not links and soup.select_one("h1.DUwDvf"):
                # Maps jumped straight to one place: keep it rather than lose it.
                place_url = br.page.url
                if "/maps/place/" in place_url:
                    ingest(con, parse_gmaps_place(html, place_url, market), stats)
            for href in links[:max_places]:
                try:
                    place = br.get_html(href, wait_selector="h1", min_gap=1.5)
                except Blocked as e:
                    db.log_event(con, "gmaps", "blocked", e)
                    return stats
                except Exception as e:  # noqa: BLE001
                    db.log_event(con, "gmaps", "error", f"{href}: {e}")
                    continue
                ingest(con, parse_gmaps_place(place, href, market), stats)
            db.mark_task(con, task, detail=str(len(links)))
            log(f"[gmaps] {market} / {q}: {len(links)} places; {stats}")
    return stats


# ---------------------------------------------------------------- YellowPages
def parse_yp(html, market, page_url):
    s = BeautifulSoup(html, "lxml")
    out = []
    for card in s.select("div.result"):
        a = card.select_one("a.business-name")
        if not a:
            continue
        href = urljoin("https://www.yellowpages.com", a.get("href", ""))
        cats = ", ".join(_txt(c) for c in card.select("div.categories a"))
        street = _txt(card.select_one(".street-address"))
        loc = _txt(card.select_one(".locality"))
        address = ", ".join(x for x in (street, loc) if x)
        web = card.select_one("a.track-visit-website")
        rating = ""
        rc = card.select_one("div.result-rating")
        if rc:
            words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5"}
            cls = [c for c in rc.get("class", []) if c in words]
            rating = words[cls[0]] + (".5" if "half" in rc.get("class", []) else "") if cls else ""
        reviews = re.sub(r"\D", "", _txt(card.select_one("span.count")))
        city, state = "", ""
        m = re.match(r"(.+?),\s*([A-Z]{2})\s*(\d{5})?", loc)
        if m:
            city, state = m.group(1), m.group(2)
        out.append({"bkey": "yp:" + sha(href.split("?")[0]), "name": _txt(a),
                    "category": cats, "phone": _txt(card.select_one(".phones")),
                    "website": root_url(web["href"]) if web and web.get("href") else "",
                    "address": address, "city": city, "state": state,
                    "market": market, "origin": "YellowPages", "rating": rating,
                    "reviews": reviews, "source_url": href.split("?")[0]})
    has_next = bool(s.select_one("a.next"))
    return out, has_next


def run_yp(br, markets, log=print, max_pages=30):
    con = db.connect()
    stats = {"new": 0, "seen": 0, "dropped": 0}
    for city, st, _ in markets:
        market = config.market_label(city, st)
        for term in config.YP_TERMS:
            for page in range(1, max_pages + 1):
                task = f"yp:{market}:{term}:{page}"
                if db.task_done(con, task):
                    continue
                url = (f"https://www.yellowpages.com/search?search_terms={quote_plus(term)}"
                       f"&geo_location_terms={quote_plus(market)}&page={page}")
                try:
                    html = br.get_html(url, wait_selector="div.result")
                except Blocked as e:
                    db.log_event(con, "yp", "blocked", e)
                    log(f"[yp] blocked: {e}")
                    return stats
                rows, has_next = parse_yp(html, market, url)
                if not rows and br.last_status != 200:
                    # Soft block (non-200 interstitial): don't record the page as done.
                    db.log_event(con, "yp", f"soft-block-{br.last_status}", url)
                    time.sleep(60)
                    break
                for r in rows:
                    ingest(con, r, stats)
                db.mark_task(con, task, detail=str(len(rows)))
                if not rows or not has_next:
                    break
            log(f"[yp] {market} / {term}: {stats}")
    return stats


# ---------------------------------------------------------------- BBB
def parse_bbb_search(html):
    s = BeautifulSoup(html, "lxml")
    links = []
    for a in s.select("a[href*='/profile/']"):
        href = urljoin("https://www.bbb.org", a["href"].split("?")[0])
        if "/addressId/" in href:
            href = href.split("/addressId/")[0]
        if href not in links:
            links.append(href)
    return links


def parse_bbb_profile(html, url, market):
    s = BeautifulSoup(html, "lxml")
    rec = {"bkey": "bbb:" + sha(url), "market": market, "origin": "BBB", "source_url": url}
    ld = {}
    for sc in s.find_all("script", type="application/ld+json"):
        try:
            d = json.loads(sc.string or "")
        except (ValueError, TypeError):
            continue
        for item in d if isinstance(d, list) else [d]:
            if isinstance(item, dict) and item.get("@type") in ("LocalBusiness", "Organization", "Store", "JewelryStore"):
                ld = item
    name = ld.get("name") or _txt(s.select_one("h1 #businessName, h1"))
    rec["name"] = re.sub(r"\s*\|.*$", "", name).strip()
    addr = ld.get("address") or {}
    if isinstance(addr, dict) and addr.get("streetAddress"):
        rec["address"] = ", ".join(x for x in (addr.get("streetAddress"), addr.get("addressLocality"),
                                               f"{addr.get('addressRegion', '')} {addr.get('postalCode', '')}".strip()) if x)
        rec["city"], rec["state"] = addr.get("addressLocality", ""), addr.get("addressRegion", "")
        rec["zip"] = addr.get("postalCode", "")
    rec["phone"] = ld.get("telephone", "") or _txt(s.select_one("a[href^='tel:']"))
    site = ld.get("url") or ""
    if "bbb.org" in site:
        site = ""   # JSON-LD url is BBB's own profile page, not the business site
    if not site:
        # The anchor holds an <svg> icon before the text, so match on get_text().
        a = next((a for a in s.select("a[href^='http']")
                  if re.search(r"visit website", a.get_text(" "), re.I)), None)
        site = a.get("href", "") if a else ""
    rec["website"] = root_url(site) if site and "bbb" not in domain_of(site) else ""
    # Category as BBB lists it (breadcrumb / "Business Categories").
    cats = [_txt(a) for a in s.select("a[href*='/category/']")]
    rec["category"] = cats[0] if cats else ""
    agg = ld.get("aggregateRating") or {}
    rec["rating"] = str(agg.get("ratingValue", "") or "")
    rec["reviews"] = str(agg.get("reviewCount", "") or "")
    # Business Management / principal contacts.
    people = []
    text = s.get_text("\n")
    m = re.search(r"(Business Management|Principal Contacts?|Customer Contacts?)\s*\n(.{0,800})", text, re.S)
    if m:
        block = m.group(2)
        for pm in re.finditer(r"(?:Mr\.|Ms\.|Mrs\.|Dr\.)?\s*([A-Z][a-zA-Z'\-]+(?:\s+[A-Z]\.)?\s+[A-Z][a-zA-Z'\-]+)\s*,\s*([A-Za-z /&\-]{3,40})", block):
            nm, role = pm.group(1).strip(), pm.group(2).strip()
            if plausible_name(nm, rec["name"]) and nm not in [p["name"] for p in people]:
                people.append({"name": nm, "role": role})
    rec["extra"] = {"bbb_people": people, "bbb_years": _bbb_years(text)}
    return rec


def _bbb_years(text):
    m = re.search(r"Business Started:\s*\n?\s*(\d{1,2}/\d{1,2}/(\d{4}))", text)
    return m.group(2) if m else ""


def _bbb_role(role):
    r = role.lower()
    for k, v in (("owner", "Owner"), ("president", "President"), ("ceo", "President"),
                 ("founder", "Founder"), ("partner", "Partner"), ("member", "Member"),
                 ("manager", "Manager")):
        if k in r:
            return v
    return "Owner" if "principal" in r else "Manager"


def run_bbb(br, markets, log=print, max_pages=15):
    con = db.connect()
    stats = {"new": 0, "seen": 0, "dropped": 0, "people": 0}
    strikes = 0
    for city, st, _ in markets:
        market = config.market_label(city, st)
        for cat in config.BBB_CATEGORIES:
            for page in range(1, max_pages + 1):
                task = f"bbb:{market}:{cat}:{page}"
                if db.task_done(con, task):
                    continue
                url = (f"https://www.bbb.org/search?find_country=USA&find_text={quote_plus(cat)}"
                       f"&find_loc={quote_plus(market)}&find_type=Category&page={page}")
                try:
                    links = parse_bbb_search(br.get_html(url, wait_selector="a[href*='/profile/']"))
                except Blocked as e:
                    db.log_event(con, "bbb", "blocked", e)
                    log(f"[bbb] blocked: {e}")
                    return stats
                if not links and br.last_status != 200:
                    db.log_event(con, "bbb", f"soft-block-{br.last_status}", url)
                    time.sleep(60)
                    break
                for href in links:
                    bkey = "bbb:" + sha(href)
                    if db.is_dropped(con, bkey) or con.execute(
                            "SELECT 1 FROM listings WHERE bkey=?", (bkey,)).fetchone():
                        continue
                    try:
                        rec = parse_bbb_profile(br.get_html(href, min_gap=BBB_GAP), href, market)
                        strikes = 0
                    except Blocked as e:
                        # BBB rate-limits bursts with 403s: back off, give up after 3 in a row.
                        db.log_event(con, "bbb", "blocked", e)
                        strikes += 1
                        if strikes >= 3:
                            log(f"[bbb] blocked 3x in a row, stopping: {e}")
                            return stats
                        time.sleep(90 * strikes)
                        continue
                    except Exception as e:  # noqa: BLE001
                        db.log_event(con, "bbb", "error", f"{href}: {e}")
                        continue
                    ingest(con, rec, stats)
                    if not db.is_dropped(con, bkey):
                        for p in rec["extra"]["bbb_people"]:
                            db.add_person(con, bkey, p["name"], _bbb_role(p["role"]), href,
                                          "bbb-profile", p["role"])
                            stats["people"] += 1
                db.mark_task(con, task, detail=str(len(links)))
                if not links:
                    break
            log(f"[bbb] {market} / {cat}: {stats}")
    return stats


# ---------------------------------------------------------------- trade directories
TRADE_DIRS = {
    # Jewelers of America "Find a Jeweler" and AGS "Find a Jeweler" locators.
    "ja": "https://www.jewelers.org/find-a-jeweler?location={loc}",
    "ags": "https://www.americangemsociety.org/find-a-jeweler/?location={loc}",
}


def parse_trade(html, base, market, which):
    """Generic member-card parser: any card holding a business name + a tel: link."""
    s = BeautifulSoup(html, "lxml")
    out = []
    for tel in s.select("a[href^='tel:']"):
        card = tel
        for _ in range(6):
            card = card.parent
            if card is None or card.find(["h2", "h3", "h4", "strong"]):
                break
        if card is None:
            continue
        name = _txt(card.find(["h2", "h3", "h4", "strong"]))
        if not name:
            continue
        web = next((a["href"] for a in card.select("a[href^='http']")
                    if "jewelers.org" not in a["href"] and "americangemsociety" not in a["href"]
                    and "google." not in a["href"]), "")
        addr = _txt(card.select_one("address, .address"))
        out.append({"bkey": f"{which}:" + sha(name + phone_digits(tel['href'])),
                    "name": name, "category": "AGS member" if which == "ags" else "JA member",
                    "phone": fmt_phone(tel["href"]), "website": root_url(web) if web else "",
                    "address": addr, "market": market, "origin": "Trade Directory",
                    "source_url": base, "extra": {"trade": which}})
    return out


def run_trade(br, markets, log=print):
    con = db.connect()
    stats = {"new": 0, "seen": 0, "dropped": 0}
    for city, st, _ in markets:
        market = config.market_label(city, st)
        for which, tmpl in TRADE_DIRS.items():
            task = f"trade:{which}:{market}"
            if db.task_done(con, task):
                continue
            url = tmpl.format(loc=quote_plus(market))
            try:
                html = br.get_html(url, wait_selector="a[href^='tel:']", scroll=3)
            except Blocked as e:
                db.log_event(con, "trade", "blocked", e)
                log(f"[trade] blocked: {e}")
                continue
            except Exception as e:  # noqa: BLE001
                db.log_event(con, "trade", "error", f"{url}: {e}")
                continue
            rows = parse_trade(html, url, market, which)
            for r in rows:
                ingest(con, r, stats)
            db.mark_task(con, task, detail=str(len(rows)))
            log(f"[trade] {which} {market}: {len(rows)} members; {stats}")
    return stats


def backfill_bbb_websites(log=print):
    """Fill missing BBB websites from cached profile pages (older parser missed
    the 'Visit Website' link). Cheap: cache only, no network."""
    from .http import cache_path
    con = db.connect()
    n = 0
    for r in con.execute("SELECT bkey, source_url, market FROM listings "
                         "WHERE origin='BBB' AND website=''").fetchall():
        p = cache_path("browser:" + r["source_url"])
        if not p.exists():
            continue
        site = parse_bbb_profile(p.read_text("utf-8", "replace"), r["source_url"], r["market"])["website"]
        if site:
            con.execute("UPDATE listings SET website=? WHERE bkey=?", (site, r["bkey"]))
            n += 1
    if n:
        log(f"[bbb] backfilled {n} websites from cached profiles")
    return n
