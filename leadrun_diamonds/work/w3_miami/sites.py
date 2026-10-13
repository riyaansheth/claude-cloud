import requests,json,re,time,sys,concurrent.futures as cf
from urllib.parse import urljoin,urlparse
from bs4 import BeautifulSoup
H={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
SITES=json.load(open('sites_in.json'))
SUB=['','contact','contact-us','pages/contact','pages/contact-us','about','about-us','pages/about','pages/about-us','our-story','team']
SOC=re.compile(r'(facebook\.com|instagram\.com|twitter\.com|x\.com|linkedin\.com|tiktok\.com|youtube\.com)',re.I)
EM=re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
def one(name,root):
    out=dict(root=root,pages={},mailto=set(),emails=set(),tel=set(),phones=set(),socials=set(),text={})
    seen=set()
    for sub in SUB:
        u=urljoin(root.rstrip('/')+'/',sub)
        try:
            r=requests.get(u,headers=H,timeout=20)
        except Exception as e: continue
        time.sleep(0.5)
        if r.status_code>=400 or r.url in seen: continue
        seen.add(r.url)
        s=BeautifulSoup(r.text,'html.parser')
        out['pages'][r.url]=r.status_code
        for a in s.find_all('a',href=True):
            h=a['href'].strip()
            if h.lower().startswith('mailto:'): out['mailto'].add((h[7:].split('?')[0].strip(),r.url))
            elif h.lower().startswith('tel:'): out['tel'].add((h[4:].strip(),r.url))
            elif SOC.search(h) and 'share' not in h and 'sharer' not in h: out['socials'].add(h.split('?')[0])
        for x in s(['script','style','noscript']): x.decompose()
        t=s.get_text(' ',strip=True)
        for e in EM.findall(t):
            if not re.search(r'\.(png|jpg|webp|gif|svg)$',e,re.I): out['emails'].add((e,r.url))
        for p in re.findall(r'\(?\b\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b',t): out['phones'].add((p,r.url))
        out['text'][r.url]=t[:4000]
    for k in ['mailto','emails','tel','phones','socials']: out[k]=sorted(out[k])
    return name,out
res={}
with cf.ThreadPoolExecutor(8) as ex:
    for name,o in ex.map(lambda kv: one(*kv), SITES.items()):
        res[name]=o
        print('##',name,o['root'],list(o['pages']))
        print('  mailto',o['mailto'][:6]); print('  emails',o['emails'][:6]); print('  tel',o['tel'][:6]); print('  socials',o['socials'][:8])
json.dump(res,open(sys.argv[1] if len(sys.argv)>1 else 'sites_out.json','w'),indent=1)
