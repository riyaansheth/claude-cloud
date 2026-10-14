# Jewelry retail lead run — REPORT

Generated 2026-10-14T14:36:09+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 23678 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 15378 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 422 |
| Qualification rate | 2.7% |
| Websites crawled OK / attempted | 12600 / 15059 |
| Listings with an owner/decision-maker name | 3395 |
| LinkedIn searches by outcome | ambiguous: 166, match: 125, none: 413, reject: 88 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 15378 (100.0%) | 422 (100.0%) |
| 2 | Segment | 15378 (100.0%) | 422 (100.0%) |
| 3 | Category (as listed) | 15344 (99.8%) | 422 (100.0%) |
| 4 | Phone | 14457 (94.0%) | 413 (97.9%) |
| 5 | Email | 3595 (23.4%) | 413 (97.9%) |
| 6 | LinkedIn Profile | 110 (0.7%) | 103 (24.4%) |
| 7 | Contact Person | 1670 (10.9%) | 215 (50.9%) |
| 8 | Role | 1670 (10.9%) | 215 (50.9%) |
| 9 | Website | 11789 (76.7%) | 422 (100.0%) |
| 10 | Address | 14770 (96.0%) | 418 (99.1%) |
| 11 | Real City | 12598 (81.9%) | 359 (85.1%) |
| 12 | Real State | 12694 (82.5%) | 358 (84.8%) |
| 13 | Market | 15378 (100.0%) | 422 (100.0%) |
| 14 | Lead Origin | 15378 (100.0%) | 422 (100.0%) |
| 15 | Rating | 4915 (32.0%) | 226 (53.6%) |
| 16 | Reviews | 4915 (32.0%) | 226 (53.6%) |
| 17 | Source | 15378 (100.0%) | 422 (100.0%) |
| 18 | Signals | 15378 (100.0%) | 422 (100.0%) |
| 19 | Match Type | 15378 (100.0%) | 422 (100.0%) |
| 20 | Email Source | 3595 (23.4%) | 413 (97.9%) |
| 21 | LinkedIn Source | 116 (0.8%) | 103 (24.4%) |
| 22 | Found At | 15378 (100.0%) | 422 (100.0%) |
| 23 | Also Listed As | 2005 (13.0%) | 116 (27.5%) |
| 24 | Other Markets | 398 (2.6%) | 40 (9.5%) |
| 25 | Merged Listings | 3671 (23.9%) | 189 (44.8%) |
| 26 | Flags | 2064 (13.4%) | 91 (21.6%) |
| 27 | Mobile Candidates | 468 (3.0%) | 330 (78.2%) |
| 28 | Socials | 3527 (22.9%) | 372 (88.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3595 | 23.4% |
| linkedin | 110 | 0.7% |
| direct-line | 468 | 3.0% |
| role-email | 1479 | 9.6% |
| gia | 932 | 6.1% |
| ags | 126 | 0.8% |
| ja | 68 | 0.4% |
| bench | 599 | 3.9% |
| custom-design | 2519 | 16.4% |
| since-yyyy | 2932 | 19.1% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 8 | 31 |
| Chicago, IL | 993 | 685 | 154 | 65 | 5 | 19 |
| Houston, TX | 1030 | 697 | 142 | 56 | 5 | 21 |
| Dallas, TX | 722 | 483 | 90 | 58 | 5 | 8 |
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
| Scottsdale, AZ | 263 | 150 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 151 | 46 | 21 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 258 | 66 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 458 | 110 | 27 | 1 | 13 |
| Austin, TX | 458 | 239 | 80 | 37 | 1 | 6 |
| San Antonio, TX | 502 | 303 | 51 | 42 | 2 | 6 |
| Fort Worth, TX | 456 | 259 | 47 | 24 | 0 | 0 |
| San Jose, CA | 522 | 288 | 36 | 16 | 0 | 3 |
| Sacramento, CA | 372 | 207 | 38 | 39 | 0 | 5 |
| Portland, OR | 504 | 274 | 67 | 49 | 1 | 3 |
| Salt Lake City, UT | 289 | 159 | 45 | 7 | 0 | 2 |
| Kansas City, MO | 282 | 168 | 54 | 15 | 0 | 4 |
| St. Louis, MO | 380 | 225 | 60 | 12 | 0 | 2 |
| Columbus, OH | 192 | 124 | 39 | 8 | 0 | 2 |
| Cleveland, OH | 326 | 199 | 53 | 8 | 0 | 2 |
| Cincinnati, OH | 339 | 204 | 53 | 9 | 1 | 2 |
| Indianapolis, IN | 258 | 162 | 40 | 12 | 0 | 6 |
| Pittsburgh, PA | 354 | 211 | 57 | 10 | 2 | 5 |
| Baltimore, MD | 300 | 207 | 47 | 8 | 1 | 6 |
| Orlando, FL | 373 | 235 | 48 | 8 | 1 | 4 |
| Tampa, FL | 342 | 233 | 53 | 6 | 0 | 7 |
| Fort Lauderdale, FL | 516 | 357 | 74 | 16 | 0 | 3 |
| Raleigh, NC | 233 | 149 | 42 | 13 | 0 | 1 |
| New Orleans, LA | 323 | 194 | 50 | 8 | 0 | 5 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 5313 | 3035 | 146 |
| YellowPages | 13634 | 9950 | 160 |
| BBB | 3062 | 1498 | 100 |
| OpenStreetMap | 1669 | 895 | 16 |

Discovery tasks completed: bbb=914, gmaps=225, osm=39, yp=705

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 109 | 0 | 35 | 144 |
| beads-craft | 629 | 53 | 5 | 687 |
| chain | 4272 | 0 | 0 | 4272 |
| coin-currency | 350 | 10 | 0 | 360 |
| costume-fashion | 577 | 219 | 45 | 841 |
| diamond-trade | 157 | 36 | 7 | 200 |
| gold-buyer | 308 | 58 | 19 | 385 |
| kiosk-battery | 15 | 0 | 0 | 15 |
| no-segment | 0 | 0 | 1368 | 1368 |
| pawn | 1064 | 57 | 15 | 1136 |
| piercing-tattoo | 786 | 63 | 16 | 865 |
| simulants | 7 | 40 | 4 | 51 |
| thrift-consignment | 95 | 0 | 0 | 95 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 97 | 10 | 1 | 108 |
| **all** | | | | **10530** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 3009 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 207 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 52 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| yp | soft-block-503 | 21 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-406 | 18 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 18 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 16 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
