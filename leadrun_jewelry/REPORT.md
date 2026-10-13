# Jewelry retail lead run — REPORT

Generated 2026-10-14T00:15:45+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 10015 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 7354 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 195 |
| Qualification rate | 2.7% |
| Websites crawled OK / attempted | 5476 / 6545 |
| Listings with an owner/decision-maker name | 1330 |
| LinkedIn searches by outcome | ambiguous: 28, match: 27, none: 151, reject: 8 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 7354 (100.0%) | 195 (100.0%) |
| 2 | Segment | 7354 (100.0%) | 195 (100.0%) |
| 3 | Category (as listed) | 7341 (99.8%) | 195 (100.0%) |
| 4 | Phone | 6727 (91.5%) | 192 (98.5%) |
| 5 | Email | 1686 (22.9%) | 193 (99.0%) |
| 6 | LinkedIn Profile | 21 (0.3%) | 15 (7.7%) |
| 7 | Contact Person | 629 (8.6%) | 84 (43.1%) |
| 8 | Role | 629 (8.6%) | 84 (43.1%) |
| 9 | Website | 5423 (73.7%) | 195 (100.0%) |
| 10 | Address | 6965 (94.7%) | 194 (99.5%) |
| 11 | Real City | 5776 (78.5%) | 168 (86.2%) |
| 12 | Real State | 5874 (79.9%) | 167 (85.6%) |
| 13 | Market | 7354 (100.0%) | 195 (100.0%) |
| 14 | Lead Origin | 7354 (100.0%) | 195 (100.0%) |
| 15 | Rating | 2086 (28.4%) | 85 (43.6%) |
| 16 | Reviews | 2086 (28.4%) | 85 (43.6%) |
| 17 | Source | 7354 (100.0%) | 195 (100.0%) |
| 18 | Signals | 7354 (100.0%) | 195 (100.0%) |
| 19 | Match Type | 7354 (100.0%) | 195 (100.0%) |
| 20 | Email Source | 1686 (22.9%) | 193 (99.0%) |
| 21 | LinkedIn Source | 21 (0.3%) | 15 (7.7%) |
| 22 | Found At | 7354 (100.0%) | 195 (100.0%) |
| 23 | Also Listed As | 815 (11.1%) | 44 (22.6%) |
| 24 | Other Markets | 72 (1.0%) | 3 (1.5%) |
| 25 | Merged Listings | 1418 (19.3%) | 75 (38.5%) |
| 26 | Flags | 917 (12.5%) | 31 (15.9%) |
| 27 | Mobile Candidates | 250 (3.4%) | 185 (94.9%) |
| 28 | Socials | 1659 (22.6%) | 168 (86.2%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 1686 | 22.9% |
| linkedin | 21 | 0.3% |
| direct-line | 250 | 3.4% |
| role-email | 782 | 10.6% |
| gia | 476 | 6.5% |
| ags | 57 | 0.8% |
| ja | 36 | 0.5% |
| bench | 256 | 3.5% |
| custom-design | 1150 | 15.6% |
| since-yyyy | 1150 | 15.6% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1443 | 1226 | 282 | 97 | 4 | 30 |
| Los Angeles, CA | 1280 | 1049 | 240 | 78 | 2 | 28 |
| Chicago, IL | 993 | 683 | 153 | 60 | 3 | 16 |
| Houston, TX | 1030 | 707 | 145 | 57 | 4 | 21 |
| Dallas, TX | 722 | 490 | 91 | 57 | 2 | 6 |
| Miami, FL | 1024 | 731 | 163 | 69 | 2 | 32 |
| Atlanta, GA | 739 | 527 | 129 | 61 | 4 | 17 |
| Philadelphia, PA | 767 | 547 | 92 | 26 | 0 | 11 |
| San Francisco, CA | 732 | 444 | 124 | 66 | 0 | 8 |
| Boston, MA | 465 | 294 | 87 | 18 | 0 | 9 |
| Seattle, WA | 188 | 127 | 54 | 11 | 0 | 4 |
| Las Vegas, NV | 151 | 127 | 33 | 11 | 0 | 4 |
| Phoenix, AZ | 180 | 152 | 39 | 9 | 0 | 7 |
| San Diego, CA | 176 | 142 | 41 | 8 | 0 | 1 |
| Denver, CO | 80 | 69 | 2 | 0 | 0 | 0 |
| Washington, DC | 46 | 39 | 11 | 1 | 0 | 1 |
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
| Google Maps | 2041 | 1366 | 59 |
| YellowPages | 5829 | 4666 | 77 |
| BBB | 986 | 548 | 45 |
| OpenStreetMap | 1160 | 774 | 14 |

Discovery tasks completed: bbb=270, gmaps=70, osm=16, yp=248

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 35 | 0 | 0 | 35 |
| beads-craft | 254 | 22 | 2 | 278 |
| chain | 1665 | 0 | 0 | 1665 |
| coin-currency | 64 | 2 | 0 | 66 |
| costume-fashion | 186 | 95 | 12 | 293 |
| diamond-trade | 107 | 28 | 5 | 140 |
| gold-buyer | 136 | 22 | 1 | 159 |
| kiosk-battery | 5 | 0 | 0 | 5 |
| no-segment | 0 | 0 | 355 | 355 |
| pawn | 298 | 22 | 13 | 333 |
| piercing-tattoo | 257 | 24 | 3 | 284 |
| simulants | 6 | 24 | 2 | 32 |
| thrift-consignment | 10 | 0 | 0 | 10 |
| trade-association | 2 | 0 | 0 | 2 |
| wholesale-manufacturer | 57 | 8 | 0 | 65 |
| **all** | | | | **3722** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 1385 | bbb:2bd7885ee7596674: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 80 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 26 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| osm | http-406 | 5 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 4 | https://overpass.kumi.systems/api/interpreter |
| linkedin | blocked | 2 | http-429 or challenge page at https://www.google.com/search?q=%22Billy+Lulo%22+Los+Angeles+linkedin&hl=en&num=10 |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |
| yp | soft-block-503 | 1 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
