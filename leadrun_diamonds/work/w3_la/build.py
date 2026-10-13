import json,re
from urllib.parse import urlparse,unquote
m=json.load(open('members.json')); S={r['i']:r for r in json.load(open('sites.json'))}
OUT='/home/user/claude-cloud/leadrun_diamonds/raw/w3_la/'
DIR='https://diamondclubwestcoast.com/company-directory-2/'
MK='Los Angeles, CA'
ST={'california':'CA','new york':'NY','nc':'NC','oklahoma':'OK','illinois':'IL','texas':'TX','ca':'CA','ny':'NY'}
EXIST={1:'Aakash Diamonds',3:'Affinity Gems',6:'Alpha Diamond Cutting Works',9:'Amit Diamonds Inc.',10:'Aspen Diamond Co.',
 34:'CVD Diamond Inc',35:'Danital Gems & Diamonds',44:'Diamond Center Inc',65:'Flawless International',71:'Gantmonds',
 72:'Gem Dynasty',86:'H. Dayan Diamonds',87:'H. Dayan Diamonds',106:'Jhaveri Diamond Corporation',113:'Karatrade Inc.',
 134:'MS Diamonds and Jewelry',137:'Manuel Strauss Inc',141:'Mathieu Attar Diamond',166:'Miro Jack Diamonds',
 173:'Rising Star Diamonds',208:'Worldwide Diamond'}
DROP={11:('pawn','Directory lists it as a pawnshop (Assured Pawn Shop / Sartori Jewelry & Loan).'),
 16:('other','Jewelry house with gemstones as secondary specialty; no diamond line listed in directory.'),
 28:('other','Jewelry services firm; no diamond line listed in directory.'),
 30:('other','Jewelry seller; no diamond line listed in directory.'),
 39:('retail-only','High-end designer jewelry; no diamond trading line listed.'),
 40:('other','Munich, Germany retailer - not a US business.'),
 53:('gemstone-only','Colored stones and jadeite; no diamond line listed.'),
 55:('appraiser-lab','Gem lab / industry services, no inventory.'),
 61:('other','Watch dealer; no diamond line listed.'),
 73:('gemstone-only','Sri Lankan gemstone importer (Jupiter Gem); no diamond line listed.'),
 76:('gemstone-only','Gemstone dealer; no diamond line listed.'),
 85:('appraiser-lab','Gemologist/appraiser laboratory.'),
 90:('gemstone-only','Gemstone and pearl dealer; no diamond line listed.'),
 92:('other','IT/network services provider.'),
 94:('other','IT, photography and videography services for jewelers.'),
 102:('appraiser-lab','Jewelers Mutual - insurance adviser, no inventory.'),
 105:('retail-only','Oklahoma City retail jeweler.'),
 110:('other','Estate jewelry and watches; no diamond line listed.'),
 116:('gemstone-only','Ruby/sapphire/tsavorite dealer.'),
 117:('retail-only','Antique and vintage jewelry retailer (Venice, CA).'),
 130:('retail-only','Directory specialty given as "Retail Store".'),
 136:('other','Malca-Amit - logistics/secure shipping, not a diamond dealer.'),
 144:('other','Finished-goods jewelry only; no diamond line listed.'),
 161:('other','Platinum Guild International - industry/trade association services.'),
 167:('other','Estate jewelry with gemstones secondary; no diamond line listed.'),
 169:('gemstone-only','Rare gems dealer; no diamond line listed.'),
 189:('appraiser-lab','Superior Gemological Laboratory - appraisals/lab services.'),
 191:('gemstone-only','Gemstone specialty; no diamond line listed.'),
 199:('beads-craft','Gold findings & stamping components supplier.'),
 209:('retail-only','Santa Monica fine jewelry & watches retailer.')}
SKIPDUP={111}  # merged into 112
CONTACT={  # idx: (name, role, contact_source, linkedin, linkedin_source)
 134:('Moshe Salem','Founder','https://msdiamonds.la/about/','https://www.linkedin.com/in/moshe-salem-a692bba/','WebSearch: "Moshe Salem" MS Diamonds Los Angeles LinkedIn'),
 68:('Nilesh Sheth','President','https://www.nicediamond.com/home/aboutus','https://www.linkedin.com/in/nilesh-sheth-a5942b19/','WebSearch: "Nilesh Sheth" Nice Diamonds LinkedIn'),
 80:('Johnny Kalo','Owner','https://goldempirejewelry.com/pages/about-us','https://www.linkedin.com/in/johnny-kalo-0ba38747/','WebSearch: "Edmund Kalo" Gold Empire Jewelry LinkedIn'),
 107:('Jonny Ritz','Owner','https://www.linkedin.com/in/jonny-ritz-48206b1/','https://www.linkedin.com/in/jonny-ritz-48206b1/','WebSearch: Jonny Ritz & Company Los Angeles jeweler LinkedIn'),
 19:('Berj Kouyoumjian','Owner','https://berjk.com/about-us/','https://www.linkedin.com/in/berj-kouyoumjian-a84a3973','WebSearch: "Berj Kouyoumjian" jewelry Los Angeles LinkedIn (URL in Clever Wholesale listing structured data)'),
 126:('Ahron Lazar','Member','https://www.linkedin.com/in/ahron-lazar-a40ba12b/','https://www.linkedin.com/in/ahron-lazar-a40ba12b/','WebSearch: Lazar Diamonds Los Angeles 550 Hill owner president LinkedIn'),
 72:('Frank Poors','Member','https://www.linkedin.com/in/frank-poors-8298a518/','https://www.linkedin.com/in/frank-poors-8298a518/','WebSearch: "Farshad Poorsalimi" Gem Dynasty LinkedIn'),
 168:('Amir Goldfiner','President','https://www.linkedin.com/in/amir-goldfiner-2b8922126/','https://www.linkedin.com/in/amir-goldfiner-2b8922126/','WebSearch: "Amir Goldfiner" Rahaminov Diamonds LinkedIn'),
 67:('Rayah Levy','President','https://www.fcdinvest.diamonds/explore-fcdinvest/executive-team','https://www.linkedin.com/in/rayahlevy','https://www.fcdinvest.diamonds/ (linked from own site)'),
 49:('Aria Ahdoot','President','https://www.dtcusa.com/about','',''),
 96:('Wyler Weir','CEO','https://jackweirandsons.com/pages/about-us','',''),
 197:('Benjamin Javaheri','Founder','https://www.uneekjewelry.com/','',''),
 118:('Kobi Katz','Founder','https://kobelli.com/pages/about','',''),
 202:('Pankaj Mehta','Founder','https://varshadiamonds.com/about-us/','',''),
 146:('Stephan Gozumian','Featured On About Page','https://www.nadis.com/about-us','',''),
 181:('Shlomi Bichachi','Founder','https://bichachi.com/about','',''),
 204:('Prakash Vora','Founder','https://www.voragems.com/about-us','',''),
 164:('Harsheel Shah','President','https://www.prijems.com/pages/about-1','',''),
 15:('Anil Maloo','President','https://bagginspearls.com/about-us/','',''),
 120:('Lalit Kothari','President','https://www.manta.com/c/mt13mx6/kothari-company','',''),
 125:('Joseph Laed','President','https://www.corporationwiki.com/California/Los-Angeles/joseph-laed/41270701.aspx/','',''),
}
PREF_EMAIL={19:'berj@berjk.com',107:'jonny@jonnyritz.com',63:'la@jrdiamgroup.com',118:'info@kobelli.com',126:'hello@lazardiamonds.com',
 124:'sales@labondiamonds.com',164:'sales@prijems.com',68:'ny@nicediamond.com',49:'info@dtcusa.com',32:'info@continentalpearl.com',
 120:'RAJ@KOTHARIANDCOMPANY.COM',15:'contact@bagginspearls.com',13:'SALES@AZARDESIGNS.COM'}
JUNK_EMAIL={'info@mysite.com','info@example.com','info@sahilstargroup.com','webadmin@nicediamond.com','mail@designer-optik.de'}
EXTRA_HOOKS={1:['melee'],12:['natural','large-stones'],22:['importer'],42:['melee'],47:['manufacturer'],0:['manufacturer'],57:['melee'],
 79:['large-stones'],100:['melee'],126:['large-stones'],129:['melee'],131:['melee'],135:['melee'],145:['melee'],148:['melee'],
 152:['large-stones'],153:['melee'],176:['large-stones'],179:['melee'],181:['manufacturer','since-1994'],146:['importer','since-1978'],
 19:['since-1973','manufacturer'],80:['since-1978','gia-gg','2nd-generation'],82:['since-1978'],99:['since-1982'],118:['since-1980','manufacturer','importer'],
 164:['since-1985','4th-generation'],168:['3rd-generation'],204:['since-1980'],96:['since-1981'],178:['since-2008'],202:['large-stones','manufacturer'],
 68:['natural'],158:['natural'],67:['natural'],3:['large-stones'],72:['importer']}
BAD_SOC=('facebook.com/tr','2008/fbml','sharer','squarespace','wixstudio','shopify','/embed','facebook.com/#','instagram.com/#','pinterest.com/#','pin/create','youtube.com/watch','instagram.com/p/','linkedin.com/company','linkedin.com/in/')
def slug(s): return re.sub(r'-+','-',re.sub(r'[^a-z0-9]+','-',s.lower())).strip('-')
def parse_addr(a):
    parts=[p.strip() for p in a.split(',')]
    if 'United States' in parts:
        k=parts.index('United States'); st=parts[k-1]; city=parts[k-2] if k>=2 else ''
        return city, ST.get(st.lower(),st[:2].upper())
    return '',''
def digits(t): return re.sub(r'\D','',t)
def site_data(i):
    r=S.get(i); d=dict(emails=[],email_src={},tels=[],tel_src=[],soc=[],root='')
    if not r: return d
    if r['final']: p=urlparse(r['final']); d['root']=f'{p.scheme}://{p.netloc}'
    if i==190: return dict(emails=[],email_src={},tels=[],tel_src=[],soc=[],root='')
    for u,pg in r['pages'].items():
        for e in pg['mailto']+pg['email_text']:
            e=unquote(e).strip()
            if e.lower() in JUNK_EMAIL or not re.match(r'^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$',e): continue
            if e not in d['email_src']: d['emails'].append(e); d['email_src'][e]=u
        got=False
        for t in pg['tel']+pg['phones']:
            t=unquote(t).strip(); dg=digits(t)
            if len(dg)<10 or dg in ('123456789','98210009630'): continue
            if dg[-10:] not in [digits(x)[-10:] for x in d['tels']]: d['tels'].append(t); got=True
            else: got=True
        if got and u not in d['tel_src']: d['tel_src'].append(u)
        for s in pg['soc']:
            if any(b in s for b in BAD_SOC): continue
            s2=s.replace('http://','https://').rstrip('/')
            if s2.lower() not in [x.lower() for x in d['soc']]: d['soc'].append(s2)
    return d
def norm_site(s):
    s=s.strip()
    if not s or '@' in s or '%20' in s: return ''
    s=s.replace('http://http://','http://')
    if not s.startswith('http'): s='http://'+s
    p=urlparse(s); return f'https://{p.netloc.lower()}'
written=[]
def write(rec):
    fn=OUT+slug(rec['business'])+'.json'
    json.dump(rec,open(fn,'w'),indent=1,ensure_ascii=False); written.append(rec)
for i,x in enumerate(m):
    if i in SKIPDUP or i==86: continue
    name=EXIST.get(i,x['name'])
    if i==112: name="K. R. Gems & Diamonds Int'l/ Eighternity USA"
    cat=', '.join([c for c in [x['spec'].rstrip(','), x['goods'] if x['goods']!='N/A' else ''] if c])
    sec=x['secondary'].split(':',1)[-1].strip() if ':' in x['secondary'] else ''
    srcreason=f"DCWC (Diamond Club West Coast bourse) member, {x['type']}; primary specialty: {x['spec'].rstrip(',')}" + (f" ({x['goods']})" if x['goods'] and x['goods']!='N/A' else '') + (f"; secondary: {sec}" if sec and sec!='N/A' else '')
    if i in DROP:
        write(dict(business=name,source_url=DIR,market=MK,is_diamond_trade=False,drop_reason=DROP[i][0],scope_reason=DROP[i][1]+' Listed in DCWC member directory.',category_as_listed=cat,lead_origin='Trade Directory'))
        continue
    city,st=parse_addr(x['addr'])
    sm=re.search(r'(Suite|Sutie|Ste\.?|Arcade|Plaza)\s*([^,]+)',x['addr'],re.I)
    suite=('Suite '+sm.group(2).strip()) if sm and sm.group(1).lower() in ('suite','sutie','ste','ste.') else (sm.group(0).strip() if sm else '')
    sd=site_data(i)
    if i==112:
        x2=m[111]; cat+= ' / '+x2['goods']
    if i==87:
        x86=m[86]; cat=cat+(', '+x86['goods'] if x86['goods'] else '')
    email=PREF_EMAIL.get(i) if PREF_EMAIL.get(i) in sd['emails'] else (sd['emails'][0] if sd['emails'] else '')
    c=CONTACT.get(i,('','','','',''))
    blob=(x['spec']+' '+x['goods']+' '+x['secondary']).lower()
    hooks=[]
    if 'manufactur' in blob or 'cutting' in blob or 'cutter' in blob: hooks.append('manufacturer')
    if 'lab grown' in blob or 'cvd' in blob or 'lab-grown' in blob: hooks.append('lab-grown')
    if 'melee' in blob or 'melle' in blob: hooks.append('melee')
    if 'import' in blob: hooks.append('importer')
    if 'natural' in blob: hooks.append('natural')
    if re.search(r'\bgia\b',blob): hooks.append('gia-certified')
    if 'estate' in blob: hooks.append('estate')
    if 'fancy' in blob or 'color' in blob: hooks.append('fancy-color')
    for h in EXTRA_HOOKS.get(i,[]):
        if h not in hooks: hooks.append(h)
    web=sd['root'] or norm_site(x['site'])
    if i==190: web=''
    is550=bool(re.search(r'550\s+S(outh|\.)?\s+Hill',x['addr'],re.I))
    rec=dict(business=name,category_as_listed=cat,phone=x['phone'],email=email,email_source=sd['email_src'].get(email,'') if email else '',
      linkedin_url=c[3],linkedin_source=c[4],contact_person=c[0],role=c[1],contact_source=c[2],website=web,
      address=x['addr'],city=city,state=st,market=MK,lead_origin='Trade Directory',rating='',reviews='',source_url=DIR,
      tel_numbers=sd['tels'],tel_source=', '.join(sd['tel_src']),socials=sd['soc'],
      building='International Jewelry Center' if is550 else '',suite=suite,trade_memberships=['Bourse','DCWC'],hooks=hooks,
      is_diamond_trade=True,scope_reason=srcreason,drop_reason='')
    if i==190: rec['scope_reason']+='; listed domain thediamondsource.com now redirects to an unrelated spam site, so no website recorded'
    write(rec)
json.dump([w['business'] for w in written],open('written.json','w'))
ins=[w for w in written if w['is_diamond_trade']]
print('files',len(written),'in-scope',len(ins),'dropped',len(written)-len(ins))
print('emails',sum(1 for w in ins if w['email']),'linkedin',sum(1 for w in ins if w['linkedin_url']),'contacts',sum(1 for w in ins if w['contact_person']),'tels',sum(1 for w in ins if w['tel_numbers']),'websites',sum(1 for w in ins if w['website']))
print('merged-existing',sorted(set(EXIST.values())))
