# Jewelry retail lead run — REPORT

Generated 2026-10-14T00:56:04+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 10609 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 7795 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 217 |
| Qualification rate | 2.8% |
| Websites crawled OK / attempted | 5777 / 6929 |
| Listings with an owner/decision-maker name | 1374 |
| LinkedIn searches by outcome | ambiguous: 32, match: 34, none: 167, reject: 11 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 7795 (100.0%) | 217 (100.0%) |
| 2 | Segment | 7795 (100.0%) | 217 (100.0%) |
| 3 | Category (as listed) | 7781 (99.8%) | 217 (100.0%) |
| 4 | Phone | 7130 (91.5%) | 214 (98.6%) |
| 5 | Email | 1820 (23.3%) | 215 (99.1%) |
| 6 | LinkedIn Profile | 28 (0.4%) | 22 (10.1%) |
| 7 | Contact Person | 658 (8.4%) | 93 (42.9%) |
| 8 | Role | 658 (8.4%) | 93 (42.9%) |
| 9 | Website | 5774 (74.1%) | 217 (100.0%) |
| 10 | Address | 7380 (94.7%) | 216 (99.5%) |
| 11 | Real City | 5850 (75.0%) | 181 (83.4%) |
| 12 | Real State | 5946 (76.3%) | 180 (82.9%) |
| 13 | Market | 7795 (100.0%) | 217 (100.0%) |
| 14 | Lead Origin | 7795 (100.0%) | 217 (100.0%) |
| 15 | Rating | 2497 (32.0%) | 101 (46.5%) |
| 16 | Reviews | 2497 (32.0%) | 101 (46.5%) |
| 17 | Source | 7795 (100.0%) | 217 (100.0%) |
| 18 | Signals | 7795 (100.0%) | 217 (100.0%) |
| 19 | Match Type | 7795 (100.0%) | 217 (100.0%) |
| 20 | Email Source | 1820 (23.3%) | 215 (99.1%) |
| 21 | LinkedIn Source | 28 (0.4%) | 22 (10.1%) |
| 22 | Found At | 7795 (100.0%) | 217 (100.0%) |
| 23 | Also Listed As | 840 (10.8%) | 46 (21.2%) |
| 24 | Other Markets | 76 (1.0%) | 3 (1.4%) |
| 25 | Merged Listings | 1475 (18.9%) | 78 (35.9%) |
| 26 | Flags | 974 (12.5%) | 32 (14.7%) |
| 27 | Mobile Candidates | 268 (3.4%) | 200 (92.2%) |
| 28 | Socials | 1827 (23.4%) | 187 (86.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1820 | 23.3% |
| linkedin | 28 | 0.4% |
| direct-line | 268 | 3.4% |
| role-email | 840 | 10.8% |
| gia | 515 | 6.6% |
| ags | 59 | 0.8% |
| ja | 37 | 0.5% |
| bench | 280 | 3.6% |
| custom-design | 1291 | 16.6% |
| since-yyyy | 1235 | 15.8% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1443 | 1226 | 282 | 97 | 5 | 31 |
| Los Angeles, CA | 1280 | 1049 | 241 | 78 | 4 | 30 |
| Chicago, IL | 993 | 683 | 153 | 60 | 3 | 16 |
| Houston, TX | 1030 | 707 | 145 | 57 | 5 | 22 |
| Dallas, TX | 722 | 490 | 91 | 57 | 2 | 6 |
| Miami, FL | 1024 | 731 | 164 | 69 | 2 | 33 |
| Atlanta, GA | 739 | 527 | 129 | 61 | 7 | 20 |
| Philadelphia, PA | 767 | 547 | 92 | 26 | 0 | 11 |
| San Francisco, CA | 732 | 444 | 124 | 66 | 0 | 8 |
| Boston, MA | 465 | 294 | 87 | 18 | 0 | 9 |
| Seattle, WA | 188 | 127 | 54 | 11 | 0 | 4 |
| Las Vegas, NV | 151 | 127 | 33 | 11 | 0 | 4 |
| Phoenix, AZ | 180 | 152 | 39 | 9 | 0 | 7 |
| San Diego, CA | 176 | 142 | 41 | 8 | 0 | 1 |
| Denver, CO | 171 | 136 | 49 | 9 | 0 | 5 |
| Washington, DC | 166 | 97 | 43 | 10 | 0 | 3 |
| Detroit, MI | 173 | 150 | 35 | 9 | 0 | 5 |
| Minneapolis, MN | 119 | 92 | 16 | 2 | 0 | 2 |
| Charlotte, NC | 91 | 74 | 2 | 0 | 0 | 0 |
| Nashville, TN | 0 | 0 | 0 | 0 | 0 | 0 |
| Scottsdale, AZ | 0 | 0 | 0 | 0 | 0 | 0 |
| Naples, FL | 0 | 0 | 0 | 0 | 0 | 0 |
| Greenwich, CT | 0 | 0 | 0 | 0 | 0 | 0 |
| Palm Beach, FL | 0 | 0 | 0 | 0 | 0 | 0 |
| Beverly Hills, CA | 0 | 0 | 0 | 0 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 2566 | 1779 | 74 |
| YellowPages | 5829 | 4666 | 77 |
| BBB | 986 | 547 | 52 |
| OpenStreetMap | 1229 | 803 | 14 |

Discovery tasks completed: bbb=270, gmaps=92, osm=19, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 37 | 0 | 0 | 37 |
| beads-craft | 260 | 23 | 2 | 285 |
| chain | 1714 | 0 | 0 | 1714 |
| coin-currency | 67 | 3 | 0 | 70 |
| costume-fashion | 193 | 99 | 12 | 304 |
| diamond-trade | 110 | 28 | 5 | 143 |
| gold-buyer | 143 | 24 | 2 | 169 |
| kiosk-battery | 6 | 0 | 0 | 6 |
| no-segment | 0 | 0 | 429 | 429 |
| pawn | 316 | 23 | 13 | 352 |
| piercing-tattoo | 275 | 26 | 4 | 305 |
| simulants | 6 | 24 | 2 | 32 |
| thrift-consignment | 13 | 0 | 0 | 13 |
| trade-association | 2 | 0 | 0 | 2 |
| wholesale-manufacturer | 59 | 8 | 0 | 67 |
| **all** | | | | **3928** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1415 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 81 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 30 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 7 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 7 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| linkedin | blocked | 3 | http-429 or challenge page at https://www.google.com/search?q=%22Billy+Lulo%22+Los+Angeles+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
