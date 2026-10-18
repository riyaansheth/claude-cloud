# Jewelry retail lead run — REPORT

Generated 2026-10-18T17:17:16+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 40926 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 25369 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 580 |
| Qualification rate | 2.3% |
| Websites crawled OK / attempted | 20262 / 24382 |
| Listings with an owner/decision-maker name | 4919 |
| LinkedIn searches by outcome | ambiguous: 293, match: 182, none: 570, reject: 135 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 25369 (100.0%) | 580 (100.0%) |
| 2 | Segment | 25369 (100.0%) | 580 (100.0%) |
| 3 | Category (as listed) | 25316 (99.8%) | 579 (99.8%) |
| 4 | Phone | 23700 (93.4%) | 565 (97.4%) |
| 5 | Email | 5432 (21.4%) | 569 (98.1%) |
| 6 | LinkedIn Profile | 164 (0.6%) | 156 (26.9%) |
| 7 | Contact Person | 2472 (9.7%) | 295 (50.9%) |
| 8 | Role | 2472 (9.7%) | 295 (50.9%) |
| 9 | Website | 19169 (75.6%) | 580 (100.0%) |
| 10 | Address | 24306 (95.8%) | 573 (98.8%) |
| 11 | Real City | 20101 (79.2%) | 486 (83.8%) |
| 12 | Real State | 20205 (79.6%) | 484 (83.4%) |
| 13 | Market | 25369 (100.0%) | 580 (100.0%) |
| 14 | Lead Origin | 25369 (100.0%) | 580 (100.0%) |
| 15 | Rating | 8725 (34.4%) | 344 (59.3%) |
| 16 | Reviews | 8725 (34.4%) | 344 (59.3%) |
| 17 | Source | 25369 (100.0%) | 580 (100.0%) |
| 18 | Signals | 25369 (100.0%) | 580 (100.0%) |
| 19 | Match Type | 25369 (100.0%) | 580 (100.0%) |
| 20 | Email Source | 5432 (21.4%) | 569 (98.1%) |
| 21 | LinkedIn Source | 168 (0.7%) | 156 (26.9%) |
| 22 | Found At | 25369 (100.0%) | 580 (100.0%) |
| 23 | Also Listed As | 3245 (12.8%) | 168 (29.0%) |
| 24 | Other Markets | 881 (3.5%) | 83 (14.3%) |
| 25 | Merged Listings | 5965 (23.5%) | 276 (47.6%) |
| 26 | Flags | 3362 (13.3%) | 127 (21.9%) |
| 27 | Mobile Candidates | 642 (2.5%) | 436 (75.2%) |
| 28 | Socials | 5231 (20.6%) | 508 (87.6%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 5432 | 21.4% |
| linkedin | 164 | 0.6% |
| direct-line | 642 | 2.5% |
| role-email | 2090 | 8.2% |
| gia | 1296 | 5.1% |
| ags | 199 | 0.8% |
| ja | 114 | 0.4% |
| bench | 901 | 3.6% |
| custom-design | 3679 | 14.5% |
| since-yyyy | 4273 | 16.8% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1440 | 1193 | 276 | 90 | 11 | 36 |
| Los Angeles, CA | 1279 | 1028 | 234 | 76 | 8 | 31 |
| Chicago, IL | 988 | 678 | 154 | 59 | 5 | 18 |
| Houston, TX | 1030 | 695 | 142 | 56 | 5 | 21 |
| Dallas, TX | 719 | 473 | 88 | 56 | 5 | 7 |
| Miami, FL | 1024 | 724 | 160 | 66 | 5 | 33 |
| Atlanta, GA | 739 | 517 | 124 | 57 | 11 | 22 |
| Philadelphia, PA | 767 | 542 | 91 | 27 | 3 | 12 |
| San Francisco, CA | 731 | 443 | 124 | 69 | 3 | 10 |
| Boston, MA | 570 | 341 | 110 | 54 | 7 | 18 |
| Seattle, WA | 589 | 346 | 92 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 400 | 73 | 74 | 3 | 11 |
| Phoenix, AZ | 730 | 461 | 93 | 57 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 331 | 103 | 85 | 5 | 11 |
| Washington, DC | 378 | 221 | 76 | 30 | 1 | 4 |
| Detroit, MI | 554 | 363 | 78 | 43 | 5 | 16 |
| Minneapolis, MN | 531 | 244 | 63 | 92 | 6 | 10 |
| Charlotte, NC | 350 | 205 | 47 | 39 | 2 | 4 |
| Nashville, TN | 341 | 178 | 44 | 51 | 4 | 4 |
| Scottsdale, AZ | 263 | 149 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 151 | 46 | 21 | 1 | 6 |
| Greenwich, CT | 141 | 80 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 256 | 65 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 457 | 110 | 29 | 1 | 13 |
| Austin, TX | 458 | 238 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 301 | 51 | 42 | 2 | 6 |
| Fort Worth, TX | 456 | 257 | 46 | 23 | 0 | 0 |
| San Jose, CA | 522 | 287 | 37 | 16 | 0 | 3 |
| Sacramento, CA | 372 | 205 | 37 | 38 | 2 | 7 |
| Portland, OR | 515 | 278 | 69 | 55 | 2 | 4 |
| Salt Lake City, UT | 445 | 237 | 65 | 71 | 7 | 9 |
| Kansas City, MO | 451 | 264 | 74 | 79 | 3 | 8 |
| St. Louis, MO | 526 | 262 | 72 | 52 | 2 | 6 |
| Columbus, OH | 238 | 132 | 41 | 20 | 2 | 4 |
| Cleveland, OH | 335 | 201 | 54 | 9 | 0 | 2 |
| Cincinnati, OH | 364 | 210 | 57 | 19 | 2 | 3 |
| Indianapolis, IN | 262 | 160 | 40 | 13 | 0 | 6 |
| Pittsburgh, PA | 394 | 224 | 59 | 16 | 2 | 6 |
| Baltimore, MD | 327 | 216 | 46 | 8 | 1 | 6 |
| Orlando, FL | 433 | 257 | 53 | 20 | 1 | 5 |
| Tampa, FL | 395 | 250 | 57 | 21 | 0 | 5 |
| Fort Lauderdale, FL | 581 | 388 | 79 | 33 | 3 | 7 |
| Raleigh, NC | 273 | 155 | 43 | 22 | 1 | 2 |
| New Orleans, LA | 511 | 279 | 65 | 39 | 3 | 9 |
| Jacksonville, FL | 333 | 195 | 42 | 13 | 2 | 4 |
| Memphis, TN | 401 | 230 | 36 | 63 | 2 | 6 |
| Louisville, KY | 203 | 122 | 35 | 28 | 2 | 4 |
| Milwaukee, WI | 290 | 150 | 44 | 9 | 0 | 0 |
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
| Savannah, GA | 177 | 81 | 19 | 4 | 1 | 1 |
| Little Rock, AR | 176 | 90 | 14 | 5 | 0 | 0 |
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
| Garden City, NY | 912 | 680 | 111 | 13 | 0 | 5 |
| Huntington, NY | 341 | 211 | 14 | 2 | 0 | 0 |
| Hackensack, NJ | 855 | 715 | 4 | 0 | 0 | 0 |
| Newark, NJ | 18 | 17 | 4 | 2 | 0 | 0 |
| Edison, NJ | 0 | 0 | 0 | 0 | 0 | 0 |
| White Plains, NY | 122 | 76 | 17 | 2 | 0 | 2 |
| Irvine, CA | 121 | 80 | 1 | 1 | 0 | 0 |
| Anaheim, CA | 58 | 53 | 0 | 0 | 0 | 0 |
| Pasadena, CA | 22 | 16 | 7 | 0 | 0 | 1 |
| Sherman Oaks, CA | 0 | 0 | 0 | 0 | 0 | 0 |
| Plano, TX | 401 | 250 | 57 | 7 | 0 | 4 |
| Schaumburg, IL | 426 | 286 | 52 | 11 | 0 | 2 |
| Northbrook, IL | 146 | 94 | 2 | 2 | 0 | 0 |
| Bethesda, MD | 198 | 128 | 3 | 1 | 0 | 0 |
| Fairfax, VA | 54 | 43 | 1 | 0 | 0 | 0 |
| King of Prussia, PA | 79 | 31 | 12 | 3 | 0 | 0 |
| Alpharetta, GA | 125 | 74 | 5 | 1 | 0 | 1 |
| Troy, MI | 51 | 39 | 4 | 0 | 0 | 1 |
| Fort Myers, FL | 9 | 9 | 0 | 0 | 0 | 0 |
| Sarasota, FL | 7 | 7 | 1 | 0 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 11128 | 5555 | 209 |
| YellowPages | 22605 | 16190 | 215 |
| BBB | 4510 | 2187 | 135 |
| OpenStreetMap | 2761 | 1437 | 21 |

Discovery tasks completed: bbb=1708, gmaps=595, osm=122, yp=1588

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 241 | 0 | 33 | 274 |
| beads-craft | 1314 | 84 | 12 | 1410 |
| chain | 6881 | 0 | 0 | 6881 |
| coin-currency | 783 | 12 | 0 | 795 |
| costume-fashion | 1062 | 338 | 99 | 1499 |
| diamond-trade | 230 | 43 | 10 | 283 |
| gold-buyer | 506 | 109 | 29 | 644 |
| kiosk-battery | 29 | 0 | 0 | 29 |
| no-segment | 0 | 0 | 3724 | 3724 |
| pawn | 2007 | 91 | 29 | 2127 |
| piercing-tattoo | 1482 | 104 | 21 | 1607 |
| simulants | 8 | 44 | 9 | 61 |
| thrift-consignment | 414 | 0 | 0 | 414 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 154 | 12 | 1 | 167 |
| **all** | | | | **19919** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 6442 | bbb:041e21befdeeed50: appraiser-lab-insurer |
| bbb | blocked | 321 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 132 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-500 | 112 | https://overpass.kumi.systems/api/interpreter |
| osm | http-504 | 34 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| yp | soft-block-503 | 34 | https://www.yellowpages.com/search?search_terms=custom+jewelry&geo_location_terms=Garden+City%2C+NY&page=7 |
| osm | http-406 | 33 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 26 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
