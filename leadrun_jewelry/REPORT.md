# Jewelry retail lead run — REPORT

Generated 2026-10-16T15:52:40+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 29783 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 18668 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 489 |
| Qualification rate | 2.6% |
| Websites crawled OK / attempted | 15352 / 18477 |
| Listings with an owner/decision-maker name | 4319 |
| LinkedIn searches by outcome | ambiguous: 217, match: 151, none: 486, reject: 110 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 18668 (100.0%) | 489 (100.0%) |
| 2 | Segment | 18668 (100.0%) | 489 (100.0%) |
| 3 | Category (as listed) | 18626 (99.8%) | 488 (99.8%) |
| 4 | Phone | 17511 (93.8%) | 478 (97.8%) |
| 5 | Email | 4301 (23.0%) | 479 (98.0%) |
| 6 | LinkedIn Profile | 134 (0.7%) | 127 (26.0%) |
| 7 | Contact Person | 2158 (11.6%) | 256 (52.4%) |
| 8 | Role | 2158 (11.6%) | 256 (52.4%) |
| 9 | Website | 14113 (75.6%) | 489 (100.0%) |
| 10 | Address | 17917 (96.0%) | 483 (98.8%) |
| 11 | Real City | 15110 (80.9%) | 418 (85.5%) |
| 12 | Real State | 15210 (81.5%) | 417 (85.3%) |
| 13 | Market | 18668 (100.0%) | 489 (100.0%) |
| 14 | Lead Origin | 18668 (100.0%) | 489 (100.0%) |
| 15 | Rating | 6258 (33.5%) | 270 (55.2%) |
| 16 | Reviews | 6258 (33.5%) | 270 (55.2%) |
| 17 | Source | 18668 (100.0%) | 489 (100.0%) |
| 18 | Signals | 18668 (100.0%) | 489 (100.0%) |
| 19 | Match Type | 18668 (100.0%) | 489 (100.0%) |
| 20 | Email Source | 4301 (23.0%) | 479 (98.0%) |
| 21 | LinkedIn Source | 140 (0.7%) | 127 (26.0%) |
| 22 | Found At | 18668 (100.0%) | 489 (100.0%) |
| 23 | Also Listed As | 2521 (13.5%) | 140 (28.6%) |
| 24 | Other Markets | 510 (2.7%) | 50 (10.2%) |
| 25 | Merged Listings | 4605 (24.7%) | 228 (46.6%) |
| 26 | Flags | 2564 (13.7%) | 107 (21.9%) |
| 27 | Mobile Candidates | 531 (2.8%) | 374 (76.5%) |
| 28 | Socials | 4202 (22.5%) | 429 (87.7%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 4301 | 23.0% |
| linkedin | 134 | 0.7% |
| direct-line | 531 | 2.8% |
| role-email | 1710 | 9.2% |
| gia | 1085 | 5.8% |
| ags | 154 | 0.8% |
| ja | 89 | 0.5% |
| bench | 733 | 3.9% |
| custom-design | 2991 | 16.0% |
| since-yyyy | 3696 | 19.8% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1031 | 235 | 77 | 8 | 31 |
| Chicago, IL | 993 | 683 | 155 | 63 | 5 | 19 |
| Houston, TX | 1030 | 696 | 142 | 56 | 5 | 21 |
| Dallas, TX | 722 | 480 | 89 | 58 | 5 | 8 |
| Miami, FL | 1024 | 725 | 160 | 66 | 5 | 33 |
| Atlanta, GA | 739 | 524 | 127 | 60 | 11 | 23 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 3 | 14 |
| San Francisco, CA | 732 | 444 | 124 | 68 | 3 | 10 |
| Boston, MA | 570 | 344 | 109 | 56 | 7 | 18 |
| Seattle, WA | 589 | 347 | 93 | 69 | 2 | 10 |
| Las Vegas, NV | 691 | 401 | 73 | 74 | 3 | 11 |
| Phoenix, AZ | 730 | 461 | 93 | 57 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 333 | 104 | 85 | 5 | 11 |
| Washington, DC | 382 | 223 | 76 | 30 | 1 | 6 |
| Detroit, MI | 554 | 377 | 82 | 51 | 6 | 18 |
| Minneapolis, MN | 531 | 245 | 61 | 91 | 6 | 9 |
| Charlotte, NC | 350 | 207 | 47 | 40 | 2 | 5 |
| Nashville, TN | 341 | 180 | 45 | 52 | 4 | 4 |
| Scottsdale, AZ | 263 | 149 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 151 | 46 | 21 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 258 | 66 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 458 | 110 | 28 | 1 | 13 |
| Austin, TX | 458 | 239 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 303 | 51 | 42 | 2 | 6 |
| Fort Worth, TX | 456 | 259 | 47 | 24 | 0 | 0 |
| San Jose, CA | 522 | 288 | 36 | 16 | 0 | 3 |
| Sacramento, CA | 372 | 207 | 38 | 39 | 2 | 7 |
| Portland, OR | 515 | 278 | 69 | 55 | 2 | 4 |
| Salt Lake City, UT | 445 | 237 | 65 | 71 | 7 | 9 |
| Kansas City, MO | 451 | 264 | 74 | 79 | 3 | 8 |
| St. Louis, MO | 526 | 263 | 72 | 53 | 2 | 6 |
| Columbus, OH | 238 | 136 | 41 | 22 | 2 | 4 |
| Cleveland, OH | 335 | 201 | 54 | 9 | 0 | 2 |
| Cincinnati, OH | 364 | 210 | 56 | 19 | 2 | 3 |
| Indianapolis, IN | 262 | 161 | 40 | 13 | 0 | 6 |
| Pittsburgh, PA | 394 | 225 | 60 | 17 | 2 | 7 |
| Baltimore, MD | 327 | 216 | 46 | 8 | 1 | 6 |
| Orlando, FL | 433 | 257 | 53 | 20 | 1 | 5 |
| Tampa, FL | 395 | 251 | 57 | 21 | 0 | 5 |
| Fort Lauderdale, FL | 581 | 389 | 79 | 33 | 3 | 7 |
| Raleigh, NC | 273 | 156 | 43 | 22 | 1 | 2 |
| New Orleans, LA | 511 | 287 | 66 | 43 | 2 | 8 |
| Jacksonville, FL | 333 | 196 | 43 | 14 | 0 | 2 |
| Memphis, TN | 371 | 209 | 32 | 54 | 0 | 4 |
| Louisville, KY | 164 | 109 | 31 | 10 | 0 | 2 |
| Milwaukee, WI | 282 | 146 | 42 | 6 | 0 | 0 |
| Albuquerque, NM | 296 | 192 | 47 | 10 | 0 | 3 |
| Tucson, AZ | 221 | 132 | 37 | 7 | 0 | 2 |
| Oklahoma City, OK | 236 | 141 | 23 | 5 | 0 | 1 |
| Tulsa, OK | 203 | 109 | 13 | 4 | 0 | 2 |
| Omaha, NE | 208 | 103 | 17 | 4 | 0 | 0 |
| Richmond, VA | 249 | 127 | 26 | 7 | 0 | 1 |
| Virginia Beach, VA | 238 | 127 | 23 | 10 | 0 | 2 |
| Birmingham, AL | 187 | 92 | 20 | 8 | 0 | 1 |
| Buffalo, NY | 276 | 164 | 43 | 9 | 0 | 2 |
| Hartford, CT | 250 | 126 | 27 | 10 | 0 | 2 |
| Providence, RI | 396 | 245 | 53 | 13 | 0 | 3 |
| El Paso, TX | 208 | 134 | 17 | 5 | 0 | 3 |
| Honolulu, HI | 452 | 274 | 56 | 10 | 0 | 7 |
| Boise, ID | 169 | 85 | 26 | 6 | 0 | 2 |
| Charleston, SC | 216 | 111 | 32 | 7 | 0 | 0 |
| Grand Rapids, MI | 124 | 71 | 13 | 3 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 7220 | 3881 | 162 |
| YellowPages | 16333 | 11702 | 181 |
| BBB | 4195 | 2033 | 128 |
| OpenStreetMap | 2048 | 1052 | 18 |

Discovery tasks completed: bbb=1393, gmaps=317, osm=65, yp=856

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 150 | 0 | 35 | 185 |
| beads-craft | 982 | 70 | 8 | 1060 |
| chain | 5411 | 0 | 0 | 5411 |
| coin-currency | 491 | 10 | 0 | 501 |
| costume-fashion | 718 | 260 | 65 | 1043 |
| diamond-trade | 183 | 40 | 9 | 232 |
| gold-buyer | 370 | 78 | 24 | 472 |
| kiosk-battery | 21 | 0 | 0 | 21 |
| no-segment | 0 | 0 | 2118 | 2118 |
| pawn | 1404 | 71 | 25 | 1500 |
| piercing-tattoo | 1044 | 83 | 20 | 1147 |
| simulants | 8 | 42 | 5 | 55 |
| thrift-consignment | 166 | 0 | 0 | 166 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 121 | 11 | 1 | 133 |
| **all** | | | | **14048** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 4249 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| bbb | blocked | 266 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 76 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 24 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| yp | soft-block-503 | 23 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-406 | 22 | https://overpass-api.de/api/interpreter |
| osm | http-500 | 22 | https://overpass.kumi.systems/api/interpreter |
| linkedin | blocked | 20 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
