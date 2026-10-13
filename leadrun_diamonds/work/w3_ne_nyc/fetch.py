import sys, requests, time, re
from bs4 import BeautifulSoup
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36','Accept-Language':'en-US,en;q=0.9','Accept':'text/html,application/xhtml+xml,*/*;q=0.8'}
def get(u):
    try:
        r=requests.get(u,headers=UA,timeout=20)
        return r
    except Exception as e:
        print('ERR',u,e); return None
if __name__=='__main__':
    mode=sys.argv[1]
    for u in sys.argv[2:]:
        r=get(u)
        if r is None: continue
        print('==',u,r.status_code,r.url,len(r.text))
        s=BeautifulSoup(r.text,'html.parser')
        if mode=='text':
            for t in s(['script','style','noscript']): t.decompose()
            print(re.sub(r'\n\s*\n+','\n',s.get_text('\n'))[:15000])
        elif mode=='links':
            for a in s.find_all('a',href=True): print(a['href'],'|',a.get_text(' ',strip=True)[:80])
        elif mode=='contact':
            hs=[a['href'] for a in s.find_all('a',href=True)]
            print('MAILTO',sorted(set(h for h in hs if h.lower().startswith('mailto:'))))
            print('TEL',sorted(set(h for h in hs if h.lower().startswith('tel:'))))
            print('EMAILS',sorted(set(re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+',r.text)))[:20])
            print('SOC',sorted(set(h for h in hs if re.search(r'facebook|instagram|twitter|x\.com|linkedin',h)))[:12])
            txt=s.get_text(' ',strip=True)
            print('PHONES',sorted(set(re.findall(r'\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}',txt)))[:10])
            for k in re.finditer(r'(?i)(founder|owner|president|since \d{4}|generation|suite \w+|ste\.? \w+|lab[- ]grown|wholesale|GIA)',txt):
                print('  ..',txt[max(0,k.start()-100):k.end()+100])
                
        time.sleep(0.6)
