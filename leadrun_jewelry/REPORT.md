# Jewelry retail lead run — REPORT

Generated 2026-10-14T06:01:18+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 16013 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10879 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 320 |
| Qualification rate | 2.9% |
| Websites crawled OK / attempted | 8610 / 10353 |
| Listings with an owner/decision-maker name | 2499 |
| LinkedIn searches by outcome | ambiguous: 117, match: 78, none: 291, reject: 29 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10879 (100.0%) | 320 (100.0%) |
| 2 | Segment | 10879 (100.0%) | 320 (100.0%) |
| 3 | Category (as listed) | 10857 (99.8%) | 320 (100.0%) |
| 4 | Phone | 10187 (93.6%) | 314 (98.1%) |
| 5 | Email | 2539 (23.3%) | 314 (98.1%) |
| 6 | LinkedIn Profile | 69 (0.6%) | 63 (19.7%) |
| 7 | Contact Person | 1222 (11.2%) | 156 (48.8%) |
| 8 | Role | 1222 (11.2%) | 156 (48.8%) |
| 9 | Website | 8335 (76.6%) | 320 (100.0%) |
| 10 | Address | 10432 (95.9%) | 317 (99.1%) |
| 11 | Real City | 9053 (83.2%) | 272 (85.0%) |
| 12 | Real State | 9149 (84.1%) | 271 (84.7%) |
| 13 | Market | 10879 (100.0%) | 320 (100.0%) |
| 14 | Lead Origin | 10879 (100.0%) | 320 (100.0%) |
| 15 | Rating | 3035 (27.9%) | 168 (52.5%) |
| 16 | Reviews | 3035 (27.9%) | 168 (52.5%) |
| 17 | Source | 10879 (100.0%) | 320 (100.0%) |
| 18 | Signals | 10879 (100.0%) | 320 (100.0%) |
| 19 | Match Type | 10879 (100.0%) | 320 (100.0%) |
| 20 | Email Source | 2539 (23.3%) | 314 (98.1%) |
| 21 | LinkedIn Source | 69 (0.6%) | 63 (19.7%) |
| 22 | Found At | 10879 (100.0%) | 320 (100.0%) |
| 23 | Also Listed As | 1377 (12.7%) | 89 (27.8%) |
| 24 | Other Markets | 240 (2.2%) | 25 (7.8%) |
| 25 | Merged Listings | 2445 (22.5%) | 138 (43.1%) |
| 26 | Flags | 1401 (12.9%) | 61 (19.1%) |
| 27 | Mobile Candidates | 359 (3.3%) | 266 (83.1%) |
| 28 | Socials | 2494 (22.9%) | 279 (87.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2539 | 23.3% |
| linkedin | 69 | 0.6% |
| direct-line | 359 | 3.3% |
| role-email | 1113 | 10.2% |
| gia | 673 | 6.2% |
| ags | 80 | 0.7% |
| ja | 46 | 0.4% |
| bench | 402 | 3.7% |
| custom-design | 1755 | 16.1% |
| since-yyyy | 2079 | 19.1% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1227 | 282 | 97 | 10 | 35 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 7 | 30 |
| Chicago, IL | 993 | 688 | 154 | 65 | 4 | 18 |
| Houston, TX | 1030 | 701 | 145 | 58 | 5 | 22 |
| Dallas, TX | 722 | 488 | 91 | 58 | 4 | 9 |
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
| Detroit, MI | 554 | 383 | 83 | 53 | 0 | 13 |
| Minneapolis, MN | 531 | 245 | 62 | 92 | 0 | 3 |
| Charlotte, NC | 315 | 193 | 44 | 27 | 0 | 3 |
| Nashville, TN | 234 | 143 | 38 | 11 | 2 | 2 |
| Scottsdale, AZ | 184 | 117 | 31 | 6 | 1 | 5 |
| Naples, FL | 239 | 139 | 40 | 13 | 0 | 4 |
| Greenwich, CT | 136 | 78 | 23 | 5 | 1 | 5 |
| Palm Beach, FL | 401 | 243 | 61 | 9 | 1 | 7 |
| Beverly Hills, CA | 586 | 442 | 106 | 20 | 0 | 12 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1940 | 115 |
| YellowPages | 9439 | 7075 | 114 |
| BBB | 2153 | 1103 | 77 |
| OpenStreetMap | 1313 | 761 | 14 |

Discovery tasks completed: bbb=550, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 64 | 0 | 35 | 99 |
| beads-craft | 429 | 34 | 3 | 466 |
| chain | 2934 | 0 | 0 | 2934 |
| coin-currency | 160 | 8 | 0 | 168 |
| costume-fashion | 369 | 140 | 32 | 541 |
| diamond-trade | 133 | 31 | 7 | 171 |
| gold-buyer | 213 | 37 | 10 | 260 |
| kiosk-battery | 9 | 0 | 0 | 9 |
| no-segment | 0 | 0 | 721 | 721 |
| pawn | 624 | 39 | 14 | 677 |
| piercing-tattoo | 506 | 41 | 12 | 559 |
| simulants | 6 | 35 | 2 | 43 |
| thrift-consignment | 46 | 0 | 0 | 46 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 78 | 8 | 1 | 87 |
| **all** | | | | **6784** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1973 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 158 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 9 | http-429 or challenge page at https://www.google.com/search?q=%22Anthony+Pampillonia%22+Dallas+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
