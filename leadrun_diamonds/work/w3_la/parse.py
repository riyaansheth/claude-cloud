import json,re
from bs4 import BeautifulSoup
s=BeautifulSoup(open('dir1.html').read(),'html.parser')
out=[]
for it in s.select('div.collection_item'):
    g=lambda sel: (it.select_one(sel).get_text(' ',strip=True) if it.select_one(sel) else '')
    a=it.select_one('span.website a')
    site=(a.get('href') or '').strip() if a else g('span.website')
    out.append(dict(name=g('.name h2'),type=g('.name span'),spec=g('.spe').replace('Speciality :','').strip(),
      goods=g('.goods-cer'),secondary=g('.spe-spec'),site=site,phone=g('span.work_phone'),addr=g('span.addr'),
      classes=it.get('class'),year=(it.select_one('.mem-sin') or {}).get('data-filter','') if it.select_one('.mem-sin') else ''))
json.dump(out,open('members.json','w'),indent=1)
print(len(out))
