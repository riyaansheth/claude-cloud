# Jewelry retail lead run — REPORT

Generated 2026-10-14T14:09:04+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 23540 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 15332 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 421 |
| Qualification rate | 2.7% |
| Websites crawled OK / attempted | 12580 / 15025 |
| Listings with an owner/decision-maker name | 3330 |
| LinkedIn searches by outcome | ambiguous: 166, match: 125, none: 413, reject: 88 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 15332 (100.0%) | 421 (100.0%) |
| 2 | Segment | 15332 (100.0%) | 421 (100.0%) |
| 3 | Category (as listed) | 15298 (99.8%) | 421 (100.0%) |
| 4 | Phone | 14432 (94.1%) | 412 (97.9%) |
| 5 | Email | 3588 (23.4%) | 412 (97.9%) |
| 6 | LinkedIn Profile | 110 (0.7%) | 103 (24.5%) |
| 7 | Contact Person | 1633 (10.7%) | 214 (50.8%) |
| 8 | Role | 1633 (10.7%) | 214 (50.8%) |
| 9 | Website | 11772 (76.8%) | 421 (100.0%) |
| 10 | Address | 14738 (96.1%) | 417 (99.0%) |
| 11 | Real City | 12562 (81.9%) | 358 (85.0%) |
| 12 | Real State | 12656 (82.5%) | 357 (84.8%) |
| 13 | Market | 15332 (100.0%) | 421 (100.0%) |
| 14 | Lead Origin | 15332 (100.0%) | 421 (100.0%) |
| 15 | Rating | 4915 (32.1%) | 226 (53.7%) |
| 16 | Reviews | 4915 (32.1%) | 226 (53.7%) |
| 17 | Source | 15332 (100.0%) | 421 (100.0%) |
| 18 | Signals | 15332 (100.0%) | 421 (100.0%) |
| 19 | Match Type | 15332 (100.0%) | 421 (100.0%) |
| 20 | Email Source | 3588 (23.4%) | 412 (97.9%) |
| 21 | LinkedIn Source | 116 (0.8%) | 103 (24.5%) |
| 22 | Found At | 15332 (100.0%) | 421 (100.0%) |
| 23 | Also Listed As | 1990 (13.0%) | 115 (27.3%) |
| 24 | Other Markets | 398 (2.6%) | 40 (9.5%) |
| 25 | Merged Listings | 3642 (23.8%) | 189 (44.9%) |
| 26 | Flags | 2034 (13.3%) | 90 (21.4%) |
| 27 | Mobile Candidates | 467 (3.0%) | 329 (78.1%) |
| 28 | Socials | 3521 (23.0%) | 371 (88.1%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 3588 | 23.4% |
| linkedin | 110 | 0.7% |
| direct-line | 467 | 3.0% |
| role-email | 1475 | 9.6% |
| gia | 929 | 6.1% |
| ags | 125 | 0.8% |
| ja | 68 | 0.4% |
| bench | 597 | 3.9% |
| custom-design | 2517 | 16.4% |
| since-yyyy | 2876 | 18.8% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1224 | 281 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 8 | 31 |
| Chicago, IL | 993 | 685 | 154 | 65 | 5 | 19 |
| Houston, TX | 1030 | 697 | 142 | 56 | 5 | 21 |
| Dallas, TX | 722 | 483 | 90 | 58 | 5 | 8 |
| Miami, FL | 1024 | 727 | 161 | 65 | 5 | 33 |
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
| Portland, OR | 424 | 247 | 61 | 13 | 1 | 2 |
| Salt Lake City, UT | 289 | 159 | 45 | 7 | 0 | 2 |
| Kansas City, MO | 282 | 168 | 54 | 15 | 0 | 4 |
| St. Louis, MO | 380 | 225 | 60 | 12 | 0 | 2 |
| Columbus, OH | 192 | 124 | 39 | 8 | 0 | 2 |
| Cleveland, OH | 313 | 192 | 53 | 8 | 0 | 2 |
| Cincinnati, OH | 321 | 198 | 52 | 9 | 1 | 2 |
| Indianapolis, IN | 250 | 160 | 40 | 12 | 0 | 6 |
| Pittsburgh, PA | 335 | 207 | 57 | 10 | 2 | 5 |
| Baltimore, MD | 300 | 207 | 47 | 8 | 1 | 6 |
| Orlando, FL | 373 | 235 | 48 | 8 | 1 | 4 |
| Tampa, FL | 342 | 233 | 53 | 6 | 0 | 7 |
| Fort Lauderdale, FL | 516 | 357 | 74 | 16 | 0 | 3 |
| Raleigh, NC | 233 | 149 | 42 | 13 | 0 | 1 |
| New Orleans, LA | 323 | 194 | 50 | 8 | 0 | 5 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 5313 | 3038 | 146 |
| YellowPages | 13634 | 9961 | 160 |
| BBB | 2982 | 1459 | 99 |
| OpenStreetMap | 1611 | 874 | 16 |

Discovery tasks completed: bbb=901, gmaps=225, osm=35, yp=705

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 107 | 0 | 35 | 142 |
| beads-craft | 623 | 52 | 4 | 679 |
| chain | 4249 | 0 | 0 | 4249 |
| coin-currency | 348 | 10 | 0 | 358 |
| costume-fashion | 574 | 218 | 45 | 837 |
| diamond-trade | 157 | 36 | 7 | 200 |
| gold-buyer | 307 | 58 | 19 | 384 |
| kiosk-battery | 15 | 0 | 0 | 15 |
| no-segment | 0 | 0 | 1360 | 1360 |
| pawn | 1060 | 57 | 15 | 1132 |
| piercing-tattoo | 783 | 63 | 16 | 862 |
| simulants | 7 | 40 | 4 | 51 |
| thrift-consignment | 94 | 0 | 0 | 94 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 96 | 10 | 1 | 107 |
| **all** | | | | **10473** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 2899 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 196 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 48 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| yp | soft-block-503 | 21 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| osm | http-504 | 18 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 16 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| osm | http-406 | 16 | https://overpass-api.de/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
