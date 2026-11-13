# Europe worker report — eu_5

Markets: **Milan, Italy** and **Valenza, Italy**. Method: RJC member sitemap (Valenza/Milan members),
europages + reteimprese trade directories, Italian-language web search, and per-business fetches of each
company's own site (/, /contatti, /chi-siamo) for mailto:/tel:. LinkedIn only where a linkedin.com/in URL
literally appeared and tied to the business. Nothing fabricated.

## Results (after `ingest.py` + `build.py`, counted in diamonds_qualified.csv)

| Market | Businesses researched (unique) | QUALIFIED (2-of-3) | with email | with personal LinkedIn |
|---|---|---|---|---|
| Valenza, Italy | 36 | **15** | 14 | 8 |
| Milan, Italy | 16 | **6** | 6 | 1 |

raw/eu_5/: 52 in-scope JSON + 7 dropped (out-of-scope).

### Valenza — 15 qualified (target 15+ met)
Alberti Gioielli, Catananti, Crivelli, Dalila Gioielli, Eurodiam, Filostil, Giorgio Visconti,
I By Iannelli, Italgold (ITG), Lenti & Villasco, Luca Carati, Newbril, Orsini, Ricci Gioielli,
Staurino Fratelli. Mix of loose-diamond wholesalers/cutters (Newbril, Eurodiam, Catananti, Namdar,
Taglieria Pietre Preziose) and high-jewellery houses that source their own stones. Personal
linkedin.com/in captured for owners/directors of Alberti (Massimo Cova), Filostil (Giorgia Cattelan),
Italgold, Lenti & Villasco (Danilo Lenti), Staurino (Stefano Staurino), Eurodiam (Andrea Pasquarelli),
Raselli/Errepi (Andrea Raselli), Catananti (Didier Catananti).

### Milan — 6 qualified
Algerini, D&D Diamonds, Diamitaly, Levidiam, Marte Gioielli, Sabbadini (Micol Sabbadini LinkedIn).
Strong diamond-trade core: D&D (wholesale since 1975, Antwerp/Tel Aviv), Levidiam (wholesale since 2002,
Valenza office), Maino (importer, IGI president — 1 signal only), Natural Diam (GIA/IGI loose, WhatsApp
only), Osigem/Forever Unique (De Beers IIDGR). Several good Milan trade firms reached only 1 verifiable
signal: Maino, Osigem, Taj, Conte, Lattanzio, Real Diamond Invest, Garatti, Cristalgemm, Natural Diam,
Diamonds4C — they publish an email OR one line but no distinct second line and no public
linkedin.com/in for a named owner, so they stayed in scope but short of the 2-of-3 bar.

## Dropped (out of scope, with reason)
Petramundi, Sanda (gemstone-only); BMC (LVMH captive) ; Vendorafa (now Gismondi, Genoa); Manglam,
Golconda, Gioie 1978 (gemstone/costume/retail).

## What blocked more
- WebFetch broken; paginegialle/paginebianche/virgilio return 403 to the sandbox, so directory phone
  pages were unusable — relied on reteimprese + europages + company sites.
- The 2-of-3 bar in Milan: many genuine diamond dealers list only a single landline and an info@ email,
  with no personal LinkedIn indexable, capping Milan qualified at 6 despite 16 researched.
- Business registers (visura camerale) that hold administrators' names are paywalled, so several owner
  names stayed company-page level without a linkable profile.
