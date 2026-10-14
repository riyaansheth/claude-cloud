# Jewelry retail lead run — REPORT

Generated 2026-10-14T12:41:26+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 21670 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 14586 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 372 |
| Qualification rate | 2.6% |
| Websites crawled OK / attempted | 10493 / 12528 |
| Listings with an owner/decision-maker name | 3015 |
| LinkedIn searches by outcome | ambiguous: 182, match: 110, none: 383, reject: 44 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 14586 (100.0%) | 372 (100.0%) |
| 2 | Segment | 14586 (100.0%) | 372 (100.0%) |
| 3 | Category (as listed) | 14563 (99.8%) | 372 (100.0%) |
| 4 | Phone | 13787 (94.5%) | 366 (98.4%) |
| 5 | Email | 2991 (20.5%) | 364 (97.8%) |
| 6 | LinkedIn Profile | 101 (0.7%) | 94 (25.3%) |
| 7 | Contact Person | 1464 (10.0%) | 194 (52.2%) |
| 8 | Role | 1464 (10.0%) | 194 (52.2%) |
| 9 | Website | 11288 (77.4%) | 372 (100.0%) |
| 10 | Address | 14034 (96.2%) | 369 (99.2%) |
| 11 | Real City | 12335 (84.6%) | 325 (87.4%) |
| 12 | Real State | 12431 (85.2%) | 324 (87.1%) |
| 13 | Market | 14586 (100.0%) | 372 (100.0%) |
| 14 | Lead Origin | 14586 (100.0%) | 372 (100.0%) |
| 15 | Rating | 4042 (27.7%) | 188 (50.5%) |
| 16 | Reviews | 4042 (27.7%) | 188 (50.5%) |
| 17 | Source | 14586 (100.0%) | 372 (100.0%) |
| 18 | Signals | 14586 (100.0%) | 372 (100.0%) |
| 19 | Match Type | 14586 (100.0%) | 372 (100.0%) |
| 20 | Email Source | 2991 (20.5%) | 364 (97.8%) |
| 21 | LinkedIn Source | 101 (0.7%) | 94 (25.3%) |
| 22 | Found At | 14586 (100.0%) | 372 (100.0%) |
| 23 | Also Listed As | 1780 (12.2%) | 108 (29.0%) |
| 24 | Other Markets | 371 (2.5%) | 40 (10.8%) |
| 25 | Merged Listings | 3238 (22.2%) | 168 (45.2%) |
| 26 | Flags | 1802 (12.4%) | 79 (21.2%) |
| 27 | Mobile Candidates | 396 (2.7%) | 288 (77.4%) |
| 28 | Socials | 2865 (19.6%) | 327 (87.9%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2991 | 20.5% |
| linkedin | 101 | 0.7% |
| direct-line | 396 | 2.7% |
| role-email | 1252 | 8.6% |
| gia | 784 | 5.4% |
| ags | 97 | 0.7% |
| ja | 53 | 0.4% |
| bench | 480 | 3.3% |
| custom-design | 2058 | 14.1% |
| since-yyyy | 2548 | 17.5% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1225 | 282 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1032 | 234 | 77 | 8 | 31 |
| Chicago, IL | 993 | 685 | 154 | 65 | 5 | 19 |
| Houston, TX | 1030 | 697 | 142 | 55 | 5 | 21 |
| Dallas, TX | 722 | 484 | 90 | 58 | 5 | 8 |
| Miami, FL | 1024 | 729 | 163 | 67 | 5 | 34 |
| Atlanta, GA | 739 | 526 | 128 | 62 | 11 | 23 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 3 | 14 |
| San Francisco, CA | 732 | 446 | 124 | 67 | 3 | 11 |
| Boston, MA | 570 | 345 | 109 | 56 | 7 | 18 |
| Seattle, WA | 589 | 347 | 93 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 403 | 75 | 75 | 3 | 12 |
| Phoenix, AZ | 730 | 469 | 95 | 59 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 382 | 226 | 76 | 33 | 1 | 6 |
| Detroit, MI | 554 | 378 | 82 | 51 | 6 | 18 |
| Minneapolis, MN | 531 | 245 | 61 | 91 | 6 | 9 |
| Charlotte, NC | 350 | 210 | 48 | 41 | 2 | 5 |
| Nashville, TN | 341 | 187 | 47 | 54 | 4 | 4 |
| Scottsdale, AZ | 263 | 150 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 153 | 46 | 22 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 258 | 66 | 22 | 2 | 9 |
| Beverly Hills, CA | 625 | 458 | 110 | 27 | 1 | 13 |
| Austin, TX | 368 | 208 | 51 | 30 | 0 | 4 |
| San Antonio, TX | 484 | 297 | 19 | 39 | 0 | 1 |
| Fort Worth, TX | 438 | 255 | 22 | 18 | 0 | 0 |
| San Jose, CA | 394 | 235 | 23 | 1 | 0 | 2 |
| Sacramento, CA | 143 | 101 | 10 | 1 | 0 | 1 |
| Portland, OR | 254 | 185 | 29 | 5 | 0 | 0 |
| Salt Lake City, UT | 143 | 110 | 20 | 3 | 0 | 1 |
| Kansas City, MO | 143 | 107 | 16 | 4 | 0 | 0 |
| St. Louis, MO | 239 | 178 | 21 | 1 | 0 | 0 |
| Columbus, OH | 43 | 37 | 5 | 1 | 0 | 0 |
| Cleveland, OH | 319 | 196 | 32 | 4 | 0 | 2 |
| Cincinnati, OH | 323 | 205 | 19 | 4 | 0 | 0 |
| Indianapolis, IN | 252 | 162 | 27 | 7 | 0 | 4 |
| Pittsburgh, PA | 292 | 193 | 28 | 4 | 0 | 1 |
| Baltimore, MD | 202 | 158 | 17 | 1 | 0 | 0 |
| Orlando, FL | 302 | 223 | 1 | 1 | 0 | 0 |
| Tampa, FL | 228 | 174 | 19 | 0 | 0 | 2 |
| Fort Lauderdale, FL | 409 | 315 | 36 | 7 | 0 | 0 |
| Raleigh, NC | 156 | 110 | 14 | 6 | 0 | 1 |
| New Orleans, LA | 197 | 143 | 17 | 2 | 0 | 3 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3937 | 2358 | 118 |
| YellowPages | 13527 | 10034 | 140 |
| BBB | 2775 | 1369 | 98 |
| OpenStreetMap | 1447 | 825 | 16 |

Discovery tasks completed: bbb=824, gmaps=157, osm=29, yp=679

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 90 | 0 | 35 | 125 |
| beads-craft | 592 | 39 | 4 | 635 |
| chain | 4109 | 0 | 0 | 4109 |
| coin-currency | 309 | 10 | 0 | 319 |
| costume-fashion | 547 | 176 | 38 | 761 |
| diamond-trade | 150 | 32 | 7 | 189 |
| gold-buyer | 266 | 42 | 17 | 325 |
| kiosk-battery | 11 | 0 | 0 | 11 |
| no-segment | 0 | 0 | 950 | 950 |
| pawn | 963 | 50 | 15 | 1028 |
| piercing-tattoo | 716 | 48 | 15 | 779 |
| simulants | 7 | 35 | 4 | 46 |
| thrift-consignment | 69 | 0 | 0 | 69 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 91 | 10 | 1 | 102 |
| **all** | | | | **9451** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 2630 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 186 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 37 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| yp | soft-block-503 | 19 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| linkedin | blocked | 15 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| osm | http-406 | 14 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 13 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
