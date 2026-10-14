# Jewelry retail lead run — REPORT

Generated 2026-10-14T16:52:11+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 24358 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 15655 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 433 |
| Qualification rate | 2.8% |
| Websites crawled OK / attempted | 12774 / 15304 |
| Listings with an owner/decision-maker name | 3786 |
| LinkedIn searches by outcome | ambiguous: 182, match: 133, none: 441, reject: 95 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 15655 (100.0%) | 433 (100.0%) |
| 2 | Segment | 15655 (100.0%) | 433 (100.0%) |
| 3 | Category (as listed) | 15611 (99.7%) | 433 (100.0%) |
| 4 | Phone | 14687 (93.8%) | 424 (97.9%) |
| 5 | Email | 3658 (23.4%) | 423 (97.7%) |
| 6 | LinkedIn Profile | 117 (0.7%) | 110 (25.4%) |
| 7 | Contact Person | 1875 (12.0%) | 227 (52.4%) |
| 8 | Role | 1875 (12.0%) | 227 (52.4%) |
| 9 | Website | 11941 (76.3%) | 433 (100.0%) |
| 10 | Address | 15014 (95.9%) | 429 (99.1%) |
| 11 | Real City | 12864 (82.2%) | 373 (86.1%) |
| 12 | Real State | 12963 (82.8%) | 372 (85.9%) |
| 13 | Market | 15655 (100.0%) | 433 (100.0%) |
| 14 | Lead Origin | 15655 (100.0%) | 433 (100.0%) |
| 15 | Rating | 4913 (31.4%) | 226 (52.2%) |
| 16 | Reviews | 4913 (31.4%) | 226 (52.2%) |
| 17 | Source | 15655 (100.0%) | 433 (100.0%) |
| 18 | Signals | 15655 (100.0%) | 433 (100.0%) |
| 19 | Match Type | 15655 (100.0%) | 433 (100.0%) |
| 20 | Email Source | 3658 (23.4%) | 423 (97.7%) |
| 21 | LinkedIn Source | 123 (0.8%) | 110 (25.4%) |
| 22 | Found At | 15655 (100.0%) | 433 (100.0%) |
| 23 | Also Listed As | 2068 (13.2%) | 118 (27.3%) |
| 24 | Other Markets | 419 (2.7%) | 40 (9.2%) |
| 25 | Merged Listings | 3792 (24.2%) | 193 (44.6%) |
| 26 | Flags | 2157 (13.8%) | 92 (21.2%) |
| 27 | Mobile Candidates | 472 (3.0%) | 335 (77.4%) |
| 28 | Socials | 3595 (23.0%) | 381 (88.0%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3658 | 23.4% |
| linkedin | 117 | 0.7% |
| direct-line | 472 | 3.0% |
| role-email | 1505 | 9.6% |
| gia | 957 | 6.1% |
| ags | 132 | 0.8% |
| ja | 72 | 0.5% |
| bench | 618 | 3.9% |
| custom-design | 2586 | 16.5% |
| since-yyyy | 3212 | 20.5% |

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
| Cincinnati, OH | 364 | 212 | 57 | 20 | 1 | 2 |
| Indianapolis, IN | 262 | 161 | 40 | 13 | 0 | 6 |
| Pittsburgh, PA | 361 | 213 | 58 | 11 | 2 | 6 |
| Baltimore, MD | 323 | 216 | 46 | 7 | 1 | 6 |
| Orlando, FL | 398 | 245 | 48 | 8 | 1 | 4 |
| Tampa, FL | 354 | 238 | 54 | 6 | 0 | 7 |
| Fort Lauderdale, FL | 519 | 359 | 75 | 17 | 0 | 3 |
| Raleigh, NC | 251 | 152 | 42 | 13 | 0 | 1 |
| New Orleans, LA | 349 | 204 | 51 | 8 | 0 | 5 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 5313 | 3030 | 144 |
| YellowPages | 13634 | 9919 | 159 |
| BBB | 3635 | 1775 | 114 |
| OpenStreetMap | 1776 | 931 | 16 |

Discovery tasks completed: bbb=1149, gmaps=225, osm=45, yp=705

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 112 | 0 | 35 | 147 |
| beads-craft | 634 | 53 | 6 | 693 |
| chain | 4524 | 0 | 0 | 4524 |
| coin-currency | 368 | 10 | 0 | 378 |
| costume-fashion | 584 | 223 | 49 | 856 |
| diamond-trade | 160 | 36 | 8 | 204 |
| gold-buyer | 315 | 58 | 20 | 393 |
| kiosk-battery | 15 | 0 | 0 | 15 |
| no-segment | 0 | 0 | 1458 | 1458 |
| pawn | 1079 | 58 | 21 | 1158 |
| piercing-tattoo | 820 | 64 | 16 | 900 |
| simulants | 7 | 40 | 4 | 51 |
| thrift-consignment | 99 | 0 | 0 | 99 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 98 | 10 | 1 | 109 |
| **all** | | | | **10988** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 3369 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| bbb | blocked | 237 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 55 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 21 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 21 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| yp | soft-block-503 | 21 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| linkedin | blocked | 17 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
