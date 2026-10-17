# Jewelry retail lead run — REPORT

Generated 2026-10-17T11:37:10+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 36949 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 22575 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 568 |
| Qualification rate | 2.5% |
| Websites crawled OK / attempted | 19014 / 22907 |
| Listings with an owner/decision-maker name | 4855 |
| LinkedIn searches by outcome | ambiguous: 276, match: 179, none: 551, reject: 131 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 22575 (100.0%) | 568 (100.0%) |
| 2 | Segment | 22575 (100.0%) | 568 (100.0%) |
| 3 | Category (as listed) | 22528 (99.8%) | 567 (99.8%) |
| 4 | Phone | 21149 (93.7%) | 555 (97.7%) |
| 5 | Email | 5121 (22.7%) | 557 (98.1%) |
| 6 | LinkedIn Profile | 161 (0.7%) | 154 (27.1%) |
| 7 | Contact Person | 2438 (10.8%) | 295 (51.9%) |
| 8 | Role | 2438 (10.8%) | 295 (51.9%) |
| 9 | Website | 16979 (75.2%) | 568 (100.0%) |
| 10 | Address | 21678 (96.0%) | 561 (98.8%) |
| 11 | Real City | 17818 (78.9%) | 478 (84.2%) |
| 12 | Real State | 17922 (79.4%) | 477 (84.0%) |
| 13 | Market | 22575 (100.0%) | 568 (100.0%) |
| 14 | Lead Origin | 22575 (100.0%) | 568 (100.0%) |
| 15 | Rating | 8086 (35.8%) | 336 (59.2%) |
| 16 | Reviews | 8086 (35.8%) | 336 (59.2%) |
| 17 | Source | 22575 (100.0%) | 568 (100.0%) |
| 18 | Signals | 22575 (100.0%) | 568 (100.0%) |
| 19 | Match Type | 22575 (100.0%) | 568 (100.0%) |
| 20 | Email Source | 5121 (22.7%) | 557 (98.1%) |
| 21 | LinkedIn Source | 166 (0.7%) | 154 (27.1%) |
| 22 | Found At | 22575 (100.0%) | 568 (100.0%) |
| 23 | Also Listed As | 2984 (13.2%) | 162 (28.5%) |
| 24 | Other Markets | 677 (3.0%) | 71 (12.5%) |
| 25 | Merged Listings | 5499 (24.4%) | 269 (47.4%) |
| 26 | Flags | 3037 (13.5%) | 123 (21.7%) |
| 27 | Mobile Candidates | 621 (2.8%) | 426 (75.0%) |
| 28 | Socials | 4985 (22.1%) | 501 (88.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 5121 | 22.7% |
| linkedin | 161 | 0.7% |
| direct-line | 621 | 2.8% |
| role-email | 1970 | 8.7% |
| gia | 1239 | 5.5% |
| ags | 193 | 0.9% |
| ja | 105 | 0.5% |
| bench | 866 | 3.8% |
| custom-design | 3519 | 15.6% |
| since-yyyy | 4156 | 18.4% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 37 |
| Los Angeles, CA | 1280 | 1029 | 234 | 76 | 8 | 31 |
| Chicago, IL | 993 | 682 | 155 | 63 | 5 | 19 |
| Houston, TX | 1030 | 696 | 142 | 56 | 5 | 21 |
| Dallas, TX | 722 | 478 | 88 | 57 | 5 | 7 |
| Miami, FL | 1024 | 724 | 160 | 66 | 5 | 33 |
| Atlanta, GA | 739 | 517 | 124 | 57 | 11 | 23 |
| Philadelphia, PA | 767 | 544 | 91 | 27 | 3 | 14 |
| San Francisco, CA | 731 | 443 | 124 | 69 | 3 | 10 |
| Boston, MA | 570 | 343 | 110 | 55 | 7 | 18 |
| Seattle, WA | 589 | 346 | 92 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 401 | 73 | 74 | 3 | 11 |
| Phoenix, AZ | 730 | 461 | 93 | 57 | 0 | 11 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 332 | 103 | 85 | 5 | 11 |
| Washington, DC | 382 | 223 | 76 | 30 | 1 | 6 |
| Detroit, MI | 554 | 364 | 77 | 43 | 5 | 16 |
| Minneapolis, MN | 531 | 244 | 63 | 92 | 6 | 10 |
| Charlotte, NC | 350 | 205 | 47 | 39 | 2 | 4 |
| Nashville, TN | 341 | 178 | 44 | 51 | 4 | 4 |
| Scottsdale, AZ | 263 | 149 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 151 | 46 | 21 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 257 | 65 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 457 | 110 | 29 | 1 | 13 |
| Austin, TX | 458 | 238 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 302 | 51 | 42 | 2 | 6 |
| Fort Worth, TX | 456 | 259 | 47 | 24 | 0 | 0 |
| San Jose, CA | 522 | 287 | 36 | 16 | 0 | 3 |
| Sacramento, CA | 372 | 205 | 37 | 38 | 2 | 7 |
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
| Tucson, AZ | 290 | 160 | 40 | 32 | 0 | 1 |
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
| Little Rock, AR | 176 | 90 | 14 | 5 | 0 | 0 |
| Baton Rouge, LA | 186 | 74 | 14 | 4 | 0 | 0 |
| Anchorage, AK | 150 | 56 | 10 | 2 | 0 | 1 |
| Akron, OH | 153 | 91 | 15 | 9 | 1 | 1 |
| Toledo, OH | 130 | 66 | 9 | 6 | 0 | 2 |
| Dayton, OH | 136 | 76 | 12 | 4 | 0 | 1 |
| Lexington, KY | 140 | 73 | 23 | 3 | 0 | 1 |
| Syracuse, NY | 123 | 55 | 11 | 3 | 0 | 0 |
| Worcester, MA | 168 | 91 | 21 | 10 | 0 | 3 |
| New Haven, CT | 203 | 117 | 20 | 6 | 0 | 1 |
| Allentown, PA | 196 | 113 | 27 | 6 | 0 | 1 |
| Harrisburg, PA | 142 | 83 | 8 | 1 | 0 | 0 |
| Durham, NC | 57 | 32 | 8 | 2 | 0 | 0 |
| Greensboro, NC | 167 | 89 | 29 | 5 | 0 | 3 |
| Winston-Salem, NC | 138 | 72 | 15 | 3 | 0 | 0 |
| Mobile, AL | 160 | 70 | 9 | 3 | 0 | 2 |
| Jackson, MS | 107 | 55 | 11 | 3 | 0 | 1 |
| Shreveport, LA | 108 | 50 | 13 | 2 | 0 | 2 |
| Lubbock, TX | 102 | 59 | 11 | 1 | 0 | 2 |
| Corpus Christi, TX | 145 | 83 | 14 | 1 | 0 | 2 |
| Reno, NV | 126 | 71 | 16 | 4 | 0 | 0 |
| Sioux Falls, SD | 96 | 37 | 3 | 1 | 0 | 0 |
| Fort Wayne, IN | 44 | 23 | 9 | 0 | 0 | 1 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 10267 | 5169 | 203 |
| YellowPages | 19807 | 14033 | 208 |
| BBB | 4508 | 2201 | 137 |
| OpenStreetMap | 2376 | 1172 | 20 |

Discovery tasks completed: bbb=1514, gmaps=515, osm=105, yp=1069

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 200 | 0 | 35 | 235 |
| beads-craft | 1163 | 84 | 12 | 1259 |
| chain | 6262 | 0 | 0 | 6262 |
| coin-currency | 704 | 12 | 0 | 716 |
| costume-fashion | 890 | 317 | 92 | 1299 |
| diamond-trade | 199 | 41 | 10 | 250 |
| gold-buyer | 451 | 97 | 27 | 575 |
| kiosk-battery | 28 | 0 | 0 | 28 |
| no-segment | 0 | 0 | 3417 | 3417 |
| pawn | 1882 | 89 | 29 | 2000 |
| piercing-tattoo | 1389 | 100 | 20 | 1509 |
| simulants | 8 | 43 | 5 | 56 |
| thrift-consignment | 378 | 0 | 0 | 378 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 141 | 11 | 1 | 153 |
| **all** | | | | **18141** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 5934 | bbb:041e21befdeeed50: appraiser-lab-insurer |
| bbb | blocked | 312 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 122 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-500 | 83 | https://overpass.kumi.systems/api/interpreter |
| osm | http-504 | 31 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 25 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 24 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-406 | 23 | https://overpass-api.de/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
