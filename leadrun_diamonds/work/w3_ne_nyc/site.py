import sys,re,time,requests,json
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse
from fetch import UA
def scan(root,extra=()):
    res={'root':root,'pages':{}}
    paths=['/','/contact','/contact-us','/about','/about-us','/our-story']+list(extra)
    seen=set()
    for p in paths:
        u=urljoin(root,p)
        try: r=requests.get(u,headers=UA,timeout=20)
        except Exception as e: res['pages'][u]='ERR '+str(e)[:80]; continue
        time.sleep(0.5)
        if r.status_code!=200 or r.url in seen: res['pages'][u]=f'{r.status_code} {r.url}'; continue
        seen.add(r.url)
        s=BeautifulSoup(r.text,'html.parser')
        hs=[a['href'].strip() for a in s.find_all('a',href=True)]
        for t in s(['script','style','noscript']): t.decompose()
        txt=s.get_text(' ',strip=True)
        d={'final':r.url,
           'mailto':sorted(set(h.split('?')[0] for h in hs if h.lower().startswith('mailto:'))),
           'tel':sorted(set(h for h in hs if h.lower().startswith('tel:'))),
           'emails':sorted(set(e for e in re.findall(r'[\w.+-]+@[\w-]+\.[a-zA-Z.]{2,}',txt) if not e.endswith(('.png','.jpg')))),
           'phones':sorted(set(re.findall(r'\(?\b\d{3}\)?[-.\s]{0,2}\d{3}[-.\s]\d{4}\b',txt)))[:8],
           'soc':sorted(set(h for h in hs if re.search(r'facebook\.com|instagram\.com|twitter\.com|linkedin\.com',h)))[:8],
           'snips':[]}
        for k in re.finditer(r'(?i)(founder|owner|president|founded|since \d{4}|generation|suite \w+|lab[- ]grown|wholesale|GIA|loose diamond|manufactur|import)',txt):
            d['snips'].append(txt[max(0,k.start()-120):k.end()+120])
        d['snips']=d['snips'][:10]
        res['pages'][u]=d
    return res
if __name__=='__main__':
    for root in sys.argv[1:]:
        print(json.dumps(scan(root),indent=0)[:6000]); print('-----')
