# Jewelry retail lead run — REPORT

Generated 2026-10-14T06:41:43+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 16181 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10953 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 328 |
| Qualification rate | 3.0% |
| Websites crawled OK / attempted | 8653 / 10407 |
| Listings with an owner/decision-maker name | 2630 |
| LinkedIn searches by outcome | ambiguous: 129, match: 87, none: 310, reject: 30 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10953 (100.0%) | 328 (100.0%) |
| 2 | Segment | 10953 (100.0%) | 328 (100.0%) |
| 3 | Category (as listed) | 10930 (99.8%) | 328 (100.0%) |
| 4 | Phone | 10257 (93.6%) | 322 (98.2%) |
| 5 | Email | 2548 (23.3%) | 321 (97.9%) |
| 6 | LinkedIn Profile | 78 (0.7%) | 72 (22.0%) |
| 7 | Contact Person | 1290 (11.8%) | 166 (50.6%) |
| 8 | Role | 1290 (11.8%) | 166 (50.6%) |
| 9 | Website | 8386 (76.6%) | 328 (100.0%) |
| 10 | Address | 10504 (95.9%) | 325 (99.1%) |
| 11 | Real City | 9131 (83.4%) | 282 (86.0%) |
| 12 | Real State | 9227 (84.2%) | 281 (85.7%) |
| 13 | Market | 10953 (100.0%) | 328 (100.0%) |
| 14 | Lead Origin | 10953 (100.0%) | 328 (100.0%) |
| 15 | Rating | 3035 (27.7%) | 171 (52.1%) |
| 16 | Reviews | 3035 (27.7%) | 171 (52.1%) |
| 17 | Source | 10953 (100.0%) | 328 (100.0%) |
| 18 | Signals | 10953 (100.0%) | 328 (100.0%) |
| 19 | Match Type | 10953 (100.0%) | 328 (100.0%) |
| 20 | Email Source | 2548 (23.3%) | 321 (97.9%) |
| 21 | LinkedIn Source | 78 (0.7%) | 72 (22.0%) |
| 22 | Found At | 10953 (100.0%) | 328 (100.0%) |
| 23 | Also Listed As | 1395 (12.7%) | 94 (28.7%) |
| 24 | Other Markets | 243 (2.2%) | 26 (7.9%) |
| 25 | Merged Listings | 2473 (22.6%) | 146 (44.5%) |
| 26 | Flags | 1416 (12.9%) | 61 (18.6%) |
| 27 | Mobile Candidates | 359 (3.3%) | 265 (80.8%) |
| 28 | Socials | 2513 (22.9%) | 286 (87.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2548 | 23.3% |
| linkedin | 78 | 0.7% |
| direct-line | 359 | 3.3% |
| role-email | 1116 | 10.2% |
| gia | 682 | 6.2% |
| ags | 81 | 0.7% |
| ja | 47 | 0.4% |
| bench | 409 | 3.7% |
| custom-design | 1776 | 16.2% |
| since-yyyy | 2166 | 19.8% |

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
| Phoenix, AZ | 730 | 468 | 95 | 55 | 0 | 12 |
| San Diego, CA | 591 | 381 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 382 | 226 | 76 | 33 | 1 | 6 |
| Detroit, MI | 554 | 382 | 82 | 53 | 5 | 17 |
| Minneapolis, MN | 531 | 245 | 62 | 92 | 4 | 7 |
| Charlotte, NC | 350 | 211 | 48 | 41 | 0 | 3 |
| Nashville, TN | 342 | 189 | 44 | 55 | 2 | 2 |
| Scottsdale, AZ | 209 | 129 | 31 | 15 | 1 | 5 |
| Naples, FL | 239 | 139 | 40 | 13 | 0 | 4 |
| Greenwich, CT | 136 | 78 | 23 | 5 | 1 | 5 |
| Palm Beach, FL | 401 | 243 | 61 | 9 | 1 | 7 |
| Beverly Hills, CA | 586 | 442 | 106 | 20 | 0 | 12 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1934 | 113 |
| YellowPages | 9439 | 7066 | 114 |
| BBB | 2321 | 1194 | 87 |
| OpenStreetMap | 1313 | 759 | 14 |

Discovery tasks completed: bbb=609, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 64 | 0 | 35 | 99 |
| beads-craft | 429 | 34 | 3 | 466 |
| chain | 3008 | 0 | 0 | 3008 |
| coin-currency | 168 | 8 | 0 | 176 |
| costume-fashion | 370 | 142 | 32 | 544 |
| diamond-trade | 135 | 31 | 7 | 173 |
| gold-buyer | 214 | 37 | 10 | 261 |
| kiosk-battery | 9 | 0 | 0 | 9 |
| no-segment | 0 | 0 | 736 | 736 |
| pawn | 633 | 41 | 15 | 689 |
| piercing-tattoo | 517 | 41 | 12 | 570 |
| simulants | 6 | 35 | 2 | 43 |
| thrift-consignment | 49 | 0 | 0 | 49 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 78 | 8 | 1 | 87 |
| **all** | | | | **6913** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 2063 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 168 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 10 | http-429 or challenge page at https://www.google.com/search?q=%22Anthony+Pampillonia%22+Dallas+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
