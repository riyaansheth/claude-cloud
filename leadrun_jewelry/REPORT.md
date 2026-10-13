# Jewelry retail lead run — REPORT

Generated 2026-10-13T18:37:09+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 8544 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 6451 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 136 |
| Qualification rate | 2.1% |
| Websites crawled OK / attempted | 4655 / 5565 |
| Listings with an owner/decision-maker name | 784 |
| LinkedIn searches by outcome | none: 40 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 6451 (100.0%) | 136 (100.0%) |
| 2 | Segment | 6451 (100.0%) | 136 (100.0%) |
| 3 | Category (as listed) | 6447 (99.9%) | 136 (100.0%) |
| 4 | Phone | 6004 (93.1%) | 133 (97.8%) |
| 5 | Email | 1294 (20.1%) | 136 (100.0%) |
| 6 | LinkedIn Profile | 0 (0.0%) | 0 (0.0%) |
| 7 | Contact Person | 335 (5.2%) | 24 (17.6%) |
| 8 | Role | 335 (5.2%) | 24 (17.6%) |
| 9 | Website | 4646 (72.0%) | 136 (100.0%) |
| 10 | Address | 6178 (95.8%) | 135 (99.3%) |
| 11 | Real City | 5340 (82.8%) | 115 (84.6%) |
| 12 | Real State | 5436 (84.3%) | 114 (83.8%) |
| 13 | Market | 6451 (100.0%) | 136 (100.0%) |
| 14 | Lead Origin | 6451 (100.0%) | 136 (100.0%) |
| 15 | Rating | 1622 (25.1%) | 71 (52.2%) |
| 16 | Reviews | 1622 (25.1%) | 71 (52.2%) |
| 17 | Source | 6451 (100.0%) | 136 (100.0%) |
| 18 | Signals | 6451 (100.0%) | 136 (100.0%) |
| 19 | Match Type | 6451 (100.0%) | 136 (100.0%) |
| 20 | Email Source | 1294 (20.1%) | 136 (100.0%) |
| 21 | LinkedIn Source | 0 (0.0%) | 0 (0.0%) |
| 22 | Found At | 6451 (100.0%) | 136 (100.0%) |
| 23 | Also Listed As | 704 (10.9%) | 36 (26.5%) |
| 24 | Other Markets | 56 (0.9%) | 3 (2.2%) |
| 25 | Merged Listings | 1191 (18.5%) | 52 (38.2%) |
| 26 | Flags | 701 (10.9%) | 19 (14.0%) |
| 27 | Mobile Candidates | 177 (2.7%) | 136 (100.0%) |
| 28 | Socials | 1182 (18.3%) | 113 (83.1%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1294 | 20.1% |
| linkedin | 0 | 0.0% |
| direct-line | 177 | 2.7% |
| role-email | 594 | 9.2% |
| gia | 312 | 4.8% |
| ags | 30 | 0.5% |
| ja | 14 | 0.2% |
| bench | 152 | 2.4% |
| custom-design | 794 | 12.3% |
| since-yyyy | 726 | 11.3% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1445 | 1232 | 233 | 96 | 0 | 20 |
| Los Angeles, CA | 1287 | 1064 | 203 | 76 | 0 | 22 |
| Chicago, IL | 996 | 688 | 133 | 58 | 0 | 12 |
| Houston, TX | 918 | 667 | 128 | 20 | 0 | 20 |
| Dallas, TX | 603 | 456 | 83 | 16 | 0 | 4 |
| Miami, FL | 867 | 656 | 134 | 12 | 0 | 24 |
| Atlanta, GA | 642 | 471 | 107 | 15 | 0 | 11 |
| Philadelphia, PA | 732 | 531 | 79 | 10 | 0 | 7 |
| San Francisco, CA | 589 | 391 | 107 | 15 | 0 | 7 |
| Boston, MA | 465 | 295 | 87 | 17 | 0 | 9 |
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
| YellowPages | 5829 | 4724 | 78 |
| BBB | 335 | 216 | 0 |
| OpenStreetMap | 891 | 597 | 12 |

Discovery tasks completed: bbb=93, gmaps=50, osm=10, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 30 | 0 | 0 | 30 |
| beads-craft | 235 | 19 | 2 | 256 |
| chain | 1153 | 0 | 0 | 1153 |
| coin-currency | 49 | 1 | 0 | 50 |
| costume-fashion | 183 | 77 | 4 | 264 |
| diamond-trade | 91 | 22 | 2 | 115 |
| gold-buyer | 93 | 18 | 1 | 112 |
| kiosk-battery | 5 | 0 | 0 | 5 |
| no-segment | 0 | 0 | 238 | 238 |
| pawn | 274 | 16 | 0 | 290 |
| piercing-tattoo | 151 | 14 | 3 | 168 |
| simulants | 5 | 17 | 2 | 24 |
| thrift-consignment | 6 | 0 | 0 | 6 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 57 | 7 | 0 | 64 |
| **all** | | | | **2776** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1249 | bbb:3149c8f046693f3b: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 34 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 20 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 3 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 2 | https://overpass.kumi.systems/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
