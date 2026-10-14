# Jewelry retail lead run — REPORT

Generated 2026-10-14T16:31:43+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 24336 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 15649 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 432 |
| Qualification rate | 2.8% |
| Websites crawled OK / attempted | 12767 / 15294 |
| Listings with an owner/decision-maker name | 3770 |
| LinkedIn searches by outcome | ambiguous: 174, match: 133, none: 433, reject: 95 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 15649 (100.0%) | 432 (100.0%) |
| 2 | Segment | 15649 (100.0%) | 432 (100.0%) |
| 3 | Category (as listed) | 15605 (99.7%) | 432 (100.0%) |
| 4 | Phone | 14681 (93.8%) | 423 (97.9%) |
| 5 | Email | 3655 (23.4%) | 422 (97.7%) |
| 6 | LinkedIn Profile | 117 (0.7%) | 110 (25.5%) |
| 7 | Contact Person | 1869 (11.9%) | 226 (52.3%) |
| 8 | Role | 1869 (11.9%) | 226 (52.3%) |
| 9 | Website | 11936 (76.3%) | 432 (100.0%) |
| 10 | Address | 15008 (95.9%) | 428 (99.1%) |
| 11 | Real City | 12857 (82.2%) | 372 (86.1%) |
| 12 | Real State | 12956 (82.8%) | 371 (85.9%) |
| 13 | Market | 15649 (100.0%) | 432 (100.0%) |
| 14 | Lead Origin | 15649 (100.0%) | 432 (100.0%) |
| 15 | Rating | 4913 (31.4%) | 226 (52.3%) |
| 16 | Reviews | 4913 (31.4%) | 226 (52.3%) |
| 17 | Source | 15649 (100.0%) | 432 (100.0%) |
| 18 | Signals | 15649 (100.0%) | 432 (100.0%) |
| 19 | Match Type | 15649 (100.0%) | 432 (100.0%) |
| 20 | Email Source | 3655 (23.4%) | 422 (97.7%) |
| 21 | LinkedIn Source | 123 (0.8%) | 110 (25.5%) |
| 22 | Found At | 15649 (100.0%) | 432 (100.0%) |
| 23 | Also Listed As | 2067 (13.2%) | 118 (27.3%) |
| 24 | Other Markets | 419 (2.7%) | 40 (9.3%) |
| 25 | Merged Listings | 3790 (24.2%) | 193 (44.7%) |
| 26 | Flags | 2157 (13.8%) | 92 (21.3%) |
| 27 | Mobile Candidates | 471 (3.0%) | 334 (77.3%) |
| 28 | Socials | 3592 (23.0%) | 380 (88.0%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3655 | 23.4% |
| linkedin | 117 | 0.7% |
| direct-line | 471 | 3.0% |
| role-email | 1505 | 9.6% |
| gia | 956 | 6.1% |
| ags | 131 | 0.8% |
| ja | 72 | 0.5% |
| bench | 616 | 3.9% |
| custom-design | 2584 | 16.5% |
| since-yyyy | 3206 | 20.5% |

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
| Salt Lake City, UT | 445 | 238 | 65 | 71 | 5 | 7 |
| Kansas City, MO | 451 | 265 | 74 | 80 | 0 | 5 |
| St. Louis, MO | 526 | 263 | 72 | 53 | 0 | 4 |
| Columbus, OH | 238 | 136 | 41 | 22 | 0 | 2 |
| Cleveland, OH | 335 | 201 | 54 | 9 | 0 | 2 |
| Cincinnati, OH | 353 | 208 | 55 | 16 | 1 | 2 |
| Indianapolis, IN | 258 | 161 | 40 | 12 | 0 | 6 |
| Pittsburgh, PA | 354 | 211 | 57 | 10 | 2 | 5 |
| Baltimore, MD | 323 | 216 | 46 | 7 | 1 | 6 |
| Orlando, FL | 398 | 245 | 48 | 8 | 1 | 4 |
| Tampa, FL | 354 | 238 | 54 | 6 | 0 | 7 |
| Fort Lauderdale, FL | 519 | 359 | 75 | 17 | 0 | 3 |
| Raleigh, NC | 251 | 152 | 42 | 13 | 0 | 1 |
| New Orleans, LA | 349 | 204 | 51 | 8 | 0 | 5 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 5313 | 3031 | 144 |
| YellowPages | 13634 | 9921 | 159 |
| BBB | 3613 | 1766 | 113 |
| OpenStreetMap | 1776 | 931 | 16 |

Discovery tasks completed: bbb=1088, gmaps=225, osm=45, yp=705

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 112 | 0 | 35 | 147 |
| beads-craft | 634 | 53 | 6 | 693 |
| chain | 4510 | 0 | 0 | 4510 |
| coin-currency | 368 | 10 | 0 | 378 |
| costume-fashion | 584 | 223 | 49 | 856 |
| diamond-trade | 160 | 36 | 8 | 204 |
| gold-buyer | 315 | 58 | 20 | 393 |
| kiosk-battery | 15 | 0 | 0 | 15 |
| no-segment | 0 | 0 | 1451 | 1451 |
| pawn | 1079 | 58 | 19 | 1156 |
| piercing-tattoo | 817 | 64 | 16 | 897 |
| simulants | 7 | 40 | 4 | 51 |
| thrift-consignment | 98 | 0 | 0 | 98 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 98 | 10 | 1 | 109 |
| **all** | | | | **10961** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 3309 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 230 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 55 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 21 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 21 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| yp | soft-block-503 | 21 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| linkedin | blocked | 17 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
