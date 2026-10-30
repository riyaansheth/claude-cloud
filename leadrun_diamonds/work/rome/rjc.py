import requests,json
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
for u in ['https://www.responsiblejewellery.com/wp-json/wp/v2/types','https://www.responsiblejewellery.com/wp-json/wp/v2/member?per_page=5']:
    r=requests.get(u,headers=UA,timeout=20,verify='/root/.ccr/ca-bundle.crt')
    print(u,r.status_code,r.text[:1500])
