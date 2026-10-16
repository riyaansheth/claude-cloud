# Jewelry retail lead run — REPORT

Generated 2026-10-16T14:40:51+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 28088 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 17997 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 469 |
| Qualification rate | 2.6% |
| Websites crawled OK / attempted | 14147 / 16944 |
| Listings with an owner/decision-maker name | 4086 |
| LinkedIn searches by outcome | ambiguous: 217, match: 151, none: 486, reject: 110 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 17997 (100.0%) | 469 (100.0%) |
| 2 | Segment | 17997 (100.0%) | 469 (100.0%) |
| 3 | Category (as listed) | 17957 (99.8%) | 469 (100.0%) |
| 4 | Phone | 16915 (94.0%) | 458 (97.7%) |
| 5 | Email | 3971 (22.1%) | 459 (97.9%) |
| 6 | LinkedIn Profile | 134 (0.7%) | 127 (27.1%) |
| 7 | Contact Person | 2022 (11.2%) | 251 (53.5%) |
| 8 | Role | 2022 (11.2%) | 251 (53.5%) |
| 9 | Website | 13681 (76.0%) | 469 (100.0%) |
| 10 | Address | 17280 (96.0%) | 463 (98.7%) |
| 11 | Real City | 14985 (83.3%) | 406 (86.6%) |
| 12 | Real State | 15085 (83.8%) | 405 (86.4%) |
| 13 | Market | 17997 (100.0%) | 469 (100.0%) |
| 14 | Lead Origin | 17997 (100.0%) | 469 (100.0%) |
| 15 | Rating | 5381 (29.9%) | 244 (52.0%) |
| 16 | Reviews | 5381 (29.9%) | 244 (52.0%) |
| 17 | Source | 17997 (100.0%) | 469 (100.0%) |
| 18 | Signals | 17997 (100.0%) | 469 (100.0%) |
| 19 | Match Type | 17997 (100.0%) | 469 (100.0%) |
| 20 | Email Source | 3971 (22.1%) | 459 (97.9%) |
| 21 | LinkedIn Source | 140 (0.8%) | 127 (27.1%) |
| 22 | Found At | 17997 (100.0%) | 469 (100.0%) |
| 23 | Also Listed As | 2350 (13.1%) | 130 (27.7%) |
| 24 | Other Markets | 491 (2.7%) | 48 (10.2%) |
| 25 | Merged Listings | 4288 (23.8%) | 215 (45.8%) |
| 26 | Flags | 2402 (13.3%) | 100 (21.3%) |
| 27 | Mobile Candidates | 497 (2.8%) | 354 (75.5%) |
| 28 | Socials | 3828 (21.3%) | 412 (87.8%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3971 | 22.1% |
| linkedin | 134 | 0.7% |
| direct-line | 497 | 2.8% |
| role-email | 1601 | 8.9% |
| gia | 1011 | 5.6% |
| ags | 142 | 0.8% |
| ja | 77 | 0.4% |
| bench | 662 | 3.7% |
| custom-design | 2762 | 15.3% |
| since-yyyy | 3470 | 19.3% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 8 | 31 |
| Chicago, IL | 993 | 684 | 155 | 64 | 5 | 19 |
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
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 11 |
| Washington, DC | 382 | 224 | 76 | 31 | 1 | 6 |
| Detroit, MI | 554 | 377 | 82 | 51 | 6 | 18 |
| Minneapolis, MN | 531 | 245 | 61 | 91 | 6 | 9 |
| Charlotte, NC | 350 | 207 | 47 | 40 | 2 | 5 |
| Nashville, TN | 341 | 183 | 47 | 53 | 4 | 4 |
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
| Cincinnati, OH | 364 | 211 | 56 | 19 | 2 | 3 |
| Indianapolis, IN | 262 | 161 | 40 | 13 | 0 | 6 |
| Pittsburgh, PA | 394 | 224 | 60 | 17 | 2 | 7 |
| Baltimore, MD | 327 | 216 | 46 | 8 | 1 | 6 |
| Orlando, FL | 433 | 257 | 52 | 19 | 1 | 5 |
| Tampa, FL | 395 | 251 | 57 | 21 | 0 | 5 |
| Fort Lauderdale, FL | 581 | 389 | 79 | 33 | 3 | 7 |
| Raleigh, NC | 273 | 156 | 43 | 22 | 1 | 2 |
| New Orleans, LA | 511 | 287 | 66 | 43 | 2 | 8 |
| Jacksonville, FL | 258 | 170 | 38 | 5 | 0 | 2 |
| Memphis, TN | 246 | 147 | 16 | 3 | 0 | 1 |
| Louisville, KY | 76 | 51 | 12 | 2 | 0 | 0 |
| Milwaukee, WI | 163 | 102 | 30 | 3 | 0 | 0 |
| Albuquerque, NM | 203 | 154 | 30 | 7 | 0 | 2 |
| Tucson, AZ | 147 | 106 | 7 | 1 | 0 | 2 |
| Oklahoma City, OK | 136 | 92 | 5 | 1 | 0 | 1 |
| Tulsa, OK | 128 | 80 | 3 | 1 | 0 | 0 |
| Omaha, NE | 92 | 63 | 4 | 1 | 0 | 0 |
| Richmond, VA | 166 | 99 | 6 | 2 | 0 | 0 |
| Virginia Beach, VA | 239 | 130 | 20 | 9 | 0 | 2 |
| Birmingham, AL | 187 | 93 | 13 | 4 | 0 | 1 |
| Buffalo, NY | 205 | 124 | 31 | 8 | 0 | 1 |
| Hartford, CT | 133 | 86 | 21 | 6 | 0 | 3 |
| Providence, RI | 276 | 209 | 20 | 6 | 0 | 1 |
| El Paso, TX | 115 | 78 | 4 | 2 | 0 | 0 |
| Honolulu, HI | 348 | 242 | 12 | 1 | 0 | 2 |
| Boise, ID | 69 | 47 | 2 | 0 | 0 | 1 |
| Charleston, SC | 124 | 81 | 12 | 1 | 0 | 0 |
| Grand Rapids, MI | 73 | 58 | 2 | 0 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 5732 | 3210 | 147 |
| YellowPages | 16342 | 11787 | 178 |
| BBB | 3994 | 1939 | 127 |
| OpenStreetMap | 2033 | 1061 | 17 |

Discovery tasks completed: bbb=1353, gmaps=245, osm=63, yp=856

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 133 | 0 | 35 | 168 |
| beads-craft | 951 | 62 | 7 | 1020 |
| chain | 5331 | 0 | 0 | 5331 |
| coin-currency | 464 | 10 | 0 | 474 |
| costume-fashion | 698 | 247 | 59 | 1004 |
| diamond-trade | 172 | 39 | 8 | 219 |
| gold-buyer | 352 | 69 | 21 | 442 |
| kiosk-battery | 18 | 0 | 0 | 18 |
| no-segment | 0 | 0 | 1661 | 1661 |
| pawn | 1328 | 65 | 23 | 1416 |
| piercing-tattoo | 960 | 72 | 19 | 1051 |
| simulants | 8 | 41 | 4 | 53 |
| thrift-consignment | 115 | 0 | 0 | 115 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 115 | 10 | 1 | 126 |
| **all** | | | | **13102** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 4040 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| bbb | blocked | 256 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 74 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 24 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| yp | soft-block-503 | 23 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-406 | 22 | https://overpass-api.de/api/interpreter |
| osm | http-500 | 22 | https://overpass.kumi.systems/api/interpreter |
| linkedin | blocked | 20 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
