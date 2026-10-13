"""Stage 1b: crawl each in-scope business's OWN website for emails, tel: numbers, socials, names.

Run when the environment's egress policy allows the business sites (this session's policy
blocked them — see REPORT.md). Results go to progress.sqlite3 table `crawl`, keyed by
listing_key; already-crawled sites are skipped, so it resumes after an interrupt.

    python3 scripts/crawl.py [--workers 12] [--browser]

--browser fetches with headless Chromium (Playwright, real UA) for sites that 403 plain requests.
"""
import argparse
import json
import os
import re
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from common import DB_PATH, classify_email, host_of, now_iso, phone_digits, site_domain

PATHS = ["/", "/about", "/about-us", "/contact", "/contact-us", "/team", "/our-story",
         "/inventory", "/wholesale", "/trade"]
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Safari/537.36")
CA = "/root/.ccr/ca-bundle.crt"
EMAIL_TXT = re.compile(r"[A-Za-z0-9._%+'-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
TITLE_RX = re.compile(r"(owner|founder|co-founder|president|ceo|partner|principal|broker|"
                      r"graduate gemologist|gia gg|ddc member)", re.I)
FREE_MAIL = {"gmail.com", "yahoo.com", "hotmail.com", "aol.com", "outlook.com", "icloud.com", "msn.com"}
SOCIAL_RX = re.compile(r"https?://(www\.)?(facebook|instagram|x|twitter|tiktok)\.com/[^\s\"'<>]+", re.I)

SCHEMA = """CREATE TABLE IF NOT EXISTS crawl (
    listing_key TEXT PRIMARY KEY, website TEXT, status TEXT, emails TEXT, tels TEXT,
    socials TEXT, name_snippets TEXT, pages TEXT, crawled_at TEXT)"""


def fetch_requests(url):
    r = requests.get(url, headers={"User-Agent": UA}, timeout=20,
                     verify=CA if os.path.exists(CA) else True)
    return r.status_code, r.text if r.ok else ""


_browser = None


def fetch_browser(url):
    global _browser
    from playwright.sync_api import sync_playwright
    if _browser is None:
        _browser = sync_playwright().start().chromium.launch()
    page = _browser.new_page(user_agent=UA)
    try:
        resp = page.goto(url, timeout=30000, wait_until="domcontentloaded")
        return (resp.status if resp else 0), page.content()
    finally:
        page.close()


def extract(html, base):
    soup = BeautifulSoup(html, "lxml")
    emails, tels, socials, names = {}, [], [], []
    for a in soup.find_all("a", href=True):
        h = a["href"].strip()
        if h.lower().startswith("mailto:"):
            emails.setdefault(h[7:].split("?")[0].strip().lower(), base)
        elif h.lower().startswith("tel:"):
            d = phone_digits(h[4:])
            if d and d not in tels:
                tels.append(d)
        elif SOCIAL_RX.match(h):
            socials.append(h.split("?")[0])
    text = soup.get_text(" ", strip=True)
    for e in EMAIL_TXT.findall(text):
        emails.setdefault(e.lower(), base)
    for m in TITLE_RX.finditer(text):
        names.append(text[max(0, m.start() - 80): m.end() + 80])
    return emails, tels, socials, names[:12]


def crawl_one(key, website, use_browser):
    fetch = fetch_browser if use_browser else fetch_requests
    emails, tels, socials, names, pages = {}, [], [], [], []
    root = website.rstrip("/")
    for p in PATHS:
        url = root + p if p != "/" else root + "/"
        try:
            code, html = fetch(url)
        except Exception as exc:  # network / DNS / TLS — record and move on
            pages.append([url, f"ERR {type(exc).__name__}"])
            continue
        pages.append([url, code])
        if not html:
            continue
        e, t, s, n = extract(html, url)
        for k, v in e.items():
            emails.setdefault(k, v)
        tels += [x for x in t if x not in tels]
        socials += [x for x in s if x not in socials]
        names += n
    dom = site_domain(website)
    good = {}
    for e, src in emails.items():
        clean, st = classify_email(e)
        # accept only addresses on the business's own domain or a personal mailbox it publishes
        if st == "ok" and ((dom and clean.endswith("@" + dom)) or clean.split("@")[1] in FREE_MAIL):
            good[clean] = src
    ok_pages = sum(1 for _, c in pages if c == 200)
    return dict(listing_key=key, website=website, status="ok" if ok_pages else "unreachable",
                emails=json.dumps(good), tels=json.dumps(tels), socials=json.dumps(socials),
                name_snippets=json.dumps(names[:20]), pages=json.dumps(pages), crawled_at=now_iso())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--browser", action="store_true")
    ap.add_argument("--retry-unreachable", action="store_true")
    args = ap.parse_args()
    con = sqlite3.connect(DB_PATH)
    con.execute(SCHEMA)
    done = {k for k, s in con.execute("SELECT listing_key, status FROM crawl")
            if s == "ok" or not args.retry_unreachable}
    todo = []
    for key, data in con.execute("SELECT listing_key, data FROM listings WHERE status='keep'"):
        w = (json.loads(data).get("website") or "").strip()
        if w and key not in done and host_of(w):
            todo.append((key, w if "://" in w else "https://" + w))
    print(f"to crawl: {len(todo)}")
    workers = 1 if args.browser else args.workers  # playwright sync API is single-threaded
    with ThreadPoolExecutor(workers) as ex:
        futs = [ex.submit(crawl_one, k, w, args.browser) for k, w in todo]
        for f in as_completed(futs):
            r = f.result()
            con.execute("INSERT OR REPLACE INTO crawl VALUES (:listing_key,:website,:status,:emails,:tels,"
                        ":socials,:name_snippets,:pages,:crawled_at)", r)
            con.commit()
            print(r["status"], r["website"], len(json.loads(r["emails"])), "emails",
                  len(json.loads(r["tels"])), "tels")


if __name__ == "__main__":
    main()
