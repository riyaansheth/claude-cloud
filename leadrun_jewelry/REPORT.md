# Jewelry retail lead run — REPORT

Generated 2026-10-13T16:08:34+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

> **Run outcome: no data collected.** The environment's network egress policy refused the connection (proxy CONNECT 403) to every discovery and enrichment source: American Gem Society, Arbitrary business site, BBB, Bing, DuckDuckGo HTML, Facebook mbasic, Google Maps, Instagram, Jewelers of America, OpenStreetMap Overpass, YellowPages. No listings were discovered, so nothing was crawled and both CSVs contain only the header row. Nothing was filled from memory. Allow these hosts (or run on an unrestricted machine) and re-run `python3 run.py all`.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 0 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 0 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 0 |
| Qualification rate | — |
| Websites crawled OK / attempted | 0 / 0 |
| Listings with an owner/decision-maker name | 0 |
| LinkedIn searches by outcome | — |
| **Shortfall vs 100 qualified** | **100** (not padded) |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 0 (—) | 0 (—) |
| 2 | Segment | 0 (—) | 0 (—) |
| 3 | Category (as listed) | 0 (—) | 0 (—) |
| 4 | Phone | 0 (—) | 0 (—) |
| 5 | Email | 0 (—) | 0 (—) |
| 6 | LinkedIn Profile | 0 (—) | 0 (—) |
| 7 | Contact Person | 0 (—) | 0 (—) |
| 8 | Role | 0 (—) | 0 (—) |
| 9 | Website | 0 (—) | 0 (—) |
| 10 | Address | 0 (—) | 0 (—) |
| 11 | Real City | 0 (—) | 0 (—) |
| 12 | Real State | 0 (—) | 0 (—) |
| 13 | Market | 0 (—) | 0 (—) |
| 14 | Lead Origin | 0 (—) | 0 (—) |
| 15 | Rating | 0 (—) | 0 (—) |
| 16 | Reviews | 0 (—) | 0 (—) |
| 17 | Source | 0 (—) | 0 (—) |
| 18 | Signals | 0 (—) | 0 (—) |
| 19 | Match Type | 0 (—) | 0 (—) |
| 20 | Email Source | 0 (—) | 0 (—) |
| 21 | LinkedIn Source | 0 (—) | 0 (—) |
| 22 | Found At | 0 (—) | 0 (—) |
| 23 | Also Listed As | 0 (—) | 0 (—) |
| 24 | Other Markets | 0 (—) | 0 (—) |
| 25 | Merged Listings | 0 (—) | 0 (—) |
| 26 | Flags | 0 (—) | 0 (—) |
| 27 | Mobile Candidates | 0 (—) | 0 (—) |
| 28 | Socials | 0 (—) | 0 (—) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 0 | 0 | 0 | 0 | 0 | 0 |
| Los Angeles, CA | 0 | 0 | 0 | 0 | 0 | 0 |
| Chicago, IL | 0 | 0 | 0 | 0 | 0 | 0 |
| Houston, TX | 0 | 0 | 0 | 0 | 0 | 0 |
| Dallas, TX | 0 | 0 | 0 | 0 | 0 | 0 |
| Miami, FL | 0 | 0 | 0 | 0 | 0 | 0 |
| Atlanta, GA | 0 | 0 | 0 | 0 | 0 | 0 |
| Philadelphia, PA | 0 | 0 | 0 | 0 | 0 | 0 |
| San Francisco, CA | 0 | 0 | 0 | 0 | 0 | 0 |
| Boston, MA | 0 | 0 | 0 | 0 | 0 | 0 |
| Seattle, WA | 0 | 0 | 0 | 0 | 0 | 0 |
| Las Vegas, NV | 0 | 0 | 0 | 0 | 0 | 0 |
| Phoenix, AZ | 0 | 0 | 0 | 0 | 0 | 0 |
| San Diego, CA | 0 | 0 | 0 | 0 | 0 | 0 |
| Denver, CO | 0 | 0 | 0 | 0 | 0 | 0 |
| Washington, DC | 0 | 0 | 0 | 0 | 0 | 0 |
| Detroit, MI | 0 | 0 | 0 | 0 | 0 | 0 |
| Minneapolis, MN | 0 | 0 | 0 | 0 | 0 | 0 |
| Charlotte, NC | 0 | 0 | 0 | 0 | 0 | 0 |
| Nashville, TN | 0 | 0 | 0 | 0 | 0 | 0 |
| Scottsdale, AZ | 0 | 0 | 0 | 0 | 0 | 0 |
| Naples, FL | 0 | 0 | 0 | 0 | 0 | 0 |
| Greenwich, CT | 0 | 0 | 0 | 0 | 0 | 0 |
| Palm Beach, FL | 0 | 0 | 0 | 0 | 0 | 0 |
| Beverly Hills, CA | 0 | 0 | 0 | 0 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|

Discovery tasks completed: none

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| **all** | | | | **0** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| osm | egress-blocked | 30 | egress-blocked overpass-api.de: HTTPSConnectionPool(host='overpass-api.de', port=443): Max retries exceeded with url: /api/interpreter (Caus |
| trade | blocked | 20 | egress-blocked https://www.americangemsociety.org/find-a-jeweler/?location=Atlanta%2C+GA |
| preflight | egress-blocked | 11 | American Gem Society: https://www.americangemsociety.org/ |
| bbb | blocked | 1 | egress-blocked https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Category&page=1 |
| gmaps | blocked | 1 | egress-blocked https://www.google.com/maps/search/jewelry+store+New+York%2C+NY?hl=en |
| yp | blocked | 1 | egress-blocked https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=New+York%2C+NY&page=1 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
