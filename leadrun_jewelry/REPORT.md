# Jewelry retail lead run — REPORT

Generated 2026-10-14T01:30:40+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 11654 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 8461 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 231 |
| Qualification rate | 2.7% |
| Websites crawled OK / attempted | 6097 / 7305 |
| Listings with an owner/decision-maker name | 1496 |
| LinkedIn searches by outcome | ambiguous: 45, match: 40, none: 189, reject: 11 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 8461 (100.0%) | 231 (100.0%) |
| 2 | Segment | 8461 (100.0%) | 231 (100.0%) |
| 3 | Category (as listed) | 8446 (99.8%) | 231 (100.0%) |
| 4 | Phone | 7776 (91.9%) | 227 (98.3%) |
| 5 | Email | 1962 (23.2%) | 228 (98.7%) |
| 6 | LinkedIn Profile | 34 (0.4%) | 28 (12.1%) |
| 7 | Contact Person | 726 (8.6%) | 100 (43.3%) |
| 8 | Role | 726 (8.6%) | 100 (43.3%) |
| 9 | Website | 6294 (74.4%) | 231 (100.0%) |
| 10 | Address | 8035 (95.0%) | 230 (99.6%) |
| 11 | Real City | 6340 (74.9%) | 191 (82.7%) |
| 12 | Real State | 6437 (76.1%) | 190 (82.3%) |
| 13 | Market | 8461 (100.0%) | 231 (100.0%) |
| 14 | Lead Origin | 8461 (100.0%) | 231 (100.0%) |
| 15 | Rating | 2797 (33.1%) | 116 (50.2%) |
| 16 | Reviews | 2797 (33.1%) | 116 (50.2%) |
| 17 | Source | 8461 (100.0%) | 231 (100.0%) |
| 18 | Signals | 8461 (100.0%) | 231 (100.0%) |
| 19 | Match Type | 8461 (100.0%) | 231 (100.0%) |
| 20 | Email Source | 1962 (23.2%) | 228 (98.7%) |
| 21 | LinkedIn Source | 34 (0.4%) | 28 (12.1%) |
| 22 | Found At | 8461 (100.0%) | 231 (100.0%) |
| 23 | Also Listed As | 923 (10.9%) | 53 (22.9%) |
| 24 | Other Markets | 95 (1.1%) | 8 (3.5%) |
| 25 | Merged Listings | 1621 (19.2%) | 89 (38.5%) |
| 26 | Flags | 1033 (12.2%) | 33 (14.3%) |
| 27 | Mobile Candidates | 290 (3.4%) | 209 (90.5%) |
| 28 | Socials | 2000 (23.6%) | 198 (85.7%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1962 | 23.2% |
| linkedin | 34 | 0.4% |
| direct-line | 290 | 3.4% |
| role-email | 897 | 10.6% |
| gia | 550 | 6.5% |
| ags | 63 | 0.7% |
| ja | 39 | 0.5% |
| bench | 316 | 3.7% |
| custom-design | 1422 | 16.8% |
| since-yyyy | 1328 | 15.7% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1226 | 282 | 97 | 7 | 32 |
| Los Angeles, CA | 1280 | 1048 | 240 | 77 | 6 | 31 |
| Chicago, IL | 993 | 683 | 153 | 60 | 3 | 16 |
| Houston, TX | 1030 | 706 | 145 | 57 | 5 | 22 |
| Dallas, TX | 722 | 490 | 91 | 57 | 3 | 7 |
| Miami, FL | 1024 | 731 | 164 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 527 | 129 | 61 | 8 | 21 |
| Philadelphia, PA | 767 | 547 | 92 | 26 | 0 | 11 |
| San Francisco, CA | 732 | 444 | 124 | 66 | 0 | 8 |
| Boston, MA | 539 | 328 | 98 | 44 | 0 | 9 |
| Seattle, WA | 456 | 303 | 54 | 11 | 0 | 3 |
| Las Vegas, NV | 409 | 284 | 33 | 11 | 0 | 4 |
| Phoenix, AZ | 180 | 152 | 39 | 9 | 0 | 7 |
| San Diego, CA | 176 | 142 | 41 | 8 | 0 | 1 |
| Denver, CO | 171 | 136 | 49 | 9 | 0 | 5 |
| Washington, DC | 166 | 96 | 42 | 10 | 0 | 3 |
| Detroit, MI | 173 | 150 | 36 | 9 | 0 | 6 |
| Minneapolis, MN | 117 | 90 | 32 | 8 | 0 | 3 |
| Charlotte, NC | 115 | 94 | 33 | 11 | 0 | 3 |
| Nashville, TN | 81 | 60 | 28 | 8 | 0 | 0 |
| Scottsdale, AZ | 56 | 46 | 14 | 3 | 0 | 2 |
| Naples, FL | 113 | 64 | 25 | 10 | 0 | 2 |
| Greenwich, CT | 85 | 52 | 17 | 4 | 0 | 3 |
| Palm Beach, FL | 89 | 62 | 1 | 1 | 0 | 0 |
| Beverly Hills, CA | 0 | 0 | 0 | 0 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 2945 | 2035 | 83 |
| YellowPages | 6355 | 5027 | 76 |
| BBB | 1060 | 582 | 57 |
| OpenStreetMap | 1295 | 817 | 15 |

Discovery tasks completed: bbb=281, gmaps=116, osm=23, yp=284

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 40 | 0 | 0 | 40 |
| beads-craft | 290 | 26 | 2 | 318 |
| chain | 1910 | 0 | 0 | 1910 |
| coin-currency | 87 | 4 | 0 | 91 |
| costume-fashion | 219 | 105 | 15 | 339 |
| diamond-trade | 118 | 28 | 6 | 152 |
| gold-buyer | 152 | 26 | 3 | 181 |
| kiosk-battery | 6 | 0 | 0 | 6 |
| no-segment | 0 | 0 | 514 | 514 |
| pawn | 347 | 23 | 13 | 383 |
| piercing-tattoo | 317 | 30 | 5 | 352 |
| simulants | 6 | 25 | 2 | 33 |
| thrift-consignment | 28 | 0 | 0 | 28 |
| trade-association | 2 | 0 | 0 | 2 |
| wholesale-manufacturer | 61 | 8 | 1 | 70 |
| **all** | | | | **4419** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1430 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 90 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 31 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-504 | 12 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| osm | http-406 | 10 | https://overpass-api.de/api/interpreter |
| linkedin | blocked | 4 | http-429 or challenge page at https://www.google.com/search?q=%22Billy+Lulo%22+Los+Angeles+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
