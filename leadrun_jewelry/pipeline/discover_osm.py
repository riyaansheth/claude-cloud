"""Discovery source 1 — OpenStreetMap Overpass (volume base).

Per market bbox: shop=jewelry, craft=jeweller, shop=watches (+ goldsmith /
silversmith crafts). Every element becomes a listing keyed osm:<type>/<id>;
the Source column is the element's openstreetmap.org URL.
"""
import json

from . import config, db, scope
from .http import fetch, Blocked
from .util import phone_digits, fmt_phone, root_url, state_from_zip

OVERPASS = ["https://overpass-api.de/api/interpreter",
            "https://overpass.kumi.systems/api/interpreter",
            "https://overpass.private.coffee/api/interpreter",
            "https://maps.mail.ru/osm/tools/overpass/api/interpreter"]


def query_for(bbox):
    s, w, n, e = bbox
    b = f"({s},{w},{n},{e})"
    return f"""[out:json][timeout:120];
(
  nwr["shop"="jewelry"]{b};
  nwr["craft"="jeweller"]{b};
  nwr["craft"="goldsmith"]{b};
  nwr["craft"="silversmith"]{b};
  nwr["shop"="watches"]{b};
);
out center tags;"""


def element_to_listing(el, market):
    t = el.get("tags", {})
    name = t.get("name") or t.get("brand") or ""
    num, street = t.get("addr:housenumber", ""), t.get("addr:street", "")
    unit = t.get("addr:unit", "") or t.get("addr:suite", "")
    city, state, zp = t.get("addr:city", ""), t.get("addr:state", ""), t.get("addr:postcode", "")
    if not state and zp:
        state = state_from_zip(zp)
    line1 = " ".join(x for x in (num, street) if x)
    if unit:
        line1 += f" {'#' if unit[0].isdigit() else ''}{unit}"
    tail = " ".join(x for x in (state, zp) if x)
    address = ", ".join(x for x in (line1, city, tail) if x) if line1 else ""
    phone = t.get("phone") or t.get("contact:phone") or ""
    phone = phone.split(";")[0].strip()
    website = t.get("website") or t.get("contact:website") or t.get("url") or ""
    # "Category (as listed)": the OSM tag string, verbatim.
    cat = (f"shop={t['shop']}" if "shop" in t else f"craft={t.get('craft', '')}")
    etype, eid = el["type"], el["id"]
    return {
        "bkey": f"osm:{etype}/{eid}",
        "name": name.strip(),
        "category": cat,
        "phone": fmt_phone(phone) if phone_digits(phone) else phone,
        "website": root_url(website) if website else "",
        "address": address,
        "city": city, "state": state.upper()[:2] if state else "", "zip": zp,
        "market": market, "origin": "OpenStreetMap",
        "source_url": f"https://www.openstreetmap.org/{etype}/{eid}",
        "extra": {"tags": t, "email": t.get("email") or t.get("contact:email") or "",
                  "socials": [t[k] for k in ("contact:facebook", "contact:instagram",
                                             "facebook", "instagram") if t.get(k)]},
    }


def run(markets, log=print):
    con = db.connect()
    stats = {"new": 0, "seen": 0, "dropped": 0, "unnamed": 0}
    for city, st, bbox in markets:
        market = config.market_label(city, st)
        task = f"osm:{market}"
        if db.task_done(con, task):
            continue
        data = None
        for ep in OVERPASS:
            try:
                status, _, text = fetch(ep, data={"data": query_for(bbox)},
                                        min_gap=2, timeout=180, use_cache=True)
            except Blocked as e:
                db.log_event(con, "osm", "egress-blocked", e)
                continue
            except Exception as e:  # noqa: BLE001 — try next mirror
                db.log_event(con, "osm", "error", f"{ep}: {e}")
                continue
            if status == 200:
                data = json.loads(text)
                break
            db.log_event(con, "osm", f"http-{status}", ep)
        if data is None:
            log(f"[osm] {market}: all Overpass endpoints failed")
            continue
        for el in data.get("elements", []):
            rec = element_to_listing(el, market)
            if not rec["name"]:
                stats["unnamed"] += 1
                continue
            if db.is_dropped(con, rec["bkey"]):
                continue
            tags = rec["extra"]["tags"]
            reason = scope.kill_reason(rec["name"], rec["category"], rec["address"],
                                       market, osm_tags=tags)
            if reason:
                db.drop(con, rec["bkey"], rec["name"], rec["category"], market,
                        "OpenStreetMap", reason, "discovery", rec["source_url"])
                stats["dropped"] += 1
                continue
            stats["new" if db.upsert_listing(con, rec) else "seen"] += 1
        db.mark_task(con, task, detail=str(len(data.get("elements", []))))
        log(f"[osm] {market}: {len(data.get('elements', []))} elements; running {stats}")
    return stats
