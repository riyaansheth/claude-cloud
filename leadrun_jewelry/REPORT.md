# Jewelry retail lead run — REPORT

Generated 2026-10-18T19:45:49+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 46526 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 28770 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 655 |
| Qualification rate | 2.3% |
| Websites crawled OK / attempted | 24693 / 29601 |
| Listings with an owner/decision-maker name | 5131 |
| LinkedIn searches by outcome | ambiguous: 321, match: 186, none: 623, reject: 137 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 28770 (100.0%) | 655 (100.0%) |
| 2 | Segment | 28770 (100.0%) | 655 (100.0%) |
| 3 | Category (as listed) | 28710 (99.8%) | 654 (99.8%) |
| 4 | Phone | 27072 (94.1%) | 640 (97.7%) |
| 5 | Email | 6382 (22.2%) | 643 (98.2%) |
| 6 | LinkedIn Profile | 168 (0.6%) | 160 (24.4%) |
| 7 | Contact Person | 2595 (9.0%) | 309 (47.2%) |
| 8 | Role | 2595 (9.0%) | 309 (47.2%) |
| 9 | Website | 21981 (76.4%) | 655 (100.0%) |
| 10 | Address | 27674 (96.2%) | 648 (98.9%) |
| 11 | Real City | 23221 (80.7%) | 552 (84.3%) |
| 12 | Real State | 23321 (81.1%) | 551 (84.1%) |
| 13 | Market | 28770 (100.0%) | 655 (100.0%) |
| 14 | Lead Origin | 28770 (100.0%) | 655 (100.0%) |
| 15 | Rating | 9757 (33.9%) | 393 (60.0%) |
| 16 | Reviews | 9757 (33.9%) | 393 (60.0%) |
| 17 | Source | 28770 (100.0%) | 655 (100.0%) |
| 18 | Signals | 28770 (100.0%) | 655 (100.0%) |
| 19 | Match Type | 28770 (100.0%) | 655 (100.0%) |
| 20 | Email Source | 6382 (22.2%) | 643 (98.2%) |
| 21 | LinkedIn Source | 172 (0.6%) | 160 (24.4%) |
| 22 | Found At | 28770 (100.0%) | 655 (100.0%) |
| 23 | Also Listed As | 3711 (12.9%) | 197 (30.1%) |
| 24 | Other Markets | 1249 (4.3%) | 110 (16.8%) |
| 25 | Merged Listings | 6814 (23.7%) | 315 (48.1%) |
| 26 | Flags | 3734 (13.0%) | 145 (22.1%) |
| 27 | Mobile Candidates | 727 (2.5%) | 508 (77.6%) |
| 28 | Socials | 5940 (20.6%) | 570 (87.0%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 6382 | 22.2% |
| linkedin | 168 | 0.6% |
| direct-line | 727 | 2.5% |
| role-email | 2456 | 8.5% |
| gia | 1478 | 5.1% |
| ags | 214 | 0.7% |
| ja | 127 | 0.4% |
| bench | 1025 | 3.6% |
| custom-design | 4169 | 14.5% |
| since-yyyy | 4631 | 16.1% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1440 | 1168 | 267 | 85 | 11 | 33 |
| Los Angeles, CA | 1278 | 999 | 229 | 73 | 9 | 29 |
| Chicago, IL | 988 | 677 | 154 | 58 | 5 | 18 |
| Houston, TX | 1029 | 694 | 142 | 56 | 5 | 21 |
| Dallas, TX | 719 | 473 | 88 | 56 | 5 | 7 |
| Miami, FL | 1024 | 724 | 160 | 66 | 5 | 33 |
| Atlanta, GA | 735 | 511 | 124 | 56 | 11 | 22 |
| Philadelphia, PA | 761 | 542 | 91 | 27 | 3 | 12 |
| San Francisco, CA | 731 | 443 | 124 | 69 | 3 | 10 |
| Boston, MA | 570 | 341 | 110 | 54 | 7 | 18 |
| Seattle, WA | 589 | 346 | 92 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 398 | 72 | 74 | 3 | 10 |
| Phoenix, AZ | 730 | 461 | 93 | 57 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 331 | 103 | 85 | 5 | 10 |
| Washington, DC | 373 | 214 | 73 | 30 | 1 | 4 |
| Detroit, MI | 550 | 357 | 77 | 42 | 5 | 15 |
| Minneapolis, MN | 531 | 244 | 63 | 92 | 6 | 10 |
| Charlotte, NC | 350 | 205 | 47 | 39 | 2 | 4 |
| Nashville, TN | 341 | 178 | 44 | 51 | 4 | 4 |
| Scottsdale, AZ | 263 | 149 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 150 | 45 | 21 | 1 | 5 |
| Greenwich, CT | 141 | 79 | 27 | 6 | 1 | 5 |
| Palm Beach, FL | 445 | 255 | 65 | 22 | 2 | 9 |
| Beverly Hills, CA | 622 | 454 | 110 | 29 | 1 | 13 |
| Austin, TX | 458 | 238 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 301 | 51 | 42 | 2 | 6 |
| Fort Worth, TX | 456 | 257 | 46 | 23 | 0 | 0 |
| San Jose, CA | 522 | 286 | 37 | 16 | 0 | 3 |
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
| Fort Lauderdale, FL | 581 | 387 | 79 | 33 | 3 | 7 |
| Raleigh, NC | 273 | 155 | 43 | 22 | 1 | 2 |
| New Orleans, LA | 511 | 279 | 65 | 39 | 3 | 9 |
| Jacksonville, FL | 333 | 195 | 42 | 13 | 2 | 4 |
| Memphis, TN | 401 | 230 | 37 | 63 | 2 | 6 |
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
| Long Beach, CA | 522 | 350 | 73 | 7 | 0 | 6 |
| Oakland, CA | 341 | 222 | 50 | 8 | 1 | 4 |
| Riverside, CA | 294 | 187 | 36 | 2 | 0 | 1 |
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
| Columbia, SC | 211 | 111 | 21 | 8 | 2 | 3 |
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
| Garden City, NY | 912 | 678 | 113 | 16 | 0 | 5 |
| Huntington, NY | 339 | 209 | 51 | 7 | 0 | 4 |
| Hackensack, NJ | 977 | 750 | 116 | 11 | 0 | 10 |
| Newark, NJ | 873 | 614 | 124 | 15 | 0 | 14 |
| Edison, NJ | 487 | 310 | 62 | 6 | 0 | 10 |
| White Plains, NY | 340 | 212 | 42 | 11 | 0 | 3 |
| Irvine, CA | 566 | 373 | 90 | 21 | 0 | 6 |
| Anaheim, CA | 411 | 243 | 43 | 7 | 0 | 2 |
| Pasadena, CA | 821 | 571 | 106 | 6 | 0 | 13 |
| Sherman Oaks, CA | 435 | 297 | 50 | 7 | 0 | 4 |
| Plano, TX | 401 | 248 | 58 | 7 | 0 | 4 |
| Schaumburg, IL | 425 | 279 | 71 | 11 | 0 | 5 |
| Northbrook, IL | 194 | 117 | 23 | 7 | 0 | 0 |
| Bethesda, MD | 378 | 238 | 55 | 8 | 0 | 4 |
| Fairfax, VA | 317 | 203 | 40 | 5 | 0 | 3 |
| King of Prussia, PA | 341 | 200 | 52 | 8 | 1 | 4 |
| Alpharetta, GA | 338 | 220 | 46 | 7 | 1 | 5 |
| Troy, MI | 377 | 225 | 51 | 6 | 0 | 2 |
| Fort Myers, FL | 231 | 119 | 28 | 3 | 0 | 1 |
| Sarasota, FL | 330 | 199 | 45 | 12 | 0 | 3 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 12465 | 6126 | 233 |
| YellowPages | 26741 | 19108 | 271 |
| BBB | 4510 | 2168 | 130 |
| OpenStreetMap | 2810 | 1368 | 21 |

Discovery tasks completed: bbb=1708, gmaps=705, osm=125, yp=2743

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 293 | 0 | 30 | 323 |
| beads-craft | 1525 | 99 | 12 | 1636 |
| chain | 7473 | 0 | 0 | 7473 |
| coin-currency | 905 | 13 | 0 | 918 |
| costume-fashion | 1322 | 413 | 113 | 1848 |
| diamond-trade | 251 | 45 | 10 | 306 |
| gold-buyer | 596 | 121 | 32 | 749 |
| kiosk-battery | 31 | 0 | 0 | 31 |
| no-segment | 0 | 0 | 4411 | 4411 |
| pawn | 2244 | 110 | 29 | 2383 |
| piercing-tattoo | 1645 | 109 | 21 | 1775 |
| simulants | 11 | 48 | 9 | 68 |
| thrift-consignment | 461 | 0 | 0 | 461 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 170 | 17 | 2 | 189 |
| **all** | | | | **22575** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 7051 | bbb:041e21befdeeed50: appraiser-lab-insurer |
| bbb | blocked | 321 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 136 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-500 | 116 | https://overpass.kumi.systems/api/interpreter |
| yp | soft-block-503 | 43 | https://www.yellowpages.com/search?search_terms=custom+jewelry&geo_location_terms=Anaheim%2C+CA&page=5 |
| osm | http-504 | 35 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 33 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 28 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
