# Jewelry retail lead run — REPORT

Generated 2026-10-14T19:07:45+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 24537 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 15724 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 443 |
| Qualification rate | 2.8% |
| Websites crawled OK / attempted | 12812 / 15369 |
| Listings with an owner/decision-maker name | 3907 |
| LinkedIn searches by outcome | ambiguous: 202, match: 144, none: 470, reject: 105 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 15724 (100.0%) | 443 (100.0%) |
| 2 | Segment | 15724 (100.0%) | 443 (100.0%) |
| 3 | Category (as listed) | 15680 (99.7%) | 443 (100.0%) |
| 4 | Phone | 14754 (93.8%) | 433 (97.7%) |
| 5 | Email | 3669 (23.3%) | 433 (97.7%) |
| 6 | LinkedIn Profile | 127 (0.8%) | 120 (27.1%) |
| 7 | Contact Person | 1927 (12.3%) | 239 (54.0%) |
| 8 | Role | 1927 (12.3%) | 239 (54.0%) |
| 9 | Website | 11985 (76.2%) | 443 (100.0%) |
| 10 | Address | 15078 (95.9%) | 438 (98.9%) |
| 11 | Real City | 12937 (82.3%) | 381 (86.0%) |
| 12 | Real State | 13035 (82.9%) | 380 (85.8%) |
| 13 | Market | 15724 (100.0%) | 443 (100.0%) |
| 14 | Lead Origin | 15724 (100.0%) | 443 (100.0%) |
| 15 | Rating | 4914 (31.3%) | 229 (51.7%) |
| 16 | Reviews | 4914 (31.3%) | 229 (51.7%) |
| 17 | Source | 15724 (100.0%) | 443 (100.0%) |
| 18 | Signals | 15724 (100.0%) | 443 (100.0%) |
| 19 | Match Type | 15724 (100.0%) | 443 (100.0%) |
| 20 | Email Source | 3669 (23.3%) | 433 (97.7%) |
| 21 | LinkedIn Source | 133 (0.8%) | 120 (27.1%) |
| 22 | Found At | 15724 (100.0%) | 443 (100.0%) |
| 23 | Also Listed As | 2095 (13.3%) | 121 (27.3%) |
| 24 | Other Markets | 422 (2.7%) | 41 (9.3%) |
| 25 | Merged Listings | 3839 (24.4%) | 199 (44.9%) |
| 26 | Flags | 2185 (13.9%) | 92 (20.8%) |
| 27 | Mobile Candidates | 472 (3.0%) | 335 (75.6%) |
| 28 | Socials | 3607 (22.9%) | 388 (87.6%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3669 | 23.3% |
| linkedin | 127 | 0.8% |
| direct-line | 472 | 3.0% |
| role-email | 1510 | 9.6% |
| gia | 962 | 6.1% |
| ags | 134 | 0.9% |
| ja | 74 | 0.5% |
| bench | 621 | 3.9% |
| custom-design | 2593 | 16.5% |
| since-yyyy | 3294 | 20.9% |

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
| Orlando, FL | 433 | 258 | 52 | 20 | 1 | 5 |
| Tampa, FL | 395 | 251 | 57 | 21 | 0 | 5 |
| Fort Lauderdale, FL | 581 | 389 | 78 | 33 | 1 | 4 |
| Raleigh, NC | 255 | 153 | 42 | 14 | 0 | 1 |
| New Orleans, LA | 349 | 204 | 51 | 8 | 0 | 5 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 5313 | 3027 | 146 |
| YellowPages | 13634 | 9913 | 159 |
| BBB | 3814 | 1853 | 122 |
| OpenStreetMap | 1776 | 931 | 16 |

Discovery tasks completed: bbb=1295, gmaps=225, osm=45, yp=705

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 112 | 0 | 35 | 147 |
| beads-craft | 636 | 53 | 6 | 695 |
| chain | 4580 | 0 | 0 | 4580 |
| coin-currency | 368 | 10 | 0 | 378 |
| costume-fashion | 585 | 223 | 49 | 857 |
| diamond-trade | 160 | 37 | 8 | 205 |
| gold-buyer | 319 | 60 | 20 | 399 |
| kiosk-battery | 15 | 0 | 0 | 15 |
| no-segment | 0 | 0 | 1464 | 1464 |
| pawn | 1090 | 58 | 21 | 1169 |
| piercing-tattoo | 831 | 64 | 16 | 911 |
| simulants | 8 | 40 | 4 | 52 |
| thrift-consignment | 100 | 0 | 0 | 100 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 100 | 10 | 1 | 111 |
| **all** | | | | **11086** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 3850 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| bbb | blocked | 249 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 55 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 21 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 21 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| yp | soft-block-503 | 21 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| linkedin | blocked | 19 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
