# Jewelry retail lead run — REPORT

Generated 2026-10-13T22:40:33+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 8970 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 6607 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 165 |
| Qualification rate | 2.5% |
| Websites crawled OK / attempted | 4985 / 5961 |
| Listings with an owner/decision-maker name | 1103 |
| LinkedIn searches by outcome | ambiguous: 1, match: 17, none: 106, reject: 6 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 6607 (100.0%) | 165 (100.0%) |
| 2 | Segment | 6607 (100.0%) | 165 (100.0%) |
| 3 | Category (as listed) | 6598 (99.9%) | 165 (100.0%) |
| 4 | Phone | 6157 (93.2%) | 162 (98.2%) |
| 5 | Email | 1457 (22.1%) | 164 (99.4%) |
| 6 | LinkedIn Profile | 13 (0.2%) | 8 (4.8%) |
| 7 | Contact Person | 504 (7.6%) | 62 (37.6%) |
| 8 | Role | 504 (7.6%) | 62 (37.6%) |
| 9 | Website | 4934 (74.7%) | 165 (100.0%) |
| 10 | Address | 6337 (95.9%) | 164 (99.4%) |
| 11 | Real City | 5518 (83.5%) | 145 (87.9%) |
| 12 | Real State | 5613 (85.0%) | 144 (87.3%) |
| 13 | Market | 6607 (100.0%) | 165 (100.0%) |
| 14 | Lead Origin | 6607 (100.0%) | 165 (100.0%) |
| 15 | Rating | 1618 (24.5%) | 72 (43.6%) |
| 16 | Reviews | 1618 (24.5%) | 72 (43.6%) |
| 17 | Source | 6607 (100.0%) | 165 (100.0%) |
| 18 | Signals | 6607 (100.0%) | 165 (100.0%) |
| 19 | Match Type | 6607 (100.0%) | 165 (100.0%) |
| 20 | Email Source | 1457 (22.1%) | 164 (99.4%) |
| 21 | LinkedIn Source | 13 (0.2%) | 8 (4.8%) |
| 22 | Found At | 6607 (100.0%) | 165 (100.0%) |
| 23 | Also Listed As | 761 (11.5%) | 41 (24.8%) |
| 24 | Other Markets | 56 (0.8%) | 3 (1.8%) |
| 25 | Merged Listings | 1286 (19.5%) | 65 (39.4%) |
| 26 | Flags | 756 (11.4%) | 28 (17.0%) |
| 27 | Mobile Candidates | 208 (3.1%) | 160 (97.0%) |
| 28 | Socials | 1387 (21.0%) | 142 (86.1%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1457 | 22.1% |
| linkedin | 13 | 0.2% |
| direct-line | 208 | 3.1% |
| role-email | 693 | 10.5% |
| gia | 391 | 5.9% |
| ags | 45 | 0.7% |
| ja | 27 | 0.4% |
| bench | 194 | 2.9% |
| custom-design | 936 | 14.2% |
| since-yyyy | 926 | 14.0% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1443 | 1227 | 283 | 97 | 3 | 29 |
| Los Angeles, CA | 1280 | 1055 | 243 | 79 | 2 | 28 |
| Chicago, IL | 993 | 683 | 152 | 60 | 2 | 15 |
| Houston, TX | 1030 | 707 | 145 | 57 | 4 | 22 |
| Dallas, TX | 722 | 490 | 91 | 57 | 1 | 5 |
| Miami, FL | 1024 | 731 | 163 | 69 | 1 | 32 |
| Atlanta, GA | 692 | 500 | 107 | 40 | 0 | 11 |
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
| BBB | 761 | 442 | 29 |
| OpenStreetMap | 891 | 587 | 12 |

Discovery tasks completed: bbb=189, gmaps=50, osm=10, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 31 | 0 | 0 | 31 |
| beads-craft | 237 | 22 | 2 | 261 |
| chain | 1399 | 0 | 0 | 1399 |
| coin-currency | 56 | 2 | 0 | 58 |
| costume-fashion | 185 | 84 | 10 | 279 |
| diamond-trade | 101 | 27 | 4 | 132 |
| gold-buyer | 110 | 19 | 1 | 130 |
| kiosk-battery | 5 | 0 | 0 | 5 |
| no-segment | 0 | 0 | 265 | 265 |
| pawn | 283 | 19 | 13 | 315 |
| piercing-tattoo | 196 | 16 | 3 | 215 |
| simulants | 5 | 19 | 2 | 26 |
| thrift-consignment | 7 | 0 | 0 | 7 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 57 | 7 | 0 | 64 |
| **all** | | | | **3188** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1325 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
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
