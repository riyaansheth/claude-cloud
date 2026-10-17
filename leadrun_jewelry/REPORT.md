# Jewelry retail lead run — REPORT

Generated 2026-10-17T10:55:28+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 36079 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 22244 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 561 |
| Qualification rate | 2.5% |
| Websites crawled OK / attempted | 18600 / 22390 |
| Listings with an owner/decision-maker name | 4788 |
| LinkedIn searches by outcome | ambiguous: 276, match: 179, none: 551, reject: 131 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 22244 (100.0%) | 561 (100.0%) |
| 2 | Segment | 22244 (100.0%) | 561 (100.0%) |
| 3 | Category (as listed) | 22200 (99.8%) | 560 (99.8%) |
| 4 | Phone | 20859 (93.8%) | 549 (97.9%) |
| 5 | Email | 5046 (22.7%) | 550 (98.0%) |
| 6 | LinkedIn Profile | 161 (0.7%) | 154 (27.5%) |
| 7 | Contact Person | 2411 (10.8%) | 294 (52.4%) |
| 8 | Role | 2411 (10.8%) | 294 (52.4%) |
| 9 | Website | 16782 (75.4%) | 561 (100.0%) |
| 10 | Address | 21358 (96.0%) | 554 (98.8%) |
| 11 | Real City | 17783 (79.9%) | 475 (84.7%) |
| 12 | Real State | 17887 (80.4%) | 474 (84.5%) |
| 13 | Market | 22244 (100.0%) | 561 (100.0%) |
| 14 | Lead Origin | 22244 (100.0%) | 561 (100.0%) |
| 15 | Rating | 7708 (34.7%) | 324 (57.8%) |
| 16 | Reviews | 7708 (34.7%) | 324 (57.8%) |
| 17 | Source | 22244 (100.0%) | 561 (100.0%) |
| 18 | Signals | 22244 (100.0%) | 561 (100.0%) |
| 19 | Match Type | 22244 (100.0%) | 561 (100.0%) |
| 20 | Email Source | 5046 (22.7%) | 550 (98.0%) |
| 21 | LinkedIn Source | 166 (0.7%) | 154 (27.5%) |
| 22 | Found At | 22244 (100.0%) | 561 (100.0%) |
| 23 | Also Listed As | 2936 (13.2%) | 159 (28.3%) |
| 24 | Other Markets | 672 (3.0%) | 69 (12.3%) |
| 25 | Merged Listings | 5387 (24.2%) | 261 (46.5%) |
| 26 | Flags | 2984 (13.4%) | 121 (21.6%) |
| 27 | Mobile Candidates | 614 (2.8%) | 419 (74.7%) |
| 28 | Socials | 4896 (22.0%) | 495 (88.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 5046 | 22.7% |
| linkedin | 161 | 0.7% |
| direct-line | 614 | 2.8% |
| role-email | 1938 | 8.7% |
| gia | 1226 | 5.5% |
| ags | 192 | 0.9% |
| ja | 105 | 0.5% |
| bench | 849 | 3.8% |
| custom-design | 3471 | 15.6% |
| since-yyyy | 4120 | 18.5% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1029 | 234 | 76 | 8 | 31 |
| Chicago, IL | 993 | 682 | 155 | 63 | 5 | 19 |
| Houston, TX | 1030 | 696 | 142 | 56 | 5 | 21 |
| Dallas, TX | 722 | 478 | 89 | 57 | 5 | 7 |
| Miami, FL | 1024 | 724 | 160 | 66 | 5 | 33 |
| Atlanta, GA | 739 | 517 | 124 | 57 | 11 | 23 |
| Philadelphia, PA | 767 | 544 | 91 | 27 | 3 | 14 |
| San Francisco, CA | 731 | 443 | 124 | 69 | 3 | 10 |
| Boston, MA | 570 | 345 | 110 | 57 | 7 | 18 |
| Seattle, WA | 589 | 346 | 92 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 401 | 73 | 74 | 3 | 11 |
| Phoenix, AZ | 730 | 461 | 93 | 57 | 0 | 11 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 332 | 103 | 85 | 5 | 11 |
| Washington, DC | 382 | 223 | 76 | 30 | 1 | 6 |
| Detroit, MI | 554 | 365 | 77 | 43 | 5 | 16 |
| Minneapolis, MN | 531 | 244 | 63 | 92 | 6 | 10 |
| Charlotte, NC | 350 | 205 | 47 | 39 | 2 | 4 |
| Nashville, TN | 341 | 178 | 44 | 51 | 4 | 4 |
| Scottsdale, AZ | 263 | 149 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 151 | 46 | 21 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 257 | 65 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 457 | 110 | 29 | 1 | 13 |
| Austin, TX | 458 | 238 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 303 | 51 | 42 | 2 | 6 |
| Fort Worth, TX | 456 | 259 | 47 | 24 | 0 | 0 |
| San Jose, CA | 522 | 287 | 36 | 16 | 0 | 3 |
| Sacramento, CA | 372 | 206 | 38 | 38 | 2 | 7 |
| Portland, OR | 515 | 278 | 69 | 55 | 2 | 4 |
| Salt Lake City, UT | 445 | 237 | 65 | 71 | 7 | 9 |
| Kansas City, MO | 451 | 264 | 74 | 79 | 3 | 8 |
| St. Louis, MO | 526 | 262 | 72 | 52 | 2 | 6 |
| Columbus, OH | 238 | 132 | 41 | 20 | 2 | 4 |
| Cleveland, OH | 335 | 201 | 54 | 9 | 0 | 2 |
| Cincinnati, OH | 364 | 210 | 57 | 19 | 2 | 3 |
| Indianapolis, IN | 262 | 160 | 40 | 13 | 0 | 6 |
| Pittsburgh, PA | 394 | 225 | 60 | 17 | 2 | 7 |
| Baltimore, MD | 327 | 216 | 46 | 8 | 1 | 6 |
| Orlando, FL | 433 | 257 | 53 | 20 | 1 | 5 |
| Tampa, FL | 395 | 251 | 57 | 21 | 0 | 5 |
| Fort Lauderdale, FL | 581 | 388 | 79 | 33 | 3 | 7 |
| Raleigh, NC | 273 | 155 | 43 | 22 | 1 | 2 |
| New Orleans, LA | 511 | 280 | 66 | 39 | 3 | 9 |
| Jacksonville, FL | 333 | 195 | 42 | 13 | 2 | 4 |
| Memphis, TN | 401 | 230 | 36 | 63 | 2 | 6 |
| Louisville, KY | 203 | 122 | 35 | 28 | 2 | 4 |
| Milwaukee, WI | 290 | 150 | 44 | 9 | 0 | 0 |
| Albuquerque, NM | 463 | 311 | 72 | 77 | 4 | 12 |
| Tucson, AZ | 263 | 143 | 37 | 21 | 0 | 1 |
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
| Grand Rapids, MI | 170 | 95 | 20 | 5 | 0 | 1 |
| Fresno, CA | 232 | 122 | 24 | 6 | 1 | 2 |
| Bakersfield, CA | 158 | 83 | 12 | 1 | 0 | 1 |
| Long Beach, CA | 523 | 355 | 74 | 8 | 0 | 5 |
| Oakland, CA | 341 | 223 | 51 | 9 | 1 | 5 |
| Riverside, CA | 294 | 188 | 37 | 2 | 0 | 2 |
| Colorado Springs, CO | 168 | 99 | 28 | 2 | 0 | 1 |
| Spokane, WA | 148 | 80 | 12 | 5 | 0 | 1 |
| Wichita, KS | 167 | 96 | 20 | 4 | 0 | 2 |
| Des Moines, IA | 158 | 79 | 19 | 10 | 2 | 3 |
| Madison, WI | 150 | 75 | 21 | 7 | 0 | 0 |
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
| Akron, OH | 153 | 91 | 15 | 9 | 1 | 1 |
| Toledo, OH | 130 | 66 | 9 | 6 | 0 | 2 |
| Dayton, OH | 137 | 76 | 10 | 3 | 0 | 1 |
| Lexington, KY | 105 | 59 | 14 | 2 | 0 | 1 |
| Syracuse, NY | 56 | 34 | 6 | 1 | 0 | 1 |
| Worcester, MA | 77 | 54 | 9 | 5 | 0 | 1 |
| New Haven, CT | 115 | 85 | 13 | 3 | 0 | 0 |
| Allentown, PA | 115 | 81 | 17 | 5 | 0 | 0 |
| Harrisburg, PA | 67 | 54 | 5 | 1 | 0 | 0 |
| Durham, NC | 57 | 32 | 8 | 2 | 0 | 0 |
| Greensboro, NC | 167 | 89 | 29 | 5 | 0 | 3 |
| Winston-Salem, NC | 138 | 72 | 15 | 3 | 0 | 0 |
| Mobile, AL | 136 | 63 | 6 | 2 | 0 | 1 |
| Jackson, MS | 56 | 37 | 7 | 2 | 0 | 1 |
| Shreveport, LA | 48 | 31 | 10 | 2 | 0 | 1 |
| Lubbock, TX | 40 | 27 | 7 | 0 | 0 | 1 |
| Corpus Christi, TX | 76 | 52 | 12 | 0 | 0 | 2 |
| Reno, NV | 63 | 43 | 7 | 3 | 0 | 0 |
| Sioux Falls, SD | 35 | 18 | 2 | 1 | 0 | 0 |
| Fort Wayne, IN | 34 | 22 | 9 | 0 | 0 | 1 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 9438 | 4818 | 194 |
| YellowPages | 19807 | 14062 | 211 |
| BBB | 4481 | 2188 | 137 |
| OpenStreetMap | 2369 | 1176 | 19 |

Discovery tasks completed: bbb=1512, gmaps=452, osm=103, yp=1069

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 193 | 0 | 35 | 228 |
| beads-craft | 1155 | 80 | 12 | 1247 |
| chain | 6250 | 0 | 0 | 6250 |
| coin-currency | 682 | 12 | 0 | 694 |
| costume-fashion | 880 | 313 | 91 | 1284 |
| diamond-trade | 198 | 41 | 10 | 249 |
| gold-buyer | 434 | 91 | 27 | 552 |
| kiosk-battery | 24 | 0 | 0 | 24 |
| no-segment | 0 | 0 | 3088 | 3088 |
| pawn | 1826 | 89 | 28 | 1943 |
| piercing-tattoo | 1334 | 98 | 20 | 1452 |
| simulants | 8 | 43 | 5 | 56 |
| thrift-consignment | 324 | 0 | 0 | 324 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 139 | 11 | 1 | 151 |
| **all** | | | | **17546** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 5766 | bbb:041e21befdeeed50: appraiser-lab-insurer |
| bbb | blocked | 305 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 120 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-500 | 81 | https://overpass.kumi.systems/api/interpreter |
| osm | http-504 | 31 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 25 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 24 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-406 | 23 | https://overpass-api.de/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
