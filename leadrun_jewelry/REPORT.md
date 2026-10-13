# Jewelry retail lead run — REPORT

Generated 2026-10-13T22:36:20+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 8950 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 6593 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 161 |
| Qualification rate | 2.4% |
| Websites crawled OK / attempted | 4948 / 5912 |
| Listings with an owner/decision-maker name | 1080 |
| LinkedIn searches by outcome | ambiguous: 1, match: 17, none: 106, reject: 6 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 6593 (100.0%) | 161 (100.0%) |
| 2 | Segment | 6593 (100.0%) | 161 (100.0%) |
| 3 | Category (as listed) | 6584 (99.9%) | 161 (100.0%) |
| 4 | Phone | 6143 (93.2%) | 158 (98.1%) |
| 5 | Email | 1435 (21.8%) | 161 (100.0%) |
| 6 | LinkedIn Profile | 13 (0.2%) | 6 (3.7%) |
| 7 | Contact Person | 492 (7.5%) | 58 (36.0%) |
| 8 | Role | 492 (7.5%) | 58 (36.0%) |
| 9 | Website | 4935 (74.9%) | 161 (100.0%) |
| 10 | Address | 6323 (95.9%) | 160 (99.4%) |
| 11 | Real City | 5504 (83.5%) | 141 (87.6%) |
| 12 | Real State | 5599 (84.9%) | 140 (87.0%) |
| 13 | Market | 6593 (100.0%) | 161 (100.0%) |
| 14 | Lead Origin | 6593 (100.0%) | 161 (100.0%) |
| 15 | Rating | 1618 (24.5%) | 72 (44.7%) |
| 16 | Reviews | 1618 (24.5%) | 72 (44.7%) |
| 17 | Source | 6593 (100.0%) | 161 (100.0%) |
| 18 | Signals | 6593 (100.0%) | 161 (100.0%) |
| 19 | Match Type | 6593 (100.0%) | 161 (100.0%) |
| 20 | Email Source | 1435 (21.8%) | 161 (100.0%) |
| 21 | LinkedIn Source | 13 (0.2%) | 6 (3.7%) |
| 22 | Found At | 6593 (100.0%) | 161 (100.0%) |
| 23 | Also Listed As | 761 (11.5%) | 41 (25.5%) |
| 24 | Other Markets | 56 (0.8%) | 3 (1.9%) |
| 25 | Merged Listings | 1281 (19.4%) | 63 (39.1%) |
| 26 | Flags | 755 (11.5%) | 27 (16.8%) |
| 27 | Mobile Candidates | 204 (3.1%) | 156 (96.9%) |
| 28 | Socials | 1360 (20.6%) | 138 (85.7%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1435 | 21.8% |
| linkedin | 13 | 0.2% |
| direct-line | 204 | 3.1% |
| role-email | 682 | 10.3% |
| gia | 377 | 5.7% |
| ags | 39 | 0.6% |
| ja | 24 | 0.4% |
| bench | 188 | 2.9% |
| custom-design | 916 | 13.9% |
| since-yyyy | 912 | 13.8% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1443 | 1227 | 276 | 97 | 3 | 28 |
| Los Angeles, CA | 1282 | 1056 | 238 | 79 | 2 | 28 |
| Chicago, IL | 993 | 683 | 149 | 60 | 2 | 13 |
| Houston, TX | 1030 | 707 | 143 | 57 | 4 | 22 |
| Dallas, TX | 722 | 490 | 89 | 57 | 1 | 5 |
| Miami, FL | 1025 | 731 | 160 | 69 | 1 | 31 |
| Atlanta, GA | 669 | 485 | 107 | 28 | 0 | 11 |
| Philadelphia, PA | 732 | 530 | 79 | 12 | 0 | 7 |
| San Francisco, CA | 589 | 390 | 107 | 15 | 0 | 7 |
| Boston, MA | 465 | 294 | 87 | 18 | 0 | 9 |
| Seattle, WA | 0 | 0 | 0 | 0 | 0 | 0 |
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
| Google Maps | 1489 | 902 | 46 |
| YellowPages | 5829 | 4676 | 78 |
| BBB | 741 | 428 | 25 |
| OpenStreetMap | 891 | 587 | 12 |

Discovery tasks completed: bbb=187, gmaps=50, osm=10, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 31 | 0 | 0 | 31 |
| beads-craft | 237 | 22 | 2 | 261 |
| chain | 1389 | 0 | 0 | 1389 |
| coin-currency | 56 | 2 | 0 | 58 |
| costume-fashion | 185 | 84 | 10 | 279 |
| diamond-trade | 100 | 27 | 4 | 131 |
| gold-buyer | 110 | 19 | 1 | 130 |
| kiosk-battery | 5 | 0 | 0 | 5 |
| no-segment | 0 | 0 | 259 | 259 |
| pawn | 281 | 19 | 13 | 313 |
| piercing-tattoo | 195 | 14 | 3 | 212 |
| simulants | 5 | 18 | 2 | 25 |
| thrift-consignment | 6 | 0 | 0 | 6 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 57 | 7 | 0 | 64 |
| **all** | | | | **3164** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1310 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 63 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 20 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 3 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 2 | https://overpass.kumi.systems/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| linkedin | blocked | 1 | http-429 or challenge page at https://www.google.com/search?q=%22David+Leonard%22+San+Luis+Obispo+linkedin&hl=en&num=10 |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
