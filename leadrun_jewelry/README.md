# leadrun_jewelry — jewelry retail B2B lead pipeline

This pipeline finds independent jewelry retailers in 25 US markets: stores, custom and
bench jewelers, goldsmiths and silversmiths, repair shops, estate and antique dealers,
and fine watch and jewelry boutiques. It enriches each one from free sources and writes
two files:

- `jewelry_qualified.csv`: rows that clear 2 of 3 (email, personal LinkedIn, direct line)
- `jewelry_all.csv`: every in-scope business researched
- `REPORT.md`: counts, fill rates, per-market and per-source tables,
  `dropped_out_of_scope` by reason, and what blocked the run

Both CSVs use the exact 28-column schema in `pipeline/config.py:COLUMNS`. Columns 1-26
match `usaENRICHEDleads.xlsx` without its two legacy verification columns. Columns 27-28
are working columns added at the end.

## Run

```bash
pip install -r requirements.txt          # Chromium: uses /opt/pw-browsers/chromium if present,
                                         # else `npx playwright install chromium`
python3 run.py preflight                 # are the source hosts reachable from here?
python3 run.py all --cities 10           # first 10 markets; --cities 0 = all 25
python3 -m pytest -q -p no:cacheprovider tests   # offline tests
```

Each stage can be run on its own, and all of them can be resumed:
`osm`, `gmaps`, `yp`, `bbb`, `trade`, `crawl`, `socials`, `linkedin`,
`agents-export`, `agents-import`, `build`, `status`.
`progress.sqlite3` keys everything by a stable business or listing key (`osm:node/123`,
`yp:<hash>`, `bbb:<hash>`, website root for crawls), never a row number. Re-running a
stage skips work that is already done, and `build` is deterministic.

## Stages

| Stage | What it does |
|---|---|
| `osm` | Overpass per-market bbox: `shop=jewelry`, `craft=jeweller/goldsmith/silversmith`, `shop=watches`. This is the volume base. |
| `gmaps` | Headless Chromium. Searches jewelry store, custom jewelry, jewelry repair, estate jewelry and goldsmith, and opens each place panel. |
| `yp` | YellowPages `/search?search_terms=jewelers&geo_location_terms=<city>`, paginated, through a real browser (curl gets a 403). |
| `bbb` | BBB category search (Jewelry Stores and Jewelry Repair). **Opens every profile page** and reads the Business Management block, which is the best source of owner names. |
| `trade` | Jewelers of America and AGS "find a jeweler" member lists. Membership is tagged `ja`/`ags` in Signals. |
| `crawl` | 16 concurrent workers. Fetches `/`, `/about`, `/about-us`, `/contact`, `/team`, `/our-story`, `/meet-the-jeweler` plus about/team links. Extracts mailto, regex and Cloudflare-obfuscated emails, every `tel:` number, socials, owner names, JSON-LD founder/address, and the signals GIA/AGS/JA, since-19xx, bench and custom-design. |
| `socials` | `mbasic.facebook.com/<page>/about` (page email and phone) and the Instagram bio/business email. |
| `linkedin` | Runs only after a name is known: `"First Last" <city> site:linkedin.com/in/` on Bing, then DuckDuckGo. It runs whether or not an email was found. |
| `agents-*` | Narrow-end subagent batches. See `AGENTS.md`. |
| `build` | Runs the kill-list a second time plus a site check, assigns a segment, dedupes with union-find (email, phone, domain, name+market; shared hosts and switchboards excluded), merges groups, qualifies 2 of 3, sets Flags (asserted), and writes the CSVs and REPORT.md. |

## Scope enforcement

`pipeline/scope.py` holds the HARD EXCLUSION KILL-LIST: pawn, gold buyers, coins,
beads and craft, costume and fashion, piercing and tattoo, kiosks and batteries,
simulants, chains and department stores, thrift and consignment, and appraisers, labs
and insurers. It also holds the diamond-trade carve-out (wholesalers, brokers, loose
diamonds, cutters, diamond-district trade offices).

The kill-list is applied at discovery, before any crawl is spent. It runs again on the
site's title, meta description and h1 after the crawl. The builder applies it twice more:
once per listing, and once immediately before each merged row is written. Dropped
businesses go only into the `dropped` table and the REPORT counts. They are never shipped.

## After the cloud run (on the Mac)

1. Download `jewelry_all.csv` to `~/lead-pipeline-work/us109/newleads/`.
2. Run `python3 merge_leads.py` to fold it into the working pool, then rebuild the sheet.

These scripts write only inside `leadrun_jewelry/`. Nothing here touches
`~/Downloads/leads250 cities/usaENRICHEDleads.xlsx`.
