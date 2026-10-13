# Jewelry retail lead run — REPORT

Generated 2026-10-13T17:12:36+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 7271 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 5025 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 97 |
| Qualification rate | 1.9% |
| Websites crawled OK / attempted | 2801 / 3220 |
| Listings with an owner/decision-maker name | 503 |
| LinkedIn searches by outcome | — |
| **Shortfall vs 100 qualified** | **3** (not padded) |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 5025 (100.0%) | 97 (100.0%) |
| 2 | Segment | 5025 (100.0%) | 97 (100.0%) |
| 3 | Category (as listed) | 5025 (100.0%) | 97 (100.0%) |
| 4 | Phone | 4694 (93.4%) | 95 (97.9%) |
| 5 | Email | 800 (15.9%) | 97 (100.0%) |
| 6 | LinkedIn Profile | 0 (0.0%) | 0 (0.0%) |
| 7 | Contact Person | 391 (7.8%) | 40 (41.2%) |
| 8 | Role | 391 (7.8%) | 40 (41.2%) |
| 9 | Website | 4345 (86.5%) | 97 (100.0%) |
| 10 | Address | 4808 (95.7%) | 95 (97.9%) |
| 11 | Real City | 4322 (86.0%) | 90 (92.8%) |
| 12 | Real State | 4425 (88.1%) | 90 (92.8%) |
| 13 | Market | 5025 (100.0%) | 97 (100.0%) |
| 14 | Lead Origin | 5025 (100.0%) | 97 (100.0%) |
| 15 | Rating | 861 (17.1%) | 26 (26.8%) |
| 16 | Reviews | 861 (17.1%) | 26 (26.8%) |
| 17 | Source | 5025 (100.0%) | 97 (100.0%) |
| 18 | Signals | 5025 (100.0%) | 97 (100.0%) |
| 19 | Match Type | 5025 (100.0%) | 97 (100.0%) |
| 20 | Email Source | 800 (15.9%) | 97 (100.0%) |
| 21 | LinkedIn Source | 0 (0.0%) | 0 (0.0%) |
| 22 | Found At | 5025 (100.0%) | 97 (100.0%) |
| 23 | Also Listed As | 416 (8.3%) | 18 (18.6%) |
| 24 | Other Markets | 59 (1.2%) | 4 (4.1%) |
| 25 | Merged Listings | 669 (13.3%) | 26 (26.8%) |
| 26 | Flags | 494 (9.8%) | 16 (16.5%) |
| 27 | Mobile Candidates | 127 (2.5%) | 97 (100.0%) |
| 28 | Socials | 728 (14.5%) | 84 (86.6%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 800 | 15.9% |
| linkedin | 0 | 0.0% |
| direct-line | 127 | 2.5% |
| role-email | 352 | 7.0% |
| gia | 164 | 3.3% |
| ags | 14 | 0.3% |
| ja | 11 | 0.2% |
| bench | 78 | 1.6% |
| custom-design | 407 | 8.1% |
| since-yyyy | 431 | 8.6% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1391 | 1167 | 246 | 176 | 0 | 25 |
| Los Angeles, CA | 1173 | 881 | 192 | 96 | 0 | 26 |
| Chicago, IL | 838 | 584 | 130 | 47 | 0 | 16 |
| Houston, TX | 838 | 428 | 89 | 27 | 0 | 13 |
| Dallas, TX | 490 | 287 | 57 | 23 | 0 | 5 |
| Miami, FL | 716 | 517 | 69 | 17 | 0 | 11 |
| Atlanta, GA | 541 | 372 | 8 | 2 | 0 | 1 |
| Philadelphia, PA | 561 | 270 | 3 | 0 | 0 | 0 |
| San Francisco, CA | 401 | 291 | 2 | 1 | 0 | 0 |
| Boston, MA | 312 | 228 | 4 | 2 | 0 | 0 |
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
| Google Maps | 602 | 400 | 10 |
| YellowPages | 5884 | 4016 | 78 |
| BBB | 148 | 114 | 0 |
| OpenStreetMap | 627 | 495 | 9 |

Discovery tasks completed: bbb=37, gmaps=17, osm=5, yp=247

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 23 | 0 | 0 | 23 |
| beads-craft | 220 | 16 | 0 | 236 |
| chain | 804 | 0 | 54 | 858 |
| coin-currency | 30 | 0 | 0 | 30 |
| costume-fashion | 179 | 48 | 3 | 230 |
| diamond-trade | 76 | 17 | 1 | 94 |
| gold-buyer | 40 | 5 | 10 | 55 |
| kiosk-battery | 3 | 0 | 0 | 3 |
| no-segment | 0 | 0 | 37 | 37 |
| pawn | 245 | 9 | 0 | 254 |
| piercing-tattoo | 115 | 8 | 1 | 124 |
| simulants | 4 | 12 | 0 | 16 |
| thrift-consignment | 3 | 0 | 0 | 3 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 50 | 5 | 0 | 55 |
| **all** | | | | **2019** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| crawl | egress-blocked | 212 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 8 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| builder | final-kill | 8 | yp:2a0711cd6a09d71c: appraiser-lab-insurer |
| osm | error | 7 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 2 | https://overpass.kumi.systems/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| osm | http-406 | 1 | https://overpass-api.de/api/interpreter |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
