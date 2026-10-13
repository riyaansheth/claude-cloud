# Jewelry retail lead run — REPORT

Generated 2026-10-14T05:20:50+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 15757 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10793 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 311 |
| Qualification rate | 2.9% |
| Websites crawled OK / attempted | 8575 / 10297 |
| Listings with an owner/decision-maker name | 2292 |
| LinkedIn searches by outcome | ambiguous: 107, match: 67, none: 282, reject: 23 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10793 (100.0%) | 311 (100.0%) |
| 2 | Segment | 10793 (100.0%) | 311 (100.0%) |
| 3 | Category (as listed) | 10771 (99.8%) | 311 (100.0%) |
| 4 | Phone | 10108 (93.7%) | 305 (98.1%) |
| 5 | Email | 2530 (23.4%) | 305 (98.1%) |
| 6 | LinkedIn Profile | 61 (0.6%) | 55 (17.7%) |
| 7 | Contact Person | 1145 (10.6%) | 147 (47.3%) |
| 8 | Role | 1145 (10.6%) | 147 (47.3%) |
| 9 | Website | 8289 (76.8%) | 311 (100.0%) |
| 10 | Address | 10348 (95.9%) | 308 (99.0%) |
| 11 | Real City | 8961 (83.0%) | 265 (85.2%) |
| 12 | Real State | 9057 (83.9%) | 264 (84.9%) |
| 13 | Market | 10793 (100.0%) | 311 (100.0%) |
| 14 | Lead Origin | 10793 (100.0%) | 311 (100.0%) |
| 15 | Rating | 3035 (28.1%) | 160 (51.4%) |
| 16 | Reviews | 3035 (28.1%) | 160 (51.4%) |
| 17 | Source | 10793 (100.0%) | 311 (100.0%) |
| 18 | Signals | 10793 (100.0%) | 311 (100.0%) |
| 19 | Match Type | 10793 (100.0%) | 311 (100.0%) |
| 20 | Email Source | 2530 (23.4%) | 305 (98.1%) |
| 21 | LinkedIn Source | 61 (0.6%) | 55 (17.7%) |
| 22 | Found At | 10793 (100.0%) | 311 (100.0%) |
| 23 | Also Listed As | 1364 (12.6%) | 86 (27.7%) |
| 24 | Other Markets | 240 (2.2%) | 24 (7.7%) |
| 25 | Merged Listings | 2355 (21.8%) | 133 (42.8%) |
| 26 | Flags | 1389 (12.9%) | 60 (19.3%) |
| 27 | Mobile Candidates | 359 (3.3%) | 265 (85.2%) |
| 28 | Socials | 2480 (23.0%) | 270 (86.8%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2530 | 23.4% |
| linkedin | 61 | 0.6% |
| direct-line | 359 | 3.3% |
| role-email | 1109 | 10.3% |
| gia | 671 | 6.2% |
| ags | 79 | 0.7% |
| ja | 46 | 0.4% |
| bench | 401 | 3.7% |
| custom-design | 1745 | 16.2% |
| since-yyyy | 1978 | 18.3% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1227 | 282 | 97 | 9 | 34 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 7 | 30 |
| Chicago, IL | 993 | 688 | 154 | 65 | 4 | 18 |
| Houston, TX | 1030 | 701 | 145 | 58 | 5 | 22 |
| Dallas, TX | 722 | 488 | 91 | 58 | 4 | 9 |
| Miami, FL | 1024 | 734 | 166 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 527 | 128 | 62 | 8 | 20 |
| Philadelphia, PA | 767 | 546 | 92 | 28 | 2 | 13 |
| San Francisco, CA | 732 | 447 | 125 | 67 | 1 | 9 |
| Boston, MA | 570 | 345 | 109 | 55 | 5 | 16 |
| Seattle, WA | 589 | 349 | 93 | 68 | 1 | 9 |
| Las Vegas, NV | 691 | 403 | 75 | 75 | 3 | 12 |
| Phoenix, AZ | 730 | 468 | 95 | 55 | 0 | 12 |
| San Diego, CA | 591 | 381 | 80 | 33 | 2 | 7 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 382 | 226 | 76 | 33 | 1 | 6 |
| Detroit, MI | 554 | 383 | 83 | 53 | 0 | 13 |
| Minneapolis, MN | 310 | 172 | 53 | 29 | 0 | 2 |
| Charlotte, NC | 282 | 180 | 44 | 13 | 0 | 3 |
| Nashville, TN | 234 | 143 | 38 | 11 | 2 | 2 |
| Scottsdale, AZ | 184 | 117 | 31 | 6 | 0 | 4 |
| Naples, FL | 239 | 139 | 40 | 13 | 0 | 4 |
| Greenwich, CT | 136 | 78 | 23 | 5 | 0 | 4 |
| Palm Beach, FL | 401 | 243 | 61 | 9 | 0 | 6 |
| Beverly Hills, CA | 586 | 442 | 106 | 20 | 0 | 12 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1946 | 107 |
| YellowPages | 9439 | 7078 | 114 |
| BBB | 1899 | 1008 | 76 |
| OpenStreetMap | 1313 | 761 | 14 |

Discovery tasks completed: bbb=514, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 64 | 0 | 33 | 97 |
| beads-craft | 427 | 34 | 3 | 464 |
| chain | 2846 | 0 | 0 | 2846 |
| coin-currency | 157 | 8 | 0 | 165 |
| costume-fashion | 369 | 139 | 32 | 540 |
| diamond-trade | 133 | 29 | 7 | 169 |
| gold-buyer | 210 | 37 | 9 | 256 |
| kiosk-battery | 9 | 0 | 0 | 9 |
| no-segment | 0 | 0 | 714 | 714 |
| pawn | 621 | 37 | 14 | 672 |
| piercing-tattoo | 494 | 39 | 12 | 545 |
| simulants | 6 | 35 | 2 | 43 |
| thrift-consignment | 44 | 0 | 0 | 44 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 74 | 8 | 1 | 83 |
| **all** | | | | **6650** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1884 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 151 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 8 | http-429 or challenge page at https://www.google.com/search?q=%22Anthony+Pampillonia%22+Dallas+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
