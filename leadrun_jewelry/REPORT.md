# Jewelry retail lead run — REPORT

Generated 2026-10-13T23:55:36+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 9579 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 7041 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 181 |
| Qualification rate | 2.6% |
| Websites crawled OK / attempted | 5209 / 6207 |
| Listings with an owner/decision-maker name | 1258 |
| LinkedIn searches by outcome | ambiguous: 21, match: 27, none: 147, reject: 8 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 7041 (100.0%) | 181 (100.0%) |
| 2 | Segment | 7041 (100.0%) | 181 (100.0%) |
| 3 | Category (as listed) | 7028 (99.8%) | 181 (100.0%) |
| 4 | Phone | 6493 (92.2%) | 178 (98.3%) |
| 5 | Email | 1558 (22.1%) | 179 (98.9%) |
| 6 | LinkedIn Profile | 21 (0.3%) | 15 (8.3%) |
| 7 | Contact Person | 584 (8.3%) | 77 (42.5%) |
| 8 | Role | 584 (8.3%) | 77 (42.5%) |
| 9 | Website | 5246 (74.5%) | 181 (100.0%) |
| 10 | Address | 6699 (95.1%) | 180 (99.4%) |
| 11 | Real City | 5667 (80.5%) | 160 (88.4%) |
| 12 | Real State | 5764 (81.9%) | 159 (87.8%) |
| 13 | Market | 7041 (100.0%) | 181 (100.0%) |
| 14 | Lead Origin | 7041 (100.0%) | 181 (100.0%) |
| 15 | Rating | 1873 (26.6%) | 74 (40.9%) |
| 16 | Reviews | 1873 (26.6%) | 74 (40.9%) |
| 17 | Source | 7041 (100.0%) | 181 (100.0%) |
| 18 | Signals | 7041 (100.0%) | 181 (100.0%) |
| 19 | Match Type | 7041 (100.0%) | 181 (100.0%) |
| 20 | Email Source | 1558 (22.1%) | 179 (98.9%) |
| 21 | LinkedIn Source | 21 (0.3%) | 15 (8.3%) |
| 22 | Found At | 7041 (100.0%) | 181 (100.0%) |
| 23 | Also Listed As | 791 (11.2%) | 42 (23.2%) |
| 24 | Other Markets | 62 (0.9%) | 3 (1.7%) |
| 25 | Merged Listings | 1363 (19.4%) | 70 (38.7%) |
| 26 | Flags | 842 (12.0%) | 30 (16.6%) |
| 27 | Mobile Candidates | 226 (3.2%) | 171 (94.5%) |
| 28 | Socials | 1512 (21.5%) | 156 (86.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1558 | 22.1% |
| linkedin | 21 | 0.3% |
| direct-line | 226 | 3.2% |
| role-email | 731 | 10.4% |
| gia | 429 | 6.1% |
| ags | 49 | 0.7% |
| ja | 34 | 0.5% |
| bench | 224 | 3.2% |
| custom-design | 1035 | 14.7% |
| since-yyyy | 1055 | 15.0% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1443 | 1226 | 282 | 97 | 4 | 30 |
| Los Angeles, CA | 1280 | 1055 | 243 | 79 | 2 | 28 |
| Chicago, IL | 993 | 683 | 152 | 60 | 3 | 16 |
| Houston, TX | 1030 | 707 | 145 | 57 | 4 | 21 |
| Dallas, TX | 722 | 490 | 91 | 57 | 2 | 6 |
| Miami, FL | 1024 | 731 | 163 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 527 | 129 | 61 | 4 | 17 |
| Philadelphia, PA | 767 | 547 | 92 | 26 | 0 | 11 |
| San Francisco, CA | 671 | 430 | 121 | 49 | 0 | 7 |
| Boston, MA | 465 | 294 | 87 | 18 | 0 | 9 |
| Seattle, WA | 193 | 132 | 52 | 11 | 0 | 4 |
| Las Vegas, NV | 159 | 136 | 1 | 0 | 0 | 0 |
| Phoenix, AZ | 94 | 83 | 0 | 0 | 0 | 0 |
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
| Google Maps | 1796 | 1155 | 49 |
| YellowPages | 5829 | 4671 | 77 |
| BBB | 925 | 533 | 43 |
| OpenStreetMap | 1030 | 682 | 12 |

Discovery tasks completed: bbb=250, gmaps=60, osm=13, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 33 | 0 | 0 | 33 |
| beads-craft | 245 | 22 | 2 | 269 |
| chain | 1607 | 0 | 0 | 1607 |
| coin-currency | 59 | 2 | 0 | 61 |
| costume-fashion | 186 | 91 | 11 | 288 |
| diamond-trade | 104 | 28 | 4 | 136 |
| gold-buyer | 122 | 20 | 1 | 143 |
| kiosk-battery | 5 | 0 | 0 | 5 |
| no-segment | 0 | 0 | 324 | 324 |
| pawn | 290 | 20 | 13 | 323 |
| piercing-tattoo | 246 | 17 | 3 | 266 |
| simulants | 6 | 21 | 2 | 29 |
| thrift-consignment | 9 | 0 | 0 | 9 |
| trade-association | 1 | 0 | 0 | 1 |
| wholesale-manufacturer | 57 | 7 | 0 | 64 |
| **all** | | | | **3558** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1370 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 76 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 24 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 4 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 3 | https://overpass.kumi.systems/api/interpreter |
| linkedin | blocked | 2 | http-429 or challenge page at https://www.google.com/search?q=%22Billy+Lulo%22+Los+Angeles+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
