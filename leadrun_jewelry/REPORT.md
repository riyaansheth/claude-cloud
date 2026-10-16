# Jewelry retail lead run — REPORT

Generated 2026-10-16T16:06:57+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 29910 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 18730 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 497 |
| Qualification rate | 2.7% |
| Websites crawled OK / attempted | 15447 / 18601 |
| Listings with an owner/decision-maker name | 4342 |
| LinkedIn searches by outcome | ambiguous: 228, match: 157, none: 509, reject: 113 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 18730 (100.0%) | 497 (100.0%) |
| 2 | Segment | 18730 (100.0%) | 497 (100.0%) |
| 3 | Category (as listed) | 18687 (99.8%) | 496 (99.8%) |
| 4 | Phone | 17568 (93.8%) | 486 (97.8%) |
| 5 | Email | 4320 (23.1%) | 487 (98.0%) |
| 6 | LinkedIn Profile | 140 (0.7%) | 133 (26.8%) |
| 7 | Contact Person | 2171 (11.6%) | 262 (52.7%) |
| 8 | Role | 2171 (11.6%) | 262 (52.7%) |
| 9 | Website | 14152 (75.6%) | 497 (100.0%) |
| 10 | Address | 17977 (96.0%) | 491 (98.8%) |
| 11 | Real City | 15139 (80.8%) | 422 (84.9%) |
| 12 | Real State | 15239 (81.4%) | 421 (84.7%) |
| 13 | Market | 18730 (100.0%) | 497 (100.0%) |
| 14 | Lead Origin | 18730 (100.0%) | 497 (100.0%) |
| 15 | Rating | 6305 (33.7%) | 278 (55.9%) |
| 16 | Reviews | 6305 (33.7%) | 278 (55.9%) |
| 17 | Source | 18730 (100.0%) | 497 (100.0%) |
| 18 | Signals | 18730 (100.0%) | 497 (100.0%) |
| 19 | Match Type | 18730 (100.0%) | 497 (100.0%) |
| 20 | Email Source | 4320 (23.1%) | 487 (98.0%) |
| 21 | LinkedIn Source | 146 (0.8%) | 133 (26.8%) |
| 22 | Found At | 18730 (100.0%) | 497 (100.0%) |
| 23 | Also Listed As | 2527 (13.5%) | 142 (28.6%) |
| 24 | Other Markets | 510 (2.7%) | 50 (10.1%) |
| 25 | Merged Listings | 4618 (24.7%) | 231 (46.5%) |
| 26 | Flags | 2572 (13.7%) | 109 (21.9%) |
| 27 | Mobile Candidates | 536 (2.9%) | 376 (75.7%) |
| 28 | Socials | 4229 (22.6%) | 437 (87.9%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 4320 | 23.1% |
| linkedin | 140 | 0.7% |
| direct-line | 536 | 2.9% |
| role-email | 1719 | 9.2% |
| gia | 1090 | 5.8% |
| ags | 154 | 0.8% |
| ja | 89 | 0.5% |
| bench | 736 | 3.9% |
| custom-design | 3006 | 16.0% |
| since-yyyy | 3721 | 19.9% |

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
| Nashville, TN | 341 | 179 | 45 | 52 | 4 | 4 |
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
| New Orleans, LA | 511 | 287 | 66 | 43 | 3 | 9 |
| Jacksonville, FL | 333 | 196 | 43 | 14 | 0 | 2 |
| Memphis, TN | 401 | 232 | 36 | 65 | 1 | 5 |
| Louisville, KY | 164 | 109 | 31 | 10 | 1 | 3 |
| Milwaukee, WI | 282 | 146 | 42 | 6 | 0 | 0 |
| Albuquerque, NM | 296 | 192 | 47 | 10 | 0 | 3 |
| Tucson, AZ | 221 | 132 | 37 | 7 | 0 | 2 |
| Oklahoma City, OK | 236 | 141 | 23 | 5 | 0 | 1 |
| Tulsa, OK | 203 | 109 | 13 | 4 | 0 | 2 |
| Omaha, NE | 208 | 103 | 17 | 4 | 0 | 0 |
| Richmond, VA | 286 | 143 | 34 | 7 | 0 | 2 |
| Virginia Beach, VA | 238 | 127 | 23 | 10 | 0 | 2 |
| Birmingham, AL | 187 | 92 | 20 | 8 | 0 | 1 |
| Buffalo, NY | 276 | 164 | 43 | 9 | 0 | 2 |
| Hartford, CT | 250 | 126 | 27 | 10 | 0 | 2 |
| Providence, RI | 396 | 245 | 53 | 13 | 1 | 4 |
| El Paso, TX | 208 | 134 | 17 | 5 | 1 | 4 |
| Honolulu, HI | 452 | 274 | 56 | 10 | 0 | 7 |
| Boise, ID | 169 | 85 | 26 | 6 | 0 | 2 |
| Charleston, SC | 216 | 111 | 32 | 7 | 1 | 1 |
| Grand Rapids, MI | 171 | 95 | 20 | 5 | 0 | 1 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 7304 | 3929 | 168 |
| YellowPages | 16333 | 11695 | 181 |
| BBB | 4225 | 2056 | 130 |
| OpenStreetMap | 2048 | 1050 | 18 |

Discovery tasks completed: bbb=1422, gmaps=325, osm=65, yp=856

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 151 | 0 | 35 | 186 |
| beads-craft | 982 | 71 | 8 | 1061 |
| chain | 5412 | 0 | 0 | 5412 |
| coin-currency | 492 | 10 | 0 | 502 |
| costume-fashion | 720 | 260 | 65 | 1045 |
| diamond-trade | 183 | 40 | 9 | 232 |
| gold-buyer | 372 | 79 | 25 | 476 |
| kiosk-battery | 22 | 0 | 0 | 22 |
| no-segment | 0 | 0 | 2175 | 2175 |
| pawn | 1406 | 71 | 25 | 1502 |
| piercing-tattoo | 1045 | 83 | 20 | 1148 |
| simulants | 8 | 42 | 5 | 55 |
| thrift-consignment | 178 | 0 | 0 | 178 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 121 | 11 | 1 | 133 |
| **all** | | | | **14131** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 4319 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| bbb | blocked | 272 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 76 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 24 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| yp | soft-block-503 | 23 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-406 | 22 | https://overpass-api.de/api/interpreter |
| osm | http-500 | 22 | https://overpass.kumi.systems/api/interpreter |
| linkedin | blocked | 21 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
