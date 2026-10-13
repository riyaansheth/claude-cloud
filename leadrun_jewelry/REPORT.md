# Jewelry retail lead run — REPORT

Generated 2026-10-13T23:00:41+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 9039 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 6646 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 168 |
| Qualification rate | 2.5% |
| Websites crawled OK / attempted | 5042 / 6023 |
| Listings with an owner/decision-maker name | 1169 |
| LinkedIn searches by outcome | ambiguous: 1, match: 17, none: 106, reject: 6 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 6646 (100.0%) | 168 (100.0%) |
| 2 | Segment | 6646 (100.0%) | 168 (100.0%) |
| 3 | Category (as listed) | 6633 (99.8%) | 168 (100.0%) |
| 4 | Phone | 6196 (93.2%) | 165 (98.2%) |
| 5 | Email | 1479 (22.3%) | 167 (99.4%) |
| 6 | LinkedIn Profile | 13 (0.2%) | 8 (4.8%) |
| 7 | Contact Person | 536 (8.1%) | 65 (38.7%) |
| 8 | Role | 536 (8.1%) | 65 (38.7%) |
| 9 | Website | 4986 (75.0%) | 168 (100.0%) |
| 10 | Address | 6376 (95.9%) | 167 (99.4%) |
| 11 | Real City | 5558 (83.6%) | 148 (88.1%) |
| 12 | Real State | 5653 (85.1%) | 147 (87.5%) |
| 13 | Market | 6646 (100.0%) | 168 (100.0%) |
| 14 | Lead Origin | 6646 (100.0%) | 168 (100.0%) |
| 15 | Rating | 1618 (24.3%) | 72 (42.9%) |
| 16 | Reviews | 1618 (24.3%) | 72 (42.9%) |
| 17 | Source | 6646 (100.0%) | 168 (100.0%) |
| 18 | Signals | 6646 (100.0%) | 168 (100.0%) |
| 19 | Match Type | 6646 (100.0%) | 168 (100.0%) |
| 20 | Email Source | 1479 (22.3%) | 167 (99.4%) |
| 21 | LinkedIn Source | 13 (0.2%) | 8 (4.8%) |
| 22 | Found At | 6646 (100.0%) | 168 (100.0%) |
| 23 | Also Listed As | 763 (11.5%) | 41 (24.4%) |
| 24 | Other Markets | 56 (0.8%) | 3 (1.8%) |
| 25 | Merged Listings | 1296 (19.5%) | 66 (39.3%) |
| 26 | Flags | 759 (11.4%) | 28 (16.7%) |
| 27 | Mobile Candidates | 214 (3.2%) | 163 (97.0%) |
| 28 | Socials | 1419 (21.4%) | 145 (86.3%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1479 | 22.3% |
| linkedin | 13 | 0.2% |
| direct-line | 214 | 3.2% |
| role-email | 700 | 10.5% |
| gia | 404 | 6.1% |
| ags | 47 | 0.7% |
| ja | 28 | 0.4% |
| bench | 201 | 3.0% |
| custom-design | 963 | 14.5% |
| since-yyyy | 967 | 14.6% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1443 | 1227 | 283 | 97 | 3 | 29 |
| Los Angeles, CA | 1280 | 1055 | 243 | 79 | 2 | 28 |
| Chicago, IL | 993 | 683 | 152 | 60 | 2 | 15 |
| Houston, TX | 1030 | 707 | 145 | 57 | 4 | 22 |
| Dallas, TX | 722 | 490 | 91 | 57 | 1 | 5 |
| Miami, FL | 1024 | 731 | 163 | 69 | 1 | 32 |
| Atlanta, GA | 739 | 528 | 129 | 62 | 0 | 14 |
| Philadelphia, PA | 754 | 541 | 79 | 22 | 0 | 7 |
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
| YellowPages | 5829 | 4675 | 78 |
| BBB | 830 | 482 | 32 |
| OpenStreetMap | 891 | 587 | 12 |

Discovery tasks completed: bbb=214, gmaps=50, osm=10, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 31 | 0 | 0 | 31 |
| beads-craft | 237 | 22 | 2 | 261 |
| chain | 1455 | 0 | 0 | 1455 |
| coin-currency | 56 | 2 | 0 | 58 |
| costume-fashion | 185 | 87 | 10 | 282 |
| diamond-trade | 101 | 27 | 4 | 132 |
| gold-buyer | 113 | 19 | 1 | 133 |
| kiosk-battery | 5 | 0 | 0 | 5 |
| no-segment | 0 | 0 | 273 | 273 |
| pawn | 285 | 19 | 13 | 317 |
| piercing-tattoo | 216 | 17 | 3 | 236 |
| simulants | 5 | 19 | 2 | 26 |
| thrift-consignment | 7 | 0 | 0 | 7 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 57 | 7 | 0 | 64 |
| **all** | | | | **3281** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1340 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 67 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 20 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 3 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 2 | https://overpass.kumi.systems/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| linkedin | blocked | 1 | http-429 or challenge page at https://www.google.com/search?q=%22David+Leonard%22+San+Luis+Obispo+linkedin&hl=en&num=10 |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
