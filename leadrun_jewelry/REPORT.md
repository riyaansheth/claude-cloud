# Jewelry retail lead run — REPORT

Generated 2026-10-14T02:11:06+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 15016 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10506 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 266 |
| Qualification rate | 2.5% |
| Websites crawled OK / attempted | 7797 / 9292 |
| Listings with an owner/decision-maker name | 1625 |
| LinkedIn searches by outcome | ambiguous: 57, match: 45, none: 210, reject: 16 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10506 (100.0%) | 266 (100.0%) |
| 2 | Segment | 10506 (100.0%) | 266 (100.0%) |
| 3 | Category (as listed) | 10491 (99.9%) | 266 (100.0%) |
| 4 | Phone | 9845 (93.7%) | 260 (97.7%) |
| 5 | Email | 2307 (22.0%) | 262 (98.5%) |
| 6 | LinkedIn Profile | 39 (0.4%) | 33 (12.4%) |
| 7 | Contact Person | 795 (7.6%) | 112 (42.1%) |
| 8 | Role | 795 (7.6%) | 112 (42.1%) |
| 9 | Website | 8125 (77.3%) | 266 (100.0%) |
| 10 | Address | 10077 (95.9%) | 265 (99.6%) |
| 11 | Real City | 8644 (82.3%) | 229 (86.1%) |
| 12 | Real State | 8739 (83.2%) | 228 (85.7%) |
| 13 | Market | 10506 (100.0%) | 266 (100.0%) |
| 14 | Lead Origin | 10506 (100.0%) | 266 (100.0%) |
| 15 | Rating | 3074 (29.3%) | 138 (51.9%) |
| 16 | Reviews | 3074 (29.3%) | 138 (51.9%) |
| 17 | Source | 10506 (100.0%) | 266 (100.0%) |
| 18 | Signals | 10506 (100.0%) | 266 (100.0%) |
| 19 | Match Type | 10506 (100.0%) | 266 (100.0%) |
| 20 | Email Source | 2307 (22.0%) | 262 (98.5%) |
| 21 | LinkedIn Source | 39 (0.4%) | 33 (12.4%) |
| 22 | Found At | 10506 (100.0%) | 266 (100.0%) |
| 23 | Also Listed As | 1286 (12.2%) | 75 (28.2%) |
| 24 | Other Markets | 233 (2.2%) | 22 (8.3%) |
| 25 | Merged Listings | 2235 (21.3%) | 119 (44.7%) |
| 26 | Flags | 1290 (12.3%) | 49 (18.4%) |
| 27 | Mobile Candidates | 328 (3.1%) | 240 (90.2%) |
| 28 | Socials | 2206 (21.0%) | 232 (87.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2307 | 22.0% |
| linkedin | 39 | 0.4% |
| direct-line | 328 | 3.1% |
| role-email | 1010 | 9.6% |
| gia | 618 | 5.9% |
| ags | 71 | 0.7% |
| ja | 42 | 0.4% |
| bench | 358 | 3.4% |
| custom-design | 1577 | 15.0% |
| since-yyyy | 1474 | 14.0% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1221 | 279 | 97 | 8 | 33 |
| Los Angeles, CA | 1280 | 1031 | 233 | 74 | 6 | 28 |
| Chicago, IL | 993 | 682 | 153 | 60 | 3 | 16 |
| Houston, TX | 1030 | 705 | 145 | 57 | 5 | 22 |
| Dallas, TX | 722 | 489 | 91 | 58 | 3 | 7 |
| Miami, FL | 1024 | 731 | 164 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 526 | 129 | 61 | 8 | 21 |
| Philadelphia, PA | 767 | 547 | 92 | 26 | 0 | 11 |
| San Francisco, CA | 732 | 443 | 123 | 66 | 0 | 8 |
| Boston, MA | 571 | 344 | 105 | 56 | 3 | 13 |
| Seattle, WA | 490 | 316 | 79 | 28 | 0 | 6 |
| Las Vegas, NV | 559 | 346 | 61 | 12 | 1 | 7 |
| Phoenix, AZ | 579 | 401 | 74 | 11 | 0 | 10 |
| San Diego, CA | 556 | 370 | 73 | 16 | 0 | 5 |
| Denver, CO | 397 | 279 | 83 | 11 | 0 | 6 |
| Washington, DC | 347 | 202 | 63 | 14 | 0 | 5 |
| Detroit, MI | 457 | 332 | 64 | 11 | 0 | 10 |
| Minneapolis, MN | 250 | 164 | 48 | 10 | 0 | 2 |
| Charlotte, NC | 282 | 178 | 43 | 12 | 0 | 3 |
| Nashville, TN | 235 | 145 | 38 | 11 | 0 | 0 |
| Scottsdale, AZ | 186 | 125 | 28 | 5 | 0 | 4 |
| Naples, FL | 239 | 141 | 37 | 13 | 0 | 3 |
| Greenwich, CT | 136 | 78 | 23 | 5 | 0 | 4 |
| Palm Beach, FL | 406 | 249 | 46 | 6 | 0 | 3 |
| Beverly Hills, CA | 598 | 461 | 33 | 6 | 0 | 7 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3110 | 2006 | 89 |
| YellowPages | 9464 | 7114 | 102 |
| BBB | 1130 | 616 | 61 |
| OpenStreetMap | 1313 | 770 | 14 |

Discovery tasks completed: bbb=306, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 60 | 0 | 0 | 60 |
| beads-craft | 419 | 31 | 3 | 453 |
| chain | 2514 | 0 | 0 | 2514 |
| coin-currency | 143 | 7 | 0 | 150 |
| costume-fashion | 362 | 124 | 24 | 510 |
| diamond-trade | 130 | 29 | 7 | 166 |
| gold-buyer | 193 | 36 | 4 | 233 |
| kiosk-battery | 7 | 0 | 0 | 7 |
| no-segment | 0 | 0 | 652 | 652 |
| pawn | 599 | 29 | 14 | 642 |
| piercing-tattoo | 419 | 33 | 10 | 462 |
| simulants | 6 | 26 | 2 | 34 |
| thrift-consignment | 43 | 0 | 0 | 43 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 74 | 8 | 1 | 83 |
| **all** | | | | **6012** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1496 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 100 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 5 | http-429 or challenge page at https://www.google.com/search?q=%22Billy+Lulo%22+Los+Angeles+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
