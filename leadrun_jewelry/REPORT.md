# Jewelry retail lead run — REPORT

Generated 2026-10-13T18:16:39+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 8371 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 6399 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 135 |
| Qualification rate | 2.1% |
| Websites crawled OK / attempted | 4608 / 5509 |
| Listings with an owner/decision-maker name | 753 |
| LinkedIn searches by outcome | — |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 6399 (100.0%) | 135 (100.0%) |
| 2 | Segment | 6399 (100.0%) | 135 (100.0%) |
| 3 | Category (as listed) | 6397 (100.0%) | 135 (100.0%) |
| 4 | Phone | 5951 (93.0%) | 132 (97.8%) |
| 5 | Email | 1274 (19.9%) | 135 (100.0%) |
| 6 | LinkedIn Profile | 0 (0.0%) | 0 (0.0%) |
| 7 | Contact Person | 386 (6.0%) | 24 (17.8%) |
| 8 | Role | 386 (6.0%) | 24 (17.8%) |
| 9 | Website | 4617 (72.2%) | 135 (100.0%) |
| 10 | Address | 6126 (95.7%) | 134 (99.3%) |
| 11 | Real City | 5324 (83.2%) | 115 (85.2%) |
| 12 | Real State | 5420 (84.7%) | 114 (84.4%) |
| 13 | Market | 6399 (100.0%) | 135 (100.0%) |
| 14 | Lead Origin | 6399 (100.0%) | 135 (100.0%) |
| 15 | Rating | 1516 (23.7%) | 65 (48.1%) |
| 16 | Reviews | 1516 (23.7%) | 65 (48.1%) |
| 17 | Source | 6399 (100.0%) | 135 (100.0%) |
| 18 | Signals | 6399 (100.0%) | 135 (100.0%) |
| 19 | Match Type | 6399 (100.0%) | 135 (100.0%) |
| 20 | Email Source | 1274 (19.9%) | 135 (100.0%) |
| 21 | LinkedIn Source | 0 (0.0%) | 0 (0.0%) |
| 22 | Found At | 6399 (100.0%) | 135 (100.0%) |
| 23 | Also Listed As | 669 (10.5%) | 34 (25.2%) |
| 24 | Other Markets | 56 (0.9%) | 3 (2.2%) |
| 25 | Merged Listings | 1124 (17.6%) | 50 (37.0%) |
| 26 | Flags | 680 (10.6%) | 17 (12.6%) |
| 27 | Mobile Candidates | 176 (2.8%) | 135 (100.0%) |
| 28 | Socials | 1161 (18.1%) | 112 (83.0%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1274 | 19.9% |
| linkedin | 0 | 0.0% |
| direct-line | 176 | 2.8% |
| role-email | 586 | 9.2% |
| gia | 304 | 4.8% |
| ags | 30 | 0.5% |
| ja | 14 | 0.2% |
| bench | 150 | 2.3% |
| custom-design | 781 | 12.2% |
| since-yyyy | 700 | 10.9% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1445 | 1232 | 233 | 124 | 0 | 20 |
| Los Angeles, CA | 1287 | 1065 | 203 | 100 | 0 | 22 |
| Chicago, IL | 974 | 680 | 133 | 63 | 0 | 12 |
| Houston, TX | 902 | 664 | 128 | 17 | 0 | 20 |
| Dallas, TX | 603 | 456 | 83 | 17 | 0 | 4 |
| Miami, FL | 867 | 656 | 134 | 13 | 0 | 24 |
| Atlanta, GA | 642 | 471 | 107 | 15 | 0 | 11 |
| Philadelphia, PA | 732 | 531 | 79 | 10 | 0 | 7 |
| San Francisco, CA | 578 | 386 | 104 | 16 | 0 | 7 |
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
| Google Maps | 1355 | 861 | 44 |
| YellowPages | 5829 | 4733 | 79 |
| BBB | 297 | 203 | 0 |
| OpenStreetMap | 891 | 602 | 12 |

Discovery tasks completed: bbb=74, gmaps=42, osm=10, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 29 | 0 | 0 | 29 |
| beads-craft | 234 | 19 | 2 | 255 |
| chain | 1101 | 0 | 0 | 1101 |
| coin-currency | 48 | 1 | 0 | 49 |
| costume-fashion | 183 | 77 | 4 | 264 |
| diamond-trade | 91 | 22 | 2 | 115 |
| gold-buyer | 89 | 17 | 1 | 107 |
| kiosk-battery | 5 | 0 | 0 | 5 |
| no-segment | 0 | 0 | 229 | 229 |
| pawn | 270 | 16 | 0 | 286 |
| piercing-tattoo | 143 | 13 | 3 | 159 |
| simulants | 5 | 17 | 2 | 24 |
| thrift-consignment | 4 | 0 | 0 | 4 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 56 | 6 | 0 | 62 |
| **all** | | | | **2690** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1225 | bbb:3149c8f046693f3b: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 27 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 20 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 3 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 2 | https://overpass.kumi.systems/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
