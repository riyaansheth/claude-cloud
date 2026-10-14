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

## Enrich worker (round 2, given SHARD=k)
Goal: turn leads in cities that have NO qualified lead yet into qualified ones (2 of 3: real email,
personal LinkedIn of a named owner, direct/mobile number ≠ main line from the business's own site/socials).
Targets: `leadrun_diamonds/work/enrich/shard_<k>.json` — each item has `file` (a raw JSON you edit IN PLACE,
keeping every other field), `have` (criteria it already meets) and `website`.
For each target:
1. Re-confirm it is diamond TRADE (AGENT_BRIEF Wave-4 rules); if not, set is_diamond_trade=false + drop_reason.
2. Owner: About/Team/Contact pages; else BBB profile "Business Management", OpenCorporates officers, LinkedIn
   company "People" snippets in search results, press/JCK/National Jeweler articles. Set contact_person, role,
   contact_source.
3. LinkedIn: WebSearch mode "extended" `"First Last" <Business> <city> LinkedIn` (and a variant without city).
   Record only a linkedin.com/in/ URL that literally appears and is tied to that person + business.
4. Email: mailto/text on own site pages (also /contact-us, /appointment, footer), Facebook "About"
   (mbasic.facebook.com/<page>/about), Instagram bio via search snippet. Domain must relate to the business
   (or a personal freemail the business itself publishes). Set email + email_source.
5. Direct line: every extra tel: number on the own site / socials into tel_numbers, tel_source = own URL(s) only.
Set `"enriched": true` on every target you processed. Budget ≤ 120 WebSearch calls; use up to 4 subagents
(split your shard by city). Commit ONLY the raw files you edited; push to your outcome branch after every
~10 targets. Report: targets, now-qualified estimate, owners, LinkedIn, emails, direct lines found, drops.

## Round-3 worker (given CITIES list and OUT=w6_<k>) — full process, new cities
1. `cd leadrun_diamonds && python3 scripts/yp_discover.py --cities <CITIES...> --pages 3 --outdir <OUT>`
2. `python3 scripts/yp_discover.py --cities <CITIES...> --pages 1 --outdir <OUT> --terms "diamond brokers" "diamond cutters" "diamond buyers"`
3. Also WebSearch (≤ 10 calls) for each city's diamond trade beyond YellowPages — e.g. `"diamond wholesaler" <city>`,
   `"loose diamonds" wholesale <city>`, `"diamond dealer" <city> LinkedIn owner` — and write any real trade
   businesses you find as new raw JSON files in `raw/<OUT>/` (AGENT_BRIEF schema, lead_origin "Web Search"/"LinkedIn").
4. `python3 scripts/ingest.py && python3 scripts/crawl.py --workers 12`
5. `python3 scripts/make_batches.py --dir <OUT> --out batches_<OUT> --size 25`
6. For every listing in those batches do BOTH Wave-4 (scope verdict, verified=true) AND the Enrich steps
   (owner, LinkedIn, email, direct line; enriched=true) — editing the raw files in place. Up to 4 subagents.
7. Commit ONLY `leadrun_diamonds/raw/<OUT>/`; push to your outcome branch after every batch.
Report: listings scraped, verified, in scope, dropped by reason, owners, LinkedIn, emails, direct lines, and
which of your cities you think now have at least one lead meeting 2 of 3.
