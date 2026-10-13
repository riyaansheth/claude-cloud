#!/usr/bin/env python3
"""Jewelry retail lead pipeline — orchestrator.

  python3 run.py preflight             # which source hosts are reachable from here
  python3 run.py all [--cities 10]     # every stage, in order, resumable
  python3 run.py osm|gmaps|yp|bbb|trade|crawl|socials|linkedin|agents-export|agents-import|build|status

Each stage is idempotent: discovery tasks, crawls, social lookups and LinkedIn
searches are keyed in progress.sqlite3 and skipped when already done. `all`
runs discovery sources concurrently (separate worker processes), then the crawl,
and prints a status line every 20 minutes.
"""
import argparse
import multiprocessing as mp
import subprocess
import sys
import threading
import time

sys.path.insert(0, __import__("os").path.dirname(__file__))

from pipeline import config, db  # noqa: E402

PREFLIGHT_HOSTS = [
    ("OpenStreetMap Overpass", "https://overpass-api.de/api/status"),
    ("Google Maps", "https://www.google.com/maps"),
    ("YellowPages", "https://www.yellowpages.com/"),
    ("BBB", "https://www.bbb.org/"),
    ("Jewelers of America", "https://www.jewelers.org/"),
    ("American Gem Society", "https://www.americangemsociety.org/"),
    ("Bing", "https://www.bing.com/"),
    ("DuckDuckGo HTML", "https://html.duckduckgo.com/html/"),
    ("Facebook mbasic", "https://mbasic.facebook.com/"),
    ("Instagram", "https://i.instagram.com/"),
    ("Arbitrary business site", "https://example.com/"),
]


def preflight():
    import requests
    from pipeline.http import session
    ok = True
    for label, url in PREFLIGHT_HOSTS:
        try:
            r = session().get(url, timeout=15)
            res = f"HTTP {r.status_code}"
        except requests.exceptions.ProxyError:
            res, ok = "BLOCKED by egress proxy (CONNECT 403)", False
            db.log_event(db.connect(), "preflight", "egress-blocked", f"{label}: {url}")
        except Exception as e:  # noqa: BLE001
            res, ok = f"ERROR {type(e).__name__}", False
        print(f"  {label:26s} {res}")
    return ok


def markets(n):
    return config.MARKETS[:n] if n else config.MARKETS


def _browser_stage(name, n):
    from pipeline import discover_web
    from pipeline.browser import Browser
    br = Browser()
    try:
        fn = {"gmaps": discover_web.run_gmaps, "yp": discover_web.run_yp,
              "bbb": discover_web.run_bbb, "trade": discover_web.run_trade}[name]
        return fn(br, markets(n))
    finally:
        br.close()


def stage(name, n=0, limit=None):
    if name == "osm":
        from pipeline import discover_osm
        return discover_osm.run(markets(n))
    if name in ("gmaps", "yp", "bbb", "trade"):
        return _browser_stage(name, n)
    if name == "crawl":
        from pipeline import crawl_sites
        return crawl_sites.run(limit=limit)
    if name == "socials":
        from pipeline import socials
        return socials.run(limit=limit)
    if name == "linkedin":
        from pipeline import linkedin
        return linkedin.run(limit=limit)
    if name == "agents-export":
        from pipeline import agent_queue
        return agent_queue.export()
    if name == "agents-import":
        from pipeline import agent_queue
        return agent_queue.import_answers()
    if name == "build":
        from pipeline import build
        return build.build()
    if name == "status":
        return status()
    raise SystemExit(f"unknown stage {name}")


def status():
    con = db.connect()
    counts = {k: con.execute(sql).fetchone()[0] for k, sql in (
        ("listings", "SELECT COUNT(*) FROM listings"),
        ("dropped", "SELECT COUNT(*) FROM dropped"),
        ("crawled", "SELECT COUNT(*) FROM crawls"),
        ("with_name", "SELECT COUNT(DISTINCT bkey) FROM people"),
        ("linkedin_match", "SELECT COUNT(*) FROM linkedin WHERE status='match'"),
        ("blocked_events", "SELECT COUNT(*) FROM events WHERE kind LIKE '%blocked%'"))}
    line = f"[status {time.strftime('%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in counts.items())
    if config.QUALIFIED_CSV.exists():
        line += f" qualified_csv_rows={max(0, sum(1 for _ in open(config.QUALIFIED_CSV)) - 1)}"
    print(line, flush=True)
    return line


def _ticker(stop, every=1200):
    while not stop.wait(every):
        status()


def run_all(n):
    stop = threading.Event()
    threading.Thread(target=_ticker, args=(stop,), daemon=True).start()
    try:
        # Discovery sources in parallel worker processes (each with its own browser).
        procs = [mp.Process(target=stage, args=(s, n), name=s)
                 for s in ("osm", "gmaps", "yp", "bbb", "trade")]
        for p in procs:
            p.start()
        # Crawl what has been discovered so far while discovery continues.
        while any(p.is_alive() for p in procs):
            stage("crawl")
            time.sleep(60)
        for p in procs:
            p.join()
        for s in ("crawl", "socials", "linkedin", "agents-export", "build"):
            stage(s, n)
        status()
    finally:
        stop.set()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage")
    ap.add_argument("--cities", type=int, default=10, help="first N markets (0 = all 25)")
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    if a.stage == "preflight":
        sys.exit(0 if preflight() else 1)
    if a.stage == "all":
        if not preflight():
            print("WARNING: some source hosts are unreachable; those stages will log "
                  "'blocked' events and produce nothing (no data is invented).")
        return run_all(a.cities)
    print(stage(a.stage, a.cities, a.limit))


if __name__ == "__main__":
    main()
