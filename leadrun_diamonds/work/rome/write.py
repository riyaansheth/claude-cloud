import json,os
OUT='/home/user/claude-cloud/leadrun_diamonds/raw/rome_it'
BASE=dict(business="",category_as_listed="",phone="",email="",email_source="",linkedin_url="",linkedin_source="",contact_person="",role="",contact_source="",website="",address="",city="Rome",state="RM",market="Rome, IT",lead_origin="Web Search",rating="",reviews="",source_url="",tel_numbers=[],tel_source="",socials=[],building="",suite="",trade_memberships=[],hooks=[],is_diamond_trade=True,scope_reason="",drop_reason="")
L=[]
def add(slug,**k):
    d=dict(BASE); d.update(k); L.append((slug,d))
add("banco-diamanti",business="Banco Diamanti",category_as_listed="Compro Diamanti / valutazione diamanti",phone="800 926 095",
 email="info@bancodiamanti.com",email_source="https://www.bancodiamanti.com/contattaci/",
 linkedin_url="https://www.linkedin.com/in/andrea-barbi-7b8804/",linkedin_source='WebSearch extended: "Andrea Barbi" "Diamanti Anversa" LinkedIn (result title: "Andrea Barbi - www.diamantianversa.com www.bancodiamanti.com")',
 contact_person="Andrea Barbi",role="Founder",contact_source="https://www.diamantianversa.com/andrea-barbi/ (founder of sister company Diamanti Anversa; his LinkedIn headline lists bancodiamanti.com)",
 website="https://www.bancodiamanti.com",address="Via Pasquale Stanislao Mancini 7, 00196 Roma (also Hoveniersstraat 30, 2018 Antwerp)",
 lead_origin="LinkedIn",source_url="https://www.bancodiamanti.com/contattaci/",
 tel_numbers=["+39 393 388 9754","800 926 095"],tel_source="https://www.bancodiamanti.com/contattaci/",
 hooks=["estate-diamond-buyer","antwerp-office","gemologists-GIA-HRD-IGI","appointment-only","broker"],trade_memberships=["GIA","HRD","IGI"],
 scope_reason="Site: 'si occupa di compravendita e valutazione di diamanti'; buys used diamonds and resells into an international trade circuit (commission paid by buyer); Rome office + Antwerp Hoveniersstraat office. Also buys gold/watches, so diamond-focused estate buyer/broker, not a plain compro oro.")
add("atelier-diamanti-e-gioielli",business="L'Atelier Diamanti e Gioielli (BDC Studio Srl)",category_as_listed="Diamond and Jewellery Atelier",phone="+39 3313395979",
 email="info@atelierdiamanti.com",email_source="https://atelierdiamanti.com/en/pages/contact",
 linkedin_url="https://www.linkedin.com/in/flavia-stella/",linkedin_source="WebSearch extended: \"Fabio D'Arrigo\" diamanti Roma LinkedIn (result title: 'Flavia Stella - L'Atelier- Diamanti e Gioielli')",
 contact_person="Flavia Stella",role="Founder",contact_source="https://atelierdiamanti.com/en/pages/diamond-gemology-and-jewelry-experts",
 website="https://atelierdiamanti.com",address="Via Appia Nuova, 59, 00183 Roma",source_url="https://atelierdiamanti.com/en/pages/contact",
 tel_numbers=["+39 3313395979","+39 3401491861"],tel_source="https://atelierdiamanti.com/en/pages/contact",
 socials=["https://www.instagram.com/atelierdiamantigioielli/","https://www.facebook.com/p/Atelier-Diamanti-Gioielli-61558126115628/"],
 hooks=["bridal","certified-GIA-IGI-HRD","short-supply-chain","bespoke","gemologist-founder","lab-grown","appointment-only","founded-2023"],
 scope_reason="Site: 'We acquire diamonds directly at the source' (short supply chain), certified GIA/IGI/HRD natural + lab-grown, bespoke engagement rings made in Rome; co-founded by gemologist Flavia Stella and Christie (ex sales mgr for an Italian 18kt/diamond wholesaler).")
add("diamanti-anversa",business="Diamanti Anversa",category_as_listed="Atelier del Diamante",phone="+39 327 3764799",
 email="info@diamantianversa.com",email_source="https://www.diamantianversa.com/contatti/ (Cloudflare-protected mailto, decoded from page HTML)",
 linkedin_url="https://www.linkedin.com/in/andrea-barbi-7b8804/",linkedin_source='WebSearch extended: "Andrea Barbi" "Diamanti Anversa" LinkedIn',
 contact_person="Andrea Barbi",role="Founder",contact_source="https://www.diamantianversa.com/team/",
 website="https://www.diamantianversa.com",address="Via Nizza, 118, 00198 Roma (foreign office: Hoveniersstraat 30, 2018 Antwerp)",
 lead_origin="LinkedIn",source_url="https://www.diamantianversa.com/team/",
 tel_numbers=["+39 327 3764799"],tel_source="https://www.diamantianversa.com/contatti/",
 socials=["https://www.facebook.com/diamantanversa","https://www.instagram.com/diamanti.anversa/","https://www.linkedin.com/company/diamanti-anversa/"],
 trade_memberships=["Antwerp Diamond Bourse (operates directly)","GIA","IGI","HRD"],
 hooks=["antwerp-office","bourse-direct","certified-GIA-IGI-HRD","bridal","rapaport-pricing","co-founder-Riccardo-Castellani","since-2011"],
 scope_reason="Team page: 'La nostra scelta di operare direttamente presso la Borsa dei Diamanti di Anversa'; sells loose certified natural diamonds priced off Rapaport plus own-production jewelry; Antwerp office. Only phone is the mobile main line (no separate direct line).")
add("diamondiamond",business="DiamonDiamonD (Diamondiamond Srl)",category_as_listed="Gioielli Unici, Diamanti Certificati",phone="06 6833289",
 linkedin_url="https://www.linkedin.com/in/andrea-falcioni-b96278165/",linkedin_source='WebSearch extended: "Andrea Falcioni" DiamonDiamonD gemmologo Roma LinkedIn (result title: "Andrea Falcioni - DiamonDiamonD")',
 contact_person="Andrea Falcioni",role="Owner",contact_source="https://diamondiamond.it/it/content/4-chi-siamo",
 website="https://diamondiamond.it",address="Via della Scrofa 73, 00186 Roma",lead_origin="LinkedIn",source_url="https://diamondiamond.it/it/content/4-chi-siamo",
 tel_numbers=["+39 06 683 3289","+39 328 709 4702 (WhatsApp link)"],tel_source="https://diamondiamond.it/it/contattaci",
 socials=["https://www.instagram.com/andrea_falcioni_ddd/"],trade_memberships=["HRD"],
 hooks=["investment-diamonds","wholesale-DBO-2013","blister-diamonds","hrd-gemologist","perito-tribunale-roma","own-goldsmiths","since-2003"],
 scope_reason="Chi siamo: owner Andrea Falcioni sells investment diamonds since 2003 and founded DBO (Diamond Business Opportunities) 'Ingrosso di diamanti a Roma' in 2013; DDD showroom adds hand-made jewelry. No email on site (contact form only).")
add("d-arrigo-diamanti-roma",business="D'Arrigo Diamanti Roma (FADA Gioielli Srl)",category_as_listed="Investimenti diamanti Roma",phone="+39 06 39031289",
 email="fabio.darrigo@email.it",email_source="https://www.darrigodiamantiroma.it/chi-siamo/",
 contact_person="Fabio D'Arrigo",role="Owner",contact_source="https://www.darrigodiamantiroma.it/chi-siamo/",
 website="https://www.darrigodiamantiroma.it",address="Viale dei Colli Portuensi, 594, 00151 Roma",source_url="https://www.darrigodiamantiroma.it/chi-siamo/",
 tel_numbers=["+39 06 39031289","+39 340 0751177"],tel_source="https://www.darrigodiamantiroma.it/chi-siamo/",
 hooks=["since-1951","3rd-generation","antwerp-bourse-direct","in-house-lab","lab-grown-CVD","investment-diamonds","gemology-degree"],
 scope_reason="Site: 'Fabio D'Arrigo acquista direttamente alla Borsa dei Diamanti di Anversa'; certified natural + CVD loose diamond search, internal lab; family business since 1951. Email is on a generic email.it address but published on own site; no LinkedIn found.")
add("orecad",business="OreCAD Srls",category_as_listed="Laboratorio orafo / Oreficeria di Roma",phone="06 8365 7935",
 email="oreficeria@orecad.it",email_source="https://orecad.it/contatti/",website="https://orecad.it",address="Via Rocca Priora, 27, 00179 Roma",
 source_url="https://orecad.it/diamanti-certificati/",tel_numbers=["06 8365 7935","+39 393 958 3777"],tel_source="https://orecad.it/contatti/",
 socials=["https://www.instagram.com/orecad.srls/","https://www.facebook.com/profile.php?id=100052680976367"],
 hooks=["since-1992","loose-certified-diamond-list-GIA-IGI-HRD","manufacturer","commission-work","CAD-wax","goldsmith-supplies-mountings"],
 scope_reason="Goldsmith lab since 1992 that publishes a priced list of loose certified diamonds (IGI/GIA/HRD, 0.10-0.91ct) and makes commissioned jewelry; also sells mountings/findings to goldsmiths. Owner name not shown on site; alt email gioielleria@orecad.it also on homepage.")
add("silvi-diamond",business="Silvi Diamond S.r.l.",category_as_listed="Diamonds and coloured gemstones trader, cutter and/or polisher",phone="06 6876297",
 email="silvidiamond@interfree.it",email_source="https://www.silvidiamond.com/",contact_person="Alessandro Silvestrini",role="Partner",contact_source="https://www.silvidiamond.com/ (sons Alessandro and Emanuele Silvestrini run the firm)",
 website="https://www.silvidiamond.com",address="Via del Leoncino, 16, 00186 Roma",lead_origin="Trade Directory",source_url="https://www.responsiblejewellery.com/member/silvi-diamond-s-r-l/",
 tel_numbers=["06 6876297"],tel_source="https://www.silvidiamond.com/",trade_memberships=["RJC","IGI","Israel Diamond Exchange (Long standing business relationship award)"],
 hooks=["since-1930s","3rd-generation","importer","loose-diamonds","fancy-shapes","laser-cutting","Bombay-cutting-partner","supplies-to-goldsmiths","IGI-gemologists-in-house"],
 scope_reason="RJC member (diamond trader/cutter); site: import-export of diamonds since the 1960s with main bourses, wide stock of loose brilliant and fancy cuts, cutting partnership in Bombay, supplies Roman jewelry brands. 06 6876552 on site is the fax, not a direct line; no LinkedIn found.")
add("diamond-house",business="Diamond House (ADM S.R.L.)",category_as_listed="Atelier romano di alta gioielleria",phone="+39 376 2974810",
 email="info@diamondhousejewels.com",email_source="https://www.diamondhousejewels.com/",contact_person="Alessandro de Maigret",role="Founder",contact_source="https://www.diamondhousejewels.com/atelier",
 website="https://www.diamondhousejewels.com",address="Via Ruggero Fauro 22, 00197 Roma (Parioli)",source_url="https://www.diamondhousejewels.com/atelier",
 tel_numbers=["+39 376 2974810"],tel_source="https://www.diamondhousejewels.com/",socials=["https://www.facebook.com/diamondhousejewels","https://www.instagram.com/diamondhouse.jewels","https://www.linkedin.com/company/diamond-house-jewels/"],
 trade_memberships=["GIA","IGI","HRD"],hooks=["bridal","stones-selected-personally-on-world-markets","gemologist-founders","bespoke","estate-buying","co-founder-Ludovica-Colambumbo"],
 scope_reason="Site: GIA/HRD/IGI stones 'selezionate personalmente nelle principali piazze mondiali', co-founder is 'Head of Stones Selection' (HRD/IGI-trained), bespoke manufacture in Rome; also buys jewels. Only one phone; no personal LinkedIn found.")
add("mercante-di-pietre",business="Mercante di Pietre S.r.l.",category_as_listed="Diamanti certificati, Pietre preziose e Anelli di fidanzamento",phone="+39 0697616739",
 email="ordini@mercantedipietre.com",email_source="https://mercantedipietre.com/policies/contact-information",contact_person="Enrico Terzo",role="Founder",contact_source="https://mercantedipietre.com/pages/chi-siamo",
 website="https://mercantedipietre.com",address="Via Ceresio 75, 00199 Roma",source_url="https://www.funweek.it/roma-news-curiosita-eventi/roma-ama-i-gioielli-ecco-chi-e-limprenditore-che-vende-oltre-1-milione-di-pietre-preziose-online/",
 tel_numbers=["+39 0697616739"],tel_source="https://mercantedipietre.com/policies/contact-information",socials=["https://www.instagram.com/mercantedipietre/"],
 trade_memberships=["IGI"],hooks=["ex-wholesale-calibrated-diamonds-Sparkline","IGI-Antwerp-gemologist","virtual-inventory-1M-stones","bespoke-via-Italian-labs","fancy-diamonds"],
 scope_reason="Founder previously wholesaled calibrated diamonds/colored stones (Sparkline brand, India sourcing); now sells certified loose diamonds (GIA/IGI/HRD) from a feed of 1M+ stones, no own warehouse. No LinkedIn found.")
add("oroproject-italia",business="Oroproject Italia S.r.l.",category_as_listed="Jewellery and watch manufacturer and/or wholesaler",phone="+39 06 9438494",
 email="info@oroproject.it",email_source="https://oroproject.it/contatti/",contact_person="Attilio Gelpi",role="Founder",contact_source="https://oroproject.it/azienda/",
 website="https://oroproject.it",address="Viale Somalia, 289, 00199 Roma",lead_origin="Trade Directory",source_url="https://www.responsiblejewellery.com/member/oroproject-italia-srl/",
 tel_numbers=["+39 06 9438494"],tel_source="https://oroproject.it/contatti/",trade_memberships=["RJC"],
 hooks=["since-1980","2nd-generation","manufacturer","contract-manufacturer-for-luxury-brands","diamond-analysis-CVD-HPHT-detection"],
 scope_reason="RJC jewellery manufacturer; site: master goldsmiths producing for 'grandi brand internazionali' since 1980, offers in-house natural-vs-synthetic diamond screening. No LinkedIn found.")
add("trepi-srl",business="TrePi Srl",category_as_listed="Jewellery and watch manufacturer and/or wholesaler",phone="+39 06 68136770",
 email="info@trepisrl.com",email_source="https://trepisrl.com/contatti/",website="https://trepisrl.com",address="Via Monte del Gallo, 26/A, 00165 Roma",lead_origin="Trade Directory",
 source_url="https://www.responsiblejewellery.com/member/tre-pi-srl/",tel_numbers=["+39 06 68136770"],tel_source="https://trepisrl.com/contatti/",trade_memberships=["RJC"],
 hooks=["manufacturer","high-jewelry-contract","stone-setting-pave","titanium-carbon"],
 scope_reason="RJC-certified high-jewelry manufacturing lab; site lists in-house stone setting (pavé etc.). Diamond use implied, not explicit. Owner not named on site.")
add("antinori-di-sanpietro",business="Antinori Di Sanpietro",category_as_listed="Alta Gioielleria · Roma",email="info@antinorijewels.com",email_source="https://www.antinorijewels.com/",
 website="https://www.antinorijewels.com",address="",source_url="https://www.antinorijewels.com/",tel_numbers=[],tel_source="",
 socials=["https://www.facebook.com/antinori.di.san.pietro/","https://www.instagram.com/antinoridisanpietro/"],
 hooks=["high-jewelry","GIA-large-stones","fancy-yellow","D-flawless","1stdibs-dealer","bespoke"],
 scope_reason="Rome high-jewelry maker sourcing exceptional stones itself ('Selezione personale di ogni pietra'), GIA-certified 5-15ct diamonds sold via 1stDibs. No phone, address or owner on site.")
for slug,name,src,web in [("roma-gem-cut-srls","Roma Gem Cut Srls","https://www.responsiblejewellery.com/member/roma-gem-cut-srls/",""),
                     ("c-paolillo-co-srl","C. Paolillo & Co SRL","https://www.responsiblejewellery.com/member/c-paolillo-co-srl/",""),
                     ("diamonds-4-u-srl","Diamonds 4 U S.R.L","https://www.responsiblejewellery.com/member/diamonds-4-u-s-r-l/","https://www.diamonds4ugroup.com"),
                     ("alice-m-srl","Alice M Srl","https://www.responsiblejewellery.com/member/alice-m-srl/","")]:
    add(slug,business=name,category_as_listed="Diamonds and coloured gemstones trader, cutter and/or polisher",website=web,lead_origin="Trade Directory",source_url=src,
        trade_memberships=["RJC"],hooks=["rjc-certified"],
        scope_reason="RJC member list: Head Office Rome, forum 'Diamonds and coloured gemstones trader, cutter and/or polisher'. No usable website/contact found"+(" (diamonds4ugroup.com is a JS redirect shell)" if web else (" (alicem.it 'Under Construction')" if 'alice' in slug else ""))+".")
D=lambda slug,name,src,reason,why,web="": L.append((slug,dict(business=name,website=web,source_url=src,market="Rome, IT",city="Rome",state="RM",is_diamond_trade=False,drop_reason=reason,scope_reason=why)))
D("gioielleria-tanini","Gioielleria Tanini","https://www.gioielleriatanini.it/en/content/4-about-us","retail-only","Family retail store selling watches (Tissot/Bulova), Trollbeads and finished jewelry.","https://www.gioielleriatanini.it")
D("bedetti-roma-1882","Bedetti Roma 1882","https://www.bedetti.it/","retail-only","Authorized watch dealer (Rolex, Cartier, Hublot...) and brand jewelry retailer (Chaumet, Fred, Pasquale Bruni).","https://www.bedetti.it")
D("romagioielli","Romagioielli","https://romagioielli.it/","retail-only","Wedding-ring shop reselling Unoaerre/Fedeinfinita collections.","https://romagioielli.it")
D("igr-istituto-gemmologico-roma","IGR Istituto Gemmologico Roma","https://www.igr-diamantiroma.it/chi-siamo/","appraiser-lab","Gem analysis/certification lab plus compro oro/compro diamanti services.","https://www.igr-diamantiroma.it")
D("tribuzio-gioielli","Tribuzio Gioielli","https://www.tribuziogioielli.it/","cash-for-gold","Compro oro + gemological appraisal shop on Via Prenestina.","https://www.tribuziogioielli.it")
D("lf-gold","LF Gold Gioielleria Roma","https://www.lfgold.it/chi-siamo/laboratorio-orafo/","cash-for-gold","Compro oro with repair/custom goldsmith service.","https://www.lfgold.it")
D("orofirst-shop","OroFirst Shop","https://www.orofirstshop.it/laboratorio-orafo-roma/","cash-for-gold","Pre-owned branded jewelry/watch reseller with 'vendi i tuoi articoli' buying.","https://www.orofirstshop.it")
D("cavalli-gioielli","Cavalli Gioielli (Ciampino)","https://cavalligioielli.com/","costume-fashion","Silver 925 / steel bracelets with zirconia.","https://cavalligioielli.com")
D("gioielleria-saccares","Gioielleria Saccares","https://www.gioielleriasaccares.it/","other","Artisan goldsmith shop (coral, gems, pearls); no clear diamond trade line.","https://www.gioielleriasaccares.it")
D("diamitaly","Diamitaly","https://www.diamitaly.it/laboratorio-orafo/","other","Engagement-ring specialist with Milan phone/Facebook (diamitaly.milano); not Rome-based.","https://www.diamitaly.it")
D("kairos-italia","KIS Kairos Italia S.r.l.","https://www.europages.co.uk/companies/italy/wholesaler/diamonds.html","appraiser-lab","Europages lists Rome 'Gemological analyses, appraisals, evaluations, estimates'; no own site found.")
D("diamond-centre-ludovisi","Diamond Centre Ludovisi","https://nz.trustpilot.com/review/www.diamondcentre.it","retail-only","Self-described retail shop 'with wholesale prices' (diamonds, jewelry, watches); site unreachable (connection reset/503).","https://www.diamondcentre.it")
os.makedirs(OUT,exist_ok=True)
for slug,d in L:
    json.dump(d,open(f"{OUT}/{slug}.json","w"),ensure_ascii=False,indent=2)
print(len(L),sum(1 for _,d in L if d['is_diamond_trade']))
