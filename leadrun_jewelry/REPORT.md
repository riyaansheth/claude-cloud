# Jewelry retail lead run — REPORT

Generated 2026-10-13T23:35:27+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 9186 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 6737 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 173 |
| Qualification rate | 2.6% |
| Websites crawled OK / attempted | 5101 / 6084 |
| Listings with an owner/decision-maker name | 1241 |
| LinkedIn searches by outcome | ambiguous: 21, match: 22, none: 140, reject: 6 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 6737 (100.0%) | 173 (100.0%) |
| 2 | Segment | 6737 (100.0%) | 173 (100.0%) |
| 3 | Category (as listed) | 6724 (99.8%) | 173 (100.0%) |
| 4 | Phone | 6281 (93.2%) | 170 (98.3%) |
| 5 | Email | 1506 (22.4%) | 172 (99.4%) |
| 6 | LinkedIn Profile | 16 (0.2%) | 10 (5.8%) |
| 7 | Contact Person | 573 (8.5%) | 70 (40.5%) |
| 8 | Role | 573 (8.5%) | 70 (40.5%) |
| 9 | Website | 5070 (75.3%) | 173 (100.0%) |
| 10 | Address | 6463 (95.9%) | 172 (99.4%) |
| 11 | Real City | 5603 (83.2%) | 153 (88.4%) |
| 12 | Real State | 5698 (84.6%) | 152 (87.9%) |
| 13 | Market | 6737 (100.0%) | 173 (100.0%) |
| 14 | Lead Origin | 6737 (100.0%) | 173 (100.0%) |
| 15 | Rating | 1662 (24.7%) | 71 (41.0%) |
| 16 | Reviews | 1662 (24.7%) | 71 (41.0%) |
| 17 | Source | 6737 (100.0%) | 173 (100.0%) |
| 18 | Signals | 6737 (100.0%) | 173 (100.0%) |
| 19 | Match Type | 6737 (100.0%) | 173 (100.0%) |
| 20 | Email Source | 1506 (22.4%) | 172 (99.4%) |
| 21 | LinkedIn Source | 16 (0.2%) | 10 (5.8%) |
| 22 | Found At | 6737 (100.0%) | 173 (100.0%) |
| 23 | Also Listed As | 773 (11.5%) | 41 (23.7%) |
| 24 | Other Markets | 58 (0.9%) | 3 (1.7%) |
| 25 | Merged Listings | 1315 (19.5%) | 67 (38.7%) |
| 26 | Flags | 768 (11.4%) | 28 (16.2%) |
| 27 | Mobile Candidates | 221 (3.3%) | 167 (96.5%) |
| 28 | Socials | 1456 (21.6%) | 150 (86.7%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1506 | 22.4% |
| linkedin | 16 | 0.2% |
| direct-line | 221 | 3.3% |
| role-email | 711 | 10.6% |
| gia | 415 | 6.2% |
| ags | 49 | 0.7% |
| ja | 34 | 0.5% |
| bench | 210 | 3.1% |
| custom-design | 992 | 14.7% |
| since-yyyy | 1024 | 15.2% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1443 | 1227 | 283 | 97 | 3 | 29 |
| Los Angeles, CA | 1280 | 1055 | 243 | 79 | 2 | 28 |
| Chicago, IL | 993 | 683 | 152 | 60 | 2 | 15 |
| Houston, TX | 1030 | 707 | 145 | 57 | 4 | 22 |
| Dallas, TX | 722 | 490 | 91 | 57 | 1 | 5 |
| Miami, FL | 1024 | 731 | 163 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 527 | 129 | 61 | 2 | 15 |
| Philadelphia, PA | 767 | 547 | 92 | 26 | 0 | 11 |
| San Francisco, CA | 671 | 430 | 121 | 49 | 0 | 7 |
| Boston, MA | 465 | 294 | 87 | 18 | 0 | 9 |
| Seattle, WA | 53 | 46 | 0 | 0 | 0 | 0 |
| Las Vegas, NV | 0 | 0 | 0 | 0 | 0 | 0 |
| Phoenix, AZ | 0 | 0 | 0 | 0 | 0 | 0 |
| San Diego, CA | 0 | 0 | 0 | 0 | 0 | 0 |
| Denver, CO | 0 | 0 | 0 | 0 | 0 | 0 |
| Washington, DC | 0 | 0 | 0 | 0 | 0 | 0 |
| Detroit, MI | 0 | 0 | 0 | 0 | 0 | 0 |
| Minneapolis, MN | 0 | 0 | 0 | 0 | 0 | 0 |
| Charlotte, NC | 0 | 0 | 0 | 0 | 0 | 0 |
| Nashville, TN | 0 | 0 | 0 | 0 | 0 | 0 |
| Scottsdale, AZ | 0 | 0 | 0 | 0 | 0 | 0 |
| Naples, FL | 0 | 0 | 0 | 0 | 0 | 0 |
| Greenwich, CT | 0 | 0 | 0 | 0 | 0 | 0 |
| Palm Beach, FL | 0 | 0 | 0 | 0 | 0 | 0 |
| Beverly Hills, CA | 0 | 0 | 0 | 0 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 1542 | 946 | 46 |
| YellowPages | 5829 | 4671 | 77 |
| BBB | 925 | 533 | 38 |
| OpenStreetMap | 891 | 587 | 12 |

Discovery tasks completed: bbb=250, gmaps=50, osm=10, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 31 | 0 | 0 | 31 |
| beads-craft | 238 | 22 | 2 | 262 |
| chain | 1518 | 0 | 0 | 1518 |
| coin-currency | 56 | 2 | 0 | 58 |
| costume-fashion | 186 | 89 | 10 | 285 |
| diamond-trade | 101 | 27 | 4 | 132 |
| gold-buyer | 116 | 19 | 1 | 136 |
| kiosk-battery | 5 | 0 | 0 | 5 |
| no-segment | 0 | 0 | 286 | 286 |
| pawn | 287 | 19 | 13 | 319 |
| piercing-tattoo | 236 | 17 | 3 | 256 |
| simulants | 5 | 19 | 2 | 26 |
| thrift-consignment | 7 | 0 | 0 | 7 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 57 | 7 | 0 | 64 |
| **all** | | | | **3386** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1355 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 76 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 21 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 3 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 2 | https://overpass.kumi.systems/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| linkedin | blocked | 1 | http-429 or challenge page at https://www.google.com/search?q=%22David+Leonard%22+San+Luis+Obispo+linkedin&hl=en&num=10 |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
