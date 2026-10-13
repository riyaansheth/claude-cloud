import json,re,os
W='/home/user/claude-cloud/leadrun_diamonds/work/w3_miami/'
OUT='/home/user/claude-cloud/leadrun_diamonds/raw/w3_miami/'
T=json.load(open(W+'tenants.json'))
S={}; S.update(json.load(open(W+'sites_out.json'))); S.update(json.load(open(W+'sites_out2.json')))
DIR='https://seyboldjewelry.com/full-directory/'
SB='https://seyboldjewelry.com/'
OC='https://opencorporates.com/companies/us_fl/'
MARKET='Miami, FL'
def slug(n): return re.sub(r'-+','-',re.sub(r'[^a-z0-9]+','-',n.lower().replace('&',' ').replace("’","").replace("'",""))).strip('-')
def suite(s):
    m=re.search(r'/\s*(.+)$',s); return ('Ste '+m.group(1).strip()) if m else s
def norm(p):
    d=re.sub(r'\D','',p)
    if len(d)==11 and d[0]=='1': d=d[1:]
    return f'({d[:3]}) {d[3:6]}-{d[6:]}' if len(d)==10 else p
def tels(name):
    o=S.get(name)
    if not o: return [],''
    by={}
    for p,u in o['tel']+o['phones']: by.setdefault(u,set()).add(norm(p))
    if not by: return [],''
    def score(u): return (('contact' in u)*10+len(by[u]))
    u=max(by,key=score)
    return sorted(by[u]),u
EXIST={'ALMAGOR DIAMONDS, INC','BBY DIAMONDS','BELGIUM DIAMONDS','BRILLIANTS INTERNATIONAL GOLDMINE ENTERPRISES','BUCHWALD JEWELERS INC','DIAMOND CLUB, INC','DIAMOND HEADQUARTERS, LLC','DIAMOND IMAGES USA, INC.','E&S HOUSE OF DIAMONDS','FRENCH DIAMOND JEWELRY','GEMS & DIAMONDS','INDIA GEMS, INTERNATIONAL','IZA AND SONS, INC.',"BALCO INT'L / S. FLORIDA JEWELRY BUYING"}
# In-scope enrichment: name -> dict of overrides
IN={
"18K Miami":dict(website="https://www.18kmiami.com",email="gold@18kmiami.com",email_source="https://www.18kmiami.com/",
  hooks=["manufacturer","wholesale","trade-only","18k-gold","natural","lab-grown","since-2024"],
  scope_reason="Own site: trade-only 18K wholesale jewelry manufacturer (own manufacturing, private label) for verified retailers, offers natural or lab-grown diamonds; showroom Suite 223 Seybold Building."),
"ADN RENDON JEWELER":dict(website="https://adnrendonjeweler.com",email="info@adnrendonjeweler.com",email_source="https://adnrendonjeweler.com/pages/contact",
  contact_person="Reiner Rendon Dominguez",role="",contact_source=OC+"P21000044800",hooks=["custom-design","manufacturer","registered-agent-name"],
  scope_reason="Own site: custom fine-jewelry maker (custom rings 'shop by stone', diamonds category) at Suite 807; small bench-maker, weak diamond-trade fit. Contact is the FL registered agent of ADN RENDON JEWELER, CORP (OpenCorporates)."),
"ALBERT'S FINE JEWELERS":dict(website="https://www.albertsfinejewelers.com",email="albertsfinejewelers@gmail.com",email_source="https://www.albertsfinejewelers.com/about",
  contact_person="Albert Albaladejo",role="Owner",contact_source="https://www.albertsfinejewelers.com/about",
  linkedin_url="https://www.linkedin.com/in/albert-albaladejo-a0348344/",linkedin_source='WebSearch extended: "Albert Albaladejo" jeweler Miami LinkedIn (result title: Albert Albaladejo - Alberts fine jewelers)',
  hooks=["gia","natural","bridal","since-2009","30-years-experience"],
  scope_reason="Own site: carries GIA certified diamonds and gemstones in a range of quality/color/size; owner sources GIA diamonds for bridal/custom work."),
"BAGUETTE MONDIAL":dict(business_override="BAGUETTE MONDIAL",website="https://baguettemondial.com",contact_person="Malka Roizen",role="President",contact_source="https://baguettemondial.com/about",
  hooks=["importer","calibrated","baguettes","matched-pairs","fancy-cut-side-stones","israel","ramat-gan-bourse","since-1979","women-owned","natural"],
  scope_reason="Own site: Baguette Mondial Diamond Importers Inc - matched pairs & fancy-cut side stones (calibrated baguettes, step cuts) from Israel, custom cutting to spec; president trained on the Ramat Gan diamond bourse."),
"BARCLAY'S JEWELERS":dict(website="https://www.barclaysjewelry.com",email="raju@barclaysmiami.com",email_source="https://seyboldjewelry.com/barclays-jewelers/",
  hooks=["natural","lab-grown","loose-diamond-search","bridal","40-years","gold-diamond-buying"],
  scope_reason="Own site: natural and lab-created loose diamond search by shape, bridal/engagement focus, also buys gold & diamonds; Seybold listing: 40+ years, brilliant diamonds."),
"BHA JEWELRY":dict(website="https://bhajewelry.com",email="marketing@bhajewelry.com",email_source="https://bhajewelry.com/about-us/",
  contact_person="Ash Chugani",role="Founder",contact_source="https://bhajewelry.com/about-us/",
  linkedin_url="https://www.linkedin.com/in/ash-chugani-0420536/",linkedin_source='WebSearch extended: "Ash Chugani" BHA Jewelry LinkedIn (result title: Ash Chugani - TIMELUXE - BHA Jewelry - Kay\'s Fine ...)',
  hooks=["wholesale","b2b","caribbean-export","gia","gemstone-sourcing"],
  scope_reason="Own site: wholesale & B2B jewelry supplier to retailers across the Caribbean; GIA-certified design lead, gemstone sourcing. Ash Chugani is co-founder / Director of Sales & Strategy."),
"D.K.N. GEMS & JEWELRY INC":dict(website="https://www.dknjewelry.com",email="info@dknjewelry.com",email_source="https://www.dknjewelry.com/contact",
  contact_person="Nitesh Budhrani",role="CEO",contact_source="https://www.linkedin.com/in/nitesh-budhrani-a737026a/",
  linkedin_url="https://www.linkedin.com/in/nitesh-budhrani-a737026a/",linkedin_source='WebSearch extended: Budhrani DKN Jewelry Miami diamonds LinkedIn (result title: Nitesh Budhrani - Ceo - DKN Jewelry)',
  hooks=["gia","manufacturer","wholesale","3rd-generation","since-1975","hong-kong-office","founder-sham-budhrani"],
  scope_reason="Own site: specializing in GIA certified diamonds, manufacturing/wholesale/retail, 3rd generation Budhrani family, founded Hong Kong 1975 by Sham Budhrani; offices HK and US."),
"DASANI JEWELS, INC / PANDORA":dict(website="http://www.dasanithejeweler.com",email="info@dasanithejeweler.com",email_source="https://seyboldjewelry.com/dasani-jewels-inc-pandora/",
  hooks=["wholesale","engagement-rings","custom"],
  scope_reason="Seybold listing: 'high end wholesale and retail jewelry store, specializing in engagement rings, custom jewelry and fine swiss watches'; own site did not resolve. Weak fit (also Pandora dealer)."),
"E. FRAI & CO.":dict(website="https://efrai.com",email="sales@efrai.com",email_source="https://seyboldjewelry.com/e-frai-co/",
  contact_person="Eran Frai",role="Owner",contact_source="https://www.startus.cc/company/e-frai-diamonds-jewelry",
  hooks=["wholesale","distributor","fancy-color","gia","natural","since-1973","family-owned"],
  scope_reason="Seybold listing: 'Wholesalers and distributors of the finest diamonds and fancy colored diamonds'; own site: established 1973, GIA natural fancy yellow diamonds. Eran Frai is FL registered agent (OpenCorporates P95000064597) and named as owner in search results."),
"ITALIAN JEWELRY, INC":dict(website="https://italianjewelry.miami",email="italianJ1@aol.com",email_source="https://seyboldjewelry.com/italian-jewelry-inc/",
  hooks=["importer","since-1979","family-owned"],
  scope_reason="Seybold listing: family-owned since 1979, 'direct importer of jewelry and diamonds'; own site did not resolve."),
"LAZARO DAVINCHY":dict(website="https://lazarodavinchyjewelry.com",
  hooks=["gia","natural","lab-grown","loose","buy-sell","custom"],
  scope_reason="Own site: buys/sells gold, diamonds & watches; diamonds natural and lab-grown, VS+, GIA certified options, loose or set; custom bench at Suite 130. Mixed diamond/watch dealer."),
"MATEO MADE IT":dict(website="https://www.mateomadeit.com",hooks=["custom","manufacturer","hip-hop"],
  scope_reason="Own site: Miami custom maker of hip-hop style gold and diamond jewelry (Suite 363). Weak fit: small custom maker."),
"MOLLIE FRANCINE, LLC":dict(website="https://molliefrancine.com",email="molliefrancinejonas@gmail.com",email_source="https://molliefrancine.com/pages/contact-us",
  contact_person="Mollie F Jonas",role="",contact_source=OC+"L14000132883",
  hooks=["loose","diamond-pairs","old-mine-cut","antique","gia","gemstones","registered-agent-name"],
  scope_reason="Own site sells loose diamonds and diamond pairs by cut (Asscher, cushion, old mine, French, rose...), GIA certified diamonds, gemstones and antique jewelry. Contact is FL registered agent of MOLLIE FRANCINE LLC (OpenCorporates)."),
"NEMARO JEWELERS INC":dict(website="https://www.nemarojewelers.com",email="sales@nemarojewelers.com",email_source="https://www.nemarojewelers.com/contact/",
  hooks=["loose","gia","egl","bridal","since-1970","family-owned","conflict-free"],
  scope_reason="Own site: family business since 1970; 'Our loose diamonds are backed up by laboratory grading reports issued by GIA and EGL'; bridal/engagement focus."),
"RICHARD’S GEMS AND JEWELRY":dict(website="https://www.richardsjewelry.com",email="sales@richardsjewelry.com",email_source="https://richardsjewelry.com/contact-us/",
  hooks=["bridal","fancy-color","since-1984","family-owned"],
  scope_reason="Own site: engagement rings by diamond shape, fancy colored/black/blue/yellow diamonds; Seybold listing: family-owned since 1984. Bridal-focused jeweler; moderate fit."),
"WHITE CARAT CO. DIAMONDS":dict(website="https://whitecaratdiamond.com",email="team@whitecaratdiamond.com",email_source="https://whitecaratdiamond.com/pages/contact-us",
  contact_person="Saveen Lalani",role="Owner",contact_source="https://trademark.justia.com/owners/lalani-saveen-4078864",
  hooks=["manufacturer","custom","hip-hop","toronto-office","gia"],
  scope_reason="Own site: diamond jewelry 'crafted by White Carat' (custom diamond pendants, chains), Miami Suite 117 + Toronto; Saveen Lalani is FL registered agent of WHITE CARAT CO. (OpenCorporates P22000055429) and WHITE CARAT trademark owner."),
"ROYAL GEMS INC":dict(website="https://royalgems.com",email="info@royalgems.com",email_source="https://royalgems.com/contact/",
  contact_person="Shashi Jain",role="President",contact_source="https://www.members.agta.org/assnfe/CompanySearch.asp?MODE=DETAIL&COID=38563",
  trade_memberships=["AGTA"],hooks=["wholesale","melee","gia","up-to-3ct","gemstones","since-1996","30-years"],
  scope_reason="Own site: Miami wholesale gems & jewelry 30+ years, trade-show exhibitor; AGTA member listing (via search) offers diamond melee and GIA certified up to 3.0 ct plus wholesale natural gemstones. Shashi Jain also FL registered agent at Ste 321 (OpenCorporates P96000044383)."),
"MOSES DIAMOND CORP":dict(contact_person="Stalin Pellissery",role="CEO",contact_source="https://www.dandb.com/businessdirectory/mosesdiamondcorporation-miami-fl-16840377.html",
  hooks=["wholesale","registered-agent-name"],
  scope_reason="Directory name; FL corp MOSES DIAMOND CORPORATION head office 36 NE 1st St #324 (OpenCorporates P03000001099, agent Stalin Pellissery); MisterWhat categorizes it 'Wholesale Diamonds'. No website found."),
"DIAMOND CONNECTION":dict(contact_person="Avinash K Thakor",role="",contact_source=OC+"P92000007649",hooks=["registered-agent-name"],
  scope_reason="Directory name (Suite 515); FL corp at 36 NE 1st St #515 with registered agent Avinash K Thakor (OpenCorporates P92000007649). No website found; diamond trade inferred from name/location only."),
"EC DIAMONDS MIAMI":dict(hooks=[],
  scope_reason="Directory name; FL LLC EC DIAMONDS USA LLC head office 36 NE 1st St #325 (OpenCorporates L26000229984, formed 2026). No website found; diamond trade inferred from name only."),
"ECOSHINE DIAMONDS":dict(hooks=[],scope_reason="Directory name only (Suite 307, NY area code phone); no website or registry match found. Diamond trade inferred from name only."),
"ELI MELEE":dict(business_override="ELI MELEE",contact_person="Zulfiya Seidova",role="President",contact_source="https://www.dnb.com/business-directory/company-profiles.eli_melee_diamonds_inc.3143bbca19035e2773e7aa1163cc4c91.html",
  hooks=["melee","since-2013"],
  scope_reason="Directory name; FL corp ELI MELEE DIAMONDS, INC (OpenCorporates P13000063733, agent Zulfiya Seidova) at 36 NE 1st St Ste 701; D&B lists Seidova as president. Melee diamond dealer by name; no website."),
"H & Y DIAMOND CUTTER":dict(hooks=["cutter"],scope_reason="Directory name: diamond cutter (Suite 1020); no website or active registry match found."),
"J&S DIAMOND JEWELERS":dict(hooks=[],scope_reason="Directory name (Suite 349); FL LLC J & S DIAMOND JEWELERS LLC registered at 340 W Flagler St #802 (OpenCorporates L24000224643). No website; weak, name-only fit."),
"MIAMI DIAMOND POLISHING BY OBC, LLC.":dict(hooks=["polisher","cutter"],scope_reason="Directory name: diamond polishing (Suite 946); FL LLC MIAMI DIAMOND POLISHING BY O.B.C LLC (OpenCorporates L25000512432, formed 2025). No website; no phone in directory."),
"SP DIAMONDS INTL TRADE CORP":dict(contact_person="Spartacus R Soares da Silva",role="",contact_source=OC+"P26000017421",hooks=["international-trade","brazil-linked","since-2026","registered-agent-name"],
  scope_reason="Directory name; FL corp SP DIAMONDS INTL TRADE CORP at 36 NE 1st Suite 310 (OpenCorporates P26000017421, filed 2026; registered agent Spartacus R Soares da Silva, officer alongside a Sao Paulo entity per bizprofile). No website."),
"ELITE CASTING":dict(contact_person="Juan M Valladares",role="",contact_source=OC+"P06000036118",hooks=["casting","manufacturer","registered-agent-name"],
  scope_reason="Directory name: jewelry casting house (Suite 1005); FL corp ELITE CASTING, INC. (OpenCorporates P06000036118, agent Juan M Valladares). No website."),
"MARIO'S CASTINGS, INC.":dict(hooks=["casting","manufacturer"],scope_reason="Directory name: jewelry casting house (Suite 851). No website or registry match found."),
"LAAL MANUFACTURING INC":dict(contact_person="Javier A Otero Garcia",role="",contact_source=OC+"P13000088326",hooks=["manufacturer","registered-agent-name"],
  scope_reason="Directory name: jewelry manufacturer; FL corp LAAL MANUFACTURING INC head office 36 NE 1st St Ste 814-816 (OpenCorporates P13000088326, agent Javier A Otero Garcia). No website; diamond line unverified."),
"LISITZKY-ROSNER JEWELRY":dict(hooks=["manufacturer","trademark-lisro"],
  scope_reason="Directory name; Lisitzky-Rosner Jewelry Inc. owns LISRO trademark for precious-metal jewelry with or without precious stones (Justia). Manufacturer; diamond line unverified."),
}
DETAIL={"ALBERT'S FINE JEWELERS":"alberts-fine-jewelers/","BARCLAY'S JEWELERS":"barclays-jewelers/","D.K.N. GEMS & JEWELRY INC":"d-k-n-gems-jewelry-inc/","DASANI JEWELS, INC / PANDORA":"dasani-jewels-inc-pandora/","E. FRAI & CO.":"e-frai-co/","ITALIAN JEWELRY, INC":"italian-jewelry-inc/","RICHARD’S GEMS AND JEWELRY":"richards-gems-jewelry/","NEMARO JEWELERS INC":"nemaro-jewelers-inc/",
 "ARUBA GOLD, INC":"aruba-gold-inc/","BOS JEWELERS INC":"bos-jewelers-inc/","BRILLIANCE JEWELS":"brilliance-jewels/","DeBRANF JEWELRY LLC":"debranf-jewelry-llc/","FERRARI EXPRESS INC":"ferrari-express-inc/","G LUXE JEWELERS":"g-luxe-jewelers/","JIMMY QUIROGA DESIGNS/LIDO JEWERLY":"jimmy-quiroga-designs-lido-jewerly/","MAIPO, CORP":"maipo-corp/","MALCA-AMIT":"malca-amit/","SWISS TIME BUYERS":"swiss-time-buyers/"}
# Explicit drops with evidence
DROP={
"ARUBA GOLD, INC":("retail-only","Seybold listing: high end jewelry store selling fine jewelry, diamonds and watches at retail; own site did not resolve."),
"BOS JEWELERS INC":("retail-only","Seybold listing/own site: retailer of fine jewelry for women and children, religious jewelry; no loose-diamond or trade line."),
"BRILLIANCE JEWELS":("retail-only","Seybold listing: designer, fine and estate brand-name jewelry reseller (pre-owned designer pieces); not diamond trade."),
"DeBRANF JEWELRY LLC":("cash-for-gold","Seybold listing: 'They pay top price for your gold & used jewelry'."),
"FERRARI EXPRESS INC":("other","Seybold listing: valuables logistics/forwarding company (IATA agent) - service provider, not a diamond trader."),
"MALCA-AMIT":("other","Seybold listing: secure logistics for luxury goods - service provider."),
"G LUXE JEWELERS":("other","Seybold listing: luxury watch store (buy/sell/trade watches) - watch-only."),
"SWISS TIME BUYERS":("other","Seybold listing: wholesale/retail luxury watches - watch-only."),
"CA33":("other","Own site miamiwatchdealer.com: luxury watch dealer - watch-only."),
"ROCKS ON CLOCKS, LLC":("other","Own site: Rolex watches and custom diamond bezels for watches - watch customization, not diamond trade."),
"MAIPO, CORP":("other","Seybold listing: Italian machine-made gold & silver chain manufacturer/importer; no diamond line."),
"JIMMY QUIROGA DESIGNS/LIDO JEWERLY":("retail-only","Own site: designer/manufacturer of gold/silver couture, coin and kids jewelry; no diamond trade line evident."),
"ITALIAN JEWELRY LUXURY COLLECTION":("retail-only","Own site is a generic retail storefront (Jewel360 template); no diamond-trade signal."),
"MJM GLOBAL INSURANCE BROKERAGE GROUP":("appraiser-lab","Jewelry insurance brokerage - no inventory."),
"MOTEK CAFÉ":("other","Cafe."),
"SEYBOLD® MANAGEMENT OFFICE":("other","Building management office."),
"UNIVERSAL JEWELRY SUPPLY CORP":("beads-craft","Name: jewelry supply company."),
"ROGER'S FINDINGS & CASTING":("beads-craft","Name: findings supplier (and casting); findings/supply."),
"AKAR PRECIOUS METALS, INC.":("cash-for-gold","Name: precious metals dealer."),
"SHARP SILVER CORP":("other","Name: silver jewelry."),
"LUIS RUIZ / CUBAN LINKS":("other","Name: Cuban link gold chains."),
"SWISS GEMSTONE SETTERS, LLC":("other","Name: stone-setting service."),
"GOLD TIP ENGRAVERS, INC":("other","Name: engraving service."),
"VAULT CONCIERGE, CORP":("other","Name: vault/storage service."),
"PENGUIN SERVICES":("other","Name: services company, not jewelry trade."),
"14K-18K GOLD EARRINGS DBA ACERO 316, INC.":("costume-fashion","Name: gold earrings / steel (Acero 316) jewelry."),
"INVERSIONES TEAM GOLD 18K, INC .":("other","Name: 18k gold jewelry, no diamond signal."),
"MACEO WATCHES & GOLD":("other","Name: watches & gold."),
"NV GOLD MINE":("other","Name: gold jewelry, no diamond signal."),
"GLOBAL GEMS GROUP":("other","Unverified: gem-named; FL LLC GLOBAL GEMS GROUP USA LLC at 36 NE 1st St (OpenCorporates L20000249621, agent James Pallissery) but no website/evidence of a diamond line found."),
"ALP GEMS":("other","Unverified: gem-named; FL corp ALP GEMS, INC. head office 36 NE 1st St (OpenCorporates P19000070880) but no website/evidence of a diamond line found."),
"JONE GEMS INC":("other","Unverified: gem-named; FL corp JONE GEMS INC 36 NE 1st St Ste 901 (OpenCorporates P18000002613, agent Jone R Ribeiro Sr.) but no website/evidence of a diamond line found."),
"RUBIN'S GEM & JEWELRY":("other","Unverified: FL corp RUBIN'S GEM & JEWELRY, INC. (OpenCorporates P06000084225) but no website/evidence of a diamond line found."),
}
WATCH=re.compile(r'WATCH|TIME|ROLEX|CLOCK',re.I); REPAIR=re.compile(r'REPAIR|POLISHER',re.I)
def base(t):
    return dict(business=t['name'],category_as_listed="",phone=t['phone'],email="",email_source="",linkedin_url="",linkedin_source="",
        contact_person="",role="",contact_source="",website="",address="36 NE 1st St",city="Miami",state="FL",market=MARKET,
        lead_origin="Building Directory",rating="",reviews="",source_url=DIR,tel_numbers=[],tel_source="",socials=[],
        building="Seybold Building",suite=suite(t['suite']),trade_memberships=[],hooks=[],is_diamond_trade=True,scope_reason="",drop_reason="")
n_in=n_drop=0; written=set()
for t in T:
    nm=t['name']
    if nm in EXIST: continue
    s=slug(nm)
    if nm in IN:
        r=base(t); ov=dict(IN[nm]); ov.pop('business_override',None)
        r.update(ov)
        if nm in DETAIL: r['source_url']=SB+DETAIL[nm]
        if nm in S:
            nums,src=tels(nm); r['tel_numbers']=nums; r['tel_source']=src
            r['socials']=sorted(set(x for x in S[nm]['socials'] if re.search(r'facebook|instagram|twitter|x\.com|tiktok|youtube',x) and '/p/' not in x.split('instagram.com')[-1][:3] and 'watch' not in x and 'profile.php' not in x))
        n_in+=1
    else:
        if nm in DROP: dr,why=DROP[nm]
        elif WATCH.search(nm): dr,why="other","Directory name indicates watch dealer/repair - watch-only."
        elif REPAIR.search(nm): dr,why="other","Directory name indicates jewelry repair/polishing shop."
        elif re.match(r"^[A-Z][A-Za-z\.]+( [A-Z]\.?)? [A-Z][A-Za-z']+$",nm) and not re.search(r'JEWEL|GEM|DIAMOND|GOLD|DESIGN|TRADING|GROUP|CORP|INC|LLC|CREATIONS|INTERNATIONAL',nm,re.I):
            dr,why="other","Unverified: directory lists an individual's name (typical bench jeweler/setter/broker) with suite and phone only; no website found by domain probe, no diamond-trade evidence."
        else: dr,why="other","Unverified: directory lists name/suite/phone only; no website found by domain probe and no diamond-trade evidence found."
        r=dict(business=nm,market=MARKET,source_url=SB+DETAIL[nm] if nm in DETAIL else DIR,phone=t['phone'],building="Seybold Building",suite=suite(t['suite']),
               lead_origin="Building Directory",is_diamond_trade=False,drop_reason=dr,scope_reason=why)
        n_drop+=1
    if s in written: s=s+'-2'
    written.add(s)
    json.dump(r,open(OUT+s+'.json','w'),indent=2,ensure_ascii=False)
print('in',n_in,'drop',n_drop,'total',len(written),'missing IN',[k for k in IN if k not in [t['name'] for t in T]])
