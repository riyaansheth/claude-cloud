# Jewelry retail lead run — REPORT

Generated 2026-10-14T04:06:15+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 15481 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10696 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 304 |
| Qualification rate | 2.8% |
| Websites crawled OK / attempted | 8461 / 10159 |
| Listings with an owner/decision-maker name | 2057 |
| LinkedIn searches by outcome | ambiguous: 84, match: 61, none: 246, reject: 19 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10696 (100.0%) | 304 (100.0%) |
| 2 | Segment | 10696 (100.0%) | 304 (100.0%) |
| 3 | Category (as listed) | 10675 (99.8%) | 304 (100.0%) |
| 4 | Phone | 10016 (93.6%) | 298 (98.0%) |
| 5 | Email | 2500 (23.4%) | 299 (98.4%) |
| 6 | LinkedIn Profile | 56 (0.5%) | 50 (16.4%) |
| 7 | Contact Person | 1031 (9.6%) | 142 (46.7%) |
| 8 | Role | 1031 (9.6%) | 142 (46.7%) |
| 9 | Website | 8213 (76.8%) | 304 (100.0%) |
| 10 | Address | 10255 (95.9%) | 302 (99.3%) |
| 11 | Real City | 8843 (82.7%) | 261 (85.9%) |
| 12 | Real State | 8938 (83.6%) | 260 (85.5%) |
| 13 | Market | 10696 (100.0%) | 304 (100.0%) |
| 14 | Lead Origin | 10696 (100.0%) | 304 (100.0%) |
| 15 | Rating | 3051 (28.5%) | 157 (51.6%) |
| 16 | Reviews | 3051 (28.5%) | 157 (51.6%) |
| 17 | Source | 10696 (100.0%) | 304 (100.0%) |
| 18 | Signals | 10696 (100.0%) | 304 (100.0%) |
| 19 | Match Type | 10696 (100.0%) | 304 (100.0%) |
| 20 | Email Source | 2500 (23.4%) | 299 (98.4%) |
| 21 | LinkedIn Source | 56 (0.5%) | 50 (16.4%) |
| 22 | Found At | 10696 (100.0%) | 304 (100.0%) |
| 23 | Also Listed As | 1340 (12.5%) | 85 (28.0%) |
| 24 | Other Markets | 242 (2.3%) | 24 (7.9%) |
| 25 | Merged Listings | 2299 (21.5%) | 133 (43.8%) |
| 26 | Flags | 1364 (12.8%) | 58 (19.1%) |
| 27 | Mobile Candidates | 355 (3.3%) | 262 (86.2%) |
| 28 | Socials | 2423 (22.7%) | 265 (87.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2500 | 23.4% |
| linkedin | 56 | 0.5% |
| direct-line | 355 | 3.3% |
| role-email | 1091 | 10.2% |
| gia | 656 | 6.1% |
| ags | 76 | 0.7% |
| ja | 45 | 0.4% |
| bench | 381 | 3.6% |
| custom-design | 1690 | 15.8% |
| since-yyyy | 1839 | 17.2% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1229 | 283 | 97 | 9 | 34 |
| Los Angeles, CA | 1280 | 1033 | 235 | 77 | 7 | 30 |
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
| San Diego, CA | 591 | 381 | 81 | 33 | 1 | 6 |
| Denver, CO | 468 | 305 | 97 | 46 | 3 | 10 |
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
| Google Maps | 3108 | 1973 | 104 |
| YellowPages | 9439 | 7085 | 114 |
| BBB | 1624 | 872 | 72 |
| OpenStreetMap | 1313 | 766 | 14 |

Discovery tasks completed: bbb=427, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 64 | 0 | 0 | 64 |
| beads-craft | 423 | 34 | 3 | 460 |
| chain | 2634 | 0 | 0 | 2634 |
| coin-currency | 149 | 7 | 0 | 156 |
| costume-fashion | 369 | 136 | 31 | 536 |
| diamond-trade | 133 | 29 | 7 | 169 |
| gold-buyer | 205 | 36 | 5 | 246 |
| kiosk-battery | 7 | 0 | 0 | 7 |
| no-segment | 0 | 0 | 689 | 689 |
| pawn | 614 | 37 | 14 | 665 |
| piercing-tattoo | 449 | 36 | 12 | 497 |
| simulants | 6 | 35 | 2 | 43 |
| thrift-consignment | 44 | 0 | 0 | 44 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 74 | 8 | 1 | 83 |
| **all** | | | | **6296** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1758 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 135 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 7 | http-429 or challenge page at https://www.google.com/search?q=%22Anthony+Pampillonia%22+Dallas+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
