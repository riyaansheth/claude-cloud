# Cloud worker playbook — diamond lead run

You are one of several parallel cloud workers. You own ONE folder: `leadrun_diamonds/raw/<OUT>/`
(and, for verify-only workers, the `raw/yp/` files of the markets you are given). Touch nothing else.
Read `leadrun_diamonds/AGENT_BRIEF.md` (all sections, esp. Wave-3 and Wave-4) — its rules apply to you.
Never fabricate; every value must come from a page or search result you saw.

## Scrape worker (given SHARD=i/n and OUT=w5_<i>)
1. `cd leadrun_diamonds && python3 scripts/yp_discover.py --skip-first 16 --shard <SHARD> --pages 3 --outdir <OUT>`
2. Second pass for more trade listings in the same cities:
   `python3 scripts/yp_discover.py --skip-first 16 --shard <SHARD> --pages 1 --outdir <OUT> --terms "diamond brokers" "diamond cutters"`
3. `python3 scripts/ingest.py && python3 scripts/crawl.py --workers 12` (local only — gives emails to prioritise)
4. `python3 scripts/make_batches.py --dir <OUT> --out batches_<OUT> --size 25`
5. Verify + enrich every listing in `work/batches_<OUT>/batch_*.json` per AGENT_BRIEF "Wave-4" — edit the raw
   JSON files in place, set `verified: true`. You may run up to 4 subagents in parallel, one batch each;
   give each the Wave-4 section and its batch file. Prioritise batches with emails (batch_01 first).
6. Commit ONLY `leadrun_diamonds/raw/<OUT>/` and push to your outcome branch. Commit + push after every
   finished batch, so partial work is never lost. Do not commit progress.sqlite3 or CSV/XLSX outputs.

## Verify-only worker (given MARKETS and OUT=yp)
1. `cd leadrun_diamonds && python3 scripts/ingest.py && python3 scripts/crawl.py --workers 12`
2. `python3 scripts/make_batches.py --dir yp --markets <MARKETS...> --out batches_v<k> --size 25`
3. Step 5 above on those batches (edit `raw/yp/*.json` of your markets only).
4. Commit ONLY those `leadrun_diamonds/raw/yp/*.json` files; push to your outcome branch after every batch.

Finish with: listings scraped, verified, in scope, dropped (by reason), owners found, LinkedIn found, emails found.
