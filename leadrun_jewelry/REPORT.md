# Jewelry retail lead run — REPORT

Generated 2026-10-14T02:51:33+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 15148 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10560 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 293 |
| Qualification rate | 2.8% |
| Websites crawled OK / attempted | 8386 / 10038 |
| Listings with an owner/decision-maker name | 1806 |
| LinkedIn searches by outcome | ambiguous: 73, match: 52, none: 226, reject: 18 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10560 (100.0%) | 293 (100.0%) |
| 2 | Segment | 10560 (100.0%) | 293 (100.0%) |
| 3 | Category (as listed) | 10545 (99.9%) | 293 (100.0%) |
| 4 | Phone | 9895 (93.7%) | 287 (98.0%) |
| 5 | Email | 2468 (23.4%) | 288 (98.3%) |
| 6 | LinkedIn Profile | 47 (0.4%) | 41 (14.0%) |
| 7 | Contact Person | 900 (8.5%) | 128 (43.7%) |
| 8 | Role | 900 (8.5%) | 128 (43.7%) |
| 9 | Website | 8135 (77.0%) | 293 (100.0%) |
| 10 | Address | 10129 (95.9%) | 291 (99.3%) |
| 11 | Real City | 8706 (82.4%) | 252 (86.0%) |
| 12 | Real State | 8801 (83.3%) | 251 (85.7%) |
| 13 | Market | 10560 (100.0%) | 293 (100.0%) |
| 14 | Lead Origin | 10560 (100.0%) | 293 (100.0%) |
| 15 | Rating | 3053 (28.9%) | 150 (51.2%) |
| 16 | Reviews | 3053 (28.9%) | 150 (51.2%) |
| 17 | Source | 10560 (100.0%) | 293 (100.0%) |
| 18 | Signals | 10560 (100.0%) | 293 (100.0%) |
| 19 | Match Type | 10560 (100.0%) | 293 (100.0%) |
| 20 | Email Source | 2468 (23.4%) | 288 (98.3%) |
| 21 | LinkedIn Source | 47 (0.4%) | 41 (14.0%) |
| 22 | Found At | 10560 (100.0%) | 293 (100.0%) |
| 23 | Also Listed As | 1303 (12.3%) | 80 (27.3%) |
| 24 | Other Markets | 234 (2.2%) | 24 (8.2%) |
| 25 | Merged Listings | 2247 (21.3%) | 125 (42.7%) |
| 26 | Flags | 1319 (12.5%) | 53 (18.1%) |
| 27 | Mobile Candidates | 351 (3.3%) | 260 (88.7%) |
| 28 | Socials | 2385 (22.6%) | 256 (87.4%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2468 | 23.4% |
| linkedin | 47 | 0.4% |
| direct-line | 351 | 3.3% |
| role-email | 1079 | 10.2% |
| gia | 645 | 6.1% |
| ags | 75 | 0.7% |
| ja | 45 | 0.4% |
| bench | 372 | 3.5% |
| custom-design | 1662 | 15.7% |
| since-yyyy | 1639 | 15.5% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1229 | 283 | 97 | 9 | 34 |
| Los Angeles, CA | 1280 | 1033 | 235 | 75 | 6 | 29 |
| Chicago, IL | 993 | 688 | 154 | 64 | 3 | 17 |
| Houston, TX | 1030 | 703 | 146 | 57 | 5 | 22 |
| Dallas, TX | 722 | 489 | 91 | 58 | 3 | 8 |
| Miami, FL | 1024 | 735 | 166 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 527 | 128 | 62 | 8 | 20 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 2 | 13 |
| San Francisco, CA | 732 | 447 | 125 | 67 | 1 | 9 |
| Boston, MA | 570 | 346 | 109 | 56 | 4 | 15 |
| Seattle, WA | 589 | 351 | 93 | 70 | 0 | 8 |
| Las Vegas, NV | 618 | 373 | 71 | 40 | 1 | 8 |
| Phoenix, AZ | 575 | 398 | 78 | 11 | 0 | 11 |
| San Diego, CA | 555 | 370 | 80 | 19 | 0 | 5 |
| Denver, CO | 396 | 279 | 89 | 14 | 1 | 9 |
| Washington, DC | 347 | 203 | 68 | 14 | 1 | 6 |
| Detroit, MI | 457 | 330 | 66 | 11 | 0 | 11 |
| Minneapolis, MN | 250 | 165 | 50 | 11 | 0 | 2 |
| Charlotte, NC | 282 | 180 | 44 | 13 | 0 | 3 |
| Nashville, TN | 234 | 143 | 38 | 11 | 1 | 1 |
| Scottsdale, AZ | 184 | 121 | 30 | 5 | 0 | 4 |
| Naples, FL | 239 | 140 | 40 | 13 | 0 | 4 |
| Greenwich, CT | 136 | 78 | 23 | 5 | 0 | 4 |
| Palm Beach, FL | 401 | 244 | 63 | 10 | 0 | 6 |
| Beverly Hills, CA | 586 | 443 | 106 | 20 | 0 | 12 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1984 | 97 |
| YellowPages | 9439 | 7107 | 115 |
| BBB | 1288 | 699 | 67 |
| OpenStreetMap | 1313 | 770 | 14 |

Discovery tasks completed: bbb=339, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 63 | 0 | 0 | 63 |
| beads-craft | 421 | 32 | 3 | 456 |
| chain | 2551 | 0 | 0 | 2551 |
| coin-currency | 143 | 7 | 0 | 150 |
| costume-fashion | 366 | 135 | 26 | 527 |
| diamond-trade | 131 | 29 | 7 | 167 |
| gold-buyer | 193 | 36 | 4 | 233 |
| kiosk-battery | 7 | 0 | 0 | 7 |
| no-segment | 0 | 0 | 664 | 664 |
| pawn | 601 | 37 | 14 | 652 |
| piercing-tattoo | 430 | 36 | 11 | 477 |
| simulants | 6 | 35 | 2 | 43 |
| thrift-consignment | 43 | 0 | 0 | 43 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 74 | 8 | 1 | 83 |
| **all** | | | | **6119** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1632 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 114 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 6 | http-429 or challenge page at https://www.google.com/search?q=%22Anthony+Pampillonia%22+Dallas+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
