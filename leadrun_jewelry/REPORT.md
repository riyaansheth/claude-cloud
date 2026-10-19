# Jewelry retail lead run — REPORT

Generated 2026-10-19T20:08:25+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 50718 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 31098 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 704 |
| Qualification rate | 2.3% |
| Websites crawled OK / attempted | 26928 / 32282 |
| Listings with an owner/decision-maker name | 5340 |
| LinkedIn searches by outcome | ambiguous: 378, match: 215, none: 739, reject: 151 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 31098 (100.0%) | 704 (100.0%) |
| 2 | Segment | 31098 (100.0%) | 704 (100.0%) |
| 3 | Category (as listed) | 31029 (99.8%) | 703 (99.9%) |
| 4 | Phone | 29199 (93.9%) | 689 (97.9%) |
| 5 | Email | 6919 (22.2%) | 690 (98.0%) |
| 6 | LinkedIn Profile | 195 (0.6%) | 187 (26.6%) |
| 7 | Contact Person | 2681 (8.6%) | 341 (48.4%) |
| 8 | Role | 2681 (8.6%) | 341 (48.4%) |
| 9 | Website | 23786 (76.5%) | 704 (100.0%) |
| 10 | Address | 29858 (96.0%) | 696 (98.9%) |
| 11 | Real City | 24941 (80.2%) | 597 (84.8%) |
| 12 | Real State | 25045 (80.5%) | 596 (84.7%) |
| 13 | Market | 31098 (100.0%) | 704 (100.0%) |
| 14 | Lead Origin | 31098 (100.0%) | 704 (100.0%) |
| 15 | Rating | 10643 (34.2%) | 422 (59.9%) |
| 16 | Reviews | 10643 (34.2%) | 422 (59.9%) |
| 17 | Source | 31098 (100.0%) | 704 (100.0%) |
| 18 | Signals | 31098 (100.0%) | 704 (100.0%) |
| 19 | Match Type | 31098 (100.0%) | 704 (100.0%) |
| 20 | Email Source | 6919 (22.2%) | 690 (98.0%) |
| 21 | LinkedIn Source | 199 (0.6%) | 187 (26.6%) |
| 22 | Found At | 31098 (100.0%) | 704 (100.0%) |
| 23 | Also Listed As | 4037 (13.0%) | 213 (30.3%) |
| 24 | Other Markets | 1562 (5.0%) | 133 (18.9%) |
| 25 | Merged Listings | 7373 (23.7%) | 344 (48.9%) |
| 26 | Flags | 4116 (13.2%) | 157 (22.3%) |
| 27 | Mobile Candidates | 749 (2.4%) | 532 (75.6%) |
| 28 | Socials | 6383 (20.5%) | 616 (87.5%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 6919 | 22.2% |
| linkedin | 195 | 0.6% |
| direct-line | 749 | 2.4% |
| role-email | 2638 | 8.5% |
| gia | 1573 | 5.1% |
| ags | 220 | 0.7% |
| ja | 133 | 0.4% |
| bench | 1095 | 3.5% |
| custom-design | 4452 | 14.3% |
| since-yyyy | 4837 | 15.6% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1440 | 1166 | 266 | 85 | 13 | 33 |
| Los Angeles, CA | 1278 | 998 | 229 | 73 | 9 | 29 |
| Chicago, IL | 988 | 674 | 153 | 60 | 5 | 17 |
| Houston, TX | 1029 | 692 | 142 | 57 | 5 | 20 |
| Dallas, TX | 719 | 472 | 88 | 57 | 5 | 7 |
| Miami, FL | 1024 | 721 | 159 | 66 | 5 | 33 |
| Atlanta, GA | 735 | 511 | 124 | 56 | 13 | 24 |
| Philadelphia, PA | 759 | 537 | 90 | 27 | 4 | 12 |
| San Francisco, CA | 731 | 438 | 123 | 66 | 4 | 12 |
| Boston, MA | 570 | 340 | 109 | 54 | 7 | 18 |
| Seattle, WA | 583 | 336 | 89 | 64 | 2 | 8 |
| Las Vegas, NV | 691 | 398 | 72 | 74 | 3 | 10 |
| Phoenix, AZ | 730 | 456 | 92 | 57 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 329 | 102 | 85 | 5 | 10 |
| Washington, DC | 373 | 214 | 73 | 30 | 1 | 4 |
| Detroit, MI | 550 | 357 | 77 | 42 | 5 | 15 |
| Minneapolis, MN | 531 | 243 | 63 | 92 | 6 | 10 |
| Charlotte, NC | 350 | 205 | 47 | 39 | 2 | 4 |
| Nashville, TN | 338 | 173 | 44 | 49 | 4 | 4 |
| Scottsdale, AZ | 263 | 146 | 35 | 25 | 1 | 5 |
| Naples, FL | 274 | 150 | 45 | 21 | 1 | 5 |
| Greenwich, CT | 141 | 79 | 27 | 6 | 1 | 5 |
| Palm Beach, FL | 445 | 252 | 64 | 23 | 2 | 7 |
| Beverly Hills, CA | 622 | 454 | 110 | 29 | 1 | 13 |
| Austin, TX | 458 | 238 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 301 | 52 | 42 | 2 | 6 |
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
| Indianapolis, IN | 260 | 159 | 40 | 12 | 0 | 5 |
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
| Tucson, AZ | 291 | 159 | 39 | 32 | 0 | 1 |
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
| Oakland, CA | 339 | 219 | 48 | 8 | 1 | 4 |
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
| Newark, NJ | 873 | 612 | 123 | 15 | 1 | 13 |
| Edison, NJ | 487 | 305 | 60 | 6 | 1 | 9 |
| White Plains, NY | 340 | 212 | 42 | 11 | 0 | 3 |
| Irvine, CA | 566 | 373 | 90 | 21 | 1 | 7 |
| Anaheim, CA | 411 | 243 | 43 | 7 | 0 | 2 |
| Pasadena, CA | 821 | 571 | 106 | 6 | 0 | 13 |
| Sherman Oaks, CA | 435 | 297 | 50 | 7 | 0 | 4 |
| Plano, TX | 401 | 247 | 58 | 7 | 0 | 4 |
| Schaumburg, IL | 425 | 278 | 71 | 11 | 0 | 5 |
| Northbrook, IL | 194 | 117 | 23 | 7 | 1 | 1 |
| Bethesda, MD | 378 | 237 | 55 | 8 | 0 | 4 |
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
| Cherry Hill, NJ | 272 | 157 | 39 | 7 | 0 | 1 |
| Boca Raton, FL | 436 | 259 | 63 | 16 | 0 | 6 |
| San Mateo, CA | 270 | 163 | 47 | 6 | 0 | 3 |
| Walnut Creek, CA | 212 | 123 | 27 | 5 | 0 | 2 |
| Chandler, AZ | 211 | 128 | 29 | 3 | 0 | 1 |
| The Woodlands, TX | 214 | 119 | 24 | 1 | 0 | 3 |
| Arlington, TX | 192 | 119 | 22 | 2 | 0 | 4 |
| Naperville, IL | 199 | 115 | 21 | 3 | 0 | 3 |
| Towson, MD | 146 | 74 | 22 | 1 | 0 | 2 |
| Columbia, MD | 161 | 86 | 22 | 3 | 0 | 1 |
| Annapolis, MD | 168 | 89 | 15 | 5 | 0 | 0 |
| Franklin, TN | 158 | 66 | 20 | 4 | 0 | 2 |
| Bellevue, WA | 211 | 131 | 22 | 8 | 0 | 1 |
| Tacoma, WA | 299 | 212 | 31 | 4 | 0 | 3 |
| Boulder, CO | 216 | 96 | 35 | 6 | 0 | 1 |
| Carmel, IN | 90 | 42 | 12 | 5 | 0 | 2 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 13987 | 6796 | 246 |
| YellowPages | 29112 | 20646 | 305 |
| BBB | 4564 | 2170 | 131 |
| OpenStreetMap | 3055 | 1486 | 22 |

Discovery tasks completed: bbb=1872, gmaps=885, osm=145, yp=3675

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 332 | 0 | 28 | 360 |
| beads-craft | 1626 | 110 | 14 | 1750 |
| chain | 8109 | 0 | 0 | 8109 |
| coin-currency | 998 | 13 | 0 | 1011 |
| costume-fashion | 1522 | 455 | 119 | 2096 |
| diamond-trade | 272 | 46 | 11 | 329 |
| gold-buyer | 655 | 136 | 39 | 830 |
| kiosk-battery | 36 | 0 | 0 | 36 |
| no-segment | 0 | 0 | 5056 | 5056 |
| pawn | 2394 | 112 | 29 | 2535 |
| piercing-tattoo | 1805 | 120 | 21 | 1946 |
| simulants | 11 | 54 | 9 | 74 |
| thrift-consignment | 519 | 0 | 0 | 519 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 171 | 19 | 2 | 192 |
| **all** | | | | **24847** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 8100 | bbb:041e21befdeeed50: appraiser-lab-insurer |
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
