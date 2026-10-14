# Jewelry retail lead run — REPORT

Generated 2026-10-14T13:43:12+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 23127 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 15159 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 402 |
| Qualification rate | 2.7% |
| Websites crawled OK / attempted | 12132 / 14496 |
| Listings with an owner/decision-maker name | 3196 |
| LinkedIn searches by outcome | ambiguous: 182, match: 110, none: 383, reject: 44 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 15159 (100.0%) | 402 (100.0%) |
| 2 | Segment | 15159 (100.0%) | 402 (100.0%) |
| 3 | Category (as listed) | 15131 (99.8%) | 402 (100.0%) |
| 4 | Phone | 14290 (94.3%) | 394 (98.0%) |
| 5 | Email | 3448 (22.7%) | 394 (98.0%) |
| 6 | LinkedIn Profile | 101 (0.7%) | 94 (23.4%) |
| 7 | Contact Person | 1559 (10.3%) | 201 (50.0%) |
| 8 | Role | 1559 (10.3%) | 201 (50.0%) |
| 9 | Website | 11704 (77.2%) | 402 (100.0%) |
| 10 | Address | 14578 (96.2%) | 398 (99.0%) |
| 11 | Real City | 12415 (81.9%) | 350 (87.1%) |
| 12 | Real State | 12510 (82.5%) | 349 (86.8%) |
| 13 | Market | 15159 (100.0%) | 402 (100.0%) |
| 14 | Lead Origin | 15159 (100.0%) | 402 (100.0%) |
| 15 | Rating | 4826 (31.8%) | 208 (51.7%) |
| 16 | Reviews | 4826 (31.8%) | 208 (51.7%) |
| 17 | Source | 15159 (100.0%) | 402 (100.0%) |
| 18 | Signals | 15159 (100.0%) | 402 (100.0%) |
| 19 | Match Type | 15159 (100.0%) | 402 (100.0%) |
| 20 | Email Source | 3448 (22.7%) | 394 (98.0%) |
| 21 | LinkedIn Source | 101 (0.7%) | 94 (23.4%) |
| 22 | Found At | 15159 (100.0%) | 402 (100.0%) |
| 23 | Also Listed As | 1959 (12.9%) | 113 (28.1%) |
| 24 | Other Markets | 393 (2.6%) | 39 (9.7%) |
| 25 | Merged Listings | 3583 (23.6%) | 183 (45.5%) |
| 26 | Flags | 1971 (13.0%) | 87 (21.6%) |
| 27 | Mobile Candidates | 450 (3.0%) | 318 (79.1%) |
| 28 | Socials | 3351 (22.1%) | 356 (88.6%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3448 | 22.7% |
| linkedin | 101 | 0.7% |
| direct-line | 450 | 3.0% |
| role-email | 1420 | 9.4% |
| gia | 885 | 5.8% |
| ags | 118 | 0.8% |
| ja | 61 | 0.4% |
| bench | 574 | 3.8% |
| custom-design | 2412 | 15.9% |
| since-yyyy | 2756 | 18.2% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 8 | 31 |
| Chicago, IL | 993 | 685 | 154 | 65 | 5 | 19 |
| Houston, TX | 1030 | 697 | 142 | 55 | 5 | 21 |
| Dallas, TX | 722 | 483 | 90 | 58 | 5 | 8 |
| Miami, FL | 1024 | 728 | 162 | 66 | 5 | 33 |
| Atlanta, GA | 739 | 526 | 128 | 62 | 11 | 23 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 3 | 14 |
| San Francisco, CA | 732 | 444 | 124 | 67 | 3 | 11 |
| Boston, MA | 570 | 345 | 109 | 56 | 7 | 18 |
| Seattle, WA | 589 | 347 | 93 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 403 | 75 | 75 | 3 | 12 |
| Phoenix, AZ | 730 | 469 | 95 | 59 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 382 | 225 | 76 | 32 | 1 | 6 |
| Detroit, MI | 554 | 378 | 82 | 51 | 6 | 18 |
| Minneapolis, MN | 531 | 245 | 61 | 91 | 6 | 9 |
| Charlotte, NC | 350 | 208 | 47 | 40 | 2 | 5 |
| Nashville, TN | 341 | 186 | 47 | 54 | 4 | 4 |
| Scottsdale, AZ | 263 | 150 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 151 | 46 | 21 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 258 | 66 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 458 | 110 | 27 | 1 | 13 |
| Austin, TX | 458 | 239 | 80 | 37 | 0 | 5 |
| San Antonio, TX | 502 | 303 | 51 | 42 | 0 | 4 |
| Fort Worth, TX | 456 | 259 | 47 | 24 | 0 | 0 |
| San Jose, CA | 458 | 256 | 33 | 6 | 0 | 2 |
| Sacramento, CA | 278 | 160 | 34 | 9 | 0 | 4 |
| Portland, OR | 370 | 233 | 60 | 12 | 0 | 1 |
| Salt Lake City, UT | 290 | 162 | 39 | 6 | 0 | 2 |
| Kansas City, MO | 288 | 179 | 31 | 8 | 0 | 2 |
| St. Louis, MO | 376 | 228 | 38 | 7 | 0 | 0 |
| Columbus, OH | 74 | 56 | 11 | 3 | 0 | 0 |
| Cleveland, OH | 313 | 192 | 53 | 8 | 0 | 2 |
| Cincinnati, OH | 321 | 198 | 52 | 9 | 0 | 1 |
| Indianapolis, IN | 250 | 160 | 40 | 12 | 0 | 6 |
| Pittsburgh, PA | 335 | 208 | 57 | 9 | 0 | 3 |
| Baltimore, MD | 300 | 207 | 47 | 8 | 0 | 5 |
| Orlando, FL | 373 | 235 | 48 | 8 | 0 | 3 |
| Tampa, FL | 342 | 233 | 49 | 4 | 0 | 5 |
| Fort Lauderdale, FL | 517 | 359 | 55 | 10 | 0 | 2 |
| Raleigh, NC | 235 | 152 | 27 | 11 | 0 | 1 |
| New Orleans, LA | 248 | 157 | 33 | 5 | 0 | 5 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 5150 | 2946 | 129 |
| YellowPages | 13634 | 9989 | 159 |
| BBB | 2824 | 1373 | 98 |
| OpenStreetMap | 1533 | 851 | 16 |

Discovery tasks completed: bbb=850, gmaps=214, osm=33, yp=705

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 104 | 0 | 35 | 139 |
| beads-craft | 619 | 51 | 4 | 674 |
| chain | 4203 | 0 | 0 | 4203 |
| coin-currency | 341 | 10 | 0 | 351 |
| costume-fashion | 568 | 209 | 44 | 821 |
| diamond-trade | 153 | 35 | 7 | 195 |
| gold-buyer | 304 | 56 | 19 | 379 |
| kiosk-battery | 14 | 0 | 0 | 14 |
| no-segment | 0 | 0 | 1218 | 1218 |
| pawn | 1051 | 55 | 15 | 1121 |
| piercing-tattoo | 779 | 58 | 16 | 853 |
| simulants | 7 | 40 | 4 | 51 |
| thrift-consignment | 90 | 0 | 0 | 90 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 96 | 10 | 1 | 107 |
| **all** | | | | **10219** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 2844 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 192 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 44 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| yp | soft-block-503 | 21 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-504 | 17 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 15 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| osm | http-406 | 15 | https://overpass-api.de/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
