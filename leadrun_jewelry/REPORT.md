# Jewelry retail lead run — REPORT

Generated 2026-10-14T04:46:41+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 15608 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 10733 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 306 |
| Qualification rate | 2.9% |
| Websites crawled OK / attempted | 8495 / 10209 |
| Listings with an owner/decision-maker name | 2164 |
| LinkedIn searches by outcome | ambiguous: 100, match: 64, none: 266, reject: 21 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 10733 (100.0%) | 306 (100.0%) |
| 2 | Segment | 10733 (100.0%) | 306 (100.0%) |
| 3 | Category (as listed) | 10712 (99.8%) | 306 (100.0%) |
| 4 | Phone | 10048 (93.6%) | 300 (98.0%) |
| 5 | Email | 2504 (23.3%) | 300 (98.0%) |
| 6 | LinkedIn Profile | 58 (0.5%) | 52 (17.0%) |
| 7 | Contact Person | 1083 (10.1%) | 144 (47.1%) |
| 8 | Role | 1083 (10.1%) | 144 (47.1%) |
| 9 | Website | 8235 (76.7%) | 306 (100.0%) |
| 10 | Address | 10289 (95.9%) | 304 (99.3%) |
| 11 | Real City | 8897 (82.9%) | 263 (85.9%) |
| 12 | Real State | 8993 (83.8%) | 262 (85.6%) |
| 13 | Market | 10733 (100.0%) | 306 (100.0%) |
| 14 | Lead Origin | 10733 (100.0%) | 306 (100.0%) |
| 15 | Rating | 3036 (28.3%) | 157 (51.3%) |
| 16 | Reviews | 3036 (28.3%) | 157 (51.3%) |
| 17 | Source | 10733 (100.0%) | 306 (100.0%) |
| 18 | Signals | 10733 (100.0%) | 306 (100.0%) |
| 19 | Match Type | 10733 (100.0%) | 306 (100.0%) |
| 20 | Email Source | 2504 (23.3%) | 300 (98.0%) |
| 21 | LinkedIn Source | 58 (0.5%) | 52 (17.0%) |
| 22 | Found At | 10733 (100.0%) | 306 (100.0%) |
| 23 | Also Listed As | 1351 (12.6%) | 85 (27.8%) |
| 24 | Other Markets | 240 (2.2%) | 24 (7.8%) |
| 25 | Merged Listings | 2326 (21.7%) | 133 (43.5%) |
| 26 | Flags | 1372 (12.8%) | 58 (19.0%) |
| 27 | Mobile Candidates | 354 (3.3%) | 263 (85.9%) |
| 28 | Socials | 2428 (22.6%) | 267 (87.3%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2504 | 23.3% |
| linkedin | 58 | 0.5% |
| direct-line | 354 | 3.3% |
| role-email | 1096 | 10.2% |
| gia | 648 | 6.0% |
| ags | 74 | 0.7% |
| ja | 44 | 0.4% |
| bench | 383 | 3.6% |
| custom-design | 1699 | 15.8% |
| since-yyyy | 1904 | 17.7% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1227 | 282 | 97 | 9 | 34 |
| Los Angeles, CA | 1280 | 1032 | 235 | 77 | 7 | 30 |
| Chicago, IL | 993 | 688 | 154 | 64 | 3 | 17 |
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
| San Diego, CA | 591 | 381 | 80 | 33 | 1 | 6 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 383 | 227 | 71 | 32 | 1 | 6 |
| Detroit, MI | 464 | 329 | 65 | 11 | 0 | 11 |
| Minneapolis, MN | 250 | 165 | 50 | 11 | 0 | 2 |
| Charlotte, NC | 282 | 180 | 44 | 13 | 0 | 3 |
| Nashville, TN | 234 | 143 | 38 | 11 | 1 | 1 |
| Scottsdale, AZ | 184 | 117 | 31 | 6 | 0 | 4 |
| Naples, FL | 239 | 139 | 40 | 13 | 0 | 4 |
| Greenwich, CT | 136 | 78 | 23 | 5 | 0 | 4 |
| Palm Beach, FL | 401 | 243 | 61 | 9 | 0 | 6 |
| Beverly Hills, CA | 586 | 442 | 106 | 20 | 0 | 12 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1953 | 104 |
| YellowPages | 9439 | 7081 | 114 |
| BBB | 1750 | 937 | 74 |
| OpenStreetMap | 1313 | 762 | 14 |

Discovery tasks completed: bbb=480, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 64 | 0 | 33 | 97 |
| beads-craft | 423 | 34 | 3 | 460 |
| chain | 2733 | 0 | 0 | 2733 |
| coin-currency | 150 | 7 | 0 | 157 |
| costume-fashion | 369 | 137 | 31 | 537 |
| diamond-trade | 133 | 29 | 7 | 169 |
| gold-buyer | 206 | 36 | 9 | 251 |
| kiosk-battery | 7 | 0 | 0 | 7 |
| no-segment | 0 | 0 | 703 | 703 |
| pawn | 617 | 37 | 14 | 668 |
| piercing-tattoo | 474 | 37 | 12 | 523 |
| simulants | 6 | 35 | 2 | 43 |
| thrift-consignment | 44 | 0 | 0 | 44 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 74 | 8 | 1 | 83 |
| **all** | | | | **6478** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1840 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 145 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 8 | http-429 or challenge page at https://www.google.com/search?q=%22Anthony+Pampillonia%22+Dallas+linkedin&hl=en&num=10 |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
