# Jewelry retail lead run — REPORT

Generated 2026-10-17T01:48:59+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 34264 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 21178 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 548 |
| Qualification rate | 2.6% |
| Websites crawled OK / attempted | 17705 / 21324 |
| Listings with an owner/decision-maker name | 4708 |
| LinkedIn searches by outcome | ambiguous: 276, match: 179, none: 551, reject: 131 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 21178 (100.0%) | 548 (100.0%) |
| 2 | Segment | 21178 (100.0%) | 548 (100.0%) |
| 3 | Category (as listed) | 21133 (99.8%) | 547 (99.8%) |
| 4 | Phone | 19844 (93.7%) | 536 (97.8%) |
| 5 | Email | 4841 (22.9%) | 537 (98.0%) |
| 6 | LinkedIn Profile | 161 (0.8%) | 154 (28.1%) |
| 7 | Contact Person | 2361 (11.1%) | 291 (53.1%) |
| 8 | Role | 2361 (11.1%) | 291 (53.1%) |
| 9 | Website | 15960 (75.4%) | 548 (100.0%) |
| 10 | Address | 20322 (96.0%) | 540 (98.5%) |
| 11 | Real City | 16865 (79.6%) | 464 (84.7%) |
| 12 | Real State | 16969 (80.1%) | 463 (84.5%) |
| 13 | Market | 21178 (100.0%) | 548 (100.0%) |
| 14 | Lead Origin | 21178 (100.0%) | 548 (100.0%) |
| 15 | Rating | 7372 (34.8%) | 316 (57.7%) |
| 16 | Reviews | 7372 (34.8%) | 316 (57.7%) |
| 17 | Source | 21178 (100.0%) | 548 (100.0%) |
| 18 | Signals | 21178 (100.0%) | 548 (100.0%) |
| 19 | Match Type | 21178 (100.0%) | 548 (100.0%) |
| 20 | Email Source | 4841 (22.9%) | 537 (98.0%) |
| 21 | LinkedIn Source | 166 (0.8%) | 154 (28.1%) |
| 22 | Found At | 21178 (100.0%) | 548 (100.0%) |
| 23 | Also Listed As | 2797 (13.2%) | 154 (28.1%) |
| 24 | Other Markets | 603 (2.8%) | 61 (11.1%) |
| 25 | Merged Listings | 5148 (24.3%) | 256 (46.7%) |
| 26 | Flags | 2865 (13.5%) | 118 (21.5%) |
| 27 | Mobile Candidates | 590 (2.8%) | 406 (74.1%) |
| 28 | Socials | 4721 (22.3%) | 482 (88.0%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 4841 | 22.9% |
| linkedin | 161 | 0.8% |
| direct-line | 590 | 2.8% |
| role-email | 1878 | 8.9% |
| gia | 1176 | 5.6% |
| ags | 177 | 0.8% |
| ja | 97 | 0.5% |
| bench | 812 | 3.8% |
| custom-design | 3331 | 15.7% |
| since-yyyy | 4019 | 19.0% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1029 | 234 | 76 | 8 | 31 |
| Chicago, IL | 993 | 682 | 155 | 63 | 5 | 19 |
| Houston, TX | 1030 | 696 | 142 | 56 | 5 | 21 |
| Dallas, TX | 722 | 478 | 88 | 57 | 5 | 7 |
| Miami, FL | 1024 | 725 | 160 | 66 | 5 | 33 |
| Atlanta, GA | 739 | 517 | 124 | 57 | 11 | 23 |
| Philadelphia, PA | 767 | 544 | 91 | 27 | 3 | 14 |
| San Francisco, CA | 731 | 443 | 124 | 69 | 3 | 10 |
| Boston, MA | 570 | 344 | 109 | 56 | 7 | 18 |
| Seattle, WA | 589 | 346 | 92 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 401 | 73 | 74 | 3 | 11 |
| Phoenix, AZ | 730 | 461 | 93 | 57 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 332 | 103 | 85 | 5 | 11 |
| Washington, DC | 382 | 223 | 76 | 30 | 1 | 6 |
| Detroit, MI | 554 | 377 | 82 | 51 | 6 | 18 |
| Minneapolis, MN | 531 | 245 | 63 | 92 | 6 | 10 |
| Charlotte, NC | 350 | 206 | 47 | 39 | 2 | 5 |
| Nashville, TN | 341 | 178 | 44 | 51 | 4 | 4 |
| Scottsdale, AZ | 263 | 149 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 151 | 46 | 21 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 258 | 66 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 457 | 110 | 29 | 1 | 13 |
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
| New Orleans, LA | 511 | 280 | 66 | 39 | 3 | 9 |
| Jacksonville, FL | 333 | 195 | 42 | 13 | 2 | 4 |
| Memphis, TN | 401 | 230 | 36 | 63 | 2 | 6 |
| Louisville, KY | 203 | 123 | 36 | 29 | 2 | 4 |
| Milwaukee, WI | 290 | 150 | 44 | 9 | 0 | 0 |
| Albuquerque, NM | 463 | 312 | 72 | 77 | 4 | 12 |
| Tucson, AZ | 236 | 136 | 37 | 14 | 0 | 1 |
| Oklahoma City, OK | 236 | 141 | 23 | 5 | 0 | 1 |
| Tulsa, OK | 203 | 109 | 13 | 4 | 0 | 2 |
| Omaha, NE | 208 | 103 | 17 | 4 | 0 | 0 |
| Richmond, VA | 286 | 142 | 34 | 7 | 3 | 5 |
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
| Fresno, CA | 232 | 122 | 24 | 6 | 1 | 2 |
| Bakersfield, CA | 158 | 83 | 12 | 1 | 0 | 1 |
| Long Beach, CA | 523 | 355 | 74 | 8 | 0 | 5 |
| Oakland, CA | 341 | 223 | 51 | 9 | 1 | 5 |
| Riverside, CA | 294 | 188 | 37 | 2 | 0 | 2 |
| Colorado Springs, CO | 168 | 99 | 28 | 2 | 0 | 1 |
| Spokane, WA | 148 | 80 | 12 | 5 | 0 | 1 |
| Wichita, KS | 167 | 96 | 20 | 4 | 0 | 2 |
| Des Moines, IA | 158 | 79 | 19 | 10 | 2 | 3 |
| Madison, WI | 150 | 76 | 22 | 7 | 0 | 0 |
| Rochester, NY | 204 | 120 | 34 | 9 | 0 | 6 |
| Albany, NY | 171 | 108 | 22 | 5 | 0 | 0 |
| Knoxville, TN | 168 | 96 | 14 | 5 | 0 | 0 |
| Chattanooga, TN | 188 | 104 | 17 | 5 | 0 | 0 |
| Greenville, SC | 156 | 96 | 34 | 6 | 0 | 0 |
| Columbia, SC | 211 | 111 | 21 | 8 | 1 | 2 |
| Savannah, GA | 177 | 81 | 19 | 4 | 0 | 0 |
| Little Rock, AR | 176 | 91 | 14 | 5 | 0 | 0 |
| Baton Rouge, LA | 186 | 74 | 14 | 4 | 0 | 0 |
| Anchorage, AK | 150 | 56 | 10 | 2 | 0 | 1 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 9058 | 4675 | 190 |
| YellowPages | 18486 | 13177 | 199 |
| BBB | 4454 | 2196 | 139 |
| OpenStreetMap | 2266 | 1130 | 20 |

Discovery tasks completed: bbb=1508, gmaps=425, osm=85, yp=987

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 179 | 0 | 35 | 214 |
| beads-craft | 1097 | 79 | 12 | 1188 |
| chain | 5923 | 0 | 0 | 5923 |
| coin-currency | 598 | 11 | 0 | 609 |
| costume-fashion | 810 | 293 | 80 | 1183 |
| diamond-trade | 193 | 41 | 10 | 244 |
| gold-buyer | 424 | 90 | 27 | 541 |
| kiosk-battery | 24 | 0 | 0 | 24 |
| no-segment | 0 | 0 | 2914 | 2914 |
| pawn | 1667 | 79 | 26 | 1772 |
| piercing-tattoo | 1250 | 97 | 20 | 1367 |
| simulants | 8 | 43 | 5 | 56 |
| thrift-consignment | 297 | 0 | 0 | 297 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 131 | 11 | 1 | 143 |
| **all** | | | | **16479** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 5602 | bbb:041e21befdeeed50: appraiser-lab-insurer |
| bbb | blocked | 297 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 101 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-500 | 59 | https://overpass.kumi.systems/api/interpreter |
| osm | http-504 | 29 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 25 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 23 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-406 | 22 | https://overpass-api.de/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
