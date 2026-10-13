import sys,json
sys.path.insert(0,'.')
import importlib.util
spec=importlib.util.spec_from_file_location('s2','site.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for root in sys.argv[1:]:
    extra=[]
    r=m.scan(root,extra)
    print('#####',root)
    agg={'mailto':set(),'tel':set(),'emails':set(),'phones':set(),'soc':set()}; sn=[]
    for u,d in r['pages'].items():
        if isinstance(d,str): print('  ',u,d[:60]); continue
        print('  OK',u,'->',d['final'])
        for k in agg: agg[k]|=set(d[k])
        for s in d['snips']:
            if not any(s[60:120] in x for x in sn): sn.append(s)
    for k,v in agg.items(): print(' ',k,sorted(v))
    for s in sn[:8]: print('   ..',s)
