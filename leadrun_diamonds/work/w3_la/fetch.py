import json,re,time,sys
from urllib.parse import urljoin,urlparse
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
H={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
m=json.load(open('members.json'))
SOC=re.compile(r'https?://(www\.)?(facebook|instagram|twitter|x|linkedin|youtube|pinterest|tiktok)\.com/[^\s"\'<>]+',re.I)
EM=re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
TITLE=re.compile(r'([^.\n]{0,120}\b(Founder|Co-Founder|Owner|President|CEO|Principal|Partner|Proprietor|founded by|owned by)\b[^.\n]{0,120})')
def norm(site):
    s=site.strip()
    if not s or '@' in s: return ''
    s=s.replace('http://http://','http://')
    if not s.startswith('http'): s='http://'+s
    if '%20' in s: return ''
    p=urlparse(s); return f'{p.scheme}://{p.netloc.lower()}'
def get(u):
    try:
        r=requests.get(u,headers=H,timeout=20,allow_redirects=True)
        return r
    except Exception as e:
        return str(e)[:120]
def one(i):
    x=m[i]; root=norm(x['site'])
    res={'i':i,'root':root,'pages':{},'final':'','err':''}
    if not root: return res
    r=get(root)
    if isinstance(r,str):
        r2=get(root.replace('http://','https://'))
        if isinstance(r2,str): res['err']=r; return res
        r=r2
    if r.status_code>=400: res['err']=f'status {r.status_code}'
    res['final']=r.url
    base=r.url
    pages=[(base,r)]
    soup=BeautifulSoup(r.text,'html.parser')
    links=set()
    for a in soup.find_all('a',href=True):
        h=a['href']; t=(a.get_text() or '').lower()+' '+h.lower()
        if any(k in t for k in ['contact','about','our-story','team','who-we-are','our story']):
            u=urljoin(base,h)
            if urlparse(u).netloc==urlparse(base).netloc: links.add(u.split('#')[0])
    for p in ['/contact','/about','/contact-us','/about-us']:
        links.add(urljoin(base,p))
    links=sorted(links)[:8]
    for u in links:
        time.sleep(0.6)
        rr=get(u)
        if not isinstance(rr,str) and rr.status_code<400: pages.append((rr.url,rr))
    for u,rr in pages:
        if u in res['pages']: continue
        s=BeautifulSoup(rr.text,'html.parser')
        mail=sorted({a['href'][7:].split('?')[0].strip() for a in s.find_all('a',href=True) if a['href'].lower().startswith('mailto:')})
        tel=sorted({a['href'][4:].strip() for a in s.find_all('a',href=True) if a['href'].lower().startswith('tel:')})
        txt=s.get_text(' ',strip=True)
        emt=sorted({e for e in EM.findall(txt) if not e.lower().endswith(('.png','.jpg','.webp','.gif'))})
        phones=sorted(set(re.findall(r'\(?\b\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b',txt)))
        soc=sorted({mm.group(0).rstrip('/').split('?')[0] for mm in SOC.finditer(rr.text)})
        titles=[t[0].strip() for t in TITLE.findall(txt)][:8]
        res['pages'][u]=dict(mailto=mail,email_text=emt,tel=tel,phones=phones[:10],soc=soc[:15],titles=titles,title=(s.title.string.strip() if s.title and s.title.string else ''))
    return res
idx=[i for i,x in enumerate(m) if norm(x['site'])]
print(len(idx),file=sys.stderr)
with ThreadPoolExecutor(8) as ex: out=list(ex.map(one,idx))
json.dump(out,open('sites.json','w'),indent=1)
