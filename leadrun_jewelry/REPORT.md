# Jewelry retail lead run — REPORT

Generated 2026-10-14T07:15:55+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 16271 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10990 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 334 |
| Qualification rate | 3.0% |
| Websites crawled OK / attempted | 8704 / 10484 |
| Listings with an owner/decision-maker name | 2705 |
| LinkedIn searches by outcome | ambiguous: 137, match: 92, none: 322, reject: 31 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10990 (100.0%) | 334 (100.0%) |
| 2 | Segment | 10990 (100.0%) | 334 (100.0%) |
| 3 | Category (as listed) | 10967 (99.8%) | 334 (100.0%) |
| 4 | Phone | 10290 (93.6%) | 328 (98.2%) |
| 5 | Email | 2561 (23.3%) | 326 (97.6%) |
| 6 | LinkedIn Profile | 83 (0.8%) | 77 (23.1%) |
| 7 | Contact Person | 1313 (11.9%) | 173 (51.8%) |
| 8 | Role | 1313 (11.9%) | 173 (51.8%) |
| 9 | Website | 8412 (76.5%) | 334 (100.0%) |
| 10 | Address | 10536 (95.9%) | 331 (99.1%) |
| 11 | Real City | 9163 (83.4%) | 289 (86.5%) |
| 12 | Real State | 9259 (84.2%) | 288 (86.2%) |
| 13 | Market | 10990 (100.0%) | 334 (100.0%) |
| 14 | Lead Origin | 10990 (100.0%) | 334 (100.0%) |
| 15 | Rating | 3035 (27.6%) | 172 (51.5%) |
| 16 | Reviews | 3035 (27.6%) | 172 (51.5%) |
| 17 | Source | 10990 (100.0%) | 334 (100.0%) |
| 18 | Signals | 10990 (100.0%) | 334 (100.0%) |
| 19 | Match Type | 10990 (100.0%) | 334 (100.0%) |
| 20 | Email Source | 2561 (23.3%) | 326 (97.6%) |
| 21 | LinkedIn Source | 83 (0.8%) | 77 (23.1%) |
| 22 | Found At | 10990 (100.0%) | 334 (100.0%) |
| 23 | Also Listed As | 1405 (12.8%) | 96 (28.7%) |
| 24 | Other Markets | 249 (2.3%) | 26 (7.8%) |
| 25 | Merged Listings | 2482 (22.6%) | 150 (44.9%) |
| 26 | Flags | 1435 (13.1%) | 63 (18.9%) |
| 27 | Mobile Candidates | 361 (3.3%) | 267 (79.9%) |
| 28 | Socials | 2532 (23.0%) | 292 (87.4%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2561 | 23.3% |
| linkedin | 83 | 0.8% |
| direct-line | 361 | 3.3% |
| role-email | 1123 | 10.2% |
| gia | 687 | 6.3% |
| ags | 82 | 0.7% |
| ja | 47 | 0.4% |
| bench | 412 | 3.7% |
| custom-design | 1791 | 16.3% |
| since-yyyy | 2215 | 20.2% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1227 | 282 | 97 | 10 | 35 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 7 | 30 |
| Chicago, IL | 993 | 688 | 154 | 65 | 4 | 18 |
| Houston, TX | 1030 | 701 | 145 | 58 | 5 | 22 |
| Dallas, TX | 722 | 487 | 91 | 59 | 4 | 9 |
| Miami, FL | 1024 | 734 | 166 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 527 | 128 | 62 | 9 | 21 |
| Philadelphia, PA | 767 | 546 | 92 | 28 | 2 | 13 |
| San Francisco, CA | 732 | 447 | 125 | 67 | 2 | 10 |
| Boston, MA | 570 | 345 | 109 | 55 | 5 | 16 |
| Seattle, WA | 589 | 349 | 93 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 403 | 75 | 75 | 3 | 12 |
| Phoenix, AZ | 730 | 469 | 95 | 59 | 0 | 12 |
| San Diego, CA | 591 | 381 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 382 | 226 | 76 | 33 | 1 | 6 |
| Detroit, MI | 554 | 382 | 82 | 53 | 6 | 18 |
| Minneapolis, MN | 531 | 245 | 62 | 92 | 5 | 8 |
| Charlotte, NC | 350 | 211 | 48 | 41 | 2 | 5 |
| Nashville, TN | 341 | 189 | 47 | 55 | 3 | 3 |
| Scottsdale, AZ | 263 | 150 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 154 | 45 | 22 | 0 | 5 |
| Greenwich, CT | 138 | 78 | 23 | 5 | 1 | 5 |
| Palm Beach, FL | 401 | 243 | 61 | 9 | 1 | 7 |
| Beverly Hills, CA | 586 | 442 | 106 | 20 | 0 | 12 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1929 | 113 |
| YellowPages | 9439 | 7067 | 114 |
| BBB | 2411 | 1235 | 93 |
| OpenStreetMap | 1313 | 759 | 14 |

Discovery tasks completed: bbb=673, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 64 | 0 | 35 | 99 |
| beads-craft | 433 | 34 | 3 | 470 |
| chain | 3055 | 0 | 0 | 3055 |
| coin-currency | 174 | 8 | 0 | 182 |
| costume-fashion | 370 | 143 | 32 | 545 |
| diamond-trade | 135 | 31 | 7 | 173 |
| gold-buyer | 214 | 38 | 10 | 262 |
| kiosk-battery | 9 | 0 | 0 | 9 |
| no-segment | 0 | 0 | 749 | 749 |
| pawn | 634 | 41 | 15 | 690 |
| piercing-tattoo | 531 | 42 | 12 | 585 |
| simulants | 6 | 35 | 3 | 44 |
| thrift-consignment | 49 | 0 | 0 | 49 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 78 | 8 | 1 | 87 |
| **all** | | | | **7002** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 2108 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 178 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 10 | http-429 or challenge page at https://www.google.com/search?q=%22Anthony+Pampillonia%22+Dallas+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
