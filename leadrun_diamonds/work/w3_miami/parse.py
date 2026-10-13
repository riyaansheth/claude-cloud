import json
from bs4 import BeautifulSoup
s=BeautifulSoup(open('dir.html').read(),'html.parser')
out=[]
for c in s.select('div.column.one-second'):
    h=c.find('h2'); p=c.select_one('.hover_color_wrapper p'); a=c.select_one('a[href^="tel:"]')
    links=[x['href'] for x in c.find_all('a',href=True) if not x['href'].startswith('tel:')]
    out.append(dict(name=h.get_text(' ',strip=True) if h else '',suite=p.get_text(' ',strip=True) if p else '',phone=a.get_text(strip=True) if a else '',links=links))
json.dump(out,open('tenants.json','w'),indent=1)
for i,o in enumerate(out): print(i,o['name'],'|',o['suite'],'|',o['phone'],o['links'])
