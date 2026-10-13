# Jewelry retail lead run — REPORT

Generated 2026-10-14T00:35:54+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 10306 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 7549 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 212 |
| Qualification rate | 2.8% |
| Websites crawled OK / attempted | 5649 / 6738 |
| Listings with an owner/decision-maker name | 1357 |
| LinkedIn searches by outcome | ambiguous: 32, match: 34, none: 167, reject: 11 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 7549 (100.0%) | 212 (100.0%) |
| 2 | Segment | 7549 (100.0%) | 212 (100.0%) |
| 3 | Category (as listed) | 7535 (99.8%) | 212 (100.0%) |
| 4 | Phone | 6896 (91.3%) | 207 (97.6%) |
| 5 | Email | 1768 (23.4%) | 210 (99.1%) |
| 6 | LinkedIn Profile | 28 (0.4%) | 22 (10.4%) |
| 7 | Contact Person | 647 (8.6%) | 91 (42.9%) |
| 8 | Role | 647 (8.6%) | 91 (42.9%) |
| 9 | Website | 5581 (73.9%) | 212 (100.0%) |
| 10 | Address | 7143 (94.6%) | 209 (98.6%) |
| 11 | Real City | 5822 (77.1%) | 179 (84.4%) |
| 12 | Real State | 5919 (78.4%) | 178 (84.0%) |
| 13 | Market | 7549 (100.0%) | 212 (100.0%) |
| 14 | Lead Origin | 7549 (100.0%) | 212 (100.0%) |
| 15 | Rating | 2259 (29.9%) | 94 (44.3%) |
| 16 | Reviews | 2259 (29.9%) | 94 (44.3%) |
| 17 | Source | 7549 (100.0%) | 212 (100.0%) |
| 18 | Signals | 7549 (100.0%) | 212 (100.0%) |
| 19 | Match Type | 7549 (100.0%) | 212 (100.0%) |
| 20 | Email Source | 1768 (23.4%) | 210 (99.1%) |
| 21 | LinkedIn Source | 28 (0.4%) | 22 (10.4%) |
| 22 | Found At | 7549 (100.0%) | 212 (100.0%) |
| 23 | Also Listed As | 827 (11.0%) | 45 (21.2%) |
| 24 | Other Markets | 74 (1.0%) | 3 (1.4%) |
| 25 | Merged Listings | 1442 (19.1%) | 76 (35.8%) |
| 26 | Flags | 952 (12.6%) | 33 (15.6%) |
| 27 | Mobile Candidates | 262 (3.5%) | 195 (92.0%) |
| 28 | Socials | 1766 (23.4%) | 183 (86.3%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1768 | 23.4% |
| linkedin | 28 | 0.4% |
| direct-line | 262 | 3.5% |
| role-email | 819 | 10.8% |
| gia | 498 | 6.6% |
| ags | 58 | 0.8% |
| ja | 37 | 0.5% |
| bench | 273 | 3.6% |
| custom-design | 1235 | 16.4% |
| since-yyyy | 1200 | 15.9% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1443 | 1226 | 282 | 97 | 5 | 31 |
| Los Angeles, CA | 1280 | 1049 | 240 | 78 | 4 | 30 |
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
| Washington, DC | 166 | 99 | 39 | 10 | 0 | 3 |
| Detroit, MI | 61 | 48 | 0 | 0 | 0 | 0 |
| Minneapolis, MN | 20 | 20 | 6 | 0 | 0 | 2 |
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
| Google Maps | 2294 | 1539 | 67 |
| YellowPages | 5829 | 4666 | 77 |
| BBB | 986 | 548 | 52 |
| OpenStreetMap | 1199 | 796 | 16 |

Discovery tasks completed: bbb=270, gmaps=80, osm=18, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 37 | 0 | 0 | 37 |
| beads-craft | 257 | 22 | 2 | 281 |
| chain | 1682 | 0 | 0 | 1682 |
| coin-currency | 65 | 2 | 0 | 67 |
| costume-fashion | 189 | 96 | 12 | 297 |
| diamond-trade | 110 | 28 | 5 | 143 |
| gold-buyer | 141 | 24 | 2 | 167 |
| kiosk-battery | 6 | 0 | 0 | 6 |
| no-segment | 0 | 0 | 401 | 401 |
| pawn | 308 | 23 | 13 | 344 |
| piercing-tattoo | 268 | 25 | 4 | 297 |
| simulants | 6 | 24 | 2 | 32 |
| thrift-consignment | 13 | 0 | 0 | 13 |
| trade-association | 2 | 0 | 0 | 2 |
| wholesale-manufacturer | 58 | 8 | 0 | 66 |
| **all** | | | | **3835** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1400 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 81 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 29 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 5 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 5 | https://overpass.kumi.systems/api/interpreter |
| linkedin | blocked | 3 | http-429 or challenge page at https://www.google.com/search?q=%22Billy+Lulo%22+Los+Angeles+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
