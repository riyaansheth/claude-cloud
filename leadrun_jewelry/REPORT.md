# Jewelry retail lead run — REPORT

Generated 2026-10-14T13:22:35+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 22658 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 14993 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 390 |
| Qualification rate | 2.6% |
| Websites crawled OK / attempted | 11493 / 13744 |
| Listings with an owner/decision-maker name | 3134 |
| LinkedIn searches by outcome | ambiguous: 182, match: 110, none: 383, reject: 44 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 14993 (100.0%) | 390 (100.0%) |
| 2 | Segment | 14993 (100.0%) | 390 (100.0%) |
| 3 | Category (as listed) | 14966 (99.8%) | 390 (100.0%) |
| 4 | Phone | 14147 (94.4%) | 384 (98.5%) |
| 5 | Email | 3271 (21.8%) | 382 (97.9%) |
| 6 | LinkedIn Profile | 101 (0.7%) | 94 (24.1%) |
| 7 | Contact Person | 1526 (10.2%) | 201 (51.5%) |
| 8 | Role | 1526 (10.2%) | 201 (51.5%) |
| 9 | Website | 11588 (77.3%) | 390 (100.0%) |
| 10 | Address | 14424 (96.2%) | 387 (99.2%) |
| 11 | Real City | 12398 (82.7%) | 342 (87.7%) |
| 12 | Real State | 12493 (83.3%) | 341 (87.4%) |
| 13 | Market | 14993 (100.0%) | 390 (100.0%) |
| 14 | Lead Origin | 14993 (100.0%) | 390 (100.0%) |
| 15 | Rating | 4580 (30.5%) | 196 (50.3%) |
| 16 | Reviews | 4580 (30.5%) | 196 (50.3%) |
| 17 | Source | 14993 (100.0%) | 390 (100.0%) |
| 18 | Signals | 14993 (100.0%) | 390 (100.0%) |
| 19 | Match Type | 14993 (100.0%) | 390 (100.0%) |
| 20 | Email Source | 3271 (21.8%) | 382 (97.9%) |
| 21 | LinkedIn Source | 101 (0.7%) | 94 (24.1%) |
| 22 | Found At | 14993 (100.0%) | 390 (100.0%) |
| 23 | Also Listed As | 1900 (12.7%) | 112 (28.7%) |
| 24 | Other Markets | 392 (2.6%) | 40 (10.3%) |
| 25 | Merged Listings | 3475 (23.2%) | 176 (45.1%) |
| 26 | Flags | 1903 (12.7%) | 83 (21.3%) |
| 27 | Mobile Candidates | 435 (2.9%) | 306 (78.5%) |
| 28 | Socials | 3177 (21.2%) | 345 (88.5%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3271 | 21.8% |
| linkedin | 101 | 0.7% |
| direct-line | 435 | 2.9% |
| role-email | 1364 | 9.1% |
| gia | 861 | 5.7% |
| ags | 113 | 0.8% |
| ja | 61 | 0.4% |
| bench | 540 | 3.6% |
| custom-design | 2297 | 15.3% |
| since-yyyy | 2691 | 17.9% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 8 | 31 |
| Chicago, IL | 993 | 685 | 154 | 65 | 5 | 19 |
| Houston, TX | 1030 | 697 | 142 | 55 | 5 | 21 |
| Dallas, TX | 722 | 483 | 90 | 57 | 5 | 8 |
| Miami, FL | 1024 | 729 | 163 | 67 | 5 | 34 |
| Atlanta, GA | 739 | 526 | 128 | 62 | 11 | 23 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 3 | 14 |
| San Francisco, CA | 732 | 444 | 124 | 67 | 3 | 11 |
| Boston, MA | 570 | 345 | 109 | 56 | 7 | 18 |
| Seattle, WA | 589 | 347 | 93 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 403 | 75 | 75 | 3 | 12 |
| Phoenix, AZ | 730 | 469 | 95 | 59 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 382 | 225 | 76 | 32 | 1 | 6 |
| Detroit, MI | 554 | 378 | 82 | 51 | 6 | 18 |
| Minneapolis, MN | 531 | 245 | 61 | 91 | 6 | 9 |
| Charlotte, NC | 350 | 208 | 47 | 40 | 2 | 5 |
| Nashville, TN | 341 | 186 | 47 | 54 | 4 | 4 |
| Scottsdale, AZ | 263 | 150 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 151 | 46 | 21 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 258 | 66 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 458 | 110 | 27 | 1 | 13 |
| Austin, TX | 458 | 239 | 75 | 37 | 0 | 5 |
| San Antonio, TX | 502 | 303 | 44 | 42 | 0 | 4 |
| Fort Worth, TX | 445 | 259 | 38 | 22 | 0 | 0 |
| San Jose, CA | 429 | 253 | 30 | 3 | 0 | 2 |
| Sacramento, CA | 279 | 164 | 22 | 4 | 0 | 4 |
| Portland, OR | 371 | 238 | 37 | 6 | 0 | 0 |
| Salt Lake City, UT | 294 | 167 | 30 | 4 | 0 | 1 |
| Kansas City, MO | 171 | 115 | 31 | 8 | 0 | 2 |
| St. Louis, MO | 236 | 174 | 37 | 7 | 0 | 0 |
| Columbus, OH | 74 | 56 | 9 | 3 | 0 | 0 |
| Cleveland, OH | 313 | 192 | 50 | 7 | 0 | 2 |
| Cincinnati, OH | 322 | 202 | 38 | 8 | 0 | 0 |
| Indianapolis, IN | 251 | 161 | 33 | 11 | 0 | 5 |
| Pittsburgh, PA | 335 | 211 | 46 | 7 | 0 | 3 |
| Baltimore, MD | 305 | 215 | 35 | 6 | 0 | 2 |
| Orlando, FL | 383 | 250 | 16 | 5 | 0 | 0 |
| Tampa, FL | 344 | 237 | 30 | 1 | 0 | 3 |
| Fort Lauderdale, FL | 444 | 326 | 47 | 8 | 0 | 1 |
| Raleigh, NC | 154 | 107 | 27 | 11 | 0 | 1 |
| New Orleans, LA | 197 | 140 | 32 | 5 | 0 | 5 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 4739 | 2749 | 119 |
| YellowPages | 13646 | 10038 | 156 |
| BBB | 2782 | 1363 | 99 |
| OpenStreetMap | 1497 | 843 | 16 |

Discovery tasks completed: bbb=834, gmaps=195, osm=31, yp=705

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 100 | 0 | 35 | 135 |
| beads-craft | 613 | 46 | 4 | 663 |
| chain | 4177 | 0 | 0 | 4177 |
| coin-currency | 326 | 10 | 0 | 336 |
| costume-fashion | 567 | 199 | 43 | 809 |
| diamond-trade | 153 | 35 | 7 | 195 |
| gold-buyer | 290 | 51 | 18 | 359 |
| kiosk-battery | 12 | 0 | 0 | 12 |
| no-segment | 0 | 0 | 1077 | 1077 |
| pawn | 1029 | 52 | 15 | 1096 |
| piercing-tattoo | 766 | 51 | 16 | 833 |
| simulants | 7 | 40 | 4 | 51 |
| thrift-consignment | 86 | 0 | 0 | 86 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 94 | 10 | 1 | 105 |
| **all** | | | | **9937** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 2789 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 189 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 42 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| yp | soft-block-503 | 21 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-504 | 16 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 15 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| osm | http-406 | 14 | https://overpass-api.de/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
