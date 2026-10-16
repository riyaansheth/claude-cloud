"""LinkedIn backfill targets: in-scope businesses with no personal LinkedIn yet, sharded by market.

Priority: already has an owner name > has a website > rest. Writes work/li/shard_K.json with the raw
`file` to edit in place (one listing per business — the most complete one).
"""
import csv, json, sqlite3, sys
from collections import defaultdict
from common import DB_PATH, RAW_DIR, RUN_DIR, norm_name

n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
rows = {(norm_name(r["Business"]), r["Market"]): r for r in csv.DictReader(open(RUN_DIR / "diamonds_all.csv"))}
con = sqlite3.connect(DB_PATH)
pick = {}
for key, data in con.execute("SELECT listing_key, data FROM listings WHERE status='keep'"):
    rec = json.loads(data)
    k = (norm_name(rec.get("business", "")), rec.get("market", ""))
    row = rows.get(k)
    if not row or row["LinkedIn Profile"]:
        continue
    score = (bool(row["Contact Person"]), bool(row["Website"]), bool(row["Email"]))
    if k not in pick or score > pick[k][0]:
        pick[k] = (score, dict(file=str(RAW_DIR / f"{key}.json"), business=rec["business"], market=k[1],
                               contact=row["Contact Person"], website=row["Website"], qualified=row["Signals"][0] in "23"))
items = sorted((v for v in pick.values()), key=lambda t: t[0], reverse=True)
items = [t[1] for t in items if t[0][0] or t[0][1]]          # needs a name or a site to work from
markets = sorted({t["market"] for t in items})
out = RUN_DIR / "work" / "li"; out.mkdir(parents=True, exist_ok=True)
for k in range(n):
    mine = [t for t in items if markets.index(t["market"]) % n == k]
    (out / f"shard_{k}.json").write_text(json.dumps(mine, indent=1))
    print(f"shard_{k}: {len(mine)}")
print(f"total {len(items)} businesses without LinkedIn (with a name or website)")
