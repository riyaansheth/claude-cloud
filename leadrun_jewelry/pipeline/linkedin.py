"""Personal LinkedIn search — only AFTER an owner name is known.

`"<business>" site:linkedin.com/in/` measured 8 hits in 5,791 rows, so we search
the human: `"First Last" <city> site:linkedin.com/in/` (+ jeweler context), via
Bing then DuckDuckGo HTML. Never gated on whether an email was found.

A result is accepted automatically only when the /in/ slug or result title
carries BOTH first and last name and the title/snippet ties it to jewelry, the
business, or the city. Name-only hits go to the subagent judging queue.
"""
import re
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
    return [f"https://www.bing.com/search?q={quote_plus(q)}&setlang=en-US",
            f"https://html.duckduckgo.com/html/?q={quote_plus(q)}",
            f"https://www.bing.com/search?q={quote_plus(q2)}&setlang=en-US"]


def parse_results(html):
    """Yield (url, title, snippet) for every linkedin.com/in/ result."""
    soup = BeautifulSoup(html, "lxml")
    out = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "duckduckgo.com/l/" in href or href.startswith("//duckduckgo.com/l/"):
            href = unquote(parse_qs(urlparse(href).query).get("uddg", [""])[0])
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


def run(workers=3, limit=None, log=print):
    con = db.connect()
    rows = con.execute("""
        SELECT p.bkey, p.name AS person, l.name AS business,
               COALESCE(NULLIF(l.city,''), substr(l.market,1,instr(l.market,',')-1)) AS city
        FROM people p JOIN listings l ON l.bkey = p.bkey
        LEFT JOIN linkedin k ON k.bkey = p.bkey AND k.person = p.name
        WHERE k.bkey IS NULL""").fetchall()
    todo = [(r["bkey"], r["person"], r["business"], r["city"]) for r in rows][: limit or None]
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
