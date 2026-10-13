# Narrow-end subagents

Subagents are used **only** on small, pre-filtered batches. They are never pointed at
the wide end (the thousands of discovered listings). Two jobs:

1. **Owner name from an About/Team page.** These are businesses whose crawled
   About/Team/Story page had text but no name that the regex could pick out.
   Measured: 8 parallel agents on 80 businesses found a name for 49% of them,
   against 7% for regex, in 1m46s.
2. **LinkedIn judging.** These are name-only search hits that `linkedin.judge()` marked
   `ambiguous`.

## Loop

```bash
python3 run.py agents-export      # writes agent_queue/names_NNN.jsonl (10 items each, max 8 batches)
# launch one subagent per batch file, in parallel (prompt below)
python3 run.py agents-import      # validates + stores answers, then:
python3 run.py linkedin           # search the newly named humans
python3 run.py build
```

## Prompt: owner name (one agent per `names_NNN.jsonl`)

> Read `leadrun_jewelry/agent_queue/names_NNN.jsonl`. Each line has `bkey`, `business`,
> `source_url` and `text`, which is the visible text of that business's About/Team page.
> For each line, find the owner or main decision-maker, if the text names one.
> Answer **only from `text`**. Do not browse, and do not use outside knowledge.
> The name must appear in `text` exactly as you write it, with a first and a last name.
> Skip the line if the only name is a first name, or a name that just repeats the
> business name. Use one of these roles: Owner, President, Founder, Manager, Partner,
> Member, Featured On About Page. Write
> `agent_queue/names_NNN_answers.jsonl` with one JSON object per answered line:
> `{"bkey": ..., "name": "First Last", "role": ..., "evidence": "<the sentence you used>"}`.

`agents-import` rejects any answer whose name does not literally appear in the page
text that was supplied. Accepted names keep that page as their source URL.

## Prompt: LinkedIn judging (`linkedin_000.jsonl`)

> Each line has a `person` and `business` (with city/market), a candidate LinkedIn
> `url`, and the search-result `evidence` (the title and snippet). Using only that
> evidence, decide whether the profile is the same human who owns or runs this
> jewelry business. Answer `match` only when the evidence ties the person to jewelry,
> to this business, or to this city. A slug that restates the business name
> (`linkedin.com/in/silversunalbuquerque`) is a company vanity page: reject it.
> Write `linkedin_000_answers.jsonl` with
> `{"bkey": ..., "person": ..., "verdict": "match"|"reject"}`.
