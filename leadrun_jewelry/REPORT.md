# Jewelry retail lead run — REPORT

Generated 2026-10-14T03:25:47+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 15304 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10627 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 295 |
| Qualification rate | 2.8% |
| Websites crawled OK / attempted | 8396 / 10068 |
| Listings with an owner/decision-maker name | 1925 |
| LinkedIn searches by outcome | ambiguous: 75, match: 52, none: 230, reject: 18 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10627 (100.0%) | 295 (100.0%) |
| 2 | Segment | 10627 (100.0%) | 295 (100.0%) |
| 3 | Category (as listed) | 10606 (99.8%) | 295 (100.0%) |
| 4 | Phone | 9958 (93.7%) | 289 (98.0%) |
| 5 | Email | 2472 (23.3%) | 290 (98.3%) |
| 6 | LinkedIn Profile | 47 (0.4%) | 41 (13.9%) |
| 7 | Contact Person | 960 (9.0%) | 130 (44.1%) |
| 8 | Role | 960 (9.0%) | 130 (44.1%) |
| 9 | Website | 8171 (76.9%) | 295 (100.0%) |
| 10 | Address | 10189 (95.9%) | 293 (99.3%) |
| 11 | Real City | 8772 (82.5%) | 254 (86.1%) |
| 12 | Real State | 8867 (83.4%) | 253 (85.8%) |
| 13 | Market | 10627 (100.0%) | 295 (100.0%) |
| 14 | Lead Origin | 10627 (100.0%) | 295 (100.0%) |
| 15 | Rating | 3052 (28.7%) | 150 (50.8%) |
| 16 | Reviews | 3052 (28.7%) | 150 (50.8%) |
| 17 | Source | 10627 (100.0%) | 295 (100.0%) |
| 18 | Signals | 10627 (100.0%) | 295 (100.0%) |
| 19 | Match Type | 10627 (100.0%) | 295 (100.0%) |
| 20 | Email Source | 2472 (23.3%) | 290 (98.3%) |
| 21 | LinkedIn Source | 47 (0.4%) | 41 (13.9%) |
| 22 | Found At | 10627 (100.0%) | 295 (100.0%) |
| 23 | Also Listed As | 1316 (12.4%) | 80 (27.1%) |
| 24 | Other Markets | 239 (2.2%) | 24 (8.1%) |
| 25 | Merged Listings | 2268 (21.3%) | 125 (42.4%) |
| 26 | Flags | 1337 (12.6%) | 54 (18.3%) |
| 27 | Mobile Candidates | 352 (3.3%) | 262 (88.8%) |
| 28 | Socials | 2389 (22.5%) | 257 (87.1%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2472 | 23.3% |
| linkedin | 47 | 0.4% |
| direct-line | 352 | 3.3% |
| role-email | 1079 | 10.2% |
| gia | 646 | 6.1% |
| ags | 75 | 0.7% |
| ja | 45 | 0.4% |
| bench | 374 | 3.5% |
| custom-design | 1663 | 15.6% |
| since-yyyy | 1726 | 16.2% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1229 | 283 | 97 | 9 | 34 |
| Los Angeles, CA | 1280 | 1033 | 235 | 76 | 6 | 29 |
| Chicago, IL | 993 | 688 | 154 | 64 | 3 | 17 |
| Houston, TX | 1030 | 703 | 146 | 57 | 5 | 22 |
| Dallas, TX | 722 | 489 | 91 | 58 | 3 | 8 |
| Miami, FL | 1024 | 735 | 166 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 527 | 128 | 62 | 8 | 20 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 2 | 13 |
| San Francisco, CA | 732 | 447 | 125 | 67 | 1 | 9 |
| Boston, MA | 570 | 346 | 109 | 56 | 4 | 15 |
| Seattle, WA | 589 | 351 | 93 | 70 | 0 | 8 |
| Las Vegas, NV | 691 | 404 | 75 | 75 | 1 | 10 |
| Phoenix, AZ | 661 | 438 | 78 | 35 | 0 | 11 |
| San Diego, CA | 555 | 370 | 80 | 19 | 0 | 5 |
| Denver, CO | 396 | 279 | 89 | 14 | 1 | 9 |
| Washington, DC | 347 | 203 | 68 | 14 | 1 | 6 |
| Detroit, MI | 457 | 330 | 66 | 11 | 0 | 11 |
| Minneapolis, MN | 250 | 165 | 50 | 11 | 0 | 2 |
| Charlotte, NC | 282 | 180 | 44 | 13 | 0 | 3 |
| Nashville, TN | 234 | 143 | 38 | 11 | 1 | 1 |
| Scottsdale, AZ | 184 | 118 | 30 | 5 | 0 | 4 |
| Naples, FL | 239 | 140 | 40 | 13 | 0 | 4 |
| Greenwich, CT | 136 | 78 | 23 | 5 | 0 | 4 |
| Palm Beach, FL | 401 | 244 | 63 | 10 | 0 | 6 |
| Beverly Hills, CA | 586 | 442 | 106 | 20 | 0 | 12 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1980 | 97 |
| YellowPages | 9439 | 7097 | 115 |
| BBB | 1447 | 781 | 69 |
| OpenStreetMap | 1313 | 769 | 14 |

Discovery tasks completed: bbb=370, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 63 | 0 | 0 | 63 |
| beads-craft | 421 | 33 | 3 | 457 |
| chain | 2583 | 0 | 0 | 2583 |
| coin-currency | 149 | 7 | 0 | 156 |
| costume-fashion | 368 | 135 | 29 | 532 |
| diamond-trade | 132 | 29 | 7 | 168 |
| gold-buyer | 196 | 36 | 5 | 237 |
| kiosk-battery | 7 | 0 | 0 | 7 |
| no-segment | 0 | 0 | 671 | 671 |
| pawn | 612 | 37 | 14 | 663 |
| piercing-tattoo | 440 | 36 | 11 | 487 |
| simulants | 6 | 35 | 2 | 43 |
| thrift-consignment | 43 | 0 | 0 | 43 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 74 | 8 | 1 | 83 |
| **all** | | | | **6196** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1672 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 124 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 6 | http-429 or challenge page at https://www.google.com/search?q=%22Anthony+Pampillonia%22+Dallas+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
