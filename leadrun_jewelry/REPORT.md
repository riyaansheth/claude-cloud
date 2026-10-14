# Jewelry retail lead run — REPORT

Generated 2026-10-14T05:41:04+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 15945 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10850 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 319 |
| Qualification rate | 2.9% |
| Websites crawled OK / attempted | 8593 / 10326 |
| Listings with an owner/decision-maker name | 2446 |
| LinkedIn searches by outcome | ambiguous: 117, match: 78, none: 291, reject: 29 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10850 (100.0%) | 319 (100.0%) |
| 2 | Segment | 10850 (100.0%) | 319 (100.0%) |
| 3 | Category (as listed) | 10828 (99.8%) | 319 (100.0%) |
| 4 | Phone | 10162 (93.7%) | 313 (98.1%) |
| 5 | Email | 2533 (23.3%) | 313 (98.1%) |
| 6 | LinkedIn Profile | 69 (0.6%) | 63 (19.7%) |
| 7 | Contact Person | 1203 (11.1%) | 155 (48.6%) |
| 8 | Role | 1203 (11.1%) | 155 (48.6%) |
| 9 | Website | 8314 (76.6%) | 319 (100.0%) |
| 10 | Address | 10404 (95.9%) | 316 (99.1%) |
| 11 | Real City | 9024 (83.2%) | 271 (85.0%) |
| 12 | Real State | 9120 (84.1%) | 270 (84.6%) |
| 13 | Market | 10850 (100.0%) | 319 (100.0%) |
| 14 | Lead Origin | 10850 (100.0%) | 319 (100.0%) |
| 15 | Rating | 3035 (28.0%) | 168 (52.7%) |
| 16 | Reviews | 3035 (28.0%) | 168 (52.7%) |
| 17 | Source | 10850 (100.0%) | 319 (100.0%) |
| 18 | Signals | 10850 (100.0%) | 319 (100.0%) |
| 19 | Match Type | 10850 (100.0%) | 319 (100.0%) |
| 20 | Email Source | 2533 (23.3%) | 313 (98.1%) |
| 21 | LinkedIn Source | 69 (0.6%) | 63 (19.7%) |
| 22 | Found At | 10850 (100.0%) | 319 (100.0%) |
| 23 | Also Listed As | 1375 (12.7%) | 89 (27.9%) |
| 24 | Other Markets | 240 (2.2%) | 25 (7.8%) |
| 25 | Merged Listings | 2425 (22.4%) | 137 (42.9%) |
| 26 | Flags | 1397 (12.9%) | 61 (19.1%) |
| 27 | Mobile Candidates | 358 (3.3%) | 265 (83.1%) |
| 28 | Socials | 2483 (22.9%) | 278 (87.1%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2533 | 23.3% |
| linkedin | 69 | 0.6% |
| direct-line | 358 | 3.3% |
| role-email | 1111 | 10.2% |
| gia | 671 | 6.2% |
| ags | 79 | 0.7% |
| ja | 46 | 0.4% |
| bench | 401 | 3.7% |
| custom-design | 1748 | 16.1% |
| since-yyyy | 2049 | 18.9% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1227 | 282 | 97 | 10 | 35 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 7 | 30 |
| Chicago, IL | 993 | 688 | 154 | 65 | 4 | 18 |
| Houston, TX | 1030 | 701 | 145 | 58 | 5 | 22 |
| Dallas, TX | 722 | 488 | 91 | 58 | 4 | 9 |
| Miami, FL | 1024 | 734 | 166 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 527 | 128 | 62 | 9 | 21 |
| Philadelphia, PA | 767 | 546 | 92 | 28 | 2 | 13 |
| San Francisco, CA | 732 | 447 | 125 | 67 | 2 | 10 |
| Boston, MA | 570 | 345 | 109 | 55 | 5 | 16 |
| Seattle, WA | 589 | 349 | 93 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 403 | 75 | 75 | 3 | 12 |
| Phoenix, AZ | 730 | 468 | 95 | 55 | 0 | 12 |
| San Diego, CA | 591 | 381 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 382 | 226 | 76 | 33 | 1 | 6 |
| Detroit, MI | 554 | 383 | 83 | 53 | 0 | 13 |
| Minneapolis, MN | 497 | 229 | 56 | 87 | 0 | 2 |
| Charlotte, NC | 282 | 180 | 44 | 13 | 0 | 3 |
| Nashville, TN | 234 | 143 | 38 | 11 | 2 | 2 |
| Scottsdale, AZ | 184 | 117 | 31 | 6 | 1 | 5 |
| Naples, FL | 239 | 139 | 40 | 13 | 0 | 4 |
| Greenwich, CT | 136 | 78 | 23 | 5 | 1 | 5 |
| Palm Beach, FL | 401 | 243 | 61 | 9 | 1 | 7 |
| Beverly Hills, CA | 586 | 442 | 106 | 20 | 0 | 12 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1942 | 115 |
| YellowPages | 9439 | 7076 | 114 |
| BBB | 2086 | 1071 | 76 |
| OpenStreetMap | 1313 | 761 | 14 |

Discovery tasks completed: bbb=523, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 64 | 0 | 35 | 99 |
| beads-craft | 429 | 34 | 3 | 466 |
| chain | 2865 | 0 | 0 | 2865 |
| coin-currency | 159 | 8 | 0 | 167 |
| costume-fashion | 369 | 140 | 32 | 541 |
| diamond-trade | 133 | 31 | 7 | 171 |
| gold-buyer | 210 | 37 | 9 | 256 |
| kiosk-battery | 9 | 0 | 0 | 9 |
| no-segment | 0 | 0 | 718 | 718 |
| pawn | 621 | 37 | 14 | 672 |
| piercing-tattoo | 494 | 40 | 12 | 546 |
| simulants | 6 | 35 | 2 | 43 |
| thrift-consignment | 44 | 0 | 0 | 44 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 78 | 8 | 1 | 87 |
| **all** | | | | **6687** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1928 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 153 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 9 | http-429 or challenge page at https://www.google.com/search?q=%22Anthony+Pampillonia%22+Dallas+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
