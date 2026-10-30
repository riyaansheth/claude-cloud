import requests,re,time,json
from concurrent.futures import ThreadPoolExecutor
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
urls=[u for u in open('rjc_members.txt').read().split() if re.search(r's-?r-?l|s-p-a|-spa|srls|-sas|-snc|gioiell|roma|rome|diamant',u)]
def f(u):
    try:
        t=requests.get(u,headers=UA,timeout=20,verify='/root/.ccr/ca-bundle.crt').text
        t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'\s+',' ',t)
        loc=re.search(r'Head Office Location:\s*(.*?)\s*Membership Forum:\s*(.*?)\s*(CODE OF|$)',t)
        web=re.search(r'Website:\s*(\S+)',t)
        return u,(loc.group(1) if loc else ''),(loc.group(2)[:80] if loc else ''),(web.group(1) if web else '')
    except Exception as e: return u,'ERR','',''
out=[]
with ThreadPoolExecutor(2) as ex:
    for res in ex.map(f,urls):
        out.append(res); time.sleep(0.3)
json.dump(out,open('rjc_it.json','w'))
for o in out:
    if re.search(r'rom',o[1],re.I): print(o)
