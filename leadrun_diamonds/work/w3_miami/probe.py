import requests,json,re,time,concurrent.futures as cf
H={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
T=json.load(open('tenants.json'))
STOP={'inc','llc','corp','corporation','co','copr','the','dba','d/b/a','int','intl','international','group','enterprises','enterprise'}
def toks(n):
    n=n.lower().replace('&',' and ').replace("’","'")
    n=re.sub(r"[^a-z0-9' ]",' ',n).replace("'",'')
    return [w for w in n.split() if w]
def guesses(n):
    w=toks(n); core=[x for x in w if x not in STOP]
    g=set()
    for base in [core, [x for x in core if x!='and'], w]:
        s=''.join(base)
        if s: g.add(s)
    s=''.join([x for x in core if x!='and'])
    g|={s+'miami', s+'jewelry', s+'jewelers', s+'inc'}
    if 'diamonds' in core: g.add(s.replace('diamonds','diamond'))
    return [x+'.com' for x in g if 3<len(x)<40]
def digits(p): return re.sub(r'\D','',p)[-7:]
def check(t,dom):
    for pre in ['https://','https://www.','http://www.']:
        try:
            r=requests.get(pre+dom,headers=H,timeout=12,allow_redirects=True)
            if r.status_code>=400: continue
            txt=r.text.lower(); d=digits(t['phone']) if t['phone'] else 'zzzz'
            plain=re.sub(r'\D','',txt)
            hit=[]
            if 'seybold' in txt: hit.append('seybold')
            if re.search(r'36\s*n\.?\s*e\.?\s*1(st)?',txt) or '36 northeast 1' in txt: hit.append('36ne1')
            if len(d)==7 and d in plain: hit.append('phone')
            return dict(dom=dom,url=r.url,hit=hit,status=r.status_code,len=len(txt))
        except Exception: pass
    return None
jobs=[]
for i,t in enumerate(T):
    for g in guesses(t['name']): jobs.append((i,g))
print(len(jobs))
res={}
with cf.ThreadPoolExecutor(24) as ex:
    fut={ex.submit(check,T[i],g):(i,g) for i,g in jobs}
    for f in cf.as_completed(fut):
        i,g=fut[f]; r=f.result()
        if r: res.setdefault(i,[]).append(r)
json.dump(res,open('probe.json','w'),indent=1)
for i in sorted(res,key=int):
    for r in res[i]:
        if r['hit']: print(i,T[i]['name'],'->',r['url'],r['hit'])
