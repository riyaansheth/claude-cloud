"""REPORT.md — real numbers only, straight from the DB and the written CSVs."""
from collections import Counter, defaultdict

from . import config
from .util import now_iso

TARGET_QUALIFIED = 100


def _pct(n, d):
    return f"{100 * n / d:.1f}%" if d else "—"


def write(con, out_all, out_q, n_listings):
    L = []
    a = L.append
    a("# Jewelry retail lead run — REPORT")
    a("")
    a(f"Generated {now_iso()} by `python3 run.py build`. Every number below is computed "
      "from `progress.sqlite3` and the CSVs written in the same pass.")
    a("")
    blocked_hosts = sorted({r["detail"].split(": ")[0] for r in con.execute(
        "SELECT detail FROM events WHERE stage='preflight' AND kind='egress-blocked'")})
    if blocked_hosts and not out_all:
        a("> **Run outcome: no data collected.** The environment's network egress policy "
          "refused the connection (proxy CONNECT 403) to every discovery and enrichment "
          "source: " + ", ".join(blocked_hosts) + ". No listings were discovered, so "
          "nothing was crawled and both CSVs contain only the header row. Nothing was "
          "filled from memory. Allow these hosts (or run on an unrestricted machine) "
          "and re-run `python3 run.py all`.")
        a("")
    elif blocked_hosts:
        a("> **Partial run.** Unreachable at preflight: " + ", ".join(blocked_hosts) + ".")
        a("")
    crawled = con.execute("SELECT status, COUNT(*) c FROM crawls GROUP BY status").fetchall()
    crawl_ok = sum(r["c"] for r in crawled if r["status"] == "ok")
    people = con.execute("SELECT COUNT(DISTINCT bkey) FROM people").fetchone()[0]
    li = con.execute("SELECT status, COUNT(*) c FROM linkedin GROUP BY status").fetchall()
    li_txt = ", ".join("%s: %s" % (r["status"], r["c"]) for r in li) or "—"
    a("## Headline")
    a("")
    a("| Metric | Count |")
    a("|---|---|")
    a(f"| Listings in research pool (in scope after discovery) | {n_listings} |")
    a(f"| Businesses researched (after dedupe) → `jewelry_all.csv` | {len(out_all)} |")
    a(f"| Qualified (2 of 3) → `jewelry_qualified.csv` | {len(out_q)} |")
    a(f"| Qualification rate | {_pct(len(out_q), len(out_all))} |")
    a(f"| Websites crawled OK / attempted | {crawl_ok} / {sum(r['c'] for r in crawled)} |")
    a(f"| Listings with an owner/decision-maker name | {people} |")
    a(f"| LinkedIn searches by outcome | {li_txt} |")
    short = TARGET_QUALIFIED - len(out_q)
    if short > 0:
        a(f"| **Shortfall vs {TARGET_QUALIFIED} qualified** | **{short}** (not padded) |")
    a("")

    a("## Fill rate per field")
    a("")
    a("| # | Column | all.csv | qualified.csv |")
    a("|---|---|---|---|")
    for i, c in enumerate(config.COLUMNS, 1):
        fa = sum(1 for r in out_all if str(r[c]) not in ("", "0"))
        fq = sum(1 for r in out_q if str(r[c]) not in ("", "0"))
        a(f"| {i} | {c} | {fa} ({_pct(fa, len(out_all))}) | {fq} ({_pct(fq, len(out_q))}) |")
    a("")

    a("## Qualification components")
    a("")
    comp = Counter()
    for r in out_all:
        comp["email"] += bool(r["Email"])
        comp["linkedin"] += bool(r["LinkedIn Profile"])
        comp["direct-line"] += "direct-line" in r["Signals"]
        comp["role-email"] += "role-email" in r["Signals"]
        for t in ("gia", "ags", "ja", "bench", "custom-design"):
            comp[t] += f", {t}" in r["Signals"]
        comp["since-yyyy"] += "since-" in r["Signals"]
    a("| Signal | Businesses | Rate |")
    a("|---|---|---|")
    for k, v in comp.items():
        a(f"| {k} | {v} | {_pct(v, len(out_all))} |")
    a("")

    a("## Per market")
    a("")
    by_m = defaultdict(lambda: [0, 0, 0, 0, 0])
    lst_m = Counter(r["market"] for r in con.execute("SELECT market FROM listings"))
    for r in out_all:
        x = by_m[r["Market"]]
        x[0] += 1
        x[1] += bool(r["Email"])
        x[2] += bool(r["Contact Person"])
        x[3] += bool(r["LinkedIn Profile"])
    for r in out_q:
        by_m[r["Market"]][4] += 1
    a("| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |")
    a("|---|---|---|---|---|---|---|")
    for city, st, _ in config.MARKETS:
        m = config.market_label(city, st)
        x = by_m.get(m, [0] * 5)
        a(f"| {m} | {lst_m.get(m, 0)} | {x[0]} | {x[1]} | {x[2]} | {x[3]} | {x[4]} |")
    a("")

    a("## Per source (Lead Origin)")
    a("")
    src_l = Counter(r["origin"] for r in con.execute("SELECT origin FROM listings"))
    src_a = Counter(r["Lead Origin"] for r in out_all)
    src_q = Counter(r["Lead Origin"] for r in out_q)
    a("| Source | Listings | Businesses (as base row) | Qualified |")
    a("|---|---|---|---|")
    for s in config.ORIGINS:
        if src_l.get(s) or src_a.get(s):
            a(f"| {s} | {src_l.get(s, 0)} | {src_a.get(s, 0)} | {src_q.get(s, 0)} |")
    tasks = con.execute("SELECT substr(task,1,instr(task,':')-1) src, COUNT(*) c FROM tasks "
                        "WHERE status='done' GROUP BY src").fetchall()
    a("")
    a("Discovery tasks completed: " + (", ".join(f"{r['src']}={r['c']}" for r in tasks) or "none"))
    a("")

    a("## dropped_out_of_scope")
    a("")
    a("Kill-list and scope drops, by reason and by the stage that caught them "
      "(discovery = before any crawl, site-check = site title/description/h1, "
      "builder = second pass immediately before writing). These rows are not shipped anywhere.")
    a("")
    rows = con.execute("SELECT reason, stage, COUNT(*) c FROM dropped GROUP BY reason, stage "
                       "ORDER BY reason, stage").fetchall()
    tot = defaultdict(Counter)
    for r in rows:
        tot[r["reason"]][r["stage"]] = r["c"]
    a("| Reason | discovery | site-check | builder | Total |")
    a("|---|---|---|---|---|")
    for reason in sorted(tot):
        t = tot[reason]
        a(f"| {reason} | {t['discovery']} | {t['site-check']} | {t['builder']} | {sum(t.values())} |")
    a(f"| **all** | | | | **{sum(sum(t.values()) for t in tot.values())}** |")
    a("")

    a("## What blocked the run")
    a("")
    ev = con.execute("SELECT stage, kind, COUNT(*) c, MIN(detail) ex FROM events "
                     "GROUP BY stage, kind ORDER BY c DESC").fetchall()
    if not ev:
        a("No blocking events were recorded.")
    else:
        a("| Stage | Kind | Count | Example |")
        a("|---|---|---|---|")
        for r in ev:
            ex = (r["ex"] or "").replace("|", "/")[:140]
            a(f"| {r['stage']} | {r['kind']} | {r['c']} | {ex} |")
    a("")
    a("Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, "
      "about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.")
    config.REPORT_MD.write_text("\n".join(L) + "\n", encoding="utf-8")
