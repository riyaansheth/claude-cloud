"""Personal LinkedIn search — only AFTER an owner name is known.

`"<business>" site:linkedin.com/in/` measured 8 hits in 5,791 rows, so we search
the human: `"First Last" <city> site:linkedin.com/in/` (+ jeweler context), via
Bing then DuckDuckGo HTML. Never gated on whether an email was found.

A result is accepted automatically only when the /in/ slug or result title
carries BOTH first and last name and the title/snippet ties it to jewelry, the
business, or the city. Name-only hits go to the subagent judging queue.
"""
import re
from html import unescape as html_unescape
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote_plus, unquote, urlparse, parse_qs

from bs4 import BeautifulSoup

from . import db
from .http import fetch, Blocked
from .util import name_tokens, now_iso

IN_RX = re.compile(r"https?://(?:[a-z]{2,3}\.)?linkedin\.com/in/([A-Za-z0-9\-_%]+)", re.I)
JEWEL_CTX = re.compile(r"jewel|goldsmith|silversmith|gemolog|GIA|diamond|bench|watch", re.I)


def search_urls(person, city):
    q = f'"{person}" {city} site:linkedin.com/in/'
    q2 = f'"{person}" jeweler site:linkedin.com/in/'
    # (html.duckduckgo.com answers 403 to scripted requests, so Bing only)
    return [f"https://www.bing.com/search?q={quote_plus(q)}&setlang=en-US",
            f"https://www.bing.com/search?q={quote_plus(q2)}&setlang=en-US"]


def _bing_target(href):
    """Bing wraps results as /ck/a?...&u=a1<base64url(target)>."""
    import base64
    u = parse_qs(urlparse(html_unescape(href)).query).get("u", [""])[0]
    if u.startswith("a1"):
        b = u[2:]
        try:
            return base64.urlsafe_b64decode(b + "=" * (-len(b) % 4)).decode("utf-8", "replace")
        except ValueError:
            return ""
    return ""


def parse_results(html):
    """Yield (url, title, snippet) for every linkedin.com/in/ result."""
    soup = BeautifulSoup(html, "lxml")
    out = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "duckduckgo.com/l/" in href or href.startswith("//duckduckgo.com/l/"):
            href = unquote(parse_qs(urlparse(href).query).get("uddg", [""])[0])
        elif "bing.com/ck/a" in href or href.startswith("/ck/a"):
            href = _bing_target(href)
        m = IN_RX.match(href)
        if not m:
            continue
        url = f"https://www.linkedin.com/in/{m.group(1).rstrip('/')}"
        if any(u == url for u, _, _ in out):
            continue
        box = a.find_parent(["li", "div"])
        out.append((url, a.get_text(" ").strip(), box.get_text(" ")[:400] if box else ""))
    return out


def judge(person, business, city, url, title, snippet):
    """'match' | 'ambiguous' | 'reject'."""
    parts = [p.lower() for p in re.findall(r"[A-Za-z]+", person)]
    if len(parts) < 2:
        return "reject"
    first, last = parts[0], parts[-1]
    slug = unquote(url.rsplit("/", 1)[-1]).lower()
    # A slug made of business-name tokens is a vanity page, not a person.
    btoks = name_tokens(business)
    slug_words = re.findall(r"[a-z]+", slug)
    if btoks and any(t in slug for t in btoks if len(t) > 3) and not (first in slug and last in slug):
        return "reject"
    if not slug_words:
        return "reject"
    title_l = title.lower()
    name_in_slug = first in slug and last in slug
    name_in_title = first in title_l and last in title_l
    if not (name_in_slug or name_in_title):
        return "reject"
    ctx = f"{title} {snippet}"
    # The owner's own surname is often the business name; it proves nothing here.
    tie_toks = [t for t in btoks if len(t) > 3 and t not in parts]
    tied = (JEWEL_CTX.search(ctx) or city.lower() in ctx.lower()
            or any(t in ctx.lower() for t in tie_toks))
    if name_in_slug and name_in_title and tied:
        return "match"
    return "ambiguous"


def _job(item):
    bkey, person, business, city = item
    best = ("none", "", "", "")
    try:
        for su in search_urls(person, city):
            status, _, html = fetch(su, min_gap=3, timeout=20)
            if status != 200:
                continue
            for url, title, snip in parse_results(html):
                v = judge(person, business, city, url, title, snip)
                if v == "match":
                    return bkey, person, ("match", url, su, f"{title} | {snip[:200]}")
                if v == "ambiguous" and best[0] == "none":
                    best = ("ambiguous", url, su, f"{title} | {snip[:200]}")
            if best[0] != "none":
                break
    except Blocked as e:
        return bkey, person, ("egress-blocked", "", "", str(e))
    except Exception as e:  # noqa: BLE001
        return bkey, person, ("error", "", "", str(e)[:200])
    return bkey, person, best


def google_url(person, city):
    q = f'"{person}" {city} linkedin'
    return f"https://www.google.com/search?q={quote_plus(q)}&hl=en&num=10"


def parse_google(html):
    """(url, title, snippet) for each linkedin.com/in/ organic result."""
    soup = BeautifulSoup(html, "lxml")
    out = []
    for a in soup.find_all("a", href=True):
        href = html_unescape(a["href"])
        if "/url?" in href:
            qs = parse_qs(urlparse(href).query)
            href = (qs.get("url") or qs.get("q") or [""])[0]
        href = unquote(href)
        m = IN_RX.match(href)
        if not m:
            continue
        url = f"https://www.linkedin.com/in/{m.group(1).rstrip('/')}"
        if any(u == url for u, _, _ in out):
            continue
        h3 = a.find("h3")
        box = a.find_parent("div", attrs={"data-hveid": True}) or a.find_parent("div")
        out.append((url, h3.get_text(" ").strip() if h3 else a.get_text(" ").strip(),
                    box.get_text(" ")[:400] if box else ""))
    return out


def parse_google_hidden(html):
    """Google now links results via /goto?url=<opaque token>; for LinkedIn
    profile results the title is 'First Last - Company - Role' and the snippet
    names the location. Return (goto_href, title, snippet) for those."""
    soup = BeautifulSoup(html, "lxml")
    out = []
    for h3 in soup.find_all("h3"):
        a = h3.find_parent("a", href=True)
        if not a:
            continue
        box = a.find_parent("div", attrs={"data-hveid": True}) or a.parent
        text = box.get_text(" ", strip=True) if box else ""
        if "linkedin" not in text.lower():
            continue
        out.append((html_unescape(a["href"]), h3.get_text(" ", strip=True), text[:400]))
    return out


def prejudge(person, business, city, title, snippet):
    """Title-level screen before spending a click: 'match' needs first+last
    name at the start of the title (profile titles read 'Name - …') and a tie
    to jewelry, the business, or the city."""
    parts = [p.lower() for p in re.findall(r"[A-Za-z]+", person)]
    if len(parts) < 2:
        return "reject"
    if " - " not in title and " – " not in title:
        return "reject"          # directory pages: '4 "X" profiles', addresses, 'Profile of X'
    if re.search(r"profiles?\b|profils|people found|address|phone number|profile of", title, re.I):
        return "reject"
    head = re.split(r" [-–] ", title)[0].lower()
    if not (parts[0] in head and parts[-1] in head):
        return "reject"
    rest = re.split(r" [-–] ", title, maxsplit=1)[1] if re.search(r" [-–] ", title) else ""
    btoks = [t for t in name_tokens(business) if len(t) > 3 and t not in parts]
    ctx = f"{rest} {snippet}".lower()
    if JEWEL_CTX.search(rest) or any(t in ctx for t in btoks):
        return "match"
    return "ambiguous"       # same name, no tie to jewelry/this business (city alone is not enough)


def resolve(br, href):
    """Follow Google's redirect and return the linkedin.com/in/ URL (LinkedIn's
    authwall keeps the original in sessionRedirect)."""
    url = href if href.startswith("http") else "https://www.google.com" + href
    try:
        br.page.goto(url, wait_until="domcontentloaded", timeout=30000)
    except Exception:  # noqa: BLE001
        pass
    final = unquote(br.page.url)
    m = IN_RX.search(final)
    return f"https://www.linkedin.com/in/{m.group(1).rstrip('/')}" if m else ""


def run_browser(limit=None, log=print, min_gap=None):
    """Search via headless Chrome on Google (Bing ignores quoted/site: queries
    from scripted clients; DuckDuckGo HTML returns 403). Sequential + polite;
    stops on the first captcha and leaves the rest for a later run."""
    import os
    from .browser import Browser
    min_gap = min_gap or float(os.environ.get("LINKEDIN_GAP", "7"))
    con = db.connect()
    rows = con.execute("""
        SELECT p.bkey, p.name AS person, l.name AS business,
               COALESCE(NULLIF(l.city,''), substr(l.market,1,instr(l.market,',')-1)) AS city
        FROM people p JOIN listings l ON l.bkey = p.bkey
        LEFT JOIN linkedin k ON k.bkey = p.bkey AND k.person = p.name
        WHERE k.bkey IS NULL ORDER BY p.method='bbb-profile' DESC, p.bkey""").fetchall()
    from .util import plausible_name
    todo = [r for r in rows if plausible_name(r["person"], r["business"], need_given=True)][: limit or None]
    log(f"[linkedin] {len(todo)} people to search (Google via browser)")
    counts = {}
    br = Browser()
    try:
        for i, r in enumerate(todo):
            su = google_url(r["person"], r["city"])
            try:
                html = br.get_html(su, min_gap=min_gap)
            except Blocked as e:
                db.log_event(con, "linkedin", "blocked", e)
                log(f"[linkedin] Google challenge after {i} searches; stopping (resumable)")
                break
            except Exception as e:  # noqa: BLE001
                db.log_event(con, "linkedin", "error", f"{su}: {e}")
                continue
            best = ("none", "", su, "")
            for href, title, snip in parse_google_hidden(html):
                v = prejudge(r["person"], r["business"], r["city"], title, snip)
                if v == "reject":
                    continue
                url = resolve(br, href) if v == "match" else ""
                if url and judge(r["person"], r["business"], r["city"], url, title, snip) != "reject":
                    best = ("match", url, su, f"{title} | {snip[:200]}")
                    break
                if best[0] == "none":
                    best = ("ambiguous", url, su, f"{title} | {snip[:200]}")
            for url, title, snip in ([] if best[0] == "match" else parse_google(html)):
                v = judge(r["person"], r["business"], r["city"], url, title, snip)
                if v == "match":
                    best = ("match", url, su, f"{title} | {snip[:200]}")
                    break
                if v == "ambiguous" and best[0] == "none":
                    best = ("ambiguous", url, su, f"{title} | {snip[:200]}")
            counts[best[0]] = counts.get(best[0], 0) + 1
            con.execute("INSERT OR REPLACE INTO linkedin VALUES (?,?,?,?,?,?,?)",
                        (r["bkey"], r["person"], best[0], best[1], best[2], best[3], now_iso()))
            if (i + 1) % 50 == 0:
                log(f"[linkedin] {i + 1}/{len(todo)} searched: {counts}")
    finally:
        br.close()
    log(f"[linkedin] {counts}")
    return counts


def run(workers=3, limit=None, log=print):
    con = db.connect()
    rows = con.execute("""
        SELECT p.bkey, p.name AS person, l.name AS business,
               COALESCE(NULLIF(l.city,''), substr(l.market,1,instr(l.market,',')-1)) AS city
        FROM people p JOIN listings l ON l.bkey = p.bkey
        LEFT JOIN linkedin k ON k.bkey = p.bkey AND k.person = p.name
        WHERE k.bkey IS NULL""").fetchall()
    from .util import plausible_name
    todo = [(r["bkey"], r["person"], r["business"], r["city"]) for r in rows
            if plausible_name(r["person"], r["business"], need_given=True)][: limit or None]
    log(f"[linkedin] {len(todo)} people to search")
    counts = {}
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for bkey, person, (status, url, su, ev) in ex.map(_job, todo):
            counts[status] = counts.get(status, 0) + 1
            if status == "egress-blocked":
                db.log_event(con, "linkedin", status, ev)
                continue
            con.execute("INSERT OR REPLACE INTO linkedin VALUES (?,?,?,?,?,?,?)",
                        (bkey, person, status, url, su, ev, now_iso()))
    log(f"[linkedin] {counts}")
    return counts
