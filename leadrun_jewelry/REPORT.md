# Jewelry retail lead run — REPORT

Generated 2026-10-14T13:01:59+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 22231 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 14836 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 382 |
| Qualification rate | 2.6% |
| Websites crawled OK / attempted | 10799 / 12926 |
| Listings with an owner/decision-maker name | 3064 |
| LinkedIn searches by outcome | ambiguous: 182, match: 110, none: 383, reject: 44 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 14836 (100.0%) | 382 (100.0%) |
| 2 | Segment | 14836 (100.0%) | 382 (100.0%) |
| 3 | Category (as listed) | 14810 (99.8%) | 382 (100.0%) |
| 4 | Phone | 14015 (94.5%) | 376 (98.4%) |
| 5 | Email | 3106 (20.9%) | 374 (97.9%) |
| 6 | LinkedIn Profile | 101 (0.7%) | 94 (24.6%) |
| 7 | Contact Person | 1493 (10.1%) | 199 (52.1%) |
| 8 | Role | 1493 (10.1%) | 199 (52.1%) |
| 9 | Website | 11475 (77.3%) | 382 (100.0%) |
| 10 | Address | 14274 (96.2%) | 379 (99.2%) |
| 11 | Real City | 12411 (83.7%) | 334 (87.4%) |
| 12 | Real State | 12506 (84.3%) | 333 (87.2%) |
| 13 | Market | 14836 (100.0%) | 382 (100.0%) |
| 14 | Lead Origin | 14836 (100.0%) | 382 (100.0%) |
| 15 | Rating | 4315 (29.1%) | 192 (50.3%) |
| 16 | Reviews | 4315 (29.1%) | 192 (50.3%) |
| 17 | Source | 14836 (100.0%) | 382 (100.0%) |
| 18 | Signals | 14836 (100.0%) | 382 (100.0%) |
| 19 | Match Type | 14836 (100.0%) | 382 (100.0%) |
| 20 | Email Source | 3106 (20.9%) | 374 (97.9%) |
| 21 | LinkedIn Source | 101 (0.7%) | 94 (24.6%) |
| 22 | Found At | 14836 (100.0%) | 382 (100.0%) |
| 23 | Also Listed As | 1842 (12.4%) | 111 (29.1%) |
| 24 | Other Markets | 384 (2.6%) | 40 (10.5%) |
| 25 | Merged Listings | 3366 (22.7%) | 171 (44.8%) |
| 26 | Flags | 1862 (12.6%) | 82 (21.5%) |
| 27 | Mobile Candidates | 414 (2.8%) | 298 (78.0%) |
| 28 | Socials | 2980 (20.1%) | 337 (88.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3106 | 20.9% |
| linkedin | 101 | 0.7% |
| direct-line | 414 | 2.8% |
| role-email | 1297 | 8.7% |
| gia | 816 | 5.5% |
| ags | 105 | 0.7% |
| ja | 56 | 0.4% |
| bench | 505 | 3.4% |
| custom-design | 2136 | 14.4% |
| since-yyyy | 2606 | 17.6% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1225 | 282 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1032 | 234 | 77 | 8 | 31 |
| Chicago, IL | 993 | 685 | 154 | 65 | 5 | 19 |
| Houston, TX | 1030 | 697 | 142 | 55 | 5 | 21 |
| Dallas, TX | 722 | 483 | 90 | 57 | 5 | 8 |
| Miami, FL | 1024 | 729 | 163 | 67 | 5 | 34 |
| Atlanta, GA | 739 | 526 | 128 | 62 | 11 | 23 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 3 | 14 |
| San Francisco, CA | 732 | 445 | 124 | 67 | 3 | 11 |
| Boston, MA | 570 | 345 | 109 | 56 | 7 | 18 |
| Seattle, WA | 589 | 347 | 93 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 403 | 75 | 75 | 3 | 12 |
| Phoenix, AZ | 730 | 469 | 95 | 59 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 382 | 225 | 76 | 32 | 1 | 6 |
| Detroit, MI | 554 | 378 | 82 | 51 | 6 | 18 |
| Minneapolis, MN | 531 | 245 | 61 | 91 | 6 | 9 |
| Charlotte, NC | 350 | 209 | 48 | 40 | 2 | 5 |
| Nashville, TN | 341 | 187 | 47 | 54 | 4 | 4 |
| Scottsdale, AZ | 263 | 150 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 153 | 46 | 22 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 258 | 66 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 458 | 110 | 27 | 1 | 13 |
| Austin, TX | 462 | 245 | 66 | 34 | 0 | 5 |
| San Antonio, TX | 506 | 307 | 34 | 41 | 0 | 3 |
| Fort Worth, TX | 447 | 264 | 28 | 21 | 0 | 0 |
| San Jose, CA | 432 | 254 | 25 | 2 | 0 | 2 |
| Sacramento, CA | 279 | 165 | 18 | 3 | 0 | 3 |
| Portland, OR | 298 | 198 | 29 | 5 | 0 | 0 |
| Salt Lake City, UT | 143 | 110 | 20 | 3 | 0 | 1 |
| Kansas City, MO | 143 | 106 | 25 | 6 | 0 | 0 |
| St. Louis, MO | 238 | 176 | 32 | 5 | 0 | 0 |
| Columbus, OH | 75 | 57 | 6 | 2 | 0 | 0 |
| Cleveland, OH | 316 | 195 | 39 | 5 | 0 | 2 |
| Cincinnati, OH | 323 | 204 | 24 | 6 | 0 | 0 |
| Indianapolis, IN | 252 | 162 | 27 | 7 | 0 | 4 |
| Pittsburgh, PA | 336 | 213 | 35 | 6 | 0 | 2 |
| Baltimore, MD | 307 | 218 | 27 | 4 | 0 | 2 |
| Orlando, FL | 342 | 233 | 1 | 1 | 0 | 0 |
| Tampa, FL | 228 | 174 | 19 | 0 | 0 | 2 |
| Fort Lauderdale, FL | 409 | 315 | 36 | 7 | 0 | 0 |
| Raleigh, NC | 155 | 108 | 24 | 10 | 0 | 1 |
| New Orleans, LA | 197 | 142 | 26 | 3 | 0 | 5 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 4326 | 2534 | 119 |
| YellowPages | 13672 | 10103 | 149 |
| BBB | 2783 | 1369 | 98 |
| OpenStreetMap | 1464 | 830 | 16 |

Discovery tasks completed: bbb=834, gmaps=175, osm=30, yp=695

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 98 | 0 | 35 | 133 |
| beads-craft | 607 | 39 | 4 | 650 |
| chain | 4158 | 0 | 0 | 4158 |
| coin-currency | 322 | 10 | 0 | 332 |
| costume-fashion | 564 | 182 | 40 | 786 |
| diamond-trade | 153 | 34 | 7 | 194 |
| gold-buyer | 277 | 43 | 17 | 337 |
| kiosk-battery | 12 | 0 | 0 | 12 |
| no-segment | 0 | 0 | 999 | 999 |
| pawn | 1003 | 50 | 15 | 1068 |
| piercing-tattoo | 748 | 48 | 15 | 811 |
| simulants | 7 | 36 | 4 | 47 |
| thrift-consignment | 83 | 0 | 0 | 83 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 92 | 10 | 1 | 103 |
| **all** | | | | **9716** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 2683 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 189 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 40 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| yp | soft-block-503 | 20 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-504 | 16 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 15 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| osm | http-406 | 14 | https://overpass-api.de/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
