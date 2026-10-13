# Research-agent brief — diamond trade lead run

You are one of several research workers. The sandbox shell has NO direct internet
(the egress proxy blocks Google/Bing/YP/BBB/LinkedIn/etc.). Use ONLY the
`WebSearch` and `WebFetch` tools for the web. Do not try curl/playwright.

## Target — US diamond TRADE only
Diamond wholesalers, importers/exporters, loose-diamond dealers, brokers, cutters/polishers,
manufacturers, certified-stone traders (GIA/IGI/HRD), lab-grown growers/distributors,
trade diamond & estate-stone buyers, bridal specialists that source their OWN loose stones,
diamond jewelry manufacturers / casting houses.

OUT of scope (record as dropped, see below — never as a lead):
plain retail jewelry stores that only sell finished pieces they buy in, repair shops,
goldsmiths, costume jewelry; chains/e-tail (Blue Nile, James Allen, Brilliant Earth, Zales, Kay,
Jared, Signet, Tiffany, Ritani, With Clarity, Clean Origin, VRAI, Shane Co, Helzberg, Ben Bridge,
Pandora, Swarovski...); gemstone-only dealers with no diamond line;
pawn / cash-for-gold / gold buyers / scrap / bullion / refinery; coin & currency; beads / findings /
jewelry supply / craft; costume / fashion jewelry; piercing / tattoo / permanent jewelry;
kiosks / battery / mall carts; simulants (moissanite, CZ, "diamond alternative" — lab-GROWN is fine);
department-store counters; thrift/consignment; appraisers / gem labs / insurers with no inventory.
Apply this BEFORE spending fetches on a business.

## NEVER FABRICATE
Every value you record must have been seen by you in a tool result in this session.
No phone, email, name, address, or URL from memory. Do not construct LinkedIn URLs — only record
a `linkedin.com/in/...` URL that literally appeared in a WebSearch/WebFetch result.
If a field is unknown leave it "" / []. A short honest file beats a padded one.

## Method (person-first where possible)
1. Discovery: WebSearch queries like `"diamond dealer" "47th Street" LinkedIn`,
   `diamond wholesaler <building/street address>`, `loose diamonds wholesale <city>`,
   `<building name> tenants diamond`, `"diamond" owner OR president linkedin <city>`.
   (`site:` is not reliably honoured — phrase queries naturally.)
   Also WebFetch building tenant lists / directory pages / exhibitor lists when you find them.
2. For each candidate business: WebFetch its website `/`, and `/contact`, `/about`
   (or `/about-us`, `/our-story`, `/team`) as available. Ask WebFetch to return VERBATIM:
   all `mailto:` addresses and emails in text, ALL `tel:` hrefs and phone numbers, social links
   (facebook/instagram/x), owner/founder/president/partner/principal names + titles,
   street address + suite, memberships (DDC, DMIA, JBT, RapNet, IDEX, AGS, AGTA, bourse, GIA GG),
   "since 19xx" / generations, lab-grown vs natural, melee vs large stones.
3. Owner name known → WebSearch `"<First Last>" "<Company>" LinkedIn`. Record the
   linkedin.com/in/ URL only if a result clearly is that person (name match + company/diamond
   context). Never a /company/ page, never a vanity slug that is just the business name.
   Do this for every business where you have an owner name, even if you already have an email.
4. Budget: aim for 25-45 researched businesses. Stop when your cluster is exhausted and say so.

## Output — one JSON file per business
Write with the Write tool to `leadrun_diamonds/raw/<YOUR_DIR>/<slug>.json` (slug = lowercase
business name, a-z0-9 and dashes). Re-writing the same slug overwrites (idempotent). Schema:

```json
{
  "business": "Exact name as listed",
  "category_as_listed": "category string the SOURCE used, verbatim (e.g. 'Diamond Dealer', 'Jewelry Wholesaler', 'Jeweler'); '' if source shows none",
  "phone": "main listed number as found",
  "email": "one real address or ''",
  "email_source": "exact URL the email was read from",
  "linkedin_url": "https://www.linkedin.com/in/... or ''",
  "linkedin_source": "the search/query or URL where that LinkedIn URL appeared",
  "contact_person": "First Last or ''",
  "role": "Owner|President|Founder|CEO|Manager|Partner|Principal|Member|Featured On About Page or ''",
  "contact_source": "URL where the name was read",
  "website": "https://root-domain or ''",
  "address": "street address as listed",
  "city": "real city", "state": "2-letter",
  "market": "search market, e.g. 'New York, NY'",
  "lead_origin": "LinkedIn|Trade Directory|Building Directory|Google Maps|YellowPages|BBB|Web Search|Trade Show",
  "rating": "", "reviews": "",
  "source_url": "REQUIRED — the real URL that produced this row",
  "tel_numbers": ["every number found as tel: link / phone on the business's OWN site or socials"],
  "tel_source": "URL those numbers came from",
  "socials": ["https://facebook.com/...", "https://instagram.com/..."],
  "building": "e.g. International Gem Tower", "suite": "e.g. Ste 2204",
  "trade_memberships": ["DDC", "RapNet", "GIA", ...],
  "hooks": ["gia-gg", "since-1982", "3rd-generation", "lab-grown", "natural", "melee", "large-stones", "manufacturer", "importer"],
  "is_diamond_trade": true,
  "scope_reason": "one line: why it is (or is not) diamond trade, from what the site/source says",
  "drop_reason": ""
}
```

Out-of-scope businesses you looked at: still write a file with `"is_diamond_trade": false` and
`"drop_reason"` set to one of: pawn, cash-for-gold, coin, beads-craft, costume-fashion, piercing,
kiosk, simulant, chain, thrift, appraiser-lab, retail-only, gemstone-only, other. Keep those files
minimal (business, source_url, drop_reason, scope_reason, market).

Finish with a short summary: files written, in-scope count, emails found, LinkedIn found,
which clusters/buildings you exhausted, and what blocked you.

## Wave-2 rules (learned from wave 1)
- **WebFetch is broken in this environment (DNS ENOTFOUND on every host).** Do not call it more than once.
  Work from WebSearch results only.
- **Budget: max 30 WebSearch calls for you.** The 200/turn budget is shared by all workers. Count them.
- **LinkedIn profiles mostly appear in `mode: "extended"` searches** — use extended for person lookups
  (e.g. `"<First Last>" <Company> diamonds LinkedIn`), standard for discovery.
- **Do NOT write helper scripts into the shared scratchpad** (wave-1 workers overwrote each other's `w.py`).
  Write each business file directly with the Write tool to your own `raw/<YOUR_DIR>/` folder. Before
  finishing, check that every file in your folder has your market.
- Emails in search summaries are often obfuscated ("[email protected]") — never reconstruct one.
- Skip businesses already researched: check `ls leadrun_diamonds/raw/*/` for their slug first.

## Wave-3 rules (egress opened at 11:42 UTC)
- The sandbox shell can now reach the web. Fetch pages with Bash + Python `requests` (header
  `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36`,
  timeout 20) and parse with BeautifulSoup. Keep helper scripts in `leadrun_diamonds/work/<YOUR_DIR>/`
  only (never /tmp, never the shared scratchpad). Be polite: ≤2 requests/second per host.
- WebSearch still works for discovery/LinkedIn; WebFetch is still broken — don't use it.
- For every business with a website: fetch `/`, `/contact`, `/about` yourself and record `mailto:`
  emails and `tel:` numbers. `tel_source` must be ONLY the business's own page URL(s) — never mix a
  directory/Yelp URL into `tel_source` (the builder rejects mixed sources).
- `phone` = the number the directory lists; put every number from the business's own site in `tel_numbers`.

## Wave-4: verifying YellowPages listings (batch work)
You get a batch file `work/batches/batch_NN.json`: a list of {file, business, market, website, phone, emails}.
Each `file` is a raw/yp/*.json record. For EACH listing, edit that JSON file IN PLACE (read it, update
fields, write it back with python json — keep all other fields) and set `"verified": true`.

1. **Scope verdict** — fetch the business's own site (`/`, `/about`, `/about-us`, `/our-story`, `/contact`)
   with Bash+requests. Diamond TRADE = wholesale / "to the trade" / loose diamonds / importer / manufacturer /
   cutter / broker / lab-grown grower or distributor / bridal specialist sourcing its own loose stones /
   trade estate-diamond buyer / bourse member. A shop that only sells finished jewelry it buys in, repair,
   pawn, gold buying, watches, simulants → `is_diamond_trade: false`, `drop_reason` (retail-only, pawn,
   cash-for-gold, simulant, chain, other). Dead / parked site → leave is_diamond_trade as is, add
   `"scope_reason": "unverified: site unreachable"` and still set verified=false (don't set true).
   Put one honest sentence in `scope_reason` quoting what the site says.
2. **Owner** — name + title from the About/Team page (or BBB/state filing if the site has none):
   `contact_person`, `role` (Owner/President/Founder/CEO/Partner/Manager), `contact_source` (URL).
3. **LinkedIn** — only if you have a First Last owner name: WebSearch (mode "extended")
   `"First Last" <Business> LinkedIn`. Record `linkedin_url` only if a linkedin.com/in/ URL literally appears
   and the result ties the name to this business. `linkedin_source` = the query. Never a /company/ page,
   never a slug that is just the business name.
4. Also capture from the site when present: `email` + `email_source` (mailto on own domain), extra numbers
   into `tel_numbers` with `tel_source` = own page URL(s) only, `socials`, `trade_memberships`
   (GIA, AGS, JBT, DDC, RapNet, IDEX, bourse...), `hooks` (since-19xx, 3rd-generation, lab-grown, melee...).
Budget: ≤ 40 WebSearch calls per batch; ≤ 2 req/s per host. Never invent anything.
Finish with: verified count, in-scope / dropped counts, owners found, LinkedIn found.
