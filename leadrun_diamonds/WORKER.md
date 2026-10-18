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

## People worker (given MARKETS and OUT=p_<k>) — person-level LinkedIn leads
Goal: up to 100 real people per market who work at US diamond-TRADE firms (owners, presidents, partners,
buyers, diamond sales, brokers, GIA graduates at wholesalers/manufacturers/importers/bourse members),
each with a personal linkedin.com/in/ URL. Quality over count: never pad, never invent.
1. Company list: start from `leadrun_diamonds/diamonds_all.csv` rows whose Market is yours (in-scope firms),
   then add more diamond-trade firms in your market from WebSearch / directories.
2. For each firm, WebSearch (mode "extended") e.g. `<Company> <city> diamonds LinkedIn`,
   `"<Company>" owner OR president OR sales LinkedIn`, `site:linkedin.com/in "<Company>"`,
   and market sweeps like `"diamond wholesaler" <city> LinkedIn`, `"diamond buyer" <city> LinkedIn`,
   `"GIA Graduate Gemologist" <city> diamonds LinkedIn`, `"47th Street" diamonds LinkedIn` (NYC).
3. Record a person ONLY if a linkedin.com/in/ URL literally appears in a result and the result ties that
   named person to a diamond-trade firm in your market. Never a /company/ page or a slug that is just the
   business name. Exclude retail-chain staff, pawn/gold buyers, simulants (AGENT_BRIEF kill-list).
4. Write one JSON per person to `leadrun_diamonds/raw_people/<OUT>/<slug>.json`:
   {"person","title","company","company_website","city","state","market","linkedin_url","linkedin_source",
    "company_email","company_phone","seniority" (owner/executive/manager/sales/other),"signals":[...],
    "source_url","is_diamond_trade":true}
   company_email/phone only if seen on the firm's own site or directory listing.
5. Budget: use your full WebSearch allowance (≈180 calls); up to 4 subagents, one market each.
   Commit ONLY `leadrun_diamonds/raw_people/<OUT>/`, push to your outcome branch every ~25 people.
Report: people per market, firms covered, what limited the count.

## LinkedIn backfill worker (given SHARD=k)
Targets: `leadrun_diamonds/work/li/shard_<k>.json` — in-scope businesses that have NO personal LinkedIn.
For each: (1) if `contact` is empty, find the owner/president name (About/Team/Contact page with requests,
BBB "Business Management", OpenCorporates officers, press) and set contact_person/role/contact_source;
(2) WebSearch mode "extended" `"First Last" <Business> LinkedIn` (and with city); record linkedin_url only if a
linkedin.com/in/ URL literally appears tied to that person + business; set linkedin_source. Edit the raw
`file` IN PLACE (keep all other fields), set `"li_backfill": true` even when nothing is found.
Prioritise items with "qualified": true or a contact name. Up to 4 subagents. Commit ONLY the raw files you
edited; push to your outcome branch every ~20 targets. Report: targets, names found, LinkedIn found.

## Qualify-push worker (given MARKETS and OUT=w13_<k>) — target 50 QUALIFIED per market
Goal: raise the number of QUALIFIED leads (2 of 3: real email / personal LinkedIn of a named owner /
direct line ≠ main line) in your markets to 50 each, or until the market is honestly exhausted.
Never fabricate — an unfilled field beats an invented one. Budget ≤ 120 WebSearch calls total.

0. Measure first: `python3 scripts/ingest.py && python3 scripts/build.py`, then count rows per market in
   `diamonds_qualified.csv` vs `diamonds_all.csv`. Re-run this after every ~20 edits to track progress.
1. UPGRADE existing leads (cheapest wins first). For every row in `diamonds_all.csv` in your markets that is
   NOT in `diamonds_qualified.csv`: find its raw JSON (`grep -rl '"<business>"' raw/`), then fill what is
   missing — fetch the business's own site `/`, `/contact`, `/about`, `/team` with Bash+requests for
   `mailto:` emails and `tel:` numbers (tel_source = own page URLs only); find the owner/founder name; then
   WebSearch (mode "extended") `"First Last" <Business> LinkedIn` and record a linkedin.com/in/ URL only if it
   literally appears and ties to this business. Edit the raw file IN PLACE (keep all fields, set
   "enriched": true). Rows flagged out of scope stay out — do not re-scope them.
2. DISCOVER new trade businesses in your markets until you reach the target: building/tenant directories
   (e.g. NYC International Gem Tower, 580 Fifth Ave, 20/36/55/62/71 W 47th St; LA St. Vincent Jewelry Center,
   International Jewelry Center, California Jewelry Mart; Miami Seybold Building; Chicago Mallers / 5 S
   Wabash; Houston/Dallas jewelry marts), DDC / DMIA / JBT / AGS / bourse member lists, JCK Las Vegas exhibitor
   lists with addresses in your market, and searches like `"diamond wholesaler" <market> owner LinkedIn`.
   Prefer businesses that publish an email and a named owner — those qualify. Write each as a new raw JSON in
   `raw/<OUT>/` (AGENT_BRIEF schema). Check `ls raw/*/` for the slug first; never duplicate.
3. Commit ONLY files under `leadrun_diamonds/raw/` (your OUT dir plus the raw files you upgraded in place);
   push to your outcome branch every ~20 files and at the end.
Report per market: qualified before → after, new businesses added, upgrades made (emails / LinkedIn /
direct lines), and why the market stopped short of 50 if it did.
