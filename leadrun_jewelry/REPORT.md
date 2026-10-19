# Jewelry retail lead run — REPORT

Generated 2026-10-19T19:41:04+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 50254 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 30927 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 689 |
| Qualification rate | 2.2% |
| Websites crawled OK / attempted | 26034 / 31216 |
| Listings with an owner/decision-maker name | 5248 |
| LinkedIn searches by outcome | ambiguous: 378, match: 215, none: 739, reject: 151 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 30927 (100.0%) | 689 (100.0%) |
| 2 | Segment | 30927 (100.0%) | 689 (100.0%) |
| 3 | Category (as listed) | 30860 (99.8%) | 688 (99.9%) |
| 4 | Phone | 29048 (93.9%) | 674 (97.8%) |
| 5 | Email | 6722 (21.7%) | 675 (98.0%) |
| 6 | LinkedIn Profile | 195 (0.6%) | 187 (27.1%) |
| 7 | Contact Person | 2647 (8.6%) | 335 (48.6%) |
| 8 | Role | 2647 (8.6%) | 335 (48.6%) |
| 9 | Website | 23675 (76.6%) | 689 (100.0%) |
| 10 | Address | 29707 (96.1%) | 681 (98.8%) |
| 11 | Real City | 24864 (80.4%) | 585 (84.9%) |
| 12 | Real State | 24968 (80.7%) | 584 (84.8%) |
| 13 | Market | 30927 (100.0%) | 689 (100.0%) |
| 14 | Lead Origin | 30927 (100.0%) | 689 (100.0%) |
| 15 | Rating | 10524 (34.0%) | 416 (60.4%) |
| 16 | Reviews | 10524 (34.0%) | 416 (60.4%) |
| 17 | Source | 30927 (100.0%) | 689 (100.0%) |
| 18 | Signals | 30927 (100.0%) | 689 (100.0%) |
| 19 | Match Type | 30927 (100.0%) | 689 (100.0%) |
| 20 | Email Source | 6722 (21.7%) | 675 (98.0%) |
| 21 | LinkedIn Source | 199 (0.6%) | 187 (27.1%) |
| 22 | Found At | 30927 (100.0%) | 689 (100.0%) |
| 23 | Also Listed As | 4018 (13.0%) | 210 (30.5%) |
| 24 | Other Markets | 1545 (5.0%) | 131 (19.0%) |
| 25 | Merged Listings | 7333 (23.7%) | 340 (49.3%) |
| 26 | Flags | 4070 (13.2%) | 155 (22.5%) |
| 27 | Mobile Candidates | 734 (2.4%) | 517 (75.0%) |
| 28 | Socials | 6230 (20.1%) | 601 (87.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 6722 | 21.7% |
| linkedin | 195 | 0.6% |
| direct-line | 734 | 2.4% |
| role-email | 2576 | 8.3% |
| gia | 1535 | 5.0% |
| ags | 219 | 0.7% |
| ja | 132 | 0.4% |
| bench | 1070 | 3.5% |
| custom-design | 4354 | 14.1% |
| since-yyyy | 4770 | 15.4% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1440 | 1166 | 266 | 84 | 13 | 33 |
| Los Angeles, CA | 1278 | 998 | 229 | 72 | 9 | 29 |
| Chicago, IL | 988 | 674 | 153 | 58 | 5 | 17 |
| Houston, TX | 1029 | 694 | 142 | 56 | 5 | 21 |
| Dallas, TX | 719 | 472 | 88 | 56 | 5 | 7 |
| Miami, FL | 1024 | 721 | 159 | 66 | 5 | 33 |
| Atlanta, GA | 735 | 511 | 124 | 56 | 13 | 24 |
| Philadelphia, PA | 759 | 538 | 90 | 27 | 4 | 12 |
| San Francisco, CA | 731 | 439 | 122 | 67 | 4 | 11 |
| Boston, MA | 570 | 340 | 109 | 54 | 7 | 18 |
| Seattle, WA | 583 | 336 | 89 | 64 | 2 | 8 |
| Las Vegas, NV | 691 | 398 | 72 | 74 | 3 | 10 |
| Phoenix, AZ | 730 | 459 | 92 | 57 | 0 | 11 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 329 | 102 | 85 | 5 | 10 |
| Washington, DC | 373 | 214 | 73 | 30 | 1 | 4 |
| Detroit, MI | 550 | 357 | 77 | 42 | 5 | 15 |
| Minneapolis, MN | 531 | 243 | 63 | 92 | 6 | 10 |
| Charlotte, NC | 350 | 205 | 47 | 39 | 2 | 4 |
| Nashville, TN | 338 | 173 | 44 | 49 | 4 | 4 |
| Scottsdale, AZ | 263 | 147 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 150 | 45 | 21 | 1 | 5 |
| Greenwich, CT | 141 | 79 | 27 | 6 | 1 | 5 |
| Palm Beach, FL | 445 | 252 | 64 | 23 | 2 | 7 |
| Beverly Hills, CA | 622 | 454 | 110 | 29 | 1 | 13 |
| Austin, TX | 458 | 238 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 301 | 51 | 42 | 2 | 6 |
| Fort Worth, TX | 454 | 251 | 44 | 23 | 1 | 1 |
| San Jose, CA | 522 | 286 | 37 | 16 | 0 | 2 |
| Sacramento, CA | 372 | 205 | 37 | 38 | 2 | 7 |
| Portland, OR | 515 | 278 | 70 | 55 | 2 | 4 |
| Salt Lake City, UT | 445 | 237 | 65 | 71 | 8 | 10 |
| Kansas City, MO | 451 | 264 | 74 | 79 | 5 | 10 |
| St. Louis, MO | 526 | 261 | 71 | 52 | 3 | 6 |
| Columbus, OH | 238 | 132 | 41 | 20 | 2 | 4 |
| Cleveland, OH | 335 | 201 | 54 | 9 | 0 | 2 |
| Cincinnati, OH | 364 | 210 | 57 | 19 | 4 | 5 |
| Indianapolis, IN | 260 | 159 | 39 | 12 | 0 | 5 |
| Pittsburgh, PA | 394 | 223 | 59 | 16 | 2 | 6 |
| Baltimore, MD | 324 | 213 | 46 | 7 | 2 | 6 |
| Orlando, FL | 433 | 257 | 53 | 20 | 1 | 5 |
| Tampa, FL | 395 | 250 | 57 | 21 | 0 | 5 |
| Fort Lauderdale, FL | 581 | 384 | 79 | 33 | 3 | 7 |
| Raleigh, NC | 273 | 155 | 43 | 22 | 2 | 3 |
| New Orleans, LA | 511 | 279 | 65 | 39 | 3 | 9 |
| Jacksonville, FL | 333 | 195 | 42 | 13 | 2 | 4 |
| Memphis, TN | 401 | 230 | 37 | 63 | 3 | 7 |
| Louisville, KY | 203 | 122 | 35 | 28 | 2 | 4 |
| Milwaukee, WI | 289 | 150 | 44 | 9 | 0 | 0 |
| Albuquerque, NM | 463 | 311 | 72 | 77 | 4 | 12 |
| Tucson, AZ | 291 | 160 | 39 | 33 | 0 | 1 |
| Oklahoma City, OK | 236 | 141 | 23 | 5 | 0 | 1 |
| Tulsa, OK | 203 | 108 | 13 | 4 | 0 | 2 |
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
| Grand Rapids, MI | 170 | 95 | 20 | 5 | 1 | 2 |
| Fresno, CA | 232 | 122 | 25 | 6 | 1 | 2 |
| Bakersfield, CA | 158 | 83 | 12 | 1 | 0 | 1 |
| Long Beach, CA | 522 | 350 | 73 | 7 | 1 | 7 |
| Oakland, CA | 339 | 221 | 49 | 8 | 1 | 4 |
| Riverside, CA | 294 | 187 | 36 | 2 | 0 | 1 |
| Colorado Springs, CO | 168 | 99 | 28 | 2 | 0 | 1 |
| Spokane, WA | 148 | 80 | 12 | 5 | 0 | 1 |
| Wichita, KS | 167 | 96 | 20 | 4 | 0 | 2 |
| Des Moines, IA | 158 | 79 | 19 | 10 | 2 | 3 |
| Madison, WI | 150 | 75 | 21 | 7 | 0 | 0 |
| Rochester, NY | 204 | 120 | 34 | 9 | 1 | 7 |
| Albany, NY | 171 | 108 | 22 | 5 | 0 | 0 |
| Knoxville, TN | 168 | 96 | 14 | 5 | 0 | 0 |
| Chattanooga, TN | 188 | 104 | 17 | 5 | 0 | 0 |
| Greenville, SC | 156 | 96 | 34 | 6 | 0 | 0 |
| Columbia, SC | 211 | 111 | 21 | 8 | 2 | 3 |
| Savannah, GA | 177 | 81 | 19 | 4 | 1 | 1 |
| Little Rock, AR | 176 | 89 | 14 | 5 | 0 | 0 |
| Baton Rouge, LA | 186 | 74 | 14 | 4 | 1 | 1 |
| Anchorage, AK | 150 | 56 | 10 | 2 | 0 | 1 |
| Akron, OH | 153 | 91 | 15 | 9 | 1 | 1 |
| Toledo, OH | 130 | 66 | 9 | 6 | 0 | 2 |
| Dayton, OH | 136 | 76 | 12 | 4 | 1 | 2 |
| Lexington, KY | 140 | 73 | 23 | 3 | 0 | 1 |
| Syracuse, NY | 123 | 55 | 11 | 3 | 1 | 1 |
| Worcester, MA | 168 | 91 | 21 | 10 | 0 | 3 |
| New Haven, CT | 203 | 117 | 20 | 6 | 0 | 1 |
| Allentown, PA | 196 | 112 | 26 | 6 | 0 | 1 |
| Harrisburg, PA | 141 | 84 | 11 | 1 | 0 | 0 |
| Durham, NC | 114 | 58 | 21 | 4 | 0 | 1 |
| Greensboro, NC | 167 | 89 | 29 | 5 | 0 | 2 |
| Winston-Salem, NC | 138 | 72 | 15 | 3 | 0 | 0 |
| Mobile, AL | 160 | 70 | 9 | 3 | 0 | 1 |
| Jackson, MS | 107 | 55 | 11 | 3 | 0 | 1 |
| Shreveport, LA | 108 | 50 | 13 | 2 | 0 | 2 |
| Lubbock, TX | 102 | 59 | 11 | 1 | 0 | 2 |
| Corpus Christi, TX | 145 | 83 | 14 | 1 | 0 | 2 |
| Reno, NV | 126 | 71 | 16 | 4 | 0 | 0 |
| Sioux Falls, SD | 95 | 33 | 4 | 1 | 0 | 0 |
| Fort Wayne, IN | 104 | 45 | 15 | 1 | 0 | 0 |
| Garden City, NY | 912 | 677 | 113 | 16 | 1 | 6 |
| Huntington, NY | 339 | 205 | 51 | 7 | 0 | 4 |
| Hackensack, NJ | 977 | 750 | 116 | 11 | 0 | 10 |
| Newark, NJ | 873 | 613 | 124 | 15 | 1 | 13 |
| Edison, NJ | 487 | 305 | 60 | 6 | 1 | 9 |
| White Plains, NY | 340 | 212 | 42 | 11 | 0 | 3 |
| Irvine, CA | 566 | 373 | 90 | 21 | 1 | 7 |
| Anaheim, CA | 411 | 243 | 43 | 7 | 0 | 2 |
| Pasadena, CA | 821 | 571 | 106 | 6 | 0 | 13 |
| Sherman Oaks, CA | 435 | 297 | 50 | 7 | 0 | 4 |
| Plano, TX | 401 | 247 | 58 | 7 | 0 | 4 |
| Schaumburg, IL | 425 | 278 | 71 | 11 | 0 | 5 |
| Northbrook, IL | 194 | 117 | 23 | 7 | 1 | 1 |
| Bethesda, MD | 378 | 238 | 55 | 8 | 0 | 4 |
| Fairfax, VA | 317 | 203 | 40 | 5 | 0 | 3 |
| King of Prussia, PA | 341 | 198 | 51 | 8 | 1 | 3 |
| Alpharetta, GA | 338 | 220 | 46 | 7 | 1 | 5 |
| Troy, MI | 377 | 225 | 51 | 6 | 2 | 4 |
| Fort Myers, FL | 231 | 119 | 28 | 3 | 0 | 1 |
| Sarasota, FL | 330 | 199 | 45 | 12 | 0 | 3 |
| Stamford, CT | 100 | 56 | 19 | 6 | 0 | 2 |
| Morristown, NJ | 183 | 112 | 17 | 2 | 0 | 0 |
| Princeton, NJ | 253 | 144 | 39 | 4 | 0 | 0 |
| Red Bank, NJ | 221 | 126 | 33 | 2 | 0 | 3 |
| Cherry Hill, NJ | 276 | 167 | 30 | 3 | 0 | 1 |
| Boca Raton, FL | 437 | 260 | 60 | 16 | 0 | 6 |
| San Mateo, CA | 270 | 163 | 27 | 4 | 0 | 1 |
| Walnut Creek, CA | 221 | 138 | 0 | 1 | 0 | 0 |
| Chandler, AZ | 163 | 100 | 3 | 0 | 0 | 1 |
| The Woodlands, TX | 5 | 5 | 0 | 0 | 0 | 0 |
| Arlington, TX | 192 | 119 | 22 | 2 | 0 | 4 |
| Naperville, IL | 199 | 115 | 21 | 3 | 0 | 3 |
| Towson, MD | 148 | 80 | 16 | 0 | 0 | 1 |
| Columbia, MD | 135 | 71 | 11 | 2 | 0 | 0 |
| Annapolis, MD | 90 | 55 | 10 | 4 | 0 | 0 |
| Franklin, TN | 158 | 66 | 20 | 4 | 0 | 2 |
| Bellevue, WA | 211 | 131 | 22 | 8 | 0 | 1 |
| Tacoma, WA | 304 | 223 | 11 | 2 | 0 | 1 |
| Boulder, CO | 184 | 80 | 1 | 0 | 0 | 0 |
| Carmel, IN | 37 | 22 | 0 | 0 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 13680 | 6667 | 239 |
| YellowPages | 28993 | 20595 | 299 |
| BBB | 4564 | 2172 | 129 |
| OpenStreetMap | 3056 | 1493 | 22 |

Discovery tasks completed: bbb=1872, gmaps=842, osm=145, yp=3614

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 329 | 0 | 28 | 357 |
| beads-craft | 1617 | 102 | 14 | 1733 |
| chain | 8076 | 0 | 0 | 8076 |
| coin-currency | 993 | 13 | 0 | 1006 |
| costume-fashion | 1508 | 437 | 119 | 2064 |
| diamond-trade | 270 | 45 | 10 | 325 |
| gold-buyer | 652 | 128 | 38 | 818 |
| kiosk-battery | 36 | 0 | 0 | 36 |
| no-segment | 0 | 0 | 4773 | 4773 |
| pawn | 2373 | 111 | 29 | 2513 |
| piercing-tattoo | 1774 | 113 | 21 | 1908 |
| simulants | 11 | 51 | 9 | 71 |
| thrift-consignment | 507 | 0 | 0 | 507 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 171 | 19 | 2 | 192 |
| **all** | | | | **24383** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 7880 | bbb:041e21befdeeed50: appraiser-lab-insurer |
| bbb | blocked | 329 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 160 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-500 | 144 | https://overpass.kumi.systems/api/interpreter |
| yp | soft-block-503 | 53 | https://www.yellowpages.com/search?search_terms=custom+jewelry&geo_location_terms=Anaheim%2C+CA&page=5 |
| osm | http-504 | 39 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 36 | http-200 or challenge page at https://www.google.com/search?q=%22Lorraine+Tunca%22+Liberty+Lake+linkedin&hl=en&num=10 |
| osm | http-406 | 33 | https://overpass-api.de/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
