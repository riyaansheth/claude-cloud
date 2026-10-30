import requests,re,time
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
g=lambda u: requests.get(u,headers=UA,timeout=20,verify='/root/.ccr/ca-bundle.crt')
r=g('https://www.responsiblejewellery.com/sitemap_index.xml'); print(r.status_code)
sm=re.findall(r'<loc>(.*?)</loc>',r.text); print(sm)
urls=[]
for s in sm:
    if 'member' in s:
        t=g(s).text; urls+=re.findall(r'<loc>(.*?)</loc>',t)
print(len(urls))
open('rjc_members.txt','w').write('\n'.join(urls))
