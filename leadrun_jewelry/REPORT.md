# Jewelry retail lead run — REPORT

Generated 2026-10-14T12:20:44+05:30 by `python3 run.py build`. Every number below is computed from `progress.sqlite3` and the CSVs written in the same pass.

## Headline

| Metric | Count |
|---|---|
| Listings in research pool (in scope after discovery) | 20254 |
| Businesses researched (after dedupe) → `jewelry_all.csv` | 13811 |
| Qualified (2 of 3) → `jewelry_qualified.csv` | 365 |
| Qualification rate | 2.6% |
| Websites crawled OK / attempted | 9705 / 11625 |
| Listings with an owner/decision-maker name | 2881 |
| LinkedIn searches by outcome | ambiguous: 182, match: 110, none: 383, reject: 44 |

## Fill rate per field

| # | Column | all.csv | qualified.csv |
|---|---|---|---|
| 1 | Business | 13811 (100.0%) | 365 (100.0%) |
| 2 | Segment | 13811 (100.0%) | 365 (100.0%) |
| 3 | Category (as listed) | 13788 (99.8%) | 365 (100.0%) |
| 4 | Phone | 13061 (94.6%) | 359 (98.4%) |
| 5 | Email | 2822 (20.4%) | 357 (97.8%) |
| 6 | LinkedIn Profile | 101 (0.7%) | 94 (25.8%) |
| 7 | Contact Person | 1403 (10.2%) | 194 (53.2%) |
| 8 | Role | 1403 (10.2%) | 194 (53.2%) |
| 9 | Website | 10708 (77.5%) | 365 (100.0%) |
| 10 | Address | 13291 (96.2%) | 362 (99.2%) |
| 11 | Real City | 11727 (84.9%) | 318 (87.1%) |
| 12 | Real State | 11824 (85.6%) | 317 (86.8%) |
| 13 | Market | 13811 (100.0%) | 365 (100.0%) |
| 14 | Lead Origin | 13811 (100.0%) | 365 (100.0%) |
| 15 | Rating | 3706 (26.8%) | 183 (50.1%) |
| 16 | Reviews | 3706 (26.8%) | 183 (50.1%) |
| 17 | Source | 13811 (100.0%) | 365 (100.0%) |
| 18 | Signals | 13811 (100.0%) | 365 (100.0%) |
| 19 | Match Type | 13811 (100.0%) | 365 (100.0%) |
| 20 | Email Source | 2822 (20.4%) | 357 (97.8%) |
| 21 | LinkedIn Source | 101 (0.7%) | 94 (25.8%) |
| 22 | Found At | 13811 (100.0%) | 365 (100.0%) |
| 23 | Also Listed As | 1665 (12.1%) | 104 (28.5%) |
| 24 | Other Markets | 351 (2.5%) | 39 (10.7%) |
| 25 | Merged Listings | 2981 (21.6%) | 163 (44.7%) |
| 26 | Flags | 1686 (12.2%) | 75 (20.5%) |
| 27 | Mobile Candidates | 378 (2.7%) | 281 (77.0%) |
| 28 | Socials | 2749 (19.9%) | 320 (87.7%) |

## Qualification components

| Signal | Businesses | Rate |
|---|---|---|
| email | 2822 | 20.4% |
| linkedin | 101 | 0.7% |
| direct-line | 378 | 2.7% |
| role-email | 1209 | 8.8% |
| gia | 755 | 5.5% |
| ags | 93 | 0.7% |
| ja | 50 | 0.4% |
| bench | 463 | 3.4% |
| custom-design | 1976 | 14.3% |
| since-yyyy | 2393 | 17.3% |

## Per market

| Market | Listings | Businesses | Email | Owner name | LinkedIn | Qualified |
|---|---|---|---|---|---|---|
| New York, NY | 1442 | 1226 | 282 | 97 | 11 | 36 |
| Los Angeles, CA | 1280 | 1032 | 234 | 77 | 8 | 31 |
| Chicago, IL | 993 | 686 | 154 | 65 | 5 | 19 |
| Houston, TX | 1030 | 697 | 142 | 55 | 5 | 21 |
| Dallas, TX | 722 | 485 | 90 | 58 | 5 | 8 |
| Miami, FL | 1024 | 731 | 163 | 67 | 5 | 34 |
| Atlanta, GA | 739 | 526 | 128 | 62 | 11 | 23 |
| Philadelphia, PA | 767 | 545 | 92 | 28 | 3 | 14 |
| San Francisco, CA | 732 | 446 | 124 | 67 | 3 | 11 |
| Boston, MA | 570 | 345 | 109 | 56 | 7 | 18 |
| Seattle, WA | 589 | 347 | 93 | 68 | 2 | 10 |
| Las Vegas, NV | 691 | 403 | 75 | 75 | 3 | 12 |
| Phoenix, AZ | 730 | 469 | 95 | 59 | 0 | 12 |
| San Diego, CA | 591 | 380 | 80 | 33 | 3 | 8 |
| Denver, CO | 551 | 334 | 105 | 86 | 5 | 12 |
| Washington, DC | 382 | 226 | 76 | 33 | 1 | 6 |
| Detroit, MI | 554 | 378 | 82 | 51 | 6 | 18 |
| Minneapolis, MN | 531 | 246 | 62 | 92 | 6 | 9 |
| Charlotte, NC | 350 | 210 | 48 | 41 | 2 | 5 |
| Nashville, TN | 341 | 187 | 47 | 54 | 4 | 4 |
| Scottsdale, AZ | 263 | 150 | 36 | 25 | 1 | 5 |
| Naples, FL | 274 | 154 | 46 | 22 | 1 | 6 |
| Greenwich, CT | 141 | 82 | 27 | 6 | 1 | 6 |
| Palm Beach, FL | 445 | 259 | 67 | 23 | 2 | 9 |
| Beverly Hills, CA | 625 | 458 | 110 | 27 | 1 | 13 |
| Austin, TX | 370 | 211 | 31 | 26 | 0 | 2 |
| San Antonio, TX | 364 | 232 | 3 | 9 | 0 | 0 |
| Fort Worth, TX | 269 | 193 | 10 | 3 | 0 | 0 |
| San Jose, CA | 240 | 166 | 10 | 0 | 0 | 1 |
| Sacramento, CA | 145 | 104 | 1 | 0 | 0 | 0 |
| Portland, OR | 254 | 185 | 29 | 5 | 0 | 0 |
| Salt Lake City, UT | 143 | 110 | 20 | 3 | 0 | 1 |
| Kansas City, MO | 147 | 108 | 7 | 1 | 0 | 0 |
| St. Louis, MO | 242 | 155 | 0 | 1 | 0 | 0 |
| Columbus, OH | 44 | 17 | 0 | 0 | 0 | 0 |
| Cleveland, OH | 284 | 184 | 29 | 3 | 0 | 2 |
| Cincinnati, OH | 152 | 108 | 8 | 2 | 0 | 0 |
| Indianapolis, IN | 154 | 112 | 27 | 7 | 0 | 5 |
| Pittsburgh, PA | 232 | 183 | 18 | 4 | 0 | 1 |
| Baltimore, MD | 174 | 143 | 0 | 0 | 0 | 0 |
| Orlando, FL | 0 | 0 | 0 | 0 | 0 | 0 |
| Tampa, FL | 167 | 134 | 19 | 0 | 0 | 2 |
| Fort Lauderdale, FL | 255 | 206 | 36 | 7 | 0 | 0 |
| Raleigh, NC | 157 | 111 | 7 | 5 | 0 | 1 |
| New Orleans, LA | 200 | 147 | 0 | 0 | 0 | 0 |

## Per source (Lead Origin)

| Source | Listings | Businesses (as base row) | Qualified |
|---|---|---|---|
| Google Maps | 3557 | 2180 | 118 |
| YellowPages | 12824 | 9551 | 134 |
| BBB | 2602 | 1295 | 97 |
| OpenStreetMap | 1367 | 785 | 16 |

Discovery tasks completed: bbb=789, gmaps=139, osm=28, yp=635

## dropped_out_of_scope

Kill-list and scope drops, by reason and by the stage that caught them (discovery = before any crawl, site-check = site title/description/h1, builder = second pass immediately before writing). These rows are not shipped anywhere.

| Reason | discovery | site-check | builder | Total |
|---|---|---|---|---|
| appraiser-lab-insurer | 81 | 0 | 35 | 116 |
| beads-craft | 559 | 39 | 3 | 601 |
| chain | 3875 | 0 | 0 | 3875 |
| coin-currency | 290 | 8 | 0 | 298 |
| costume-fashion | 518 | 163 | 35 | 716 |
| diamond-trade | 145 | 32 | 7 | 184 |
| gold-buyer | 251 | 40 | 12 | 303 |
| kiosk-battery | 10 | 0 | 0 | 10 |
| no-segment | 0 | 0 | 880 | 880 |
| pawn | 902 | 48 | 15 | 965 |
| piercing-tattoo | 665 | 46 | 15 | 726 |
| simulants | 7 | 35 | 4 | 46 |
| thrift-consignment | 62 | 0 | 0 | 62 |
| trade-association | 3 | 0 | 0 | 3 |
| wholesale-manufacturer | 86 | 10 | 1 | 97 |
| **all** | | | | **8882** |

## What blocked the run

| Stage | Kind | Count | Example |
|---|---|---|---|
| builder | final-kill | 2578 | bbb:1fc7a0b0fac80fee: appraiser-lab-insurer |
| crawl | egress-blocked | 237 | https://3dnailspa.com: egress-blocked 3dnailspa.com: HTTPSConnectionPool(host='3dnailspa.com', port=443): Max retries exceeded with url: / ( |
| bbb | blocked | 184 | http-200 or challenge page at https://www.bbb.org/search?find_country=USA&find_text=Jewelry+Stores&find_loc=New+York%2C+NY&find_type=Categor |
| osm | error | 34 | https://overpass-api.de/api/interpreter: https://overpass-api.de/api/interpreter: ('Connection aborted.', ConnectionResetError(104, 'Connect |
| yp | soft-block-503 | 18 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Austin%2C+TX&page=1 |
| linkedin | blocked | 15 | http-200 or challenge page at https://www.google.com/search?q=%22Rachel+Clinnick-Barbagelata%22+San+Francisco+linkedin&hl=en&num=10 |
| osm | http-406 | 14 | https://overpass-api.de/api/interpreter |
| osm | http-504 | 13 | https://maps.mail.ru/osm/tools/overpass/api/interpreter |
| trade | blocked | 2 | http-403 or challenge page at https://www.americangemsociety.org/find-a-jeweler/?location=Los+Angeles%2C+CA |
| yp | soft-block-404 | 2 | https://www.yellowpages.com/search?search_terms=jewelers&geo_location_terms=Los+Angeles%2C+CA&page=30 |

Expected ceilings from earlier measured runs: about 19% owner names, about 12% emails, about 9% personal LinkedIn, and about 2% of researched businesses clearing 2 of 3.
