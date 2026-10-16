# Jewelry retail lead run — REPORT

Generated 2026-10-16T18:08:31+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 32535 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 20490 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 518 |
| Qualification rate | 2.5% |
| Websites crawled OK / attempted | 16203 / 19515 |
| Listings with an owner/decision-maker name | 4427 |
| LinkedIn searches by outcome | ambiguous: 260, match: 170, none: 538, reject: 126 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 20490 (100.0%) | 518 (100.0%) |
| 2 | Segment | 20490 (100.0%) | 518 (100.0%) |
| 3 | Category (as listed) | 20448 (99.8%) | 517 (99.8%) |
| 4 | Phone | 19249 (93.9%) | 506 (97.7%) |
| 5 | Email | 4498 (22.0%) | 508 (98.1%) |
| 6 | LinkedIn Profile | 152 (0.7%) | 145 (28.0%) |
| 7 | Contact Person | 2228 (10.9%) | 277 (53.5%) |
| 8 | Role | 2228 (10.9%) | 277 (53.5%) |
| 9 | Website | 15567 (76.0%) | 518 (100.0%) |
| 10 | Address | 19663 (96.0%) | 512 (98.8%) |
| 11 | Real City | 16738 (81.7%) | 443 (85.5%) |
| 12 | Real State | 16841 (82.2%) | 442 (85.3%) |
| 13 | Market | 20490 (100.0%) | 518 (100.0%) |
| 14 | Lead Origin | 20490 (100.0%) | 518 (100.0%) |
| 15 | Rating | 6653 (32.5%) | 293 (56.6%) |
| 16 | Reviews | 6653 (32.5%) | 293 (56.6%) |
| 17 | Source | 20490 (100.0%) | 518 (100.0%) |
| 18 | Signals | 20490 (100.0%) | 518 (100.0%) |
| 19 | Match Type | 20490 (100.0%) | 518 (100.0%) |
| 20 | Email Source | 4498 (22.0%) | 508 (98.1%) |
| 21 | LinkedIn Source | 158 (0.8%) | 145 (28.0%) |
| 22 | Found At | 20490 (100.0%) | 518 (100.0%) |
| 23 | Also Listed As | 2683 (13.1%) | 148 (28.6%) |
| 24 | Other Markets | 583 (2.8%) | 57 (11.0%) |
| 25 | Merged Listings | 4924 (24.0%) | 245 (47.3%) |
| 26 | Flags | 2743 (13.4%) | 111 (21.4%) |
| 27 | Mobile Candidates | 553 (2.7%) | 384 (74.1%) |
| 28 | Socials | 4377 (21.4%) | 456 (88.0%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 4498 | 22.0% |
| linkedin | 152 | 0.7% |
| direct-line | 553 | 2.7% |
| role-email | 1772 | 8.6% |
| gia | 1128 | 5.5% |
| ags | 164 | 0.8% |
| ja | 91 | 0.4% |
| bench | 767 | 3.7% |
| custom-design | 3121 | 15.2% |
| since-yyyy | 3813 | 18.6% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1029 | 234 | 76 | 8 | 31 |
| Chicago, IL | 993 | 682 | 155 | 63 | 5 | 19 |
| Houston, TX | 1030 | 696 | 142 | 56 | 5 | 21 |
| Dallas, TX | 722 | 479 | 88 | 57 | 5 | 7 |
| Miami, FL | 1024 | 725 | 160 | 66 | 5 | 33 |
| Atlanta, GA | 739 | 520 | 125 | 59 | 11 | 23 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 3 | 14 |
| San Francisco, CA | 731 | 444 | 124 | 68 | 3 | 10 |
| Boston, MA | 570 | 344 | 109 | 56 | 7 | 18 |
| Seattle, WA | 589 | 347 | 93 | 69 | 2 | 10 |
| Las Vegas, NV | 691 | 401 | 73 | 74 | 3 | 11 |
| Phoenix, AZ | 730 | 461 | 93 | 57 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 332 | 103 | 85 | 5 | 11 |
| Washington, DC | 382 | 223 | 76 | 30 | 1 | 6 |
| Detroit, MI | 554 | 377 | 82 | 51 | 6 | 18 |
| Minneapolis, MN | 531 | 245 | 61 | 92 | 6 | 9 |
| Charlotte, NC | 350 | 206 | 47 | 39 | 2 | 5 |
| Nashville, TN | 341 | 178 | 44 | 51 | 4 | 4 |
| Scottsdale, AZ | 263 | 149 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 151 | 46 | 21 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 258 | 66 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 457 | 110 | 28 | 1 | 13 |
| Austin, TX | 458 | 239 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 303 | 51 | 42 | 2 | 6 |
| Fort Worth, TX | 456 | 259 | 47 | 24 | 0 | 0 |
| San Jose, CA | 522 | 287 | 36 | 16 | 0 | 3 |
| Sacramento, CA | 372 | 207 | 38 | 39 | 2 | 7 |
| Portland, OR | 515 | 278 | 69 | 55 | 2 | 4 |
| Salt Lake City, UT | 445 | 237 | 65 | 71 | 7 | 9 |
| Kansas City, MO | 451 | 264 | 74 | 79 | 3 | 8 |
| St. Louis, MO | 526 | 263 | 72 | 53 | 2 | 6 |
| Columbus, OH | 238 | 136 | 41 | 22 | 2 | 4 |
| Cleveland, OH | 335 | 201 | 54 | 9 | 0 | 2 |
| Cincinnati, OH | 364 | 210 | 56 | 19 | 2 | 3 |
| Indianapolis, IN | 262 | 160 | 40 | 13 | 0 | 6 |
| Pittsburgh, PA | 394 | 225 | 60 | 17 | 2 | 7 |
| Baltimore, MD | 327 | 216 | 46 | 8 | 1 | 6 |
| Orlando, FL | 433 | 257 | 53 | 20 | 1 | 5 |
| Tampa, FL | 395 | 251 | 57 | 21 | 0 | 5 |
| Fort Lauderdale, FL | 581 | 389 | 79 | 33 | 3 | 7 |
| Raleigh, NC | 273 | 156 | 43 | 22 | 1 | 2 |
| New Orleans, LA | 511 | 281 | 66 | 40 | 3 | 9 |
| Jacksonville, FL | 333 | 196 | 43 | 14 | 2 | 4 |
| Memphis, TN | 401 | 230 | 36 | 63 | 2 | 6 |
| Louisville, KY | 203 | 123 | 36 | 29 | 2 | 4 |
| Milwaukee, WI | 290 | 150 | 42 | 9 | 0 | 0 |
| Albuquerque, NM | 296 | 192 | 47 | 10 | 0 | 3 |
| Tucson, AZ | 221 | 132 | 37 | 7 | 0 | 2 |
| Oklahoma City, OK | 236 | 141 | 23 | 5 | 0 | 1 |
| Tulsa, OK | 203 | 109 | 13 | 4 | 0 | 2 |
| Omaha, NE | 208 | 103 | 17 | 4 | 0 | 0 |
| Richmond, VA | 286 | 143 | 34 | 7 | 3 | 5 |
| Virginia Beach, VA | 238 | 127 | 23 | 10 | 1 | 3 |
| Birmingham, AL | 187 | 92 | 20 | 8 | 0 | 1 |
| Buffalo, NY | 276 | 164 | 43 | 9 | 1 | 3 |
| Hartford, CT | 250 | 126 | 27 | 10 | 1 | 3 |
| Providence, RI | 396 | 245 | 52 | 13 | 1 | 4 |
| El Paso, TX | 208 | 134 | 17 | 5 | 1 | 4 |
| Honolulu, HI | 452 | 274 | 56 | 10 | 0 | 7 |
| Boise, ID | 169 | 85 | 26 | 6 | 1 | 3 |
| Charleston, SC | 216 | 111 | 32 | 7 | 2 | 2 |
| Grand Rapids, MI | 171 | 95 | 20 | 5 | 0 | 1 |
| Fresno, CA | 233 | 128 | 14 | 5 | 0 | 1 |
| Bakersfield, CA | 82 | 48 | 6 | 0 | 0 | 0 |
| Long Beach, CA | 419 | 315 | 62 | 6 | 0 | 4 |
| Oakland, CA | 193 | 155 | 8 | 2 | 0 | 1 |
| Riverside, CA | 222 | 157 | 0 | 0 | 0 | 0 |
| Colorado Springs, CO | 89 | 68 | 1 | 0 | 0 | 0 |
| Spokane, WA | 67 | 50 | 0 | 0 | 0 | 0 |
| Wichita, KS | 71 | 56 | 0 | 1 | 0 | 0 |
| Des Moines, IA | 76 | 50 | 0 | 0 | 0 | 0 |
| Madison, WI | 98 | 65 | 0 | 0 | 0 | 0 |
| Rochester, NY | 199 | 119 | 25 | 9 | 0 | 4 |
| Albany, NY | 155 | 96 | 17 | 4 | 0 | 0 |
| Knoxville, TN | 100 | 72 | 10 | 4 | 0 | 0 |
| Chattanooga, TN | 88 | 60 | 9 | 3 | 0 | 0 |
| Greenville, SC | 103 | 73 | 17 | 2 | 0 | 0 |
| Columbia, SC | 103 | 62 | 10 | 4 | 0 | 0 |
| Savannah, GA | 68 | 46 | 0 | 0 | 0 | 0 |
| Little Rock, AR | 81 | 59 | 1 | 1 | 0 | 0 |
| Baton Rouge, LA | 88 | 44 | 0 | 3 | 0 | 0 |
| Anchorage, AK | 54 | 41 | 0 | 0 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 7542 | 4026 | 176 |
| YellowPages | 18501 | 13259 | 193 |
| BBB | 4272 | 2067 | 130 |
| OpenStreetMap | 2230 | 1138 | 19 |

Discovery tasks completed: bbb=1470, gmaps=337, osm=78, yp=987

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 164 | 0 | 35 | 199 |
| beads-craft | 1065 | 72 | 9 | 1146 |
| chain | 5880 | 0 | 0 | 5880 |
| coin-currency | 571 | 10 | 0 | 581 |
| costume-fashion | 801 | 276 | 73 | 1150 |
| diamond-trade | 188 | 41 | 10 | 239 |
| gold-buyer | 394 | 83 | 25 | 502 |
| kiosk-battery | 24 | 0 | 0 | 24 |
| no-segment | 0 | 0 | 2276 | 2276 |
| pawn | 1590 | 74 | 26 | 1690 |
| piercing-tattoo | 1145 | 85 | 20 | 1250 |
| simulants | 8 | 43 | 5 | 56 |
| thrift-consignment | 198 | 0 | 0 | 198 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 128 | 11 | 1 | 140 |
| **all** | | | | **15335** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 4881 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| bbb | blocked | 283 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 93 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-500 | 50 | https://overpass.kumi.systems/api/interpreter |
| osm | http-504 | 28 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 23 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 23 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-406 | 22 | https://overpass-api.de/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
