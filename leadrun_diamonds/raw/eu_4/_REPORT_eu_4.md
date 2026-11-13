# Europe worker report — OUT=eu_4

Markets: **Geneva, Switzerland** and **Zurich, Switzerland**
Diamond-TRADE lead run. Every value was seen in a WebSearch/WebFetch(Bash+requests) result this session; nothing fabricated.

## Summary by city

### Geneva, Switzerland
- Businesses written: **39** files (31 in-scope diamond trade, 8 dropped).
- Emails (own-site / directory): **20** in-scope. Named owners/contacts: **15**. Personal LinkedIn /in/ recorded: **5**.
- **Qualified (2-of-3 per builder): 4** — Boghossian SA, DiamAlps (Yazam Sàrl), Horovitz et Totah SA, Oselieri-Racine SA.
  - Note: Manuel Bouvier has own-site email **and** a real personal linkedin.com/in URL, but the builder rejects the LinkedIn because the firm's name *is* the person's name (slug == business). It is genuinely 2-of-3 in substance.
- Sources used: Responsible Jewellery Council member sitemap (Swiss SA/AG/Sàrl filter), GemGenève 2026 exhibitor list (Swiss exhibitors), local.ch / search.ch Geneva "diamantaires / pierres précieuses / diamants" directories, then each firm's own /, /contact, /about pages via Bash+requests, and LinkedIn via WebSearch extended.
- In scope captured: diamond wholesalers/traders, cutters/polishers, estate-diamond buyers and high-jewellery houses sourcing their own stones (Vernain, Golay Fils & Stahl, Bomare, Belfont, BenGems, Abouchar, Faerber-Collection, Diarough Geneva, SwissDiam, Gemcut, Boghossian, Chatila, Eurostar Diamonds Suisse, JFS Diamond, Diamond Sky, Golcondia, LP Lapidaires, Emilio Gindraux, Niru Swiss, Manobla, Astra Diamants, Platin'or, Alfion, Daniel Fehlmann, G. Torroni, DiamAlps, Oselieri-Racine, Horovitz & Totah, Manuel Bouvier).
- Dropped (recorded): gemstone-only (SEBEX, Filippo G&G, AGD Trading, Yvon Gindre, F. Torroni), other (Sudamerica Stones = mineral shop, Diatheke = watch-case finishing, KARAT/Diamant-Gems = Paris firm with only a Geneva "partner").

### Zurich, Switzerland
- Businesses written: **16** files (11 in-scope, 5 dropped).
- Emails: **11** in-scope. Named owners/contacts: **7**. Personal LinkedIn /in/ recorded: **4**.
- **Qualified (2-of-3): 6** — David & Sohn AG, Edigem Fine Jewels AG, Green World Diamonds AG, Harry Hofmann AG, Vintage Jewellery (Hedley Prynn), Diamond Online (N. Karouni).
- In scope captured: David & Sohn (diamantaire since 1917), Edigem (Gübelin subsidiary, estate diamonds), Green World Diamonds (lab-grown, loose + B2B), Diamond Online (bourse-price loose diamonds + Andkstone B2B), Harry Hofmann (estate diamond buyer), Vintage Jewellery, Vintage Diamonds (Christophe Walser), van Loggem Diamantenhandel AG (Baar/Zug — diamond wholesaler, nearest hub to Zurich), Natural Color Diamonds GmbH (Egg), Rabinowitsch AG, Blum Juwelier (GIA maker), AGUAdeORO (Geneva+Zurich ethical bridal, own-sourced stones).
- Dropped: 77 Diamonds (UK e-tail chain), Isler/Schmuckmarkt (cash-for-gold), Crystal Art Gallery (mineral/crystal gallery), Beatrice Rossi (retail-only), Kapur Jewels (gold/zirconia reseller).

## What blocked higher qualified counts
- The Swiss diamond trade is small and **bourse/appointment-based**: many RJC-listed Geneva traders (Diamond Sky, Golcondia, LP Lapidaires, Emilio Gindraux, Niru, JFS) publish **no website and no email** — only an RJC forum line and (sometimes) a directory phone. They are recorded in-scope but can't reach 2-of-3.
- Personal linkedin.com/in URLs are rarely indexed for these owners; I only recorded ones that literally appeared in a WebSearch result and tie to the named person + firm. I did **not** construct any LinkedIn URL, and did not record /company/ pages or business-name slugs.
- Most firms list a single main line (plus a fax), so a "direct line ≠ main line" third signal was usually unavailable from own sites.
- Phones for directory-only firms come from local.ch/search.ch (recorded as `phone`, not as own-site `tel_numbers`), per the schema.

## Budget
~50 WebSearch calls; website fetches via Bash+requests (CA bundle). Scratch scripts in work/eu_4/ only. Committed only raw/eu_4/, pushed to leadrun/eu-4 in batches.
