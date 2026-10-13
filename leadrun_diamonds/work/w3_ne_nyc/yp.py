import requests,re,json,time,sys
from bs4 import BeautifulSoup
from fetch import UA
def parse(u):
    r=requests.get(u,headers=UA,timeout=25)
    s=BeautifulSoup(r.text,'html.parser'); out=[]
    for res in s.select('div.result'):
        n=res.select_one('a.business-name')
        if not n: continue
        a=res.select_one('.street-address'); loc=res.select_one('.locality'); p=res.select_one('.phones'); c=res.select_one('.categories'); w=res.select_one('a.track-visit-website')
        out.append(dict(name=n.get_text(strip=True),addr=a.get_text(' ',strip=True) if a else '',loc=loc.get_text(' ',strip=True) if loc else '',phone=p.get_text(strip=True) if p else '',cats=c.get_text(',',strip=True) if c else '',mip='https://www.yellowpages.com'+n.get('href',''),web=w['href'] if w else '',src=u))
    return r.status_code,out
if __name__=='__main__':
    base=sys.argv[1]; pages=int(sys.argv[2]); outf=sys.argv[3]
    allr={}
    for i in range(1,pages+1):
        u=base+(('&' if '?' in base else '?')+f'page={i}' if i>1 else '')
        st,o=parse(u); print(u,st,len(o),file=sys.stderr)
        new=0
        for x in o:
            if x['mip'] not in allr: allr[x['mip']]=x; new+=1
        if not o or new==0: break
        time.sleep(1)
    json.dump(list(allr.values()),open(outf,'w'),indent=1)
    for x in allr.values(): print(x['name'],'|',x['addr'],'|',x['loc'],'|',x['phone'],'|',x['cats'],'|',x['web'])
