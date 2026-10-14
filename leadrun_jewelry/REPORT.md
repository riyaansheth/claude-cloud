# Jewelry retail lead run — REPORT

Generated 2026-10-14T10:11:45+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 16357 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 11025 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 353 |
| Qualification rate | 3.2% |
| Websites crawled OK / attempted | 8730 / 10516 |
| Listings with an owner/decision-maker name | 2747 |
| LinkedIn searches by outcome | ambiguous: 182, match: 110, none: 383, reject: 44 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 11025 (100.0%) | 353 (100.0%) |
| 2 | Segment | 11025 (100.0%) | 353 (100.0%) |
| 3 | Category (as listed) | 11002 (99.8%) | 353 (100.0%) |
| 4 | Phone | 10318 (93.6%) | 347 (98.3%) |
| 5 | Email | 2574 (23.3%) | 344 (97.5%) |
| 6 | LinkedIn Profile | 101 (0.9%) | 95 (26.9%) |
| 7 | Contact Person | 1337 (12.1%) | 194 (55.0%) |
| 8 | Role | 1337 (12.1%) | 194 (55.0%) |
| 9 | Website | 8435 (76.5%) | 353 (100.0%) |
| 10 | Address | 10567 (95.8%) | 350 (99.2%) |
| 11 | Real City | 9197 (83.4%) | 306 (86.7%) |
| 12 | Real State | 9293 (84.3%) | 305 (86.4%) |
| 13 | Market | 11025 (100.0%) | 353 (100.0%) |
| 14 | Lead Origin | 11025 (100.0%) | 353 (100.0%) |
| 15 | Rating | 3036 (27.5%) | 179 (50.7%) |
| 16 | Reviews | 3036 (27.5%) | 179 (50.7%) |
| 17 | Source | 11025 (100.0%) | 353 (100.0%) |
| 18 | Signals | 11025 (100.0%) | 353 (100.0%) |
| 19 | Match Type | 11025 (100.0%) | 353 (100.0%) |
| 20 | Email Source | 2574 (23.3%) | 344 (97.5%) |
| 21 | LinkedIn Source | 101 (0.9%) | 95 (26.9%) |
| 22 | Found At | 11025 (100.0%) | 353 (100.0%) |
| 23 | Also Listed As | 1415 (12.8%) | 99 (28.0%) |
| 24 | Other Markets | 251 (2.3%) | 27 (7.6%) |
| 25 | Merged Listings | 2503 (22.7%) | 158 (44.8%) |
| 26 | Flags | 1456 (13.2%) | 69 (19.5%) |
| 27 | Mobile Candidates | 362 (3.3%) | 269 (76.2%) |
| 28 | Socials | 2546 (23.1%) | 311 (88.1%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2574 | 23.3% |
| linkedin | 101 | 0.9% |
| direct-line | 362 | 3.3% |
| role-email | 1132 | 10.3% |
| gia | 690 | 6.3% |
| ags | 83 | 0.8% |
| ja | 47 | 0.4% |
| bench | 413 | 3.7% |
| custom-design | 1796 | 16.3% |
| since-yyyy | 2253 | 20.4% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1227 | 282 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1033 | 235 | 78 | 8 | 31 |
| Chicago, IL | 993 | 687 | 154 | 65 | 5 | 19 |
| Houston, TX | 1030 | 701 | 145 | 58 | 5 | 22 |
| Dallas, TX | 722 | 487 | 91 | 59 | 5 | 10 |
| Miami, FL | 1024 | 733 | 165 | 69 | 5 | 34 |
| Atlanta, GA | 739 | 527 | 128 | 62 | 11 | 23 |
| Philadelphia, PA | 767 | 546 | 92 | 28 | 3 | 14 |
| San Francisco, CA | 732 | 447 | 125 | 67 | 3 | 11 |
| Boston, MA | 570 | 345 | 109 | 56 | 7 | 18 |
| Seattle, WA | 589 | 349 | 93 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 403 | 75 | 75 | 3 | 12 |
| Phoenix, AZ | 730 | 469 | 95 | 59 | 0 | 12 |
| San Diego, CA | 591 | 381 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 382 | 226 | 76 | 33 | 1 | 6 |
| Detroit, MI | 554 | 382 | 82 | 53 | 6 | 18 |
| Minneapolis, MN | 531 | 245 | 62 | 92 | 6 | 9 |
| Charlotte, NC | 350 | 211 | 48 | 41 | 2 | 5 |
| Nashville, TN | 341 | 189 | 47 | 55 | 4 | 4 |
| Scottsdale, AZ | 263 | 150 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 154 | 45 | 22 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 259 | 67 | 23 | 2 | 9 |
| Beverly Hills, CA | 625 | 458 | 110 | 27 | 1 | 13 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3108 | 1929 | 117 |
| YellowPages | 9439 | 7061 | 122 |
| BBB | 2497 | 1276 | 98 |
| OpenStreetMap | 1313 | 759 | 16 |

Discovery tasks completed: bbb=750, gmaps=125, osm=25, yp=462

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 64 | 0 | 35 | 99 |
| beads-craft | 433 | 34 | 3 | 470 |
| chain | 3078 | 0 | 0 | 3078 |
| coin-currency | 174 | 8 | 0 | 182 |
| costume-fashion | 370 | 144 | 32 | 546 |
| diamond-trade | 135 | 31 | 7 | 173 |
| gold-buyer | 215 | 38 | 11 | 264 |
| kiosk-battery | 9 | 0 | 0 | 9 |
| no-segment | 0 | 0 | 755 | 755 |
| pawn | 636 | 41 | 15 | 692 |
| piercing-tattoo | 537 | 42 | 12 | 591 |
| simulants | 6 | 35 | 4 | 45 |
| thrift-consignment | 49 | 0 | 0 | 49 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 78 | 8 | 1 | 87 |
| **all** | | | | **7043** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 2484 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 181 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 32 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| linkedin | blocked | 14 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 11 | https://overpass-api.de/api/interpreter |
| yp | soft-block-503 | 4 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Denver%2C+CO&page=11 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
