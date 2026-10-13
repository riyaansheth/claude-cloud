# Jewelry retail lead run — REPORT

Generated 2026-10-14T02:31:20+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 15084 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10507 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 275 |
| Qualification rate | 2.6% |
| Websites crawled OK / attempted | 8165 / 9743 |
| Listings with an owner/decision-maker name | 1727 |
| LinkedIn searches by outcome | ambiguous: 62, match: 45, none: 216, reject: 16 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10507 (100.0%) | 275 (100.0%) |
| 2 | Segment | 10507 (100.0%) | 275 (100.0%) |
| 3 | Category (as listed) | 10492 (99.9%) | 275 (100.0%) |
| 4 | Phone | 9842 (93.7%) | 269 (97.8%) |
| 5 | Email | 2395 (22.8%) | 271 (98.5%) |
| 6 | LinkedIn Profile | 39 (0.4%) | 33 (12.0%) |
| 7 | Contact Person | 847 (8.1%) | 114 (41.5%) |
| 8 | Role | 847 (8.1%) | 114 (41.5%) |
| 9 | Website | 8112 (77.2%) | 275 (100.0%) |
| 10 | Address | 10078 (95.9%) | 273 (99.3%) |
| 11 | Real City | 8653 (82.4%) | 236 (85.8%) |
| 12 | Real State | 8748 (83.3%) | 235 (85.5%) |
| 13 | Market | 10507 (100.0%) | 275 (100.0%) |
| 14 | Lead Origin | 10507 (100.0%) | 275 (100.0%) |
| 15 | Rating | 3066 (29.2%) | 141 (51.3%) |
| 16 | Reviews | 3066 (29.2%) | 141 (51.3%) |
| 17 | Source | 10507 (100.0%) | 275 (100.0%) |
| 18 | Signals | 10507 (100.0%) | 275 (100.0%) |
| 19 | Match Type | 10507 (100.0%) | 275 (100.0%) |
| 20 | Email Source | 2395 (22.8%) | 271 (98.5%) |
| 21 | LinkedIn Source | 39 (0.4%) | 33 (12.0%) |
| 22 | Found At | 10507 (100.0%) | 275 (100.0%) |
| 23 | Also Listed As | 1299 (12.4%) | 76 (27.6%) |
| 24 | Other Markets | 234 (2.2%) | 22 (8.0%) |
| 25 | Merged Listings | 2251 (21.4%) | 120 (43.6%) |
| 26 | Flags | 1307 (12.4%) | 51 (18.5%) |
| 27 | Mobile Candidates | 341 (3.2%) | 249 (90.5%) |
| 28 | Socials | 2298 (21.9%) | 240 (87.3%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2395 | 22.8% |
| linkedin | 39 | 0.4% |
| direct-line | 341 | 3.2% |
| role-email | 1044 | 9.9% |
| gia | 633 | 6.0% |
| ags | 73 | 0.7% |
| ja | 44 | 0.4% |
| bench | 369 | 3.5% |
| custom-design | 1630 | 15.5% |
| since-yyyy | 1568 | 14.9% |

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
| Boston, MA | 570 | 343 | 109 | 55 | 3 | 14 |
| Seattle, WA | 578 | 347 | 88 | 68 | 0 | 7 |
| Las Vegas, NV | 558 | 344 | 63 | 12 | 1 | 7 |
| Phoenix, AZ | 575 | 397 | 78 | 11 | 0 | 11 |
| San Diego, CA | 555 | 369 | 80 | 18 | 0 | 5 |
| Denver, CO | 396 | 278 | 88 | 14 | 0 | 7 |
| Washington, DC | 347 | 201 | 65 | 14 | 0 | 5 |
| Detroit, MI | 457 | 331 | 65 | 11 | 0 | 10 |
| Minneapolis, MN | 250 | 164 | 49 | 11 | 0 | 2 |
| Charlotte, NC | 282 | 178 | 44 | 12 | 0 | 3 |
| Nashville, TN | 234 | 144 | 38 | 11 | 0 | 0 |
| Scottsdale, AZ | 184 | 123 | 30 | 5 | 0 | 4 |
| Naples, FL | 239 | 141 | 40 | 13 | 0 | 4 |
| Greenwich, CT | 136 | 78 | 23 | 5 | 0 | 4 |
| Palm Beach, FL | 401 | 241 | 58 | 9 | 0 | 5 |
| Beverly Hills, CA | 592 | 453 | 68 | 10 | 0 | 9 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1994 | 91 |
| YellowPages | 9445 | 7082 | 108 |
| BBB | 1217 | 661 | 62 |
| OpenStreetMap | 1313 | 770 | 14 |

Discovery tasks completed: bbb=315, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 62 | 0 | 0 | 62 |
| beads-craft | 420 | 31 | 3 | 454 |
| chain | 2520 | 0 | 0 | 2520 |
| coin-currency | 143 | 7 | 0 | 150 |
| costume-fashion | 365 | 131 | 26 | 522 |
| diamond-trade | 130 | 29 | 7 | 166 |
| gold-buyer | 193 | 36 | 4 | 233 |
| kiosk-battery | 7 | 0 | 0 | 7 |
| no-segment | 0 | 0 | 676 | 676 |
| pawn | 601 | 36 | 14 | 651 |
| piercing-tattoo | 422 | 35 | 10 | 467 |
| simulants | 6 | 32 | 2 | 40 |
| thrift-consignment | 43 | 0 | 0 | 43 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 74 | 8 | 1 | 83 |
| **all** | | | | **6077** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1529 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
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
