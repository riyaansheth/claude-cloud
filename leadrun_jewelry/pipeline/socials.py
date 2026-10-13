"""Social pages: mbasic.facebook.com/<page>/about exposes the page contact email
and phone; Instagram bios often carry an email. Only emails that relate to the
business (own domain, consumer domain, or name-token domain) are kept later by
the builder."""
import json
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from . import db
from .http import fetch, Blocked
from .util import EMAIL_RX, clean_email, email_status, now_iso, phone_digits

IG_APP_ID = "936619743392459"   # public web app id used by instagram.com itself


def fb_about_url(u):
    p = urlparse(u)
    path = p.path.strip("/")
    if not path or path.startswith(("profile.php", "people/")):
        if "id=" in (p.query or ""):
            return f"https://mbasic.facebook.com/profile.php?{p.query}&v=info"
        if path.startswith("people/"):
            pid = path.rstrip("/").split("/")[-1]
            return f"https://mbasic.facebook.com/profile.php?id={pid}&v=info"
        return ""
    return f"https://mbasic.facebook.com/{path.split('/')[0]}/about"


def lookup(u):
    host = urlparse(u).hostname or ""
    res = {"emails": {}, "tels": {}, "bio": ""}
    if "facebook.com" in host:
        url = fb_about_url(u)
        if not url:
            return "skip", res
        status, final, html = fetch(url, min_gap=4, timeout=20)
        if status != 200 or "login" in urlparse(final).path:
            return f"http-{status}" if status != 200 else "login-wall", res
        soup = BeautifulSoup(html, "lxml")
        text = soup.get_text(" ")
        for a in soup.select("a[href^='mailto:']"):
            res["emails"][clean_email(a["href"])] = url
        for e in EMAIL_RX.findall(text):
            res["emails"].setdefault(clean_email(e), url)
        for a in soup.select("a[href^='tel:']"):
            d = phone_digits(a["href"])
            if d:
                res["tels"][d] = url
        return "ok", res
    if "instagram.com" in host:
        user = urlparse(u).path.strip("/").split("/")[0]
        if not user:
            return "skip", res
        api = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}"
        from .http import session
        s = session()
        s.headers["x-ig-app-id"] = IG_APP_ID
        try:
            status, _, body = fetch(api, min_gap=6, timeout=20)
        finally:
            s.headers.pop("x-ig-app-id", None)
        if status != 200:
            return f"http-{status}", res
        try:
            uinfo = json.loads(body)["data"]["user"]
        except (ValueError, KeyError, TypeError):
            return "parse-error", res
        bio = uinfo.get("biography") or ""
        res["bio"] = bio[:500]
        src = f"https://www.instagram.com/{user}/"
        for e in EMAIL_RX.findall(bio):
            res["emails"].setdefault(clean_email(e), src)
        if uinfo.get("business_email"):
            res["emails"].setdefault(clean_email(uinfo["business_email"]), src)
        for k in ("business_phone_number",):
            d = phone_digits(uinfo.get(k) or "")
            if d:
                res["tels"][d] = src
        return "ok", res
    return "skip", res


def _job(u):
    try:
        st, res = lookup(u)
    except Blocked as e:
        return u, "egress-blocked", {"error": str(e)}
    except Exception as e:  # noqa: BLE001
        return u, "error", {"error": str(e)[:200]}
    res["emails"] = {e: s for e, s in res["emails"].items() if email_status(e) == "ok"}
    return u, st, res


def run(workers=4, limit=None, log=print):
    con = db.connect()
    urls = set()
    for r in con.execute("SELECT result FROM crawls WHERE status='ok'"):
        for s in json.loads(r["result"]).get("socials", []):
            if re.search(r"facebook\.com|instagram\.com", s):
                urls.add(s)
    for r in con.execute("SELECT extra FROM listings WHERE origin='OpenStreetMap'"):
        for s in (json.loads(r["extra"] or "{}").get("socials") or []):
            if s.startswith("http"):
                urls.add(s.rstrip("/"))
    done = {r["url"] for r in con.execute("SELECT url FROM socials")}
    todo = sorted(urls - done)[: limit or None]
    log(f"[socials] {len(todo)} pages to look up")
    n = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for u, st, res in ex.map(_job, todo):
            if st == "egress-blocked":
                db.log_event(con, "socials", st, u)
                continue
            con.execute("INSERT OR REPLACE INTO socials VALUES (?,?,?,?)",
                        (u, st, json.dumps(res), now_iso()))
            n += 1
    log(f"[socials] looked up {n}")
    return {"looked_up": n}
