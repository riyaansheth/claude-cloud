# Jewelry retail lead run — REPORT

Generated 2026-10-18T17:50:50+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 44099 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 27335 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 615 |
| Qualification rate | 2.2% |
| Websites crawled OK / attempted | 22366 / 26844 |
| Listings with an owner/decision-maker name | 5004 |
| LinkedIn searches by outcome | ambiguous: 293, match: 182, none: 570, reject: 135 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 27335 (100.0%) | 615 (100.0%) |
| 2 | Segment | 27335 (100.0%) | 615 (100.0%) |
| 3 | Category (as listed) | 27278 (99.8%) | 614 (99.8%) |
| 4 | Phone | 25647 (93.8%) | 600 (97.6%) |
| 5 | Email | 5896 (21.6%) | 604 (98.2%) |
| 6 | LinkedIn Profile | 164 (0.6%) | 156 (25.4%) |
| 7 | Contact Person | 2528 (9.2%) | 300 (48.8%) |
| 8 | Role | 2528 (9.2%) | 300 (48.8%) |
| 9 | Website | 20824 (76.2%) | 615 (100.0%) |
| 10 | Address | 26253 (96.0%) | 608 (98.9%) |
| 11 | Real City | 21862 (80.0%) | 517 (84.1%) |
| 12 | Real State | 21961 (80.3%) | 516 (83.9%) |
| 13 | Market | 27335 (100.0%) | 615 (100.0%) |
| 14 | Lead Origin | 27335 (100.0%) | 615 (100.0%) |
| 15 | Rating | 9365 (34.3%) | 364 (59.2%) |
| 16 | Reviews | 9365 (34.3%) | 364 (59.2%) |
| 17 | Source | 27335 (100.0%) | 615 (100.0%) |
| 18 | Signals | 27335 (100.0%) | 615 (100.0%) |
| 19 | Match Type | 27335 (100.0%) | 615 (100.0%) |
| 20 | Email Source | 5896 (21.6%) | 604 (98.2%) |
| 21 | LinkedIn Source | 168 (0.6%) | 156 (25.4%) |
| 22 | Found At | 27335 (100.0%) | 615 (100.0%) |
| 23 | Also Listed As | 3503 (12.8%) | 182 (29.6%) |
| 24 | Other Markets | 1086 (4.0%) | 96 (15.6%) |
| 25 | Merged Listings | 6450 (23.6%) | 293 (47.6%) |
| 26 | Flags | 3576 (13.1%) | 138 (22.4%) |
| 27 | Mobile Candidates | 684 (2.5%) | 471 (76.6%) |
| 28 | Socials | 5578 (20.4%) | 539 (87.6%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 5896 | 21.6% |
| linkedin | 164 | 0.6% |
| direct-line | 684 | 2.5% |
| role-email | 2279 | 8.3% |
| gia | 1400 | 5.1% |
| ags | 208 | 0.8% |
| ja | 121 | 0.4% |
| bench | 972 | 3.6% |
| custom-design | 3933 | 14.4% |
| since-yyyy | 4459 | 16.3% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1440 | 1175 | 272 | 87 | 11 | 34 |
| Los Angeles, CA | 1279 | 1025 | 235 | 74 | 8 | 31 |
| Chicago, IL | 988 | 677 | 154 | 58 | 5 | 18 |
| Houston, TX | 1030 | 695 | 142 | 56 | 5 | 21 |
| Dallas, TX | 719 | 473 | 88 | 56 | 5 | 7 |
| Miami, FL | 1024 | 724 | 160 | 66 | 5 | 33 |
| Atlanta, GA | 735 | 511 | 124 | 56 | 11 | 22 |
| Philadelphia, PA | 761 | 542 | 91 | 27 | 3 | 12 |
| San Francisco, CA | 731 | 443 | 124 | 69 | 3 | 10 |
| Boston, MA | 570 | 341 | 110 | 54 | 7 | 18 |
| Seattle, WA | 589 | 346 | 92 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 399 | 72 | 74 | 3 | 10 |
| Phoenix, AZ | 730 | 461 | 93 | 57 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 331 | 103 | 85 | 5 | 11 |
| Washington, DC | 373 | 214 | 73 | 30 | 1 | 4 |
| Detroit, MI | 554 | 364 | 78 | 43 | 5 | 16 |
| Minneapolis, MN | 531 | 244 | 63 | 92 | 6 | 10 |
| Charlotte, NC | 350 | 205 | 47 | 39 | 2 | 4 |
| Nashville, TN | 341 | 178 | 44 | 51 | 4 | 4 |
| Scottsdale, AZ | 263 | 149 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 150 | 45 | 21 | 1 | 5 |
| Greenwich, CT | 141 | 79 | 27 | 6 | 1 | 5 |
| Palm Beach, FL | 445 | 256 | 65 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 457 | 110 | 29 | 1 | 13 |
| Austin, TX | 458 | 238 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 301 | 51 | 42 | 2 | 6 |
| Fort Worth, TX | 456 | 257 | 46 | 23 | 0 | 0 |
| San Jose, CA | 522 | 287 | 37 | 16 | 0 | 3 |
| Sacramento, CA | 372 | 205 | 37 | 38 | 2 | 7 |
| Portland, OR | 515 | 278 | 70 | 55 | 2 | 4 |
| Salt Lake City, UT | 445 | 237 | 65 | 71 | 7 | 9 |
| Kansas City, MO | 451 | 264 | 74 | 79 | 3 | 8 |
| St. Louis, MO | 526 | 261 | 71 | 52 | 2 | 5 |
| Columbus, OH | 238 | 132 | 41 | 20 | 2 | 4 |
| Cleveland, OH | 335 | 201 | 54 | 9 | 0 | 2 |
| Cincinnati, OH | 364 | 210 | 57 | 19 | 2 | 3 |
| Indianapolis, IN | 262 | 160 | 40 | 13 | 0 | 6 |
| Pittsburgh, PA | 394 | 223 | 59 | 16 | 2 | 6 |
| Baltimore, MD | 327 | 216 | 46 | 8 | 1 | 6 |
| Orlando, FL | 433 | 257 | 53 | 20 | 1 | 5 |
| Tampa, FL | 395 | 250 | 57 | 21 | 0 | 5 |
| Fort Lauderdale, FL | 581 | 388 | 79 | 33 | 3 | 7 |
| Raleigh, NC | 273 | 155 | 43 | 22 | 1 | 2 |
| New Orleans, LA | 511 | 279 | 65 | 39 | 3 | 9 |
| Jacksonville, FL | 333 | 195 | 42 | 13 | 2 | 4 |
| Memphis, TN | 401 | 230 | 36 | 63 | 2 | 6 |
| Louisville, KY | 203 | 122 | 35 | 28 | 2 | 4 |
| Milwaukee, WI | 289 | 150 | 44 | 9 | 0 | 0 |
| Albuquerque, NM | 463 | 311 | 72 | 77 | 4 | 12 |
| Tucson, AZ | 291 | 161 | 40 | 33 | 0 | 1 |
| Oklahoma City, OK | 236 | 141 | 23 | 5 | 0 | 1 |
| Tulsa, OK | 203 | 109 | 13 | 4 | 0 | 2 |
| Omaha, NE | 208 | 103 | 17 | 4 | 0 | 0 |
| Richmond, VA | 286 | 142 | 34 | 7 | 3 | 5 |
| Virginia Beach, VA | 238 | 127 | 23 | 10 | 1 | 3 |
| Birmingham, AL | 187 | 92 | 20 | 8 | 0 | 1 |
| Buffalo, NY | 276 | 164 | 43 | 9 | 1 | 3 |
| Hartford, CT | 250 | 126 | 27 | 10 | 1 | 3 |
| Providence, RI | 396 | 244 | 52 | 13 | 1 | 4 |
| El Paso, TX | 208 | 134 | 17 | 5 | 1 | 4 |
| Honolulu, HI | 452 | 274 | 56 | 10 | 0 | 7 |
| Boise, ID | 169 | 85 | 26 | 6 | 1 | 3 |
| Charleston, SC | 216 | 111 | 32 | 7 | 2 | 2 |
| Grand Rapids, MI | 170 | 95 | 20 | 5 | 0 | 1 |
| Fresno, CA | 232 | 122 | 25 | 6 | 1 | 2 |
| Bakersfield, CA | 158 | 83 | 12 | 1 | 0 | 1 |
| Long Beach, CA | 522 | 352 | 73 | 7 | 0 | 6 |
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
| Savannah, GA | 177 | 81 | 19 | 4 | 1 | 1 |
| Little Rock, AR | 176 | 89 | 14 | 5 | 0 | 0 |
| Baton Rouge, LA | 186 | 74 | 14 | 4 | 0 | 0 |
| Anchorage, AK | 150 | 56 | 10 | 2 | 0 | 1 |
| Akron, OH | 153 | 91 | 15 | 9 | 1 | 1 |
| Toledo, OH | 130 | 66 | 9 | 6 | 0 | 2 |
| Dayton, OH | 136 | 76 | 12 | 4 | 1 | 2 |
| Lexington, KY | 140 | 73 | 23 | 3 | 0 | 1 |
| Syracuse, NY | 123 | 55 | 11 | 3 | 1 | 1 |
| Worcester, MA | 168 | 91 | 21 | 10 | 0 | 3 |
| New Haven, CT | 203 | 117 | 20 | 6 | 0 | 1 |
| Allentown, PA | 196 | 113 | 27 | 6 | 0 | 1 |
| Harrisburg, PA | 141 | 84 | 11 | 1 | 0 | 0 |
| Durham, NC | 114 | 58 | 21 | 4 | 0 | 1 |
| Greensboro, NC | 167 | 89 | 29 | 5 | 0 | 3 |
| Winston-Salem, NC | 138 | 72 | 15 | 3 | 0 | 0 |
| Mobile, AL | 160 | 70 | 9 | 3 | 0 | 2 |
| Jackson, MS | 107 | 55 | 11 | 3 | 0 | 1 |
| Shreveport, LA | 108 | 50 | 13 | 2 | 0 | 2 |
| Lubbock, TX | 102 | 59 | 11 | 1 | 0 | 2 |
| Corpus Christi, TX | 145 | 83 | 14 | 1 | 0 | 2 |
| Reno, NV | 126 | 71 | 16 | 4 | 0 | 0 |
| Sioux Falls, SD | 95 | 33 | 4 | 1 | 0 | 0 |
| Fort Wayne, IN | 104 | 45 | 15 | 1 | 0 | 0 |
| Garden City, NY | 912 | 675 | 111 | 13 | 0 | 5 |
| Huntington, NY | 339 | 209 | 51 | 7 | 0 | 4 |
| Hackensack, NJ | 977 | 752 | 113 | 10 | 0 | 10 |
| Newark, NJ | 839 | 599 | 106 | 12 | 0 | 8 |
| Edison, NJ | 351 | 254 | 26 | 2 | 0 | 4 |
| White Plains, NY | 348 | 214 | 25 | 5 | 0 | 2 |
| Irvine, CA | 574 | 327 | 43 | 12 | 0 | 4 |
| Anaheim, CA | 204 | 133 | 9 | 3 | 0 | 0 |
| Pasadena, CA | 68 | 29 | 6 | 0 | 0 | 1 |
| Sherman Oaks, CA | 0 | 0 | 0 | 0 | 0 | 0 |
| Plano, TX | 401 | 248 | 58 | 7 | 0 | 4 |
| Schaumburg, IL | 425 | 279 | 71 | 11 | 0 | 5 |
| Northbrook, IL | 194 | 117 | 23 | 7 | 0 | 0 |
| Bethesda, MD | 379 | 244 | 47 | 8 | 0 | 2 |
| Fairfax, VA | 285 | 176 | 25 | 0 | 0 | 2 |
| King of Prussia, PA | 342 | 203 | 12 | 3 | 0 | 0 |
| Alpharetta, GA | 339 | 223 | 24 | 7 | 0 | 2 |
| Troy, MI | 119 | 74 | 13 | 2 | 0 | 1 |
| Fort Myers, FL | 99 | 55 | 2 | 0 | 0 | 0 |
| Sarasota, FL | 7 | 7 | 2 | 0 | 0 | 2 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 11909 | 5910 | 217 |
| YellowPages | 25018 | 17854 | 244 |
| BBB | 4510 | 2177 | 131 |
| OpenStreetMap | 2810 | 1394 | 23 |

Discovery tasks completed: bbb=1708, gmaps=660, osm=125, yp=2220

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 269 | 0 | 32 | 301 |
| beads-craft | 1437 | 89 | 12 | 1538 |
| chain | 7264 | 0 | 0 | 7264 |
| coin-currency | 849 | 13 | 0 | 862 |
| costume-fashion | 1223 | 368 | 109 | 1700 |
| diamond-trade | 246 | 45 | 10 | 301 |
| gold-buyer | 576 | 113 | 31 | 720 |
| kiosk-battery | 30 | 0 | 0 | 30 |
| no-segment | 0 | 0 | 4032 | 4032 |
| pawn | 2128 | 99 | 29 | 2256 |
| piercing-tattoo | 1588 | 105 | 21 | 1714 |
| simulants | 10 | 46 | 9 | 65 |
| thrift-consignment | 440 | 0 | 0 | 440 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 165 | 16 | 1 | 182 |
| **all** | | | | **21409** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 6536 | bbb:041e21befdeeed50: appraiser-lab-insurer |
| bbb | blocked | 321 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 136 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-500 | 116 | https://overpass.kumi.systems/api/interpreter |
| yp | soft-block-503 | 41 | https://www.yellowpages.com/search?search_terms=custom+jewelry&geo_location_terms=Garden+City%2C+NY&page=7 |
| osm | http-504 | 35 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 33 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 26 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
