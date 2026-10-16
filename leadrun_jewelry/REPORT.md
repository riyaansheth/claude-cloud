# Jewelry retail lead run — REPORT

Generated 2026-10-16T18:29:28+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 33004 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 20656 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 535 |
| Qualification rate | 2.6% |
| Websites crawled OK / attempted | 17070 / 20553 |
| Listings with an owner/decision-maker name | 4551 |
| LinkedIn searches by outcome | ambiguous: 260, match: 170, none: 538, reject: 126 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 20656 (100.0%) | 535 (100.0%) |
| 2 | Segment | 20656 (100.0%) | 535 (100.0%) |
| 3 | Category (as listed) | 20614 (99.8%) | 534 (99.8%) |
| 4 | Phone | 19388 (93.9%) | 522 (97.6%) |
| 5 | Email | 4689 (22.7%) | 525 (98.1%) |
| 6 | LinkedIn Profile | 152 (0.7%) | 145 (27.1%) |
| 7 | Contact Person | 2280 (11.0%) | 280 (52.3%) |
| 8 | Role | 2280 (11.0%) | 280 (52.3%) |
| 9 | Website | 15646 (75.7%) | 535 (100.0%) |
| 10 | Address | 19825 (96.0%) | 529 (98.9%) |
| 11 | Real City | 16747 (81.1%) | 457 (85.4%) |
| 12 | Real State | 16849 (81.6%) | 456 (85.2%) |
| 13 | Market | 20656 (100.0%) | 535 (100.0%) |
| 14 | Lead Origin | 20656 (100.0%) | 535 (100.0%) |
| 15 | Rating | 6849 (33.2%) | 298 (55.7%) |
| 16 | Reviews | 6849 (33.2%) | 298 (55.7%) |
| 17 | Source | 20656 (100.0%) | 535 (100.0%) |
| 18 | Signals | 20656 (100.0%) | 535 (100.0%) |
| 19 | Match Type | 20656 (100.0%) | 535 (100.0%) |
| 20 | Email Source | 4689 (22.7%) | 525 (98.1%) |
| 21 | LinkedIn Source | 158 (0.8%) | 145 (27.1%) |
| 22 | Found At | 20656 (100.0%) | 535 (100.0%) |
| 23 | Also Listed As | 2720 (13.2%) | 150 (28.0%) |
| 24 | Other Markets | 587 (2.8%) | 59 (11.0%) |
| 25 | Merged Listings | 4986 (24.1%) | 247 (46.2%) |
| 26 | Flags | 2782 (13.5%) | 112 (20.9%) |
| 27 | Mobile Candidates | 583 (2.8%) | 401 (75.0%) |
| 28 | Socials | 4550 (22.0%) | 472 (88.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 4689 | 22.7% |
| linkedin | 152 | 0.7% |
| direct-line | 583 | 2.8% |
| role-email | 1832 | 8.9% |
| gia | 1154 | 5.6% |
| ags | 172 | 0.8% |
| ja | 93 | 0.5% |
| bench | 800 | 3.9% |
| custom-design | 3250 | 15.7% |
| since-yyyy | 3909 | 18.9% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1029 | 234 | 76 | 8 | 31 |
| Chicago, IL | 993 | 682 | 155 | 63 | 5 | 19 |
| Houston, TX | 1030 | 696 | 142 | 56 | 5 | 21 |
| Dallas, TX | 722 | 479 | 88 | 57 | 5 | 7 |
| Miami, FL | 1024 | 725 | 160 | 66 | 5 | 33 |
| Atlanta, GA | 739 | 517 | 124 | 57 | 11 | 23 |
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
| Minneapolis, MN | 531 | 245 | 62 | 92 | 6 | 9 |
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
| New Orleans, LA | 511 | 281 | 66 | 40 | 3 | 9 |
| Jacksonville, FL | 333 | 196 | 43 | 14 | 2 | 4 |
| Memphis, TN | 401 | 230 | 36 | 63 | 2 | 6 |
| Louisville, KY | 203 | 123 | 36 | 29 | 2 | 4 |
| Milwaukee, WI | 290 | 150 | 44 | 9 | 0 | 0 |
| Albuquerque, NM | 365 | 220 | 53 | 35 | 0 | 6 |
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
| Fresno, CA | 232 | 122 | 24 | 6 | 0 | 1 |
| Bakersfield, CA | 158 | 83 | 12 | 1 | 0 | 1 |
| Long Beach, CA | 523 | 356 | 73 | 6 | 0 | 5 |
| Oakland, CA | 235 | 161 | 28 | 3 | 0 | 2 |
| Riverside, CA | 216 | 150 | 25 | 2 | 0 | 2 |
| Colorado Springs, CO | 89 | 68 | 12 | 1 | 0 | 1 |
| Spokane, WA | 65 | 47 | 5 | 4 | 0 | 1 |
| Wichita, KS | 71 | 55 | 11 | 3 | 0 | 1 |
| Des Moines, IA | 74 | 48 | 12 | 7 | 0 | 1 |
| Madison, WI | 96 | 64 | 17 | 4 | 0 | 2 |
| Rochester, NY | 199 | 119 | 34 | 9 | 0 | 6 |
| Albany, NY | 171 | 108 | 22 | 5 | 0 | 0 |
| Knoxville, TN | 168 | 96 | 14 | 5 | 0 | 0 |
| Chattanooga, TN | 188 | 109 | 15 | 4 | 0 | 0 |
| Greenville, SC | 116 | 75 | 19 | 2 | 0 | 0 |
| Columbia, SC | 103 | 62 | 12 | 4 | 0 | 0 |
| Savannah, GA | 68 | 44 | 8 | 0 | 0 | 0 |
| Little Rock, AR | 85 | 58 | 7 | 2 | 0 | 0 |
| Baton Rouge, LA | 88 | 41 | 6 | 3 | 0 | 0 |
| Anchorage, AK | 55 | 39 | 7 | 1 | 0 | 1 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 7960 | 4206 | 180 |
| YellowPages | 18486 | 13215 | 202 |
| BBB | 4341 | 2100 | 133 |
| OpenStreetMap | 2238 | 1135 | 20 |

Discovery tasks completed: bbb=1476, gmaps=360, osm=81, yp=987

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 165 | 0 | 35 | 200 |
| beads-craft | 1070 | 76 | 11 | 1157 |
| chain | 5901 | 0 | 0 | 5901 |
| coin-currency | 575 | 11 | 0 | 586 |
| costume-fashion | 805 | 284 | 75 | 1164 |
| diamond-trade | 188 | 41 | 10 | 239 |
| gold-buyer | 399 | 87 | 26 | 512 |
| kiosk-battery | 24 | 0 | 0 | 24 |
| no-segment | 0 | 0 | 2450 | 2450 |
| pawn | 1600 | 79 | 26 | 1705 |
| piercing-tattoo | 1193 | 89 | 20 | 1302 |
| simulants | 8 | 43 | 5 | 56 |
| thrift-consignment | 215 | 0 | 0 | 215 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 128 | 11 | 1 | 140 |
| **all** | | | | **15655** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 4957 | bbb:041e21befdeeed50: appraiser-lab-insurer |
| bbb | blocked | 285 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 96 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-500 | 54 | https://overpass.kumi.systems/api/interpreter |
| osm | http-504 | 28 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 23 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 23 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-406 | 22 | https://overpass-api.de/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
