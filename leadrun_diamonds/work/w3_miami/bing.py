import requests,sys,time,json
from bs4 import BeautifulSoup
H={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36','Accept-Language':'en-US,en;q=0.9'}
def bing(q,n=8):
    r=requests.get('https://www.bing.com/search',params={'q':q,'setlang':'en','cc':'US'},headers=H,timeout=20)
    s=BeautifulSoup(r.text,'html.parser'); out=[]
    for li in s.select('li.b_algo')[:n]:
        a=li.select_one('h2 a'); sn=li.select_one('.b_caption p, .b_lineclamp2, .b_lineclamp3, .b_lineclamp4')
        cite=li.select_one('cite')
        out.append(dict(title=a.get_text(' ',strip=True) if a else '',url=a['href'] if a else '',cite=cite.get_text(strip=True) if cite else '',snip=sn.get_text(' ',strip=True) if sn else ''))
    return out
if __name__=='__main__':
    for q in sys.argv[1:]:
        print('=== ',q)
        for o in bing(q): print(' -',o['title'],'|',o['cite'],'|',o['url'][:120]); print('    ',o['snip'][:250])
        time.sleep(1.5)
