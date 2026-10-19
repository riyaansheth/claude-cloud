# Jewelry retail lead run — REPORT

Generated 2026-10-20T02:57:47+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 54281 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 32908 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 733 |
| Qualification rate | 2.2% |
| Websites crawled OK / attempted | 29058 / 34797 |
| Listings with an owner/decision-maker name | 5540 |
| LinkedIn searches by outcome | ambiguous: 391, match: 223, none: 757, reject: 156 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 32908 (100.0%) | 733 (100.0%) |
| 2 | Segment | 32908 (100.0%) | 733 (100.0%) |
| 3 | Category (as listed) | 32835 (99.8%) | 732 (99.9%) |
| 4 | Phone | 30903 (93.9%) | 717 (97.8%) |
| 5 | Email | 7462 (22.7%) | 718 (98.0%) |
| 6 | LinkedIn Profile | 201 (0.6%) | 193 (26.3%) |
| 7 | Contact Person | 2768 (8.4%) | 349 (47.6%) |
| 8 | Role | 2768 (8.4%) | 349 (47.6%) |
| 9 | Website | 25227 (76.7%) | 733 (100.0%) |
| 10 | Address | 31571 (95.9%) | 723 (98.6%) |
| 11 | Real City | 26190 (79.6%) | 616 (84.0%) |
| 12 | Real State | 26294 (79.9%) | 615 (83.9%) |
| 13 | Market | 32908 (100.0%) | 733 (100.0%) |
| 14 | Lead Origin | 32908 (100.0%) | 733 (100.0%) |
| 15 | Rating | 11478 (34.9%) | 448 (61.1%) |
| 16 | Reviews | 11478 (34.9%) | 448 (61.1%) |
| 17 | Source | 32908 (100.0%) | 733 (100.0%) |
| 18 | Signals | 32908 (100.0%) | 733 (100.0%) |
| 19 | Match Type | 32908 (100.0%) | 733 (100.0%) |
| 20 | Email Source | 7462 (22.7%) | 718 (98.0%) |
| 21 | LinkedIn Source | 205 (0.6%) | 193 (26.3%) |
| 22 | Found At | 32908 (100.0%) | 733 (100.0%) |
| 23 | Also Listed As | 4280 (13.0%) | 221 (30.2%) |
| 24 | Other Markets | 1771 (5.4%) | 145 (19.8%) |
| 25 | Merged Listings | 7814 (23.7%) | 358 (48.8%) |
| 26 | Flags | 4366 (13.3%) | 161 (22.0%) |
| 27 | Mobile Candidates | 777 (2.4%) | 556 (75.9%) |
| 28 | Socials | 6841 (20.8%) | 642 (87.6%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 7462 | 22.7% |
| linkedin | 201 | 0.6% |
| direct-line | 777 | 2.4% |
| role-email | 2807 | 8.5% |
| gia | 1652 | 5.0% |
| ags | 232 | 0.7% |
| ja | 138 | 0.4% |
| bench | 1163 | 3.5% |
| custom-design | 4730 | 14.4% |
| since-yyyy | 5015 | 15.2% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1440 | 1166 | 266 | 85 | 13 | 33 |
| Los Angeles, CA | 1278 | 998 | 229 | 73 | 9 | 29 |
| Chicago, IL | 988 | 674 | 153 | 60 | 5 | 17 |
| Houston, TX | 1029 | 692 | 143 | 57 | 5 | 21 |
| Dallas, TX | 719 | 472 | 88 | 57 | 5 | 7 |
| Miami, FL | 1024 | 719 | 158 | 65 | 5 | 33 |
| Atlanta, GA | 735 | 506 | 122 | 55 | 13 | 23 |
| Philadelphia, PA | 759 | 535 | 88 | 26 | 4 | 10 |
| San Francisco, CA | 731 | 436 | 121 | 66 | 4 | 13 |
| Boston, MA | 561 | 337 | 109 | 53 | 7 | 17 |
| Seattle, WA | 583 | 336 | 89 | 64 | 2 | 8 |
| Las Vegas, NV | 691 | 398 | 72 | 74 | 3 | 10 |
| Phoenix, AZ | 730 | 456 | 92 | 57 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 328 | 101 | 84 | 5 | 10 |
| Washington, DC | 373 | 214 | 73 | 30 | 1 | 4 |
| Detroit, MI | 550 | 353 | 78 | 42 | 5 | 15 |
| Minneapolis, MN | 531 | 242 | 63 | 91 | 6 | 10 |
| Charlotte, NC | 350 | 204 | 47 | 39 | 2 | 4 |
| Nashville, TN | 338 | 170 | 44 | 48 | 4 | 4 |
| Scottsdale, AZ | 263 | 146 | 35 | 25 | 1 | 5 |
| Naples, FL | 274 | 150 | 45 | 21 | 1 | 5 |
| Greenwich, CT | 141 | 78 | 27 | 6 | 1 | 5 |
| Palm Beach, FL | 443 | 249 | 64 | 23 | 2 | 7 |
| Beverly Hills, CA | 622 | 454 | 110 | 29 | 1 | 13 |
| Austin, TX | 458 | 238 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 300 | 51 | 41 | 2 | 6 |
| Fort Worth, TX | 454 | 251 | 44 | 23 | 1 | 1 |
| San Jose, CA | 519 | 280 | 37 | 16 | 0 | 2 |
| Sacramento, CA | 372 | 205 | 37 | 38 | 2 | 7 |
| Portland, OR | 515 | 278 | 70 | 55 | 2 | 4 |
| Salt Lake City, UT | 445 | 237 | 65 | 71 | 8 | 10 |
| Kansas City, MO | 447 | 255 | 71 | 75 | 5 | 9 |
| St. Louis, MO | 522 | 257 | 71 | 51 | 3 | 6 |
| Columbus, OH | 238 | 132 | 41 | 20 | 2 | 4 |
| Cleveland, OH | 335 | 201 | 54 | 9 | 0 | 2 |
| Cincinnati, OH | 364 | 210 | 57 | 19 | 4 | 5 |
| Indianapolis, IN | 260 | 158 | 40 | 12 | 0 | 5 |
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
| Oakland, CA | 339 | 218 | 48 | 8 | 1 | 4 |
| Riverside, CA | 290 | 187 | 36 | 2 | 0 | 0 |
| Colorado Springs, CO | 168 | 99 | 28 | 2 | 0 | 1 |
| Spokane, WA | 148 | 80 | 12 | 5 | 0 | 1 |
| Wichita, KS | 167 | 96 | 20 | 4 | 0 | 2 |
| Des Moines, IA | 158 | 79 | 19 | 10 | 2 | 3 |
| Madison, WI | 150 | 75 | 21 | 7 | 0 | 0 |
| Rochester, NY | 204 | 120 | 34 | 9 | 1 | 7 |
| Albany, NY | 171 | 108 | 22 | 5 | 0 | 0 |
| Knoxville, TN | 168 | 96 | 14 | 5 | 0 | 0 |
| Chattanooga, TN | 188 | 104 | 17 | 5 | 0 | 0 |
| Greenville, SC | 156 | 95 | 34 | 6 | 0 | 0 |
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
| Worcester, MA | 167 | 91 | 21 | 10 | 0 | 3 |
| New Haven, CT | 202 | 117 | 20 | 6 | 0 | 1 |
| Allentown, PA | 196 | 112 | 26 | 6 | 0 | 1 |
| Harrisburg, PA | 141 | 84 | 11 | 1 | 0 | 0 |
| Durham, NC | 114 | 58 | 21 | 4 | 0 | 1 |
| Greensboro, NC | 167 | 89 | 29 | 5 | 0 | 2 |
| Winston-Salem, NC | 138 | 71 | 14 | 3 | 0 | 0 |
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
| Hackensack, NJ | 977 | 749 | 115 | 10 | 0 | 9 |
| Newark, NJ | 873 | 612 | 123 | 15 | 1 | 13 |
| Edison, NJ | 487 | 305 | 60 | 6 | 1 | 9 |
| White Plains, NY | 340 | 212 | 42 | 11 | 0 | 3 |
| Irvine, CA | 566 | 373 | 90 | 21 | 1 | 7 |
| Anaheim, CA | 411 | 241 | 43 | 7 | 0 | 2 |
| Pasadena, CA | 821 | 571 | 106 | 6 | 0 | 13 |
| Sherman Oaks, CA | 435 | 294 | 49 | 7 | 0 | 4 |
| Plano, TX | 401 | 247 | 58 | 7 | 0 | 4 |
| Schaumburg, IL | 425 | 278 | 71 | 11 | 0 | 5 |
| Northbrook, IL | 194 | 117 | 23 | 7 | 1 | 1 |
| Bethesda, MD | 378 | 237 | 55 | 8 | 0 | 4 |
| Fairfax, VA | 317 | 203 | 40 | 5 | 0 | 3 |
| King of Prussia, PA | 341 | 197 | 51 | 7 | 1 | 3 |
| Alpharetta, GA | 338 | 220 | 46 | 7 | 1 | 5 |
| Troy, MI | 377 | 225 | 51 | 6 | 2 | 4 |
| Fort Myers, FL | 231 | 119 | 28 | 3 | 0 | 1 |
| Sarasota, FL | 330 | 198 | 45 | 12 | 0 | 3 |
| Stamford, CT | 100 | 58 | 19 | 6 | 1 | 3 |
| Morristown, NJ | 183 | 112 | 17 | 2 | 0 | 0 |
| Princeton, NJ | 253 | 144 | 39 | 4 | 0 | 0 |
| Red Bank, NJ | 221 | 126 | 33 | 2 | 0 | 3 |
| Cherry Hill, NJ | 272 | 157 | 39 | 7 | 0 | 1 |
| Boca Raton, FL | 436 | 259 | 63 | 16 | 1 | 7 |
| San Mateo, CA | 270 | 162 | 47 | 6 | 2 | 6 |
| Walnut Creek, CA | 212 | 123 | 27 | 5 | 0 | 2 |
| Chandler, AZ | 211 | 128 | 29 | 3 | 0 | 1 |
| The Woodlands, TX | 213 | 112 | 30 | 2 | 0 | 3 |
| Arlington, TX | 192 | 119 | 22 | 2 | 0 | 4 |
| Naperville, IL | 199 | 115 | 21 | 3 | 0 | 3 |
| Towson, MD | 146 | 74 | 22 | 1 | 0 | 2 |
| Columbia, MD | 161 | 86 | 22 | 3 | 0 | 1 |
| Annapolis, MD | 168 | 86 | 18 | 5 | 0 | 0 |
| Franklin, TN | 158 | 66 | 20 | 4 | 0 | 2 |
| Bellevue, WA | 211 | 131 | 22 | 8 | 1 | 2 |
| Tacoma, WA | 299 | 212 | 31 | 4 | 0 | 3 |
| Boulder, CO | 216 | 96 | 35 | 6 | 1 | 2 |
| Carmel, IN | 90 | 38 | 13 | 5 | 0 | 2 |
| Palo Alto, CA | 218 | 110 | 25 | 4 | 0 | 0 |
| Santa Barbara, CA | 169 | 84 | 32 | 8 | 0 | 0 |
| Thousand Oaks, CA | 205 | 114 | 35 | 6 | 0 | 3 |
| Santa Rosa, CA | 172 | 91 | 18 | 5 | 0 | 1 |
| Rancho Cucamonga, CA | 181 | 108 | 25 | 4 | 0 | 2 |
| Temecula, CA | 135 | 81 | 28 | 2 | 0 | 0 |
| Palm Desert, CA | 198 | 102 | 24 | 5 | 0 | 1 |
| Wellesley, MA | 341 | 206 | 62 | 9 | 0 | 5 |
| Westport, CT | 148 | 78 | 22 | 3 | 0 | 0 |
| Wilmington, DE | 229 | 117 | 35 | 3 | 0 | 2 |
| Lancaster, PA | 200 | 101 | 23 | 5 | 0 | 0 |
| Ann Arbor, MI | 158 | 76 | 24 | 1 | 0 | 1 |
| Chesterfield, MO | 179 | 90 | 29 | 11 | 0 | 2 |
| Overland Park, KS | 126 | 60 | 27 | 7 | 0 | 3 |
| Fort Collins, CO | 210 | 96 | 27 | 6 | 0 | 1 |
| Asheville, NC | 181 | 96 | 40 | 7 | 0 | 2 |
| Murfreesboro, TN | 123 | 49 | 6 | 5 | 0 | 0 |
| Huntsville, AL | 151 | 80 | 26 | 2 | 0 | 2 |
| Tallahassee, FL | 151 | 89 | 21 | 3 | 0 | 2 |
| Jupiter, FL | 117 | 55 | 17 | 5 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 15795 | 7455 | 264 |
| YellowPages | 30815 | 21808 | 320 |
| BBB | 4564 | 2144 | 128 |
| OpenStreetMap | 3107 | 1501 | 21 |

Discovery tasks completed: bbb=1879, gmaps=1065, osm=151, yp=4256

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 370 | 0 | 27 | 397 |
| beads-craft | 1712 | 116 | 14 | 1842 |
| chain | 8461 | 0 | 0 | 8461 |
| coin-currency | 1094 | 14 | 0 | 1108 |
| costume-fashion | 1695 | 490 | 130 | 2315 |
| diamond-trade | 282 | 46 | 11 | 339 |
| gold-buyer | 705 | 144 | 40 | 889 |
| kiosk-battery | 36 | 0 | 0 | 36 |
| no-segment | 0 | 0 | 5961 | 5961 |
| pawn | 2506 | 122 | 29 | 2657 |
| piercing-tattoo | 1984 | 138 | 21 | 2143 |
| simulants | 11 | 57 | 9 | 77 |
| thrift-consignment | 629 | 0 | 0 | 629 |
| trade-association | 4 | 0 | 0 | 4 |
| wholesale-manufacturer | 180 | 19 | 3 | 202 |
| **all** | | | | **27060** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 8682 | bbb:041e21befdeeed50: appraiser-lab-insurer |
| bbb | blocked | 332 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 172 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-500 | 144 | https://overpass.kumi.systems/api/interpreter |
| yp | soft-block-503 | 58 | https://www.yellowpages.com/search?search_terms=custom+jewelry&geo_location_terms=Anaheim%2C+CA&page=5 |
| osm | http-504 | 41 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 38 | http-200 or challenge page at https://www.google.com/search?q=%22Lorraine+Tunca%22+Liberty+Lake+linkedin&hl=en&num=10 |
| osm | http-406 | 36 | https://overpass-api.de/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
