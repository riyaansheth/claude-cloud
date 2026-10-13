"""progress.sqlite3: every table is keyed by a stable business/listing key
(source-native id or URL hash), never a row number, so any stage can be
interrupted and re-run without re-researching or duplicating rows."""
import json
import sqlite3
import threading

from . import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS listings (
  bkey TEXT PRIMARY KEY,          -- e.g. osm:node/123, yp:<hash>, bbb:<hash>, gmaps:<hash>
  name TEXT NOT NULL,
  category TEXT,                  -- verbatim source category
  phone TEXT, website TEXT, address TEXT,
  city TEXT, state TEXT, zip TEXT,
  market TEXT NOT NULL,           -- "City, ST" of the search
  origin TEXT NOT NULL,           -- config.ORIGINS
  rating TEXT, reviews TEXT,
  source_url TEXT NOT NULL,
  segment TEXT,
  extra TEXT,                     -- json: osm tags, bbb principals, etc.
  discovered_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS dropped (
  bkey TEXT PRIMARY KEY, name TEXT, category TEXT, market TEXT, origin TEXT,
  reason TEXT NOT NULL, stage TEXT NOT NULL, source_url TEXT, dropped_at TEXT
);
CREATE TABLE IF NOT EXISTS tasks (          -- discovery pages / queries done
  task TEXT PRIMARY KEY, status TEXT, detail TEXT, done_at TEXT
);
CREATE TABLE IF NOT EXISTS crawls (         -- one per website domain
  domain TEXT PRIMARY KEY, root TEXT, status TEXT, pages TEXT,
  result TEXT, crawled_at TEXT
);
CREATE TABLE IF NOT EXISTS socials (        -- facebook/instagram page lookups
  url TEXT PRIMARY KEY, status TEXT, result TEXT, fetched_at TEXT
);
CREATE TABLE IF NOT EXISTS people (         -- owner/decision-maker names
  bkey TEXT NOT NULL, name TEXT NOT NULL, role TEXT, source_url TEXT NOT NULL,
  method TEXT, evidence TEXT, found_at TEXT,
  PRIMARY KEY (bkey, name)
);
CREATE TABLE IF NOT EXISTS linkedin (       -- searched per (bkey, person)
  bkey TEXT NOT NULL, person TEXT NOT NULL, status TEXT,
  url TEXT, search_url TEXT, evidence TEXT, checked_at TEXT,
  PRIMARY KEY (bkey, person)
);
CREATE TABLE IF NOT EXISTS events (         -- blockers / errors for REPORT.md
  id INTEGER PRIMARY KEY AUTOINCREMENT, stage TEXT, kind TEXT, detail TEXT, at TEXT
);
"""

_local = threading.local()


def connect(path=None):
    path = str(path or config.DB_PATH)
    con = getattr(_local, "con", None)
    if con is None or getattr(_local, "path", None) != path:
        con = sqlite3.connect(path, timeout=60, isolation_level=None)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA journal_mode=WAL")
        con.execute("PRAGMA busy_timeout=60000")
        con.executescript(SCHEMA)
        _local.con, _local.path = con, path
    return con


def task_done(con, task):
    r = con.execute("SELECT status FROM tasks WHERE task=?", (task,)).fetchone()
    return bool(r and r["status"] == "done")


def mark_task(con, task, status="done", detail=""):
    from .util import now_iso
    con.execute("INSERT OR REPLACE INTO tasks VALUES (?,?,?,?)",
                (task, status, detail, now_iso()))


def log_event(con, stage, kind, detail):
    from .util import now_iso
    con.execute("INSERT INTO events(stage,kind,detail,at) VALUES (?,?,?,?)",
                (stage, kind, str(detail)[:500], now_iso()))


def upsert_listing(con, rec):
    """Insert a listing if new; on re-discovery, fill only empty fields.
    Returns True when the key was new."""
    from .util import now_iso
    rec = dict(rec)
    rec.setdefault("discovered_at", now_iso())
    if isinstance(rec.get("extra"), (dict, list)):
        rec["extra"] = json.dumps(rec["extra"], ensure_ascii=False)
    cols = ["bkey", "name", "category", "phone", "website", "address", "city",
            "state", "zip", "market", "origin", "rating", "reviews", "source_url",
            "segment", "extra", "discovered_at"]
    row = con.execute("SELECT * FROM listings WHERE bkey=?", (rec["bkey"],)).fetchone()
    if row is None:
        con.execute(f"INSERT INTO listings({','.join(cols)}) VALUES ({','.join('?' * len(cols))})",
                    [rec.get(c) or "" for c in cols])
        return True
    updates = {c: rec[c] for c in cols[1:] if rec.get(c) and not row[c]}
    if updates:
        con.execute(f"UPDATE listings SET {', '.join(f'{c}=?' for c in updates)} WHERE bkey=?",
                    [*updates.values(), rec["bkey"]])
    return False


def drop(con, bkey, name, category, market, origin, reason, stage, source_url):
    from .util import now_iso
    con.execute("INSERT OR IGNORE INTO dropped VALUES (?,?,?,?,?,?,?,?,?)",
                (bkey, name, category, market, origin, reason, stage, source_url, now_iso()))
    # A listing dropped later (site check / builder) leaves the research pool.
    con.execute("DELETE FROM listings WHERE bkey=?", (bkey,))


def is_dropped(con, bkey):
    return con.execute("SELECT 1 FROM dropped WHERE bkey=?", (bkey,)).fetchone() is not None


def add_person(con, bkey, name, role, source_url, method, evidence=""):
    from .util import now_iso
    con.execute("INSERT OR IGNORE INTO people VALUES (?,?,?,?,?,?,?)",
                (bkey, name, role, source_url, method, evidence[:400], now_iso()))
