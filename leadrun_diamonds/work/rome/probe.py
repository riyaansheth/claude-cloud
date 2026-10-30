import requests,sys,re
from concurrent.futures import ThreadPoolExecutor
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
def f(d):
    try:
        r=requests.get('https://'+d,headers=UA,timeout=15,verify='/root/.ccr/ca-bundle.crt')
        ti=re.search(r'<title[^>]*>(.*?)</title>',r.text,re.S|re.I)
        return d,r.status_code,r.url,(ti.group(1).strip()[:100] if ti else '')
    except Exception as e: return d,'ERR',str(e)[:60],''
with ThreadPoolExecutor(4) as ex:
    for x in ex.map(f,sys.argv[1:]): print(x)
