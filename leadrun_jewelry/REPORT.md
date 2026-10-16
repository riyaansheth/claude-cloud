# Jewelry retail lead run — REPORT

Generated 2026-10-16T15:01:28+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 28587 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 18175 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 482 |
| Qualification rate | 2.7% |
| Websites crawled OK / attempted | 14799 / 17768 |
| Listings with an owner/decision-maker name | 4157 |
| LinkedIn searches by outcome | ambiguous: 217, match: 151, none: 486, reject: 110 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 18175 (100.0%) | 482 (100.0%) |
| 2 | Segment | 18175 (100.0%) | 482 (100.0%) |
| 3 | Category (as listed) | 18134 (99.8%) | 481 (99.8%) |
| 4 | Phone | 17056 (93.8%) | 471 (97.7%) |
| 5 | Email | 4160 (22.9%) | 472 (97.9%) |
| 6 | LinkedIn Profile | 134 (0.7%) | 127 (26.3%) |
| 7 | Contact Person | 2068 (11.4%) | 254 (52.7%) |
| 8 | Role | 2068 (11.4%) | 254 (52.7%) |
| 9 | Website | 13795 (75.9%) | 482 (100.0%) |
| 10 | Address | 17447 (96.0%) | 476 (98.8%) |
| 11 | Real City | 14983 (82.4%) | 416 (86.3%) |
| 12 | Real State | 15083 (83.0%) | 415 (86.1%) |
| 13 | Market | 18175 (100.0%) | 482 (100.0%) |
| 14 | Lead Origin | 18175 (100.0%) | 482 (100.0%) |
| 15 | Rating | 5673 (31.2%) | 255 (52.9%) |
| 16 | Reviews | 5673 (31.2%) | 255 (52.9%) |
| 17 | Source | 18175 (100.0%) | 482 (100.0%) |
| 18 | Signals | 18175 (100.0%) | 482 (100.0%) |
| 19 | Match Type | 18175 (100.0%) | 482 (100.0%) |
| 20 | Email Source | 4160 (22.9%) | 472 (97.9%) |
| 21 | LinkedIn Source | 140 (0.8%) | 127 (26.3%) |
| 22 | Found At | 18175 (100.0%) | 482 (100.0%) |
| 23 | Also Listed As | 2406 (13.2%) | 137 (28.4%) |
| 24 | Other Markets | 497 (2.7%) | 49 (10.2%) |
| 25 | Merged Listings | 4386 (24.1%) | 223 (46.3%) |
| 26 | Flags | 2443 (13.4%) | 104 (21.6%) |
| 27 | Mobile Candidates | 520 (2.9%) | 367 (76.1%) |
| 28 | Socials | 4028 (22.2%) | 423 (87.8%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 4160 | 22.9% |
| linkedin | 134 | 0.7% |
| direct-line | 520 | 2.9% |
| role-email | 1659 | 9.1% |
| gia | 1065 | 5.9% |
| ags | 152 | 0.8% |
| ja | 86 | 0.5% |
| bench | 708 | 3.9% |
| custom-design | 2902 | 16.0% |
| since-yyyy | 3566 | 19.6% |

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
| San Francisco, CA | 732 | 444 | 124 | 67 | 3 | 10 |
| Boston, MA | 570 | 344 | 109 | 56 | 7 | 18 |
| Seattle, WA | 589 | 347 | 93 | 69 | 2 | 10 |
| Las Vegas, NV | 691 | 401 | 73 | 74 | 3 | 11 |
| Phoenix, AZ | 730 | 464 | 94 | 58 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 333 | 104 | 85 | 5 | 11 |
| Washington, DC | 382 | 224 | 76 | 31 | 1 | 6 |
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
| Pittsburgh, PA | 394 | 224 | 60 | 17 | 2 | 7 |
| Baltimore, MD | 327 | 216 | 46 | 8 | 1 | 6 |
| Orlando, FL | 433 | 257 | 52 | 19 | 1 | 5 |
| Tampa, FL | 395 | 251 | 57 | 21 | 0 | 5 |
| Fort Lauderdale, FL | 581 | 389 | 79 | 33 | 3 | 7 |
| Raleigh, NC | 273 | 156 | 43 | 22 | 1 | 2 |
| New Orleans, LA | 511 | 287 | 66 | 43 | 2 | 8 |
| Jacksonville, FL | 258 | 166 | 41 | 7 | 0 | 2 |
| Memphis, TN | 245 | 146 | 26 | 4 | 0 | 2 |
| Louisville, KY | 164 | 109 | 31 | 9 | 0 | 2 |
| Milwaukee, WI | 282 | 149 | 42 | 6 | 0 | 0 |
| Albuquerque, NM | 248 | 169 | 31 | 8 | 0 | 2 |
| Tucson, AZ | 147 | 105 | 26 | 4 | 0 | 3 |
| Oklahoma City, OK | 135 | 90 | 14 | 3 | 0 | 2 |
| Tulsa, OK | 128 | 78 | 8 | 2 | 0 | 1 |
| Omaha, NE | 92 | 63 | 11 | 2 | 0 | 0 |
| Richmond, VA | 164 | 96 | 18 | 6 | 0 | 1 |
| Virginia Beach, VA | 239 | 127 | 23 | 10 | 0 | 2 |
| Birmingham, AL | 187 | 92 | 20 | 8 | 0 | 1 |
| Buffalo, NY | 276 | 164 | 43 | 9 | 0 | 2 |
| Hartford, CT | 252 | 129 | 24 | 7 | 0 | 2 |
| Providence, RI | 324 | 212 | 33 | 9 | 0 | 3 |
| El Paso, TX | 123 | 81 | 9 | 2 | 0 | 1 |
| Honolulu, HI | 347 | 235 | 37 | 6 | 0 | 4 |
| Boise, ID | 68 | 45 | 12 | 4 | 0 | 2 |
| Charleston, SC | 122 | 79 | 19 | 3 | 0 | 0 |
| Grand Rapids, MI | 79 | 62 | 12 | 3 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 6222 | 3428 | 152 |
| YellowPages | 16333 | 11747 | 185 |
| BBB | 3994 | 1934 | 127 |
| OpenStreetMap | 2048 | 1066 | 18 |

Discovery tasks completed: bbb=1353, gmaps=265, osm=65, yp=856

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 137 | 0 | 35 | 172 |
| beads-craft | 959 | 64 | 7 | 1030 |
| chain | 5350 | 0 | 0 | 5350 |
| coin-currency | 474 | 10 | 0 | 484 |
| costume-fashion | 707 | 256 | 59 | 1022 |
| diamond-trade | 177 | 39 | 9 | 225 |
| gold-buyer | 358 | 72 | 23 | 453 |
| kiosk-battery | 18 | 0 | 0 | 18 |
| no-segment | 0 | 0 | 1841 | 1841 |
| pawn | 1349 | 70 | 24 | 1443 |
| piercing-tattoo | 976 | 72 | 20 | 1068 |
| simulants | 8 | 41 | 4 | 53 |
| thrift-consignment | 133 | 0 | 0 | 133 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 116 | 10 | 1 | 127 |
| **all** | | | | **13423** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 4109 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| bbb | blocked | 256 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
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
