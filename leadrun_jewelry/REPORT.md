# Jewelry retail lead run — REPORT

Generated 2026-10-13T21:22:07+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 8673 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 6511 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 136 |
| Qualification rate | 2.1% |
| Websites crawled OK / attempted | 4655 / 5565 |
| Listings with an owner/decision-maker name | 880 |
| LinkedIn searches by outcome | none: 51 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 6511 (100.0%) | 136 (100.0%) |
| 2 | Segment | 6511 (100.0%) | 136 (100.0%) |
| 3 | Category (as listed) | 6507 (99.9%) | 136 (100.0%) |
| 4 | Phone | 6061 (93.1%) | 133 (97.8%) |
| 5 | Email | 1294 (19.9%) | 136 (100.0%) |
| 6 | LinkedIn Profile | 0 (0.0%) | 0 (0.0%) |
| 7 | Contact Person | 390 (6.0%) | 37 (27.2%) |
| 8 | Role | 390 (6.0%) | 37 (27.2%) |
| 9 | Website | 4646 (71.4%) | 136 (100.0%) |
| 10 | Address | 6239 (95.8%) | 135 (99.3%) |
| 11 | Real City | 5404 (83.0%) | 115 (84.6%) |
| 12 | Real State | 5500 (84.5%) | 114 (83.8%) |
| 13 | Market | 6511 (100.0%) | 136 (100.0%) |
| 14 | Lead Origin | 6511 (100.0%) | 136 (100.0%) |
| 15 | Rating | 1622 (24.9%) | 71 (52.2%) |
| 16 | Reviews | 1622 (24.9%) | 71 (52.2%) |
| 17 | Source | 6511 (100.0%) | 136 (100.0%) |
| 18 | Signals | 6511 (100.0%) | 136 (100.0%) |
| 19 | Match Type | 6511 (100.0%) | 136 (100.0%) |
| 20 | Email Source | 1294 (19.9%) | 136 (100.0%) |
| 21 | LinkedIn Source | 0 (0.0%) | 0 (0.0%) |
| 22 | Found At | 6511 (100.0%) | 136 (100.0%) |
| 23 | Also Listed As | 727 (11.2%) | 37 (27.2%) |
| 24 | Other Markets | 56 (0.9%) | 3 (2.2%) |
| 25 | Merged Listings | 1221 (18.8%) | 52 (38.2%) |
| 26 | Flags | 713 (11.0%) | 20 (14.7%) |
| 27 | Mobile Candidates | 176 (2.7%) | 136 (100.0%) |
| 28 | Socials | 1182 (18.2%) | 113 (83.1%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1294 | 19.9% |
| linkedin | 0 | 0.0% |
| direct-line | 176 | 2.7% |
| role-email | 594 | 9.1% |
| gia | 312 | 4.8% |
| ags | 30 | 0.5% |
| ja | 14 | 0.2% |
| bench | 152 | 2.3% |
| custom-design | 794 | 12.2% |
| since-yyyy | 803 | 12.3% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1445 | 1232 | 233 | 97 | 0 | 20 |
| Los Angeles, CA | 1287 | 1064 | 203 | 79 | 0 | 22 |
| Chicago, IL | 996 | 688 | 133 | 60 | 0 | 12 |
| Houston, TX | 1031 | 719 | 128 | 56 | 0 | 20 |
| Dallas, TX | 620 | 464 | 83 | 25 | 0 | 4 |
| Miami, FL | 867 | 656 | 134 | 12 | 0 | 24 |
| Atlanta, GA | 642 | 471 | 107 | 16 | 0 | 11 |
| Philadelphia, PA | 732 | 531 | 79 | 12 | 0 | 7 |
| San Francisco, CA | 589 | 391 | 107 | 15 | 0 | 7 |
| Boston, MA | 465 | 295 | 87 | 18 | 0 | 9 |
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
| Google Maps | 1489 | 914 | 46 |
| YellowPages | 5829 | 4723 | 78 |
| BBB | 465 | 279 | 0 |
| OpenStreetMap | 891 | 595 | 12 |

Discovery tasks completed: bbb=124, gmaps=50, osm=10, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 30 | 0 | 0 | 30 |
| beads-craft | 235 | 19 | 2 | 256 |
| chain | 1237 | 0 | 0 | 1237 |
| coin-currency | 51 | 1 | 0 | 52 |
| costume-fashion | 184 | 77 | 4 | 265 |
| diamond-trade | 94 | 22 | 2 | 118 |
| gold-buyer | 95 | 18 | 1 | 114 |
| kiosk-battery | 5 | 0 | 0 | 5 |
| no-segment | 0 | 0 | 242 | 242 |
| pawn | 276 | 16 | 0 | 292 |
| piercing-tattoo | 161 | 14 | 3 | 178 |
| simulants | 5 | 17 | 2 | 24 |
| thrift-consignment | 6 | 0 | 0 | 6 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 57 | 7 | 0 | 64 |
| **all** | | | | **2884** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1273 | bbb:3149c8f046693f3b: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 46 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 20 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 3 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 2 | https://overpass.kumi.systems/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
