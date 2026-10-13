# Jewelry retail lead run — REPORT

Generated 2026-10-13T17:56:32+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 8058 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 6282 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 133 |
| Qualification rate | 2.1% |
| Websites crawled OK / attempted | 4453 / 5329 |
| Listings with an owner/decision-maker name | 701 |
| LinkedIn searches by outcome | — |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 6282 (100.0%) | 133 (100.0%) |
| 2 | Segment | 6282 (100.0%) | 133 (100.0%) |
| 3 | Category (as listed) | 6280 (100.0%) | 133 (100.0%) |
| 4 | Phone | 5834 (92.9%) | 130 (97.7%) |
| 5 | Email | 1201 (19.1%) | 133 (100.0%) |
| 6 | LinkedIn Profile | 0 (0.0%) | 0 (0.0%) |
| 7 | Contact Person | 354 (5.6%) | 24 (18.0%) |
| 8 | Role | 354 (5.6%) | 24 (18.0%) |
| 9 | Website | 4541 (72.3%) | 133 (100.0%) |
| 10 | Address | 6009 (95.7%) | 132 (99.2%) |
| 11 | Real City | 5296 (84.3%) | 116 (87.2%) |
| 12 | Real State | 5392 (85.8%) | 115 (86.5%) |
| 13 | Market | 6282 (100.0%) | 133 (100.0%) |
| 14 | Lead Origin | 6282 (100.0%) | 133 (100.0%) |
| 15 | Rating | 1297 (20.6%) | 59 (44.4%) |
| 16 | Reviews | 1297 (20.6%) | 59 (44.4%) |
| 17 | Source | 6282 (100.0%) | 133 (100.0%) |
| 18 | Signals | 6282 (100.0%) | 133 (100.0%) |
| 19 | Match Type | 6282 (100.0%) | 133 (100.0%) |
| 20 | Email Source | 1201 (19.1%) | 133 (100.0%) |
| 21 | LinkedIn Source | 0 (0.0%) | 0 (0.0%) |
| 22 | Found At | 6282 (100.0%) | 133 (100.0%) |
| 23 | Also Listed As | 612 (9.7%) | 31 (23.3%) |
| 24 | Other Markets | 54 (0.9%) | 2 (1.5%) |
| 25 | Merged Listings | 1012 (16.1%) | 45 (33.8%) |
| 26 | Flags | 651 (10.4%) | 17 (12.8%) |
| 27 | Mobile Candidates | 172 (2.7%) | 133 (100.0%) |
| 28 | Socials | 1080 (17.2%) | 111 (83.5%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1201 | 19.1% |
| linkedin | 0 | 0.0% |
| direct-line | 172 | 2.7% |
| role-email | 555 | 8.8% |
| gia | 276 | 4.4% |
| ags | 28 | 0.4% |
| ja | 14 | 0.2% |
| bench | 144 | 2.3% |
| custom-design | 722 | 11.5% |
| since-yyyy | 650 | 10.3% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1445 | 1233 | 234 | 125 | 0 | 20 |
| Los Angeles, CA | 1287 | 1065 | 203 | 100 | 0 | 22 |
| Chicago, IL | 938 | 660 | 134 | 43 | 0 | 12 |
| Houston, TX | 902 | 665 | 128 | 17 | 0 | 20 |
| Dallas, TX | 603 | 456 | 83 | 17 | 0 | 4 |
| Miami, FL | 867 | 656 | 134 | 13 | 0 | 24 |
| Atlanta, GA | 608 | 448 | 80 | 11 | 0 | 8 |
| Philadelphia, PA | 598 | 489 | 55 | 7 | 0 | 7 |
| San Francisco, CA | 469 | 352 | 80 | 10 | 0 | 8 |
| Boston, MA | 342 | 258 | 70 | 11 | 0 | 8 |
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
| Google Maps | 1078 | 725 | 38 |
| YellowPages | 5829 | 4765 | 83 |
| BBB | 261 | 182 | 0 |
| OpenStreetMap | 891 | 610 | 12 |

Discovery tasks completed: bbb=67, gmaps=31, osm=10, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 27 | 0 | 0 | 27 |
| beads-craft | 232 | 18 | 2 | 252 |
| chain | 1057 | 0 | 0 | 1057 |
| coin-currency | 42 | 1 | 0 | 43 |
| costume-fashion | 182 | 75 | 4 | 261 |
| diamond-trade | 87 | 22 | 1 | 110 |
| gold-buyer | 79 | 13 | 1 | 93 |
| kiosk-battery | 4 | 0 | 0 | 4 |
| no-segment | 0 | 0 | 217 | 217 |
| pawn | 266 | 16 | 0 | 282 |
| piercing-tattoo | 132 | 10 | 1 | 143 |
| simulants | 5 | 17 | 2 | 24 |
| thrift-consignment | 4 | 0 | 0 | 4 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 56 | 6 | 0 | 62 |
| **all** | | | | **2580** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1219 | bbb:3149c8f046693f3b: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 21 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 20 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 3 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 2 | https://overpass.kumi.systems/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
