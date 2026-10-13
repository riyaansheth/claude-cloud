## What blocked this run (read first)

1. **Sandbox egress policy denies every scraping host.** From the container, `curl`/`requests`/Playwright got
   HTTP 403 from the egress proxy for www.google.com, html.duckduckgo.com, www.bing.com, www.yellowpages.com,
   www.bbb.org, www.linkedin.com, ddcny.com, overpass-api.de, every business website, and even example.com.
   Only package registries and GitHub are allowed. So the plain concurrent Python/Playwright workers could not
   run; `scripts/crawl.py` is written and tested but recorded all 49 business sites as `unreachable`.
   Fix: environment settings → Network access → broader level, or add the hosts under Allowed domains
   (https://code.claude.com/docs/en/cloud-environments#network-access), then
   `python3 scripts/crawl.py --retry-unreachable && ./run.sh`.
2. **Fallback channel was server-side WebSearch/WebFetch via 8 research agents.** WebFetch failed with
   `getaddrinfo ENOTFOUND` on every domain for the whole run, so **no company site, /contact page, tenant
   roster or directory profile was ever opened**. Every value comes from search-result summaries, which
   obfuscate emails ("[email protected]"). That is why email and direct-line fill are ~0.
3. **WebSearch is capped at 200 calls per turn shared by all agents**; the 8 workers exhausted it after
   ~25 queries each. The search tool also declined most "<person> LinkedIn" lookups.
4. **Push to GitHub was refused (403):** the Claude GitHub App has no access to riyaansheth/claude-cloud.
   Commits exist locally on branch `claude/sweet-cerf-k5mpge` only.

**Consequence: 0 rows clear the 2-of-3 bar.** The pool below is real (every row has a real source URL)
but it is a discovery list, not a qualified sheet. Nothing was padded or relabelled to raise the count.
One row (DVG Diamonds) briefly scored 2 of 3 until the builder was tightened: its second number came from
Yelp, not its own site, so it does not count as a direct line.

## Cluster status

Wave 1 = 8 agents; wave 2 = 6 agents (unstarted cities + NYC DMIA people), web-search only.

| Market | Cluster | Status |
|---|---|---|
| New York, NY | International Gem Tower (50 W 47th) | Partial — tenants from 2010-14 news; no roster reachable |
| New York, NY | 580 Fifth Ave / DDC | Partial — DDC has no public member list; nyddc.com unfetchable |
| New York, NY | 1 / 10 / 20 / 22 W 47th | Searched, no in-scope leads surfaced (20/22 only retail, dropped) |
| New York, NY | 15 / 30 / 36 / 45 / 62 W 47th | Partial |
| New York, NY | DMIA officers/board (person-first) | Partial — 10 named board members still need LinkedIn/company lookup |
| Los Angeles, CA | International Jewelry Center 550 S Hill / Diamond Club West Coast | Partial — DCWC directory (diamondclubwestcoast.com/company-directory-2/) unreadable |
| Los Angeles, CA | 650 / 607 S Hill | Partial; 640 S Hill and 220 W 5th St: nothing surfaced |
| San Diego, CA | 861 6th Ave Jewelry Exchange + city | Wave 2: exhausted as far as search allows (no tenant roster) |
| Miami, FL | Seybold Building 36 NE 1st St | Partial — directory A–J only; seyboldjewelry.com/full-directory/ unfetchable |
| San Juan, PR | — | Wave 2: **exhausted** — no true wholesalers, retail only |
| Chicago, IL | Mallers Building 5 S Wabash, 29 E Madison | Partial (31 tenants) |
| Chicago, IL | 55 E Washington | Searched — no diamond dealer surfaced |
| Boston, MA | 333 Washington (Jewelers Bldg) | Wave 2: partial — ~15 of 100-155 tenants surfaced |
| Boston, MA | 387 Washington | Wave 2: largely exhausted |
| Philadelphia, PA | Sansom St 700 block | Wave 2: largely exhausted for 720-740 Sansom; 740 Sansom roster and 8th St side incomplete |
| Detroit, MI | Greenfield Rd (Southfield / Oak Park) | Wave 2: exhausted for search; Michigan Ave cluster not found |
| Minneapolis, MN | — | Wave 2: **exhausted** — very few trade firms |
| Denver, CO | Denver Mart showrooms | Wave 2: mostly exhausted (roster may date from 2019) |
| Dallas, TX | Dallas Market Center Diamond District (WTC 7th floor) | Partial; Preston Center, Thanksgiving Tower not started |
| Houston, TX | 6222 Richmond Ave / Post Oak | Wave 2: Post Oak/Galleria **exhausted** — no wholesale offices; trade is on Richmond Ave |
| Atlanta, GA | Tower Place 100 / 3344 Peachtree | Wave 2: **exhausted** for search |
| Charlotte, NC | — | Wave 2: near exhausted — importing retailers only |
| Washington, DC | DC / Bethesda / Rockville / Silver Spring | Wave 2: partial |
| San Francisco, CA | Phelan Building 760 Market, 101 Post | **Exhausted** — no diamond tenants remain (trade moved to 888 / 868 Brannan) |
| San Francisco, CA | 888 / 868 Brannan | Partial |
| Seattle, WA | Joshua Green Bldg 1425 4th Ave | Wave 2: **exhausted** — no diamond tenants since 2008; cluster is 1424 4th Ave (partial) |
| Phoenix / Scottsdale, AZ | — | Wave 2: YP wholesale listings largely covered |
| Las Vegas, NV (local) | — | Wave 2: **exhausted** — no trade-only local wholesaler found |
| Trade shows (JCK, AGTA, Couture, JIS, Atlanta) | — | Not reachable; JA Las Vegas 2026 supplier PDF identified as next fetch |
| Directories (JBT, 24karat, AGS, NDC, DCA, RapNet/IDEX) | — | Not reachable |

## Caveats on the pool
- Several rows are flagged in their raw `scope_reason` as thin evidence (in scope on name + trade-building
  address only): e.g. Delicate Gem, Brichelle, Loose Diamond Exchange, Abe Mor (NYC); Diamond Headquarters,
  Diamond Images USA, E&S House of Diamonds, French Diamond Jewelry, Gems & Diamonds, Belgium Diamonds, BBY
  Diamonds (Miami); Inter Diamond, Starlight Diamonds, B&J Diamond, VHS Diamond (LA); Bitton, B V Gems (Dallas).
  Borderline retail-facing: Buchwald Jewelers (Miami), Diamonds on Wabash, Tucker (Chicago).
- Some tenancy data is from 2008-2014 articles; Derco (SF) may be in Chapter 11; Rising Star Diamonds (LA) may be closed.
- `Found At` is the first-ingest timestamp of the raw record into progress.sqlite3.
- `Category (as listed)` is blank where the search result showed no category — not normalised or invented.
