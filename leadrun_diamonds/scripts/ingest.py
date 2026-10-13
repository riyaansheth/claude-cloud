"""Stage 1: ingest research-worker JSON records into progress.sqlite3.

Keyed by a stable listing key (<worker dir>/<business slug>), never a row number.
Re-running is idempotent: unchanged files are skipped, changed files update in place,
and found_at keeps the first-ingest timestamp. Kill-list gate #1 is applied here.
"""
import hashlib
import json
import sqlite3
import sys

from common import DB_PATH, RAW_DIR, JUDGEMENT_DROPS, kill_reason, now_iso, norm_name

SCHEMA = """
CREATE TABLE IF NOT EXISTS listings (
    listing_key TEXT PRIMARY KEY,
    biz_key     TEXT NOT NULL,
    worker      TEXT NOT NULL,
    content_sha TEXT NOT NULL,
    data        TEXT NOT NULL,
    status      TEXT NOT NULL,          -- keep | dropped | invalid
    drop_reason TEXT NOT NULL DEFAULT '',
    drop_stage  TEXT NOT NULL DEFAULT '',
    found_at    TEXT NOT NULL,
    updated_at  TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_listings_biz ON listings(biz_key);
"""


def connect():
    con = sqlite3.connect(DB_PATH)
    con.executescript(SCHEMA)
    return con


def gate(rec: dict):
    """Discovery-time kill-list + scope gate -> (status, reason)."""
    if not (rec.get("business") or "").strip():
        return "invalid", "no-business-name"
    if not (rec.get("source_url") or "").startswith("http"):
        return "invalid", "no-source-url"
    reason = kill_reason(rec.get("business", ""), rec.get("category_as_listed", ""))
    if reason:
        return "dropped", reason
    if rec.get("is_diamond_trade") is False:
        dr = (rec.get("drop_reason") or "other").strip().lower()
        if (rec.get("scope_reason") or "").lower().startswith("unverified"):
            dr = "unverified"  # could not confirm a diamond line — not shipped, but not proven out of scope
        return "dropped", dr if dr in JUDGEMENT_DROPS else "other"
    return "keep", ""


def main():
    con = connect()
    seen = new = changed = 0
    bad = []
    for path in sorted(RAW_DIR.glob("*/*.json")):
        seen += 1
        raw = path.read_bytes()
        sha = hashlib.sha1(raw).hexdigest()
        key = f"{path.parent.name}/{path.stem}"
        try:
            rec = json.loads(raw)
            assert isinstance(rec, dict)
        except Exception as exc:  # malformed worker output — record, don't crash
            bad.append(f"{key}: {exc}")
            continue
        row = con.execute("SELECT content_sha, found_at FROM listings WHERE listing_key=?", (key,)).fetchone()
        if row and row[0] == sha:
            # unchanged file: re-apply the gate only (rules may have changed); keeps found_at
            status, reason = gate(rec)
            con.execute("UPDATE listings SET status=?, drop_reason=?, drop_stage=? WHERE listing_key=? "
                        "AND (status!=? OR drop_reason!=?)",
                        (status, reason, "discovery" if status == "dropped" else "", key, status, reason))
            continue
        status, reason = gate(rec)
        biz_key = f"{norm_name(rec.get('business', ''))}|{(rec.get('market') or '').lower()}"
        ts = now_iso()
        if row:
            changed += 1
            con.execute("""UPDATE listings SET biz_key=?, content_sha=?, data=?, status=?, drop_reason=?,
                           drop_stage=?, updated_at=? WHERE listing_key=?""",
                        (biz_key, sha, json.dumps(rec), status, reason,
                         "discovery" if status == "dropped" else "", ts, key))
        else:
            new += 1
            con.execute("INSERT INTO listings VALUES (?,?,?,?,?,?,?,?,?,?)",
                        (key, biz_key, path.parent.name, sha, json.dumps(rec), status, reason,
                         "discovery" if status == "dropped" else "", ts, ts))
    con.commit()
    counts = dict(con.execute("SELECT status, COUNT(*) FROM listings GROUP BY status").fetchall())
    print(f"files={seen} new={new} changed={changed} malformed={len(bad)} db={counts}")
    for b in bad:
        print("  MALFORMED", b, file=sys.stderr)


if __name__ == "__main__":
    main()
