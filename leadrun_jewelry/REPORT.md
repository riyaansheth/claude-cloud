# Jewelry retail lead run — REPORT

Generated 2026-10-14T03:46:00+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 15409 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10671 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 305 |
| Qualification rate | 2.9% |
| Websites crawled OK / attempted | 8443 / 10138 |
| Listings with an owner/decision-maker name | 1998 |
| LinkedIn searches by outcome | ambiguous: 84, match: 61, none: 246, reject: 19 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10671 (100.0%) | 305 (100.0%) |
| 2 | Segment | 10671 (100.0%) | 305 (100.0%) |
| 3 | Category (as listed) | 10650 (99.8%) | 305 (100.0%) |
| 4 | Phone | 9994 (93.7%) | 299 (98.0%) |
| 5 | Email | 2491 (23.3%) | 300 (98.4%) |
| 6 | LinkedIn Profile | 56 (0.5%) | 50 (16.4%) |
| 7 | Contact Person | 998 (9.4%) | 140 (45.9%) |
| 8 | Role | 998 (9.4%) | 140 (45.9%) |
| 9 | Website | 8194 (76.8%) | 305 (100.0%) |
| 10 | Address | 10230 (95.9%) | 303 (99.3%) |
| 11 | Real City | 8817 (82.6%) | 262 (85.9%) |
| 12 | Real State | 8912 (83.5%) | 261 (85.6%) |
| 13 | Market | 10671 (100.0%) | 305 (100.0%) |
| 14 | Lead Origin | 10671 (100.0%) | 305 (100.0%) |
| 15 | Rating | 3051 (28.6%) | 157 (51.5%) |
| 16 | Reviews | 3051 (28.6%) | 157 (51.5%) |
| 17 | Source | 10671 (100.0%) | 305 (100.0%) |
| 18 | Signals | 10671 (100.0%) | 305 (100.0%) |
| 19 | Match Type | 10671 (100.0%) | 305 (100.0%) |
| 20 | Email Source | 2491 (23.3%) | 300 (98.4%) |
| 21 | LinkedIn Source | 56 (0.5%) | 50 (16.4%) |
| 22 | Found At | 10671 (100.0%) | 305 (100.0%) |
| 23 | Also Listed As | 1329 (12.5%) | 82 (26.9%) |
| 24 | Other Markets | 242 (2.3%) | 24 (7.9%) |
| 25 | Merged Listings | 2289 (21.5%) | 130 (42.6%) |
| 26 | Flags | 1356 (12.7%) | 56 (18.4%) |
| 27 | Mobile Candidates | 355 (3.3%) | 263 (86.2%) |
| 28 | Socials | 2414 (22.6%) | 266 (87.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2491 | 23.3% |
| linkedin | 56 | 0.5% |
| direct-line | 355 | 3.3% |
| role-email | 1085 | 10.2% |
| gia | 651 | 6.1% |
| ags | 76 | 0.7% |
| ja | 45 | 0.4% |
| bench | 379 | 3.6% |
| custom-design | 1678 | 15.7% |
| since-yyyy | 1793 | 16.8% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1229 | 283 | 97 | 9 | 34 |
| Los Angeles, CA | 1280 | 1033 | 235 | 76 | 7 | 30 |
| Chicago, IL | 993 | 688 | 154 | 64 | 3 | 17 |
| Houston, TX | 1030 | 703 | 146 | 58 | 5 | 22 |
| Dallas, TX | 722 | 489 | 91 | 58 | 4 | 9 |
| Miami, FL | 1024 | 735 | 166 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 527 | 128 | 62 | 8 | 20 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 2 | 13 |
| San Francisco, CA | 732 | 447 | 125 | 67 | 1 | 9 |
| Boston, MA | 570 | 346 | 109 | 56 | 5 | 16 |
| Seattle, WA | 589 | 351 | 93 | 70 | 1 | 9 |
| Las Vegas, NV | 691 | 404 | 75 | 75 | 3 | 12 |
| Phoenix, AZ | 730 | 471 | 96 | 57 | 0 | 12 |
| San Diego, CA | 588 | 382 | 80 | 33 | 1 | 6 |
| Denver, CO | 396 | 279 | 89 | 14 | 3 | 11 |
| Washington, DC | 347 | 203 | 68 | 14 | 1 | 6 |
| Detroit, MI | 457 | 330 | 66 | 11 | 0 | 11 |
| Minneapolis, MN | 250 | 165 | 50 | 11 | 0 | 2 |
| Charlotte, NC | 282 | 180 | 44 | 13 | 0 | 3 |
| Nashville, TN | 234 | 143 | 38 | 11 | 1 | 1 |
| Scottsdale, AZ | 184 | 117 | 31 | 6 | 0 | 4 |
| Naples, FL | 239 | 140 | 40 | 13 | 0 | 4 |
| Greenwich, CT | 136 | 78 | 23 | 5 | 0 | 4 |
| Palm Beach, FL | 401 | 244 | 63 | 10 | 0 | 6 |
| Beverly Hills, CA | 586 | 442 | 106 | 20 | 0 | 12 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1978 | 104 |
| YellowPages | 9439 | 7091 | 115 |
| BBB | 1549 | 836 | 72 |
| OpenStreetMap | 1313 | 766 | 14 |

Discovery tasks completed: bbb=411, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 63 | 0 | 0 | 63 |
| beads-craft | 422 | 34 | 3 | 459 |
| chain | 2605 | 0 | 0 | 2605 |
| coin-currency | 149 | 7 | 0 | 156 |
| costume-fashion | 369 | 136 | 31 | 536 |
| diamond-trade | 133 | 29 | 7 | 169 |
| gold-buyer | 203 | 36 | 5 | 244 |
| kiosk-battery | 7 | 0 | 0 | 7 |
| no-segment | 0 | 0 | 683 | 683 |
| pawn | 614 | 37 | 14 | 665 |
| piercing-tattoo | 442 | 36 | 11 | 489 |
| simulants | 6 | 35 | 2 | 43 |
| thrift-consignment | 44 | 0 | 0 | 44 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 74 | 8 | 1 | 83 |
| **all** | | | | **6249** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1715 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 129 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 7 | http-429 or challenge page at https://www.google.com/search?q=%22Anthony+Pampillonia%22+Dallas+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
