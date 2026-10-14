# Jewelry retail lead run — REPORT

Generated 2026-10-14T15:29:20+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 24058 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 15547 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 429 |
| Qualification rate | 2.8% |
| Websites crawled OK / attempted | 12678 / 15170 |
| Listings with an owner/decision-maker name | 3598 |
| LinkedIn searches by outcome | ambiguous: 174, match: 133, none: 433, reject: 95 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 15547 (100.0%) | 429 (100.0%) |
| 2 | Segment | 15547 (100.0%) | 429 (100.0%) |
| 3 | Category (as listed) | 15512 (99.8%) | 429 (100.0%) |
| 4 | Phone | 14579 (93.8%) | 420 (97.9%) |
| 5 | Email | 3631 (23.4%) | 419 (97.7%) |
| 6 | LinkedIn Profile | 117 (0.8%) | 110 (25.6%) |
| 7 | Contact Person | 1782 (11.5%) | 224 (52.2%) |
| 8 | Role | 1782 (11.5%) | 224 (52.2%) |
| 9 | Website | 11872 (76.4%) | 429 (100.0%) |
| 10 | Address | 14912 (95.9%) | 425 (99.1%) |
| 11 | Real City | 12752 (82.0%) | 368 (85.8%) |
| 12 | Real State | 12851 (82.7%) | 367 (85.5%) |
| 13 | Market | 15547 (100.0%) | 429 (100.0%) |
| 14 | Lead Origin | 15547 (100.0%) | 429 (100.0%) |
| 15 | Rating | 4913 (31.6%) | 227 (52.9%) |
| 16 | Reviews | 4913 (31.6%) | 227 (52.9%) |
| 17 | Source | 15547 (100.0%) | 429 (100.0%) |
| 18 | Signals | 15547 (100.0%) | 429 (100.0%) |
| 19 | Match Type | 15547 (100.0%) | 429 (100.0%) |
| 20 | Email Source | 3631 (23.4%) | 419 (97.7%) |
| 21 | LinkedIn Source | 123 (0.8%) | 110 (25.6%) |
| 22 | Found At | 15547 (100.0%) | 429 (100.0%) |
| 23 | Also Listed As | 2032 (13.1%) | 118 (27.5%) |
| 24 | Other Markets | 402 (2.6%) | 40 (9.3%) |
| 25 | Merged Listings | 3735 (24.0%) | 191 (44.5%) |
| 26 | Flags | 2127 (13.7%) | 92 (21.4%) |
| 27 | Mobile Candidates | 470 (3.0%) | 331 (77.2%) |
| 28 | Socials | 3563 (22.9%) | 377 (87.9%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3631 | 23.4% |
| linkedin | 117 | 0.8% |
| direct-line | 470 | 3.0% |
| role-email | 1497 | 9.6% |
| gia | 943 | 6.1% |
| ags | 129 | 0.8% |
| ja | 72 | 0.5% |
| bench | 608 | 3.9% |
| custom-design | 2556 | 16.4% |
| since-yyyy | 3074 | 19.8% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 8 | 31 |
| Chicago, IL | 993 | 685 | 154 | 65 | 5 | 19 |
| Houston, TX | 1030 | 697 | 142 | 56 | 5 | 21 |
| Dallas, TX | 722 | 482 | 90 | 58 | 5 | 8 |
| Miami, FL | 1024 | 727 | 161 | 66 | 5 | 33 |
| Atlanta, GA | 739 | 526 | 128 | 62 | 11 | 23 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 3 | 14 |
| San Francisco, CA | 732 | 444 | 124 | 67 | 3 | 10 |
| Boston, MA | 570 | 345 | 109 | 56 | 7 | 18 |
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
| Kansas City, MO | 388 | 217 | 66 | 57 | 0 | 4 |
| St. Louis, MO | 380 | 225 | 60 | 12 | 0 | 2 |
| Columbus, OH | 192 | 124 | 39 | 8 | 0 | 2 |
| Cleveland, OH | 326 | 199 | 53 | 8 | 0 | 2 |
| Cincinnati, OH | 339 | 204 | 53 | 9 | 1 | 2 |
| Indianapolis, IN | 258 | 162 | 40 | 12 | 0 | 6 |
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
| Google Maps | 5313 | 3032 | 145 |
| YellowPages | 13634 | 9937 | 159 |
| BBB | 3335 | 1645 | 109 |
| OpenStreetMap | 1776 | 933 | 16 |

Discovery tasks completed: bbb=968, gmaps=225, osm=45, yp=705

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 110 | 0 | 35 | 145 |
| beads-craft | 631 | 53 | 6 | 690 |
| chain | 4379 | 0 | 0 | 4379 |
| coin-currency | 354 | 10 | 0 | 364 |
| costume-fashion | 581 | 222 | 48 | 851 |
| diamond-trade | 158 | 36 | 8 | 202 |
| gold-buyer | 310 | 58 | 20 | 388 |
| kiosk-battery | 15 | 0 | 0 | 15 |
| no-segment | 0 | 0 | 1400 | 1400 |
| pawn | 1068 | 57 | 15 | 1140 |
| piercing-tattoo | 794 | 63 | 16 | 873 |
| simulants | 7 | 40 | 4 | 51 |
| thrift-consignment | 95 | 0 | 0 | 95 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 98 | 10 | 1 | 109 |
| **all** | | | | **10705** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 3189 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 220 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 55 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 21 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 21 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| yp | soft-block-503 | 21 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| linkedin | blocked | 17 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
