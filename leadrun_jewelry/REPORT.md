# Jewelry retail lead run — REPORT

Generated 2026-10-13T17:36:26+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 7706 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 6071 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 123 |
| Qualification rate | 2.0% |
| Websites crawled OK / attempted | 4316 / 5176 |
| Listings with an owner/decision-maker name | 652 |
| LinkedIn searches by outcome | — |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 6071 (100.0%) | 123 (100.0%) |
| 2 | Segment | 6071 (100.0%) | 123 (100.0%) |
| 3 | Category (as listed) | 6069 (100.0%) | 123 (100.0%) |
| 4 | Phone | 5625 (92.7%) | 120 (97.6%) |
| 5 | Email | 1135 (18.7%) | 123 (100.0%) |
| 6 | LinkedIn Profile | 0 (0.0%) | 0 (0.0%) |
| 7 | Contact Person | 326 (5.4%) | 24 (19.5%) |
| 8 | Role | 326 (5.4%) | 24 (19.5%) |
| 9 | Website | 4363 (71.9%) | 123 (100.0%) |
| 10 | Address | 5799 (95.5%) | 122 (99.2%) |
| 11 | Real City | 5212 (85.9%) | 113 (91.9%) |
| 12 | Real State | 5310 (87.5%) | 112 (91.1%) |
| 13 | Market | 6071 (100.0%) | 123 (100.0%) |
| 14 | Lead Origin | 6071 (100.0%) | 123 (100.0%) |
| 15 | Rating | 1072 (17.7%) | 44 (35.8%) |
| 16 | Reviews | 1072 (17.7%) | 44 (35.8%) |
| 17 | Source | 6071 (100.0%) | 123 (100.0%) |
| 18 | Signals | 6071 (100.0%) | 123 (100.0%) |
| 19 | Match Type | 6071 (100.0%) | 123 (100.0%) |
| 20 | Email Source | 1135 (18.7%) | 123 (100.0%) |
| 21 | LinkedIn Source | 0 (0.0%) | 0 (0.0%) |
| 22 | Found At | 6071 (100.0%) | 123 (100.0%) |
| 23 | Also Listed As | 554 (9.1%) | 29 (23.6%) |
| 24 | Other Markets | 53 (0.9%) | 2 (1.6%) |
| 25 | Merged Listings | 910 (15.0%) | 41 (33.3%) |
| 26 | Flags | 612 (10.1%) | 14 (11.4%) |
| 27 | Mobile Candidates | 161 (2.7%) | 123 (100.0%) |
| 28 | Socials | 1006 (16.6%) | 105 (85.4%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1135 | 18.7% |
| linkedin | 0 | 0.0% |
| direct-line | 161 | 2.7% |
| role-email | 525 | 8.6% |
| gia | 261 | 4.3% |
| ags | 27 | 0.4% |
| ja | 13 | 0.2% |
| bench | 136 | 2.2% |
| custom-design | 679 | 11.2% |
| since-yyyy | 611 | 10.1% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1411 | 1229 | 231 | 123 | 0 | 20 |
| Los Angeles, CA | 1225 | 1035 | 198 | 100 | 0 | 21 |
| Chicago, IL | 870 | 648 | 133 | 25 | 0 | 12 |
| Houston, TX | 873 | 660 | 128 | 16 | 0 | 20 |
| Dallas, TX | 547 | 440 | 69 | 13 | 0 | 4 |
| Miami, FL | 676 | 559 | 93 | 10 | 0 | 15 |
| Atlanta, GA | 505 | 410 | 78 | 11 | 0 | 8 |
| Philadelphia, PA | 575 | 484 | 55 | 7 | 0 | 7 |
| San Francisco, CA | 446 | 350 | 80 | 10 | 0 | 8 |
| Boston, MA | 324 | 256 | 70 | 11 | 0 | 8 |
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
| Google Maps | 802 | 567 | 25 |
| YellowPages | 5579 | 4720 | 86 |
| BBB | 221 | 172 | 0 |
| OpenStreetMap | 850 | 612 | 12 |

Discovery tasks completed: bbb=60, gmaps=22, osm=10, yp=247

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 24 | 0 | 0 | 24 |
| beads-craft | 227 | 18 | 1 | 246 |
| chain | 913 | 0 | 111 | 1024 |
| coin-currency | 33 | 1 | 0 | 34 |
| costume-fashion | 180 | 73 | 3 | 256 |
| diamond-trade | 81 | 21 | 5 | 107 |
| gold-buyer | 65 | 13 | 18 | 96 |
| kiosk-battery | 4 | 0 | 0 | 4 |
| no-segment | 0 | 0 | 283 | 283 |
| pawn | 247 | 15 | 0 | 262 |
| piercing-tattoo | 127 | 10 | 1 | 138 |
| simulants | 5 | 17 | 1 | 23 |
| thrift-consignment | 3 | 0 | 0 | 3 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 52 | 6 | 0 | 58 |
| **all** | | | | **2559** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1215 | bbb:3149c8f046693f3b: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 15 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 10 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 3 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 2 | https://overpass.kumi.systems/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
