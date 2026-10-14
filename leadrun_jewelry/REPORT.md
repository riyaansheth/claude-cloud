# Jewelry retail lead run — REPORT

Generated 2026-10-14T18:47:17+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 24429 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 15681 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 445 |
| Qualification rate | 2.8% |
| Websites crawled OK / attempted | 12791 / 15331 |
| Listings with an owner/decision-maker name | 3827 |
| LinkedIn searches by outcome | ambiguous: 202, match: 144, none: 470, reject: 105 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 15681 (100.0%) | 445 (100.0%) |
| 2 | Segment | 15681 (100.0%) | 445 (100.0%) |
| 3 | Category (as listed) | 15637 (99.7%) | 445 (100.0%) |
| 4 | Phone | 14712 (93.8%) | 435 (97.8%) |
| 5 | Email | 3664 (23.4%) | 435 (97.8%) |
| 6 | LinkedIn Profile | 127 (0.8%) | 120 (27.0%) |
| 7 | Contact Person | 1894 (12.1%) | 239 (53.7%) |
| 8 | Role | 1894 (12.1%) | 239 (53.7%) |
| 9 | Website | 11957 (76.3%) | 445 (100.0%) |
| 10 | Address | 15036 (95.9%) | 440 (98.9%) |
| 11 | Real City | 12890 (82.2%) | 383 (86.1%) |
| 12 | Real State | 12989 (82.8%) | 382 (85.8%) |
| 13 | Market | 15681 (100.0%) | 445 (100.0%) |
| 14 | Lead Origin | 15681 (100.0%) | 445 (100.0%) |
| 15 | Rating | 4913 (31.3%) | 231 (51.9%) |
| 16 | Reviews | 4913 (31.3%) | 231 (51.9%) |
| 17 | Source | 15681 (100.0%) | 445 (100.0%) |
| 18 | Signals | 15681 (100.0%) | 445 (100.0%) |
| 19 | Match Type | 15681 (100.0%) | 445 (100.0%) |
| 20 | Email Source | 3664 (23.4%) | 435 (97.8%) |
| 21 | LinkedIn Source | 133 (0.8%) | 120 (27.0%) |
| 22 | Found At | 15681 (100.0%) | 445 (100.0%) |
| 23 | Also Listed As | 2076 (13.2%) | 123 (27.6%) |
| 24 | Other Markets | 422 (2.7%) | 41 (9.2%) |
| 25 | Merged Listings | 3812 (24.3%) | 201 (45.2%) |
| 26 | Flags | 2169 (13.8%) | 93 (20.9%) |
| 27 | Mobile Candidates | 474 (3.0%) | 337 (75.7%) |
| 28 | Socials | 3602 (23.0%) | 390 (87.6%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3664 | 23.4% |
| linkedin | 127 | 0.8% |
| direct-line | 474 | 3.0% |
| role-email | 1508 | 9.6% |
| gia | 960 | 6.1% |
| ags | 133 | 0.8% |
| ja | 74 | 0.5% |
| bench | 621 | 4.0% |
| custom-design | 2591 | 16.5% |
| since-yyyy | 3245 | 20.7% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 8 | 31 |
| Chicago, IL | 993 | 685 | 154 | 65 | 5 | 19 |
| Houston, TX | 1030 | 697 | 142 | 56 | 5 | 21 |
| Dallas, TX | 722 | 481 | 89 | 58 | 5 | 8 |
| Miami, FL | 1024 | 727 | 161 | 66 | 5 | 33 |
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
| Beverly Hills, CA | 625 | 458 | 110 | 27 | 1 | 13 |
| Austin, TX | 458 | 239 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 303 | 51 | 42 | 2 | 6 |
| Fort Worth, TX | 456 | 259 | 47 | 24 | 0 | 0 |
| San Jose, CA | 522 | 288 | 36 | 16 | 0 | 3 |
| Sacramento, CA | 372 | 207 | 38 | 39 | 1 | 6 |
| Portland, OR | 515 | 278 | 69 | 55 | 2 | 4 |
| Salt Lake City, UT | 445 | 238 | 65 | 71 | 7 | 9 |
| Kansas City, MO | 451 | 265 | 74 | 80 | 3 | 8 |
| St. Louis, MO | 526 | 263 | 72 | 53 | 2 | 6 |
| Columbus, OH | 238 | 136 | 41 | 22 | 2 | 4 |
| Cleveland, OH | 335 | 201 | 54 | 9 | 0 | 2 |
| Cincinnati, OH | 364 | 212 | 57 | 20 | 1 | 2 |
| Indianapolis, IN | 262 | 161 | 40 | 13 | 0 | 6 |
| Pittsburgh, PA | 394 | 225 | 60 | 17 | 2 | 7 |
| Baltimore, MD | 327 | 217 | 46 | 8 | 1 | 6 |
| Orlando, FL | 432 | 258 | 52 | 20 | 1 | 5 |
| Tampa, FL | 354 | 238 | 54 | 6 | 0 | 7 |
| Fort Lauderdale, FL | 519 | 359 | 75 | 17 | 1 | 4 |
| Raleigh, NC | 251 | 152 | 42 | 13 | 0 | 1 |
| New Orleans, LA | 349 | 204 | 51 | 8 | 0 | 5 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 5313 | 3029 | 147 |
| YellowPages | 13634 | 9919 | 160 |
| BBB | 3706 | 1802 | 122 |
| OpenStreetMap | 1776 | 931 | 16 |

Discovery tasks completed: bbb=1229, gmaps=225, osm=45, yp=705

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 112 | 0 | 35 | 147 |
| beads-craft | 634 | 53 | 6 | 693 |
| chain | 4556 | 0 | 0 | 4556 |
| coin-currency | 368 | 10 | 0 | 378 |
| costume-fashion | 584 | 223 | 49 | 856 |
| diamond-trade | 160 | 36 | 8 | 204 |
| gold-buyer | 318 | 59 | 20 | 397 |
| kiosk-battery | 15 | 0 | 0 | 15 |
| no-segment | 0 | 0 | 1462 | 1462 |
| pawn | 1079 | 58 | 21 | 1158 |
| piercing-tattoo | 830 | 64 | 16 | 910 |
| simulants | 7 | 40 | 4 | 51 |
| thrift-consignment | 99 | 0 | 0 | 99 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 100 | 10 | 1 | 111 |
| **all** | | | | **11040** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 3789 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| bbb | blocked | 246 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 55 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 21 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 21 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| yp | soft-block-503 | 21 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| linkedin | blocked | 19 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
