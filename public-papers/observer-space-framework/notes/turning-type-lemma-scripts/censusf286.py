# Double-precision port of g201/census.py reach(c, restricted=True) (same rule, same (a) test, same dedupe key: 10 significant
# digits of the range), for the c=0.001 census. Validated by reproducing c=0.1 and c=0.01 exactly. Any edge whose (a) decision
# or turning type sits within 1e-9 (relative) of a boundary is re-decided in mpmath (tt.py, dps 40) and counted.
import sys, math, time
from collections import Counter
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__))); import tt, mpmath as mp
mp.mp.dps=40
def ell(r): return math.sqrt(r*(r-2))+2*math.log((math.sqrt(r)+math.sqrt(r-2))/math.sqrt(2))
def target(r,sg,c):
    eps=c*r**1.5/48**0.25; goal=ell(r)+sg*eps
    if goal<=0: return None
    x=r+sg*eps                                   # Newton on ell(x)=goal, d ell/dx = sqrt(x/(x-2))
    for _ in range(100):
        dx=(ell(x)-goal)/math.sqrt(x/(x-2)); xn=x-dx
        if xn<=2: xn=2+(x-2)/2
        if abs(xn-x)<=1e-15*x: x=xn; break
        x=xn
    return x
def EL(a,b):
    p=2*a*b/(a+b); e=(b-a)/(b+a)
    return math.sqrt((p-2-2*e)*(p-2+2*e)/(p*(p-3-e*e))), math.sqrt(p*p/(p-3-e*e))
def classify(rp,E,L):
    a=E*E-1; b=2.0; cc=-L*L; q1=b+a*rp; q0=cc+q1*rp; disc=q1*q1-4*a*q0
    if a!=0 and disc>=0:
        s=math.sqrt(disc); others=sorted([(-q1-s)/(2*a),(-q1+s)/(2*a)])
    elif a==0: others=[-q0/q1]
    else: others=[]
    g=-(2/rp**2)*(1+L*L/rp**2)+(1-2/rp)*(2*L*L/rp**3)
    if g>0:
        hi=[x for x in others if x>rp]
        return ('peri-bound',rp,min(hi)) if (E<1 and hi) else ('peri-unbound',rp,math.inf), g
    hi_=[x for x in others if 2<x<rp]
    return (('apo-bound',max(hi_),rp) if hi_ else ('apo-plunge',2.0,rp)), g
FALLBACK=Counter()
def edge(r,sg,c,E,L):
    rp=target(r,sg,c)
    if rp is None: return None
    E2=E*math.sqrt((1-2/rp)/(1-2/r)); L2=L*rp/r
    (kind,lo,hi),g=classify(rp,E2,L2)
    ok=lo<=r<=hi
    tight = min(abs(r-lo),abs(r-hi) if hi!=math.inf else 1)/r<1e-9 or abs(g)*rp*rp<1e-9
    if tight:                                     # re-decide in mpmath
        FALLBACK['edges re-decided in mpmath']+=1
        v=tt.v_from_EL(mp.mpf(r),mp.mpf(E),mp.mpf(L)); e=tt.edge(mp.mpf(r),sg,mp.mpf(c),v,'stop')
        kind,lo,hi,ok=e['kind'],float(e['lo']),float(e['hi']),e['ok']; FALLBACK['  of which changed']+= int(ok!=(lo<=r<=hi))
    return dict(rp=rp,kind=kind,lo=lo,hi=hi,ok=ok,E=E2,L=L2)
def key(lo,hi): return (f'{lo:.9e}',f'{hi:.9e}')
def reach(c,cap=10**8,depth=10**9):
    E,L=EL(10.0,20.0); seen={key(10.0,20.0)}; fr=[(10.0,20.0,E,L)]; tab=Counter(); stuck=Counter(); d=0; amax=20.0; THR=Counter()
    while fr and len(seen)<cap and d<depth:
        nf=[]
        for lo,hi,E,L in fr:
            adm=0
            for rs,turn in ((lo,'peri'),(hi,'apo')):
                for sg in (1,-1):
                    e=edge(rs,sg,c,E,L)
                    if e is None: THR['throat']+=1; continue
                    away=(turn=='peri' and sg<0) or (turn=='apo' and sg>0)
                    tab[(turn,'out' if sg>0 else 'in','away' if away else 'toward',e['kind'],'PASS' if e['ok'] else 'FAIL')]+=1
                    if e['ok']:
                        adm+=1
                        if e['kind'] in ('peri-bound','apo-bound'):
                            k=key(e['lo'],e['hi'])
                            if k not in seen: seen.add(k); nf.append((e['lo'],e['hi'],e['E'],e['L'])); amax=max(amax,e['hi'])
            if adm==0: stuck['no admissible edge']+=1
        fr=nf; d+=1
        print(f'  depth {d}: orbits {len(seen)}, frontier {len(fr)}',file=sys.stderr,flush=True)
    return len(seen),tab,stuck,d,amax,THR
if __name__=='__main__':
    c=float(sys.argv[1]); t0=time.time()
    n,tab,stuck,d,amax,THR=reach(c,depth=int(sys.argv[2]) if len(sys.argv)>2 else 10**9)
    tw=sum(v for k,v in tab.items() if k[2]=='toward'); tp=sum(v for k,v in tab.items() if k[2]=='toward' and k[4]=='PASS')
    kept=sum(v for k,v in tab.items() if k[2]=='toward' and k[3].startswith(k[0]))
    print(f'c={c}: reachable orbits {n} (depth {d}; frontier at stop {len(fr_left)}) ;' if False else f'c={c}: orbits {n} (BFS depth {d}); into-range edges {tw}, passing {tp}, type kept {kept}; stuck {dict(stuck)}; '
          f'max apastron {amax:.6g}; throat {dict(THR)}; {dict(FALLBACK)}; {time.time()-t0:.0f}s')
    for k,v in sorted(tab.items()): print('  ',k,v)
