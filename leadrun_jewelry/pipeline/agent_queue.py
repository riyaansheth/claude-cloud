"""Narrow-end subagent work (never the wide end).

export: writes small batches to agent_queue/
  names_NNN.jsonl    — businesses with About/Team text but no regex owner name
  linkedin_NNN.jsonl — name-only LinkedIn hits that need a human-judgement call
Each line carries the exact source URL + text; the agent may only answer from
that text. See AGENTS.md for the prompt the orchestrator gives each subagent.

import: reads *_answers.jsonl written by the agents and stores them, keeping the
source URL the agent read. Answers without a source URL, or with a name that is
not literally present in the supplied text, are rejected (no fabrication).
"""
import json
import re

from . import config, db
from .util import plausible_name

BATCH = 10


def export(max_batches=8, log=print):
    con = db.connect()
    config.AGENT_DIR.mkdir(parents=True, exist_ok=True)
    have_people = {r["bkey"] for r in con.execute("SELECT DISTINCT bkey FROM people")}
    queued = set()
    for f in config.AGENT_DIR.glob("names_*.jsonl"):
        for line in f.read_text().splitlines():
            if line.strip():
                queued.add(json.loads(line)["bkey"])
    items = []
    for c in con.execute("SELECT root, result FROM crawls WHERE status='ok'"):
        res = json.loads(c["result"])
        if not res.get("about_text") or len(res["about_text"]) < 200:
            continue
        for l in con.execute("SELECT bkey, name FROM listings WHERE website=?", (c["root"],)):
            if l["bkey"] in have_people or l["bkey"] in queued:
                continue
            items.append({"bkey": l["bkey"], "business": l["name"],
                          "source_url": res["about_url"], "text": res["about_text"][:5000]})
            break  # one per domain is enough
    n_batches = 0
    start = len(list(config.AGENT_DIR.glob("names_*.jsonl")))
    for i in range(0, min(len(items), max_batches * BATCH), BATCH):
        p = config.AGENT_DIR / f"names_{start + n_batches:03d}.jsonl"
        p.write_text("\n".join(json.dumps(x) for x in items[i:i + BATCH]) + "\n")
        n_batches += 1
    amb = con.execute("""SELECT k.bkey, k.person, k.url, k.search_url, k.evidence, l.name AS business,
                                l.city, l.market FROM linkedin k JOIN listings l USING(bkey)
                         WHERE k.status='ambiguous'""").fetchall()
    if amb:
        (config.AGENT_DIR / "linkedin_000.jsonl").write_text(
            "\n".join(json.dumps(dict(r)) for r in amb) + "\n")
    log(f"[agents] exported {n_batches} name batches ({len(items)} candidates), "
        f"{len(amb)} ambiguous LinkedIn hits")
    return {"name_batches": n_batches, "linkedin_ambiguous": len(amb)}


def import_answers(log=print):
    con = db.connect()
    texts = {}
    for f in config.AGENT_DIR.glob("names_[0-9]*.jsonl"):
        for line in f.read_text().splitlines():
            if line.strip():
                x = json.loads(line)
                texts[x["bkey"]] = x
    ok = rej = 0
    for f in config.AGENT_DIR.glob("names_*_answers.jsonl"):
        for line in f.read_text().splitlines():
            if not line.strip():
                continue
            a = json.loads(line)
            src = texts.get(a.get("bkey"))
            name = (a.get("name") or "").strip()
            if not src or not name:
                continue
            # The name must literally appear in the page text the agent was given.
            if (not re.search(re.escape(name), src["text"]) or not plausible_name(name, src["business"], need_given=False)):
                rej += 1
                continue
            db.add_person(con, a["bkey"], name, a.get("role") or "Featured On About Page",
                          src["source_url"], "agent-about", (a.get("evidence") or "")[:300])
            ok += 1
    lk = 0
    for f in config.AGENT_DIR.glob("linkedin_*_answers.jsonl"):
        for line in f.read_text().splitlines():
            if not line.strip():
                continue
            a = json.loads(line)
            verdict = "match" if a.get("verdict") == "match" else "reject"
            con.execute("UPDATE linkedin SET status=? WHERE bkey=? AND person=? AND status='ambiguous'",
                        (verdict, a["bkey"], a["person"]))
            lk += 1
    log(f"[agents] imported {ok} names ({rej} rejected), {lk} LinkedIn verdicts")
    return {"names": ok, "rejected": rej, "linkedin_verdicts": lk}
