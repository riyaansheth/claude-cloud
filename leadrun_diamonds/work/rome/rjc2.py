import requests,json
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
r=requests.get('https://www.responsiblejewellery.com/wp-json/wp/v2/types',headers=UA,timeout=20,verify='/root/.ccr/ca-bundle.crt')
d=r.json()
for k,v in d.items(): print(k,v.get('rest_base'),v.get('taxonomies'))
