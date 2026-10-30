import sys,re,requests,time
from bs4 import BeautifulSoup
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
mode=sys.argv[1]
for u in sys.argv[2:]:
    try:
        r=requests.get(u,headers=UA,timeout=20,verify='/root/.ccr/ca-bundle.crt')
        s=BeautifulSoup(r.text,'html.parser')
        print('=====',u,r.status_code,r.url)
        mails=set(); tels=set(); soc=set(); links=[]
        for a in s.find_all('a',href=True):
            h=a['href']
            if h.startswith('mailto:'): mails.add(h)
            elif h.startswith('tel:'): tels.add(h)
            elif any(x in h for x in ['facebook.com','instagram.com','linkedin.com']): soc.add(h)
            links.append(h)
        txt=s.get_text(' ',strip=True)
        mails|=set(re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+',txt))
        ph=set(re.findall(r'(?:\+39[\s.]?)?(?:0\d{1,3}|3\d{2})[\s./-]?\d{3,4}[\s./-]?\d{2,5}',txt))
        print('MAIL',mails);print('TEL',tels);print('PHTXT',list(ph)[:12]);print('SOC',soc)
        if mode=='t': print('TXT',txt[:int(sys.argv[0:1] and 3000)])
        if mode=='l': print('LINKS',[l for l in links if l.startswith('http')][:150])
    except Exception as e: print('ERR',u,e)
    time.sleep(0.6)
