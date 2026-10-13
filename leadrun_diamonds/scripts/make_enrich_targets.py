"""Round-2 targets: listings in cities that have no qualified lead yet, split into N worker shards.

Picks (a) every 1-of-3 listing in such a city, (b) up to 3 more listings per such city that have a website.
Writes work/enrich/shard_K.json = [{file, business, city, market, website, have}] — workers edit `file` in place.
"""
import csv, json, sqlite3, sys
from collections import defaultdict
from common import DB_PATH, RAW_DIR, RUN_DIR, norm_name

n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
rows = list(csv.DictReader(open(RUN_DIR / "diamonds_all.csv")))
city = lambda c, s: f"{c.strip().title()}, {s}"
qualified_cities = {city(r["Real City"], r["Real State"]) for r in rows if r["Signals"][0] in "23"}
score = {(norm_name(r["Business"]), r["Market"]): r for r in rows}

con = sqlite3.connect(DB_PATH)
by_city = defaultdict(list)
for key, data in con.execute("SELECT listing_key, data FROM listings WHERE status='keep'"):
    rec = json.loads(data)
    c = city(rec.get("city", ""), (rec.get("state") or "").upper()[:2])
    if c in qualified_cities or not rec.get("city"):
        continue
    row = score.get((norm_name(rec.get("business", "")), rec.get("market", "")))
    sig = row["Signals"][0] if row else "0"
    have = [k for k, col in (("email", "Email"), ("linkedin", "LinkedIn Profile"), ("direct", "Mobile Candidates"))
            if row and row[col]]
    by_city[c].append(dict(file=str(RAW_DIR / f"{key}.json"), business=rec["business"], city=c,
                           market=rec.get("market", ""), website=rec.get("website", ""), have=have,
                           _rank=(sig != "1", not rec.get("website"), not rec.get("verified"))))
targets, seen = [], set()
for c, items in sorted(by_city.items()):
    items.sort(key=lambda t: t["_rank"])
    picked = [t for t in items if t["_rank"][0] is False]  # all near-misses
    picked += [t for t in items if t["_rank"][0] and t["website"]][:3]
    for t in picked:
        k = (norm_name(t["business"]), t["city"])
        if k not in seen:
            seen.add(k)
            t.pop("_rank")
            targets.append(t)
out = RUN_DIR / "work" / "enrich"
out.mkdir(parents=True, exist_ok=True)
cities = sorted({t["city"] for t in targets})
for k in range(n):  # shard by city so each worker owns whole cities
    mine = [t for t in targets if cities.index(t["city"]) % n == k]
    (out / f"shard_{k}.json").write_text(json.dumps(mine, indent=1))
    print(f"shard_{k}: {len(mine)} listings, {len({t['city'] for t in mine})} cities")
print(f"total {len(targets)} listings in {len(cities)} cities without a qualified lead")
