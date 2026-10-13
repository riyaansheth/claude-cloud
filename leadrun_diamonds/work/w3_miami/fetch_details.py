import requests,time,json,re,os
from bs4 import BeautifulSoup
H={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
paths=['first-floor-directory/','second-floor-directory/','brands/','online-shopping/','aruba-gold-inc/','alberts-fine-jewelers','barclays-jewelers','bos-jewelers-inc','brilliance-jewels','buchwald-jewelers-inc','d-k-n-gems-jewelry-inc','dasani-jewels-inc-pandora','debranf-jewelry-llc','diamantero-corp','diamond-club-inc','e-frai-co','ferrari-express-inc','g-luxe-jewelers','italian-jewelry-inc','jimmy-quiroga-designs-lido-jewerly','maipo-corp','malca-amit','nemaro-jewelers-inc','richards-gems-jewelry/','siriporn-inc','swiss-time-buyers','?page_id=2818','?page_id=5644']
os.makedirs('pages',exist_ok=True)
res={}
for p in paths:
    u='https://seyboldjewelry.com/'+p
    try:
        r=requests.get(u,headers=H,timeout=20)
        s=BeautifulSoup(r.text,'html.parser')
        main=s.select_one('#Content') or s
        for x in main.select('script,style,nav,header,footer'): x.decompose()
        txt=main.get_text(' | ',strip=True)
        links=sorted(set(a['href'] for a in main.find_all('a',href=True) if 'seyboldjewelry' not in a['href'] and a['href'].startswith(('http','mailto','tel'))))
        res[p]=dict(url=r.url,status=r.status_code,text=txt[:1500],links=links)
        print('###',p,r.status_code,r.url); print(txt[:700]); print(links[:20])
    except Exception as e: print('ERR',p,e)
    time.sleep(0.6)
json.dump(res,open('details.json','w'),indent=1)
