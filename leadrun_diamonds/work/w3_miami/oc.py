import requests,json,time,re,sys
from bs4 import BeautifulSoup
H={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
Q=json.load(open(sys.argv[1]))
out=json.load(open('oc_out.json')) if __import__('os').path.exists('oc_out.json') else {}
for key,q in Q.items():
    if key in out: continue
    try:
        r=requests.get('https://opencorporates.com/companies',params={'q':q,'jurisdiction_code':'us_fl'},headers=H,timeout=20)
        s=BeautifulSoup(r.text,'html.parser')
        res=[]
        for li in s.select('li.search-result')[:8]:
            a=li.select_one('a.company_search_result')
            if a: res.append(dict(name=a.get_text(' ',strip=True),href=a['href'],inactive='inactive' in li.get('class',[]) or 'dissolved' in li.get_text().lower() or 'inactive' in li.get_text().lower()))
        det=[]
        for c in [x for x in res if not x['inactive']][:2]:
            time.sleep(1.2)
            rr=requests.get('https://opencorporates.com'+c['href'],headers=H,timeout=20)
            t=BeautifulSoup(rr.text,'html.parser').get_text(' ',strip=True)
            m=re.search(r'Company Number(.*?)Data source',t)
            det.append(dict(url='https://opencorporates.com'+c['href'],name=c['name'],info=(m.group(1) if m else t[:600])[:700]))
        out[key]=dict(q=q,results=res,details=det)
        print('##',key,'|',[x['name']+(' (inactive)' if x['inactive'] else '') for x in res][:5])
        for d in det: print('   ',d['url'],d['info'][:400])
    except Exception as e: print('ERR',key,e)
    time.sleep(1.2)
    json.dump(out,open('oc_out.json','w'),indent=1)
