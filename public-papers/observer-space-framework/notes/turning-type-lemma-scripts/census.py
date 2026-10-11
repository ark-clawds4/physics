# Is "at the periastron the outward edge fails (a) and the inward passes; at the apastron the reverse" general?
# Uses r1.py's from-scratch rule and (a) test (analytic dV for speed, 30 digits).
# Part A: every turning point of every orbit reachable under the (a)-restricted rule from [10,20], c=0.01 (C33's census),
#         and c=0.1. Part B: rule as stated (no (a)), all orbits reachable within depth D. Part C: a grid of bound orbits.
import sys, mpmath as mp, r1
from collections import Counter
mp.mp.dps=30
r1.dV=lambda r,E,L: -(2/r**2)*(1+L**2/r**2)+(1-2/r)*(2*L**2/r**3)
_tgt=r1.target
def _target(r,sign,c,E,L):
    goal=r1.s(r)+sign*c*(48/r**6)**(-mp.mpf(1)/4)
    if goal<=r1.s(mp.mpf(2)): raise AssertionError('throat')
    rp=mp.findroot(lambda x: r1.s(x)-goal, mp.mpf(2)+ (r-2)*mp.e**(sign*c*(48/r**6)**(-mp.mpf(1)/4)/r) , solver='anderson' if False else 'secant')
    rp=mp.re(rp); rp=mp.findroot(lambda x: r1.s(x)-goal, rp)
    assert abs(mp.im(rp))<mp.mpf('1e-20'); rp=mp.re(rp)
    return rp, E*mp.sqrt((1-2/rp)/(1-2/r)), L*rp/r, None
r1.target=_target
THROAT=Counter()
def tp_edges(rs,E,L,c):
    out={}
    for sg in (1,-1):
        try: out[sg]=r1.edge(rs,sg,c,E,L)
        except AssertionError: THROAT['throat reached (edge skipped)']+=1
    return out
def label(turn,sg,e):
    d='out' if sg>0 else 'in'
    away = (turn=='peri' and sg<0) or (turn=='apo' and sg>0)     # jumps away from the orbit's radial range
    return (turn, d, 'away' if away else 'toward', e['kind'], 'PASS' if e['ok'] else 'FAIL')
def reach(c, restricted, depth=10**9, cap=10**6):
    E,L=r1.EL(10,20); key=lambda lo,hi:(mp.nstr(lo,10),mp.nstr(hi,10))
    seen={key(mp.mpf(10),mp.mpf(20)):(mp.mpf(10),mp.mpf(20),E,L)}; fr=list(seen.values()); tab=Counter(); stuck=Counter(); ex=[]
    d=0
    while fr and d<depth and len(seen)<cap:
        nf=[]
        for lo,hi,E,L in fr:
            adm=0
            for rs,turn in ((lo,'peri'),(hi,'apo')):
                for sg,e in tp_edges(rs,E,L,c).items():
                    lab=label(turn,sg,e); tab[lab]+=1
                    if (lab[2]=='toward' and e['ok']) or (lab[2]=='away' and not e['ok']):
                        if len(ex)<400: ex.append((mp.nstr(lo,8),mp.nstr(hi,8),turn,lab[1],mp.nstr(e['rp'],8),e['kind'],mp.nstr(e['lo'],6),mp.nstr(e['hi'],6),lab[4]))
                    if e['ok']: adm+=1
                    if (e['ok'] or not restricted) and e['kind'] in ('peri-bound','apo-bound'):
                        k=key(e['lo'],e['hi'])
                        if k not in seen: seen[k]=(e['lo'],e['hi'],e['E'],e['L']); nf.append(seen[k])
            if adm==0: stuck['no admissible edge']+=1
        fr=nf; d+=1
    return len(seen), tab, stuck, ex, d
if __name__=='__main__':
    part=sys.argv[1]
    if part=='A':
        c=mp.mpf(sys.argv[2])
        n,tab,stuck,ex,d=reach(c,True)
        print(f'A: (a)-restricted, c={c}: reachable orbits {n}; stuck {dict(stuck)}')
        for k,v in sorted(tab.items()): print('  ',k,v)
        print('  exceptions (toward passes / away fails):',len(ex)); [print('   ',x) for x in ex[:20]]
        from collections import Counter as C
        print('  exception types:',C((x[2],x[3],x[5],x[8]) for x in ex))
    if part=='B':
        c=mp.mpf(sys.argv[2]); D=int(sys.argv[3])
        n,tab,stuck,ex,d=reach(c,False,depth=D)
        print(f'B: rule as stated, c={c}, depth {d}: orbits {n}; {dict(THROAT)}')
        for k,v in sorted(tab.items()): print('  ',k,v)
        print('  exceptions:',len(ex)); from collections import Counter as C; print('  exception types:',C((x[2],x[3],x[5],x[8]) for x in ex)); [print('   ',x) for x in ex[:8]]
    if part=='C':
        tab=Counter(); ex=[]
        r1s=[mp.mpf(x) for x in ('4.5','5','6','7','8','10','12','15','20','30','50','100')]
        for c in ('0.001','0.01','0.1','0.3'):
            c=mp.mpf(c)
            for a in r1s:
                for f in ('1.001','1.01','1.1','1.5','2','3','5','10','30'):
                    b=a*mp.mpf(f); p=2*a*b/(a+b); e=(b-a)/(b+a)
                    if p<=6+2*e: continue      # not a stable bound orbit
                    E,L=r1.EL(a,b)
                    for rs,turn in ((a,'peri'),(b,'apo')):
                        try: es=tp_edges(rs,E,L,c)
                        except AssertionError: continue
                        for sg,ed in es.items():
                            lab=label(turn,sg,ed); tab[lab]+=1
                            if (lab[2]=='toward' and ed['ok']) or (lab[2]=='away' and not ed['ok']):
                                ex.append((mp.nstr(c,3),mp.nstr(a,5),mp.nstr(b,6),turn,lab[1],mp.nstr(ed['rp'],7),ed['kind'],mp.nstr(ed['lo'],6),mp.nstr(ed['hi'],6),lab[4]))
        print('C: grid', dict(THROAT)); [print('  ',k,v) for k,v in sorted(tab.items())]
        from collections import Counter as C
        print('  exceptions:',len(ex),C((x[3],x[4],x[6],x[9]) for x in ex)); [print('   ',x) for x in ex[:25]]
