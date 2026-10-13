# Jewelry retail lead run — REPORT

Generated 2026-10-14T01:50:53+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 14416 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10121 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 235 |
| Qualification rate | 2.3% |
| Websites crawled OK / attempted | 6727 / 8025 |
| Listings with an owner/decision-maker name | 1543 |
| LinkedIn searches by outcome | ambiguous: 60, match: 40, none: 205, reject: 11 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10121 (100.0%) | 235 (100.0%) |
| 2 | Segment | 10121 (100.0%) | 235 (100.0%) |
| 3 | Category (as listed) | 10106 (99.9%) | 235 (100.0%) |
| 4 | Phone | 9468 (93.5%) | 231 (98.3%) |
| 5 | Email | 2075 (20.5%) | 232 (98.7%) |
| 6 | LinkedIn Profile | 34 (0.3%) | 28 (11.9%) |
| 7 | Contact Person | 746 (7.4%) | 100 (42.6%) |
| 8 | Role | 746 (7.4%) | 100 (42.6%) |
| 9 | Website | 7817 (77.2%) | 235 (100.0%) |
| 10 | Address | 9702 (95.9%) | 234 (99.6%) |
| 11 | Real City | 8205 (81.1%) | 202 (86.0%) |
| 12 | Real State | 8300 (82.0%) | 201 (85.5%) |
| 13 | Market | 10121 (100.0%) | 235 (100.0%) |
| 14 | Lead Origin | 10121 (100.0%) | 235 (100.0%) |
| 15 | Rating | 3060 (30.2%) | 124 (52.8%) |
| 16 | Reviews | 3060 (30.2%) | 124 (52.8%) |
| 17 | Source | 10121 (100.0%) | 235 (100.0%) |
| 18 | Signals | 10121 (100.0%) | 235 (100.0%) |
| 19 | Match Type | 10121 (100.0%) | 235 (100.0%) |
| 20 | Email Source | 2075 (20.5%) | 232 (98.7%) |
| 21 | LinkedIn Source | 34 (0.3%) | 28 (11.9%) |
| 22 | Found At | 10121 (100.0%) | 235 (100.0%) |
| 23 | Also Listed As | 1223 (12.1%) | 69 (29.4%) |
| 24 | Other Markets | 189 (1.9%) | 19 (8.1%) |
| 25 | Merged Listings | 2139 (21.1%) | 108 (46.0%) |
| 26 | Flags | 1228 (12.1%) | 44 (18.7%) |
| 27 | Mobile Candidates | 296 (2.9%) | 213 (90.6%) |
| 28 | Socials | 2056 (20.3%) | 201 (85.5%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2075 | 20.5% |
| linkedin | 34 | 0.3% |
| direct-line | 296 | 2.9% |
| role-email | 926 | 9.1% |
| gia | 565 | 5.6% |
| ags | 67 | 0.7% |
| ja | 40 | 0.4% |
| bench | 326 | 3.2% |
| custom-design | 1464 | 14.5% |
| since-yyyy | 1376 | 13.6% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 7 | 32 |
| Los Angeles, CA | 1280 | 1042 | 238 | 75 | 6 | 30 |
| Chicago, IL | 993 | 682 | 153 | 60 | 3 | 16 |
| Houston, TX | 1030 | 706 | 145 | 57 | 5 | 22 |
| Dallas, TX | 722 | 489 | 91 | 57 | 3 | 7 |
| Miami, FL | 1024 | 731 | 164 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 526 | 129 | 61 | 8 | 21 |
| Philadelphia, PA | 767 | 547 | 92 | 26 | 0 | 11 |
| San Francisco, CA | 732 | 444 | 124 | 66 | 0 | 8 |
| Boston, MA | 571 | 344 | 101 | 55 | 0 | 9 |
| Seattle, WA | 453 | 300 | 62 | 11 | 0 | 3 |
| Las Vegas, NV | 559 | 350 | 50 | 11 | 0 | 4 |
| Phoenix, AZ | 582 | 409 | 57 | 10 | 0 | 8 |
| San Diego, CA | 559 | 375 | 55 | 14 | 0 | 2 |
| Denver, CO | 399 | 281 | 63 | 9 | 0 | 6 |
| Washington, DC | 347 | 204 | 53 | 10 | 0 | 3 |
| Detroit, MI | 458 | 333 | 44 | 10 | 0 | 6 |
| Minneapolis, MN | 253 | 168 | 34 | 8 | 0 | 2 |
| Charlotte, NC | 283 | 180 | 33 | 11 | 0 | 3 |
| Nashville, TN | 229 | 145 | 29 | 8 | 0 | 0 |
| Scottsdale, AZ | 181 | 124 | 15 | 3 | 0 | 2 |
| Naples, FL | 240 | 140 | 26 | 11 | 0 | 3 |
| Greenwich, CT | 136 | 79 | 17 | 4 | 0 | 3 |
| Palm Beach, FL | 361 | 215 | 14 | 3 | 0 | 1 |
| Beverly Hills, CA | 97 | 83 | 5 | 0 | 0 | 1 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3117 | 2037 | 81 |
| YellowPages | 8933 | 6720 | 83 |
| BBB | 1092 | 596 | 57 |
| OpenStreetMap | 1295 | 768 | 14 |

Discovery tasks completed: bbb=300, gmaps=124, osm=23, yp=429

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 54 | 0 | 0 | 54 |
| beads-craft | 400 | 27 | 3 | 430 |
| chain | 2404 | 0 | 0 | 2404 |
| coin-currency | 141 | 4 | 0 | 145 |
| costume-fashion | 342 | 111 | 21 | 474 |
| diamond-trade | 129 | 28 | 7 | 164 |
| gold-buyer | 179 | 29 | 3 | 211 |
| kiosk-battery | 7 | 0 | 0 | 7 |
| no-segment | 0 | 0 | 583 | 583 |
| pawn | 568 | 25 | 14 | 607 |
| piercing-tattoo | 400 | 31 | 8 | 439 |
| simulants | 6 | 25 | 2 | 33 |
| thrift-consignment | 42 | 0 | 0 | 42 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 72 | 8 | 1 | 81 |
| **all** | | | | **5677** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1463 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 92 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 31 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 10 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 4 | http-429 or challenge page at https://www.google.com/search?q=%22Billy+Lulo%22+Los+Angeles+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
