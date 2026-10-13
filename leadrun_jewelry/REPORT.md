# Jewelry retail lead run — REPORT

Generated 2026-10-14T02:32:26+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 15081 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10534 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 283 |
| Qualification rate | 2.7% |
| Websites crawled OK / attempted | 8267 / 9862 |
| Listings with an owner/decision-maker name | 1730 |
| LinkedIn searches by outcome | ambiguous: 63, match: 45, none: 217, reject: 16 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10534 (100.0%) | 283 (100.0%) |
| 2 | Segment | 10534 (100.0%) | 283 (100.0%) |
| 3 | Category (as listed) | 10519 (99.9%) | 283 (100.0%) |
| 4 | Phone | 9867 (93.7%) | 277 (97.9%) |
| 5 | Email | 2430 (23.1%) | 278 (98.2%) |
| 6 | LinkedIn Profile | 40 (0.4%) | 34 (12.0%) |
| 7 | Contact Person | 861 (8.2%) | 119 (42.0%) |
| 8 | Role | 861 (8.2%) | 119 (42.0%) |
| 9 | Website | 8125 (77.1%) | 283 (100.0%) |
| 10 | Address | 10103 (95.9%) | 281 (99.3%) |
| 11 | Real City | 8678 (82.4%) | 244 (86.2%) |
| 12 | Real State | 8773 (83.3%) | 243 (85.9%) |
| 13 | Market | 10534 (100.0%) | 283 (100.0%) |
| 14 | Lead Origin | 10534 (100.0%) | 283 (100.0%) |
| 15 | Rating | 3054 (29.0%) | 143 (50.5%) |
| 16 | Reviews | 3054 (29.0%) | 143 (50.5%) |
| 17 | Source | 10534 (100.0%) | 283 (100.0%) |
| 18 | Signals | 10534 (100.0%) | 283 (100.0%) |
| 19 | Match Type | 10534 (100.0%) | 283 (100.0%) |
| 20 | Email Source | 2430 (23.1%) | 278 (98.2%) |
| 21 | LinkedIn Source | 40 (0.4%) | 34 (12.0%) |
| 22 | Found At | 10534 (100.0%) | 283 (100.0%) |
| 23 | Also Listed As | 1296 (12.3%) | 78 (27.6%) |
| 24 | Other Markets | 235 (2.2%) | 24 (8.5%) |
| 25 | Merged Listings | 2240 (21.3%) | 123 (43.5%) |
| 26 | Flags | 1310 (12.4%) | 53 (18.7%) |
| 27 | Mobile Candidates | 347 (3.3%) | 257 (90.8%) |
| 28 | Socials | 2338 (22.2%) | 246 (86.9%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2430 | 23.1% |
| linkedin | 40 | 0.4% |
| direct-line | 347 | 3.3% |
| role-email | 1060 | 10.1% |
| gia | 637 | 6.0% |
| ags | 73 | 0.7% |
| ja | 44 | 0.4% |
| bench | 370 | 3.5% |
| custom-design | 1639 | 15.6% |
| since-yyyy | 1586 | 15.1% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1230 | 284 | 97 | 8 | 33 |
| Los Angeles, CA | 1280 | 1035 | 235 | 75 | 6 | 29 |
| Chicago, IL | 993 | 688 | 154 | 64 | 3 | 17 |
| Houston, TX | 1030 | 703 | 146 | 57 | 5 | 22 |
| Dallas, TX | 722 | 490 | 92 | 58 | 3 | 8 |
| Miami, FL | 1024 | 735 | 166 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 527 | 128 | 62 | 8 | 20 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 1 | 12 |
| San Francisco, CA | 732 | 448 | 126 | 67 | 0 | 9 |
| Boston, MA | 570 | 346 | 109 | 56 | 3 | 14 |
| Seattle, WA | 579 | 346 | 88 | 68 | 0 | 7 |
| Las Vegas, NV | 558 | 344 | 64 | 13 | 1 | 7 |
| Phoenix, AZ | 575 | 398 | 78 | 11 | 0 | 11 |
| San Diego, CA | 555 | 370 | 80 | 19 | 0 | 5 |
| Denver, CO | 396 | 279 | 89 | 14 | 0 | 8 |
| Washington, DC | 347 | 203 | 68 | 14 | 0 | 5 |
| Detroit, MI | 457 | 330 | 66 | 11 | 0 | 11 |
| Minneapolis, MN | 250 | 165 | 50 | 11 | 0 | 2 |
| Charlotte, NC | 282 | 180 | 44 | 12 | 0 | 3 |
| Nashville, TN | 234 | 143 | 38 | 11 | 0 | 0 |
| Scottsdale, AZ | 184 | 121 | 30 | 5 | 0 | 4 |
| Naples, FL | 239 | 140 | 40 | 13 | 0 | 4 |
| Greenwich, CT | 136 | 78 | 23 | 5 | 0 | 4 |
| Palm Beach, FL | 401 | 244 | 60 | 9 | 0 | 6 |
| Beverly Hills, CA | 588 | 446 | 80 | 12 | 0 | 10 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1984 | 91 |
| YellowPages | 9441 | 7115 | 114 |
| BBB | 1218 | 663 | 64 |
| OpenStreetMap | 1313 | 772 | 14 |

Discovery tasks completed: bbb=319, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 62 | 0 | 0 | 62 |
| beads-craft | 420 | 32 | 3 | 455 |
| chain | 2521 | 0 | 0 | 2521 |
| coin-currency | 143 | 7 | 0 | 150 |
| costume-fashion | 365 | 133 | 26 | 524 |
| diamond-trade | 130 | 29 | 7 | 166 |
| gold-buyer | 193 | 36 | 4 | 233 |
| kiosk-battery | 7 | 0 | 0 | 7 |
| no-segment | 0 | 0 | 649 | 649 |
| pawn | 601 | 37 | 14 | 652 |
| piercing-tattoo | 424 | 35 | 10 | 469 |
| simulants | 6 | 32 | 2 | 40 |
| thrift-consignment | 43 | 0 | 0 | 43 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 74 | 8 | 1 | 83 |
| **all** | | | | **6057** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1595 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 108 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 5 | http-429 or challenge page at https://www.google.com/search?q=%22Billy+Lulo%22+Los+Angeles+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
