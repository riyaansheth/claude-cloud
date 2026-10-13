"""Split YellowPages listings that still need a scope verdict / owner / LinkedIn into agent batches.

Writes work/batches/batch_NN.json: [{file, business, market, website, phone, emails}] — the narrow end
handed to research agents, who edit those raw/yp files in place (verified=true, verdict, owner, LinkedIn).
Priority: listings whose own-site crawl already found an email (one more criterion away from qualifying).
"""
import json
import sqlite3
import sys
from pathlib import Path

from common import DB_PATH, RAW_DIR, RUN_DIR

size = int(sys.argv[1]) if len(sys.argv) > 1 else 40
con = sqlite3.connect(DB_PATH)
crawl = {k: json.loads(e) for k, e in con.execute("SELECT listing_key, emails FROM crawl WHERE status='ok'")}
todo = []
for f in sorted((RAW_DIR / "yp").glob("*.json")):
    r = json.loads(f.read_text())
    if not r.get("is_diamond_trade") or r.get("verified") or not r.get("website"):
        continue
    emails = crawl.get(f"yp/{f.stem}", {})
    todo.append(dict(file=str(f), business=r["business"], market=r["market"], website=r["website"],
                     phone=r["phone"], emails=list(emails)))
todo.sort(key=lambda t: (not t["emails"], t["market"]))
out = RUN_DIR / "work" / "batches"
out.mkdir(parents=True, exist_ok=True)
for old in out.glob("batch_*.json"):
    old.unlink()
for i in range(0, len(todo), size):
    (out / f"batch_{i // size + 1:02d}.json").write_text(json.dumps(todo[i:i + size], indent=1))
print(f"{len(todo)} listings -> {(len(todo) + size - 1) // size} batches of <= {size}")
