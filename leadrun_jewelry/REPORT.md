# Jewelry retail lead run — REPORT

Generated 2026-10-13T22:00:18+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 8798 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 6552 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 136 |
| Qualification rate | 2.1% |
| Websites crawled OK / attempted | 4655 / 5565 |
| Listings with an owner/decision-maker name | 955 |
| LinkedIn searches by outcome | none: 90 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 6552 (100.0%) | 136 (100.0%) |
| 2 | Segment | 6552 (100.0%) | 136 (100.0%) |
| 3 | Category (as listed) | 6543 (99.9%) | 136 (100.0%) |
| 4 | Phone | 6102 (93.1%) | 133 (97.8%) |
| 5 | Email | 1293 (19.7%) | 136 (100.0%) |
| 6 | LinkedIn Profile | 0 (0.0%) | 0 (0.0%) |
| 7 | Contact Person | 432 (6.6%) | 38 (27.9%) |
| 8 | Role | 432 (6.6%) | 38 (27.9%) |
| 9 | Website | 4647 (70.9%) | 136 (100.0%) |
| 10 | Address | 6279 (95.8%) | 135 (99.3%) |
| 11 | Real City | 5449 (83.2%) | 115 (84.6%) |
| 12 | Real State | 5545 (84.6%) | 114 (83.8%) |
| 13 | Market | 6552 (100.0%) | 136 (100.0%) |
| 14 | Lead Origin | 6552 (100.0%) | 136 (100.0%) |
| 15 | Rating | 1621 (24.7%) | 71 (52.2%) |
| 16 | Reviews | 1621 (24.7%) | 71 (52.2%) |
| 17 | Source | 6552 (100.0%) | 136 (100.0%) |
| 18 | Signals | 6552 (100.0%) | 136 (100.0%) |
| 19 | Match Type | 6552 (100.0%) | 136 (100.0%) |
| 20 | Email Source | 1293 (19.7%) | 136 (100.0%) |
| 21 | LinkedIn Source | 0 (0.0%) | 0 (0.0%) |
| 22 | Found At | 6552 (100.0%) | 136 (100.0%) |
| 23 | Also Listed As | 738 (11.3%) | 37 (27.2%) |
| 24 | Other Markets | 56 (0.9%) | 3 (2.2%) |
| 25 | Merged Listings | 1251 (19.1%) | 53 (39.0%) |
| 26 | Flags | 734 (11.2%) | 20 (14.7%) |
| 27 | Mobile Candidates | 176 (2.7%) | 136 (100.0%) |
| 28 | Socials | 1181 (18.0%) | 113 (83.1%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1293 | 19.7% |
| linkedin | 0 | 0.0% |
| direct-line | 176 | 2.7% |
| role-email | 593 | 9.1% |
| gia | 311 | 4.7% |
| ags | 30 | 0.5% |
| ja | 14 | 0.2% |
| bench | 151 | 2.3% |
| custom-design | 795 | 12.1% |
| since-yyyy | 847 | 12.9% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1445 | 1232 | 233 | 97 | 0 | 20 |
| Los Angeles, CA | 1287 | 1064 | 203 | 79 | 0 | 22 |
| Chicago, IL | 996 | 688 | 133 | 60 | 0 | 12 |
| Houston, TX | 1031 | 719 | 128 | 56 | 0 | 20 |
| Dallas, TX | 725 | 500 | 82 | 61 | 0 | 4 |
| Miami, FL | 886 | 661 | 134 | 18 | 0 | 24 |
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
| Google Maps | 1489 | 915 | 46 |
| YellowPages | 5829 | 4722 | 78 |
| BBB | 589 | 322 | 0 |
| OpenStreetMap | 891 | 593 | 12 |

Discovery tasks completed: bbb=152, gmaps=50, osm=10, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 31 | 0 | 0 | 31 |
| beads-craft | 237 | 19 | 2 | 258 |
| chain | 1291 | 0 | 0 | 1291 |
| coin-currency | 51 | 1 | 0 | 52 |
| costume-fashion | 185 | 77 | 4 | 266 |
| diamond-trade | 99 | 22 | 2 | 123 |
| gold-buyer | 95 | 18 | 1 | 114 |
| kiosk-battery | 5 | 0 | 0 | 5 |
| no-segment | 0 | 0 | 255 | 255 |
| pawn | 277 | 16 | 0 | 293 |
| piercing-tattoo | 172 | 14 | 3 | 189 |
| simulants | 5 | 17 | 2 | 24 |
| thrift-consignment | 6 | 0 | 0 | 6 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 57 | 7 | 0 | 64 |
| **all** | | | | **2972** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1287 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 57 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 20 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 3 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 2 | https://overpass.kumi.systems/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| linkedin | blocked | 1 | http-429 or challenge page at https://www.google.com/search?q=%22David+Leonard%22+San+Luis+Obispo+linkedin&hl=en&num=10 |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
