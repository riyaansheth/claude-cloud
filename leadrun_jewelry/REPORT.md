# Jewelry retail lead run — REPORT

Generated 2026-10-13T16:52:31+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 6395 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 4449 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 36 |
| Qualification rate | 0.8% |
| Websites crawled OK / attempted | 1313 / 1483 |
| Listings with an owner/decision-maker name | 233 |
| LinkedIn searches by outcome | — |
| **Shortfall vs 100 qualified** | **64** (not padded) |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 4449 (100.0%) | 36 (100.0%) |
| 2 | Segment | 4449 (100.0%) | 36 (100.0%) |
| 3 | Category (as listed) | 4449 (100.0%) | 36 (100.0%) |
| 4 | Phone | 4182 (94.0%) | 34 (94.4%) |
| 5 | Email | 344 (7.7%) | 36 (100.0%) |
| 6 | LinkedIn Profile | 0 (0.0%) | 0 (0.0%) |
| 7 | Contact Person | 189 (4.2%) | 17 (47.2%) |
| 8 | Role | 189 (4.2%) | 17 (47.2%) |
| 9 | Website | 3913 (88.0%) | 36 (100.0%) |
| 10 | Address | 4271 (96.0%) | 35 (97.2%) |
| 11 | Real City | 3913 (88.0%) | 34 (94.4%) |
| 12 | Real State | 4009 (90.1%) | 35 (97.2%) |
| 13 | Market | 4449 (100.0%) | 36 (100.0%) |
| 14 | Lead Origin | 4449 (100.0%) | 36 (100.0%) |
| 15 | Rating | 590 (13.3%) | 6 (16.7%) |
| 16 | Reviews | 590 (13.3%) | 6 (16.7%) |
| 17 | Source | 4449 (100.0%) | 36 (100.0%) |
| 18 | Signals | 4449 (100.0%) | 36 (100.0%) |
| 19 | Match Type | 4449 (100.0%) | 36 (100.0%) |
| 20 | Email Source | 344 (7.7%) | 36 (100.0%) |
| 21 | LinkedIn Source | 0 (0.0%) | 0 (0.0%) |
| 22 | Found At | 4449 (100.0%) | 36 (100.0%) |
| 23 | Also Listed As | 342 (7.7%) | 7 (19.4%) |
| 24 | Other Markets | 55 (1.2%) | 4 (11.1%) |
| 25 | Merged Listings | 515 (11.6%) | 9 (25.0%) |
| 26 | Flags | 372 (8.4%) | 6 (16.7%) |
| 27 | Mobile Candidates | 56 (1.3%) | 36 (100.0%) |
| 28 | Socials | 302 (6.8%) | 34 (94.4%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 344 | 7.7% |
| linkedin | 0 | 0.0% |
| direct-line | 56 | 1.3% |
| role-email | 141 | 3.2% |
| gia | 55 | 1.2% |
| ags | 3 | 0.1% |
| ja | 7 | 0.2% |
| bench | 31 | 0.7% |
| custom-design | 158 | 3.6% |
| since-yyyy | 219 | 4.9% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1409 | 1180 | 209 | 153 | 0 | 24 |
| Los Angeles, CA | 1100 | 827 | 45 | 10 | 0 | 3 |
| Chicago, IL | 700 | 534 | 47 | 16 | 0 | 5 |
| Houston, TX | 715 | 366 | 16 | 2 | 0 | 2 |
| Dallas, TX | 473 | 264 | 12 | 4 | 0 | 0 |
| Miami, FL | 694 | 506 | 14 | 4 | 0 | 2 |
| Atlanta, GA | 546 | 372 | 0 | 0 | 0 | 0 |
| Philadelphia, PA | 565 | 272 | 1 | 0 | 0 | 0 |
| San Francisco, CA | 160 | 128 | 0 | 0 | 0 | 0 |
| Boston, MA | 0 | 0 | 0 | 0 | 0 | 0 |
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
| Google Maps | 318 | 242 | 2 |
| YellowPages | 5444 | 3711 | 31 |
| BBB | 104 | 83 | 0 |
| OpenStreetMap | 496 | 413 | 3 |

Discovery tasks completed: bbb=22, gmaps=8, osm=2, yp=223

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 22 | 0 | 0 | 22 |
| beads-craft | 187 | 8 | 0 | 195 |
| chain | 556 | 0 | 0 | 556 |
| coin-currency | 24 | 0 | 0 | 24 |
| costume-fashion | 149 | 26 | 1 | 176 |
| diamond-trade | 68 | 5 | 0 | 73 |
| gold-buyer | 37 | 2 | 0 | 39 |
| kiosk-battery | 2 | 0 | 0 | 2 |
| no-segment | 0 | 0 | 29 | 29 |
| pawn | 230 | 2 | 0 | 232 |
| piercing-tattoo | 90 | 3 | 1 | 94 |
| simulants | 3 | 3 | 0 | 6 |
| thrift-consignment | 3 | 0 | 0 | 3 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 46 | 1 | 0 | 47 |
| **all** | | | | **1499** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| crawl | egress-blocked | 74 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| osm | error | 4 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| bbb | blocked | 3 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| builder | final-kill | 2 | yp:2a0711cd6a09d71c: appraiser-lab-insurer |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| osm | http-504 | 1 | https://overpass.kumi.systems/api/interpreter |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
