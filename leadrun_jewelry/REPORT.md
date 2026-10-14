# Jewelry retail lead run — REPORT

Generated 2026-10-14T19:45:48+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 24717 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 15813 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 452 |
| Qualification rate | 2.9% |
| Websites crawled OK / attempted | 12866 / 15438 |
| Listings with an owner/decision-maker name | 3991 |
| LinkedIn searches by outcome | ambiguous: 217, match: 151, none: 486, reject: 110 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 15813 (100.0%) | 452 (100.0%) |
| 2 | Segment | 15813 (100.0%) | 452 (100.0%) |
| 3 | Category (as listed) | 15769 (99.7%) | 452 (100.0%) |
| 4 | Phone | 14838 (93.8%) | 442 (97.8%) |
| 5 | Email | 3688 (23.3%) | 442 (97.8%) |
| 6 | LinkedIn Profile | 134 (0.8%) | 127 (28.1%) |
| 7 | Contact Person | 1971 (12.5%) | 247 (54.6%) |
| 8 | Role | 1971 (12.5%) | 247 (54.6%) |
| 9 | Website | 12030 (76.1%) | 452 (100.0%) |
| 10 | Address | 15165 (95.9%) | 447 (98.9%) |
| 11 | Real City | 13028 (82.4%) | 390 (86.3%) |
| 12 | Real State | 13126 (83.0%) | 389 (86.1%) |
| 13 | Market | 15813 (100.0%) | 452 (100.0%) |
| 14 | Lead Origin | 15813 (100.0%) | 452 (100.0%) |
| 15 | Rating | 4913 (31.1%) | 233 (51.5%) |
| 16 | Reviews | 4913 (31.1%) | 233 (51.5%) |
| 17 | Source | 15813 (100.0%) | 452 (100.0%) |
| 18 | Signals | 15813 (100.0%) | 452 (100.0%) |
| 19 | Match Type | 15813 (100.0%) | 452 (100.0%) |
| 20 | Email Source | 3688 (23.3%) | 442 (97.8%) |
| 21 | LinkedIn Source | 140 (0.9%) | 127 (28.1%) |
| 22 | Found At | 15813 (100.0%) | 452 (100.0%) |
| 23 | Also Listed As | 2113 (13.4%) | 123 (27.2%) |
| 24 | Other Markets | 425 (2.7%) | 42 (9.3%) |
| 25 | Merged Listings | 3860 (24.4%) | 205 (45.4%) |
| 26 | Flags | 2204 (13.9%) | 94 (20.8%) |
| 27 | Mobile Candidates | 474 (3.0%) | 337 (74.6%) |
| 28 | Socials | 3630 (23.0%) | 396 (87.6%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3688 | 23.3% |
| linkedin | 134 | 0.8% |
| direct-line | 474 | 3.0% |
| role-email | 1518 | 9.6% |
| gia | 965 | 6.1% |
| ags | 135 | 0.9% |
| ja | 75 | 0.5% |
| bench | 627 | 4.0% |
| custom-design | 2613 | 16.5% |
| since-yyyy | 3373 | 21.3% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 8 | 31 |
| Chicago, IL | 993 | 685 | 154 | 65 | 5 | 19 |
| Houston, TX | 1030 | 697 | 142 | 56 | 5 | 21 |
| Dallas, TX | 722 | 481 | 89 | 58 | 5 | 8 |
| Miami, FL | 1024 | 726 | 160 | 66 | 5 | 33 |
| Atlanta, GA | 739 | 526 | 128 | 62 | 11 | 23 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 3 | 14 |
| San Francisco, CA | 732 | 444 | 124 | 67 | 3 | 10 |
| Boston, MA | 570 | 345 | 109 | 57 | 7 | 18 |
| Seattle, WA | 589 | 347 | 93 | 69 | 2 | 10 |
| Las Vegas, NV | 691 | 402 | 74 | 75 | 3 | 12 |
| Phoenix, AZ | 730 | 469 | 95 | 59 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 382 | 225 | 76 | 32 | 1 | 6 |
| Detroit, MI | 554 | 378 | 82 | 51 | 6 | 18 |
| Minneapolis, MN | 531 | 245 | 61 | 91 | 6 | 9 |
| Charlotte, NC | 350 | 208 | 47 | 40 | 2 | 5 |
| Nashville, TN | 341 | 186 | 47 | 54 | 4 | 4 |
| Scottsdale, AZ | 263 | 149 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 151 | 46 | 21 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 258 | 66 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 458 | 110 | 28 | 1 | 13 |
| Austin, TX | 458 | 239 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 303 | 51 | 42 | 2 | 6 |
| Fort Worth, TX | 456 | 259 | 47 | 24 | 0 | 0 |
| San Jose, CA | 522 | 288 | 36 | 16 | 0 | 3 |
| Sacramento, CA | 372 | 207 | 38 | 39 | 2 | 7 |
| Portland, OR | 515 | 278 | 69 | 55 | 2 | 4 |
| Salt Lake City, UT | 445 | 238 | 65 | 71 | 7 | 9 |
| Kansas City, MO | 451 | 265 | 74 | 80 | 3 | 8 |
| St. Louis, MO | 526 | 263 | 72 | 53 | 2 | 6 |
| Columbus, OH | 238 | 136 | 41 | 22 | 2 | 4 |
| Cleveland, OH | 335 | 201 | 54 | 9 | 0 | 2 |
| Cincinnati, OH | 364 | 212 | 57 | 20 | 2 | 3 |
| Indianapolis, IN | 262 | 161 | 40 | 13 | 0 | 6 |
| Pittsburgh, PA | 394 | 225 | 60 | 17 | 2 | 7 |
| Baltimore, MD | 327 | 217 | 46 | 8 | 1 | 6 |
| Orlando, FL | 433 | 258 | 52 | 20 | 1 | 5 |
| Tampa, FL | 395 | 251 | 57 | 21 | 0 | 5 |
| Fort Lauderdale, FL | 581 | 389 | 79 | 33 | 3 | 7 |
| Raleigh, NC | 273 | 159 | 45 | 23 | 1 | 2 |
| New Orleans, LA | 511 | 287 | 66 | 43 | 2 | 8 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 5313 | 3024 | 146 |
| YellowPages | 13634 | 9903 | 162 |
| BBB | 3994 | 1957 | 128 |
| OpenStreetMap | 1776 | 929 | 16 |

Discovery tasks completed: bbb=1350, gmaps=225, osm=45, yp=705

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 112 | 0 | 35 | 147 |
| beads-craft | 638 | 53 | 6 | 697 |
| chain | 4630 | 0 | 0 | 4630 |
| coin-currency | 369 | 10 | 0 | 379 |
| costume-fashion | 587 | 224 | 49 | 860 |
| diamond-trade | 161 | 37 | 8 | 206 |
| gold-buyer | 319 | 61 | 20 | 400 |
| kiosk-battery | 15 | 0 | 0 | 15 |
| no-segment | 0 | 0 | 1476 | 1476 |
| pawn | 1096 | 58 | 21 | 1175 |
| piercing-tattoo | 836 | 65 | 16 | 917 |
| simulants | 8 | 40 | 4 | 52 |
| thrift-consignment | 100 | 0 | 0 | 100 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 101 | 10 | 1 | 112 |
| **all** | | | | **11169** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 3972 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| bbb | blocked | 253 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 55 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 21 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 21 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| yp | soft-block-503 | 21 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| linkedin | blocked | 20 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
