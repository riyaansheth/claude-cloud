"""Discovery stage: YellowPages "diamonds wholesale" listings for every diamond-trade city.

Writes one raw JSON per listing to raw/yp/<slug>.json (same schema as the research agents), so
ingest.py / build.py treat it like any other source. Kill-list gate #1 runs here: killed listings
are written as dropped records (is_diamond_trade=false) so the REPORT can count them.
Fetched pages are cached in progress.sqlite3 (table yp_pages) — re-runs don't re-fetch.

    python3 scripts/yp_discover.py [--pages 3] [--cities "Tulsa, OK" ...]
"""
import argparse
import json
import os
import re
import sqlite3
import time
from urllib.parse import quote_plus, urljoin

import requests
from bs4 import BeautifulSoup

from common import DB_PATH, RAW_DIR, kill_reason, now_iso

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Safari/537.36")
CA = "/root/.ccr/ca-bundle.crt"
BASE = "https://www.yellowpages.com"
TERMS = ["diamonds wholesale"]
# Categories that make a YP listing a diamond-trade candidate (verbatim YP category names).
TRADE_CATS = {"Diamonds-Wholesale", "Diamond Cutters", "Diamond Brokers", "Diamond Buyers",
              "Jewelers-Wholesale & Manufacturers"}
NAME_DIAMOND = re.compile(r"diamond|gem|carat|brilliant", re.I)

# US diamond-trade cities: the cluster markets plus every metro with a real wholesale / bourse /
# importer presence. Market strings are "City, ST".
CITIES = [
    "New York, NY", "Los Angeles, CA", "Miami, FL", "Chicago, IL", "Boston, MA", "Philadelphia, PA",
    "Dallas, TX", "Houston, TX", "Atlanta, GA", "San Francisco, CA", "Seattle, WA", "Las Vegas, NV",
    "Southfield, MI", "Minneapolis, MN", "Denver, CO", "San Diego, CA", "Washington, DC", "Charlotte, NC",
    "Phoenix, AZ", "Scottsdale, AZ", "San Juan, PR", "Fort Lauderdale, FL", "Boca Raton, FL", "Orlando, FL",
    "Tampa, FL", "Jacksonville, FL", "Austin, TX", "San Antonio, TX", "Fort Worth, TX", "El Paso, TX",
    "New Orleans, LA", "Nashville, TN", "Memphis, TN", "Saint Louis, MO", "Kansas City, MO",
    "Cleveland, OH", "Columbus, OH", "Cincinnati, OH", "Pittsburgh, PA", "Baltimore, MD", "Richmond, VA",
    "Raleigh, NC", "Indianapolis, IN", "Milwaukee, WI", "Louisville, KY", "Oklahoma City, OK", "Tulsa, OK",
    "Salt Lake City, UT", "Portland, OR", "Sacramento, CA", "San Jose, CA", "Fresno, CA", "Irvine, CA",
    "Beverly Hills, CA", "Pasadena, CA", "Glendale, CA", "Honolulu, HI", "Albuquerque, NM", "Tucson, AZ",
    "Omaha, NE", "Birmingham, AL", "Buffalo, NY", "Rochester, NY", "Hartford, CT", "Providence, RI",
    "Iselin, NJ", "Edison, NJ", "Hackensack, NJ", "Great Neck, NY", "White Plains, NY", "Stamford, CT",
    "Durham, NC", "Bethesda, MD", "Rockville, MD", "Boise, ID", "Anchorage, AK", "Des Moines, IA",
    "Little Rock, AR", "Charleston, SC", "Savannah, GA", "Palm Beach, FL", "Naples, FL", "Sarasota, FL",
]

SCHEMA = """CREATE TABLE IF NOT EXISTS yp_pages (
    url TEXT PRIMARY KEY, status INTEGER, html TEXT, fetched_at TEXT)"""


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:80]


def fetch(con, url):
    row = con.execute("SELECT status, html FROM yp_pages WHERE url=?", (url,)).fetchone()
    if row and row[0] == 200:
        return row[1]
    for attempt in range(3):
        try:
            r = requests.get(url, headers={"User-Agent": UA}, timeout=25,
                             verify=CA if os.path.exists(CA) else True)
        except requests.RequestException:
            time.sleep(4 * (attempt + 1))
            continue
        if r.status_code in (429, 503):
            time.sleep(10 * (attempt + 1))
            continue
        con.execute("INSERT OR REPLACE INTO yp_pages VALUES (?,?,?,?)",
                    (url, r.status_code, r.text if r.ok else "", now_iso()))
        con.commit()
        time.sleep(1.5)
        return r.text if r.ok else ""
    return ""


def text(node):
    return node.get_text(" ", strip=True) if node else ""


def parse(html, market, page_url):
    soup = BeautifulSoup(html, "lxml")
    out = []
    for c in soup.select("div.result"):
        a = c.select_one("a.business-name")
        if not a:
            continue
        cats = [text(x) for x in c.select(".categories a")]
        web = c.select_one("a.track-visit-website")
        website = web.get("href", "") if web else ""
        if "localsearch.com" in website or "yellowpages.com" in website:
            website = ""
        locality = text(c.select_one(".locality"))
        m = re.match(r"(.+?),\s*([A-Z]{2})\b", locality)
        rating = c.select_one(".result-rating")
        stars = ""
        if rating:
            cls = " ".join(rating.get("class", []))
            word = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
            mm = re.search(r"\b(one|two|three|four|five)\b(\s+half)?", cls)
            if mm:
                stars = str(word[mm.group(1)] + (0.5 if mm.group(2) else 0)).rstrip("0").rstrip(".")
        reviews = re.sub(r"\D", "", text(c.select_one(".count")))
        out.append(dict(
            business=text(a), category_as_listed=", ".join(cats), cats=cats,
            phone=text(c.select_one("div.phones")) or text(c.select_one(".phone")),
            website=website, address=text(c.select_one(".street-address")),
            city=m.group(1) if m else "", state=m.group(2) if m else "",
            market=market, rating=stars, reviews=reviews,
            source_url=urljoin(BASE, a.get("href", "")) or page_url,
        ))
    nxt = soup.select_one("a.next")
    return out, bool(nxt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, default=3)
    ap.add_argument("--cities", nargs="*")
    args = ap.parse_args()
    con = sqlite3.connect(DB_PATH)
    con.execute(SCHEMA)
    outdir = RAW_DIR / "yp"
    outdir.mkdir(parents=True, exist_ok=True)
    kept = dropped = skipped = 0
    for market in args.cities or CITIES:
        for term in TERMS:
            for page in range(1, args.pages + 1):
                url = (f"{BASE}/search?search_terms={quote_plus(term)}"
                       f"&geo_location_terms={quote_plus(market)}" + (f"&page={page}" if page > 1 else ""))
                html = fetch(con, url)
                if not html:
                    break
                rows, more = parse(html, market, url)
                for r in rows:
                    cats = set(r.pop("cats"))
                    trade = bool(cats & {"Diamonds-Wholesale", "Diamond Cutters", "Diamond Brokers"}) or (
                        bool(cats & TRADE_CATS) and NAME_DIAMOND.search(r["business"]))
                    if not trade:
                        skipped += 1          # not a diamond-trade listing — never written
                        continue
                    kr = kill_reason(r["business"], r["category_as_listed"])
                    rec = dict(r, lead_origin="YellowPages", email="", email_source="", linkedin_url="",
                               linkedin_source="", contact_person="", role="", contact_source="",
                               tel_numbers=[], tel_source="", socials=[], building="", suite="",
                               trade_memberships=[], hooks=[],
                               is_diamond_trade=not kr, drop_reason=kr,
                               scope_reason=f"YellowPages categories: {r['category_as_listed']}")
                    m = re.search(r"\b(?:Ste|Suite|Unit|#|Rm|Room)\s*([\w-]+)", r["address"], re.I)
                    if m:
                        rec["suite"] = f"Ste {m.group(1)}"
                    fn = outdir / f"{slug(r['business'])}--{slug(r['city'] or market)}.json"
                    fn.write_text(json.dumps(rec, indent=1))
                    dropped += bool(kr)
                    kept += not kr
                if not more:
                    break
        print(f"{market}: running kept={kept} dropped={dropped} non-trade-skipped={skipped}", flush=True)


if __name__ == "__main__":
    main()
