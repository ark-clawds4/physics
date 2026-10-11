# Exact law of the jump count for the (a)-restricted Kretschmann rule (rule as stated otherwise; kr.py THROAT default,
# irrelevant under (a): throat never reached), EPP1 chance process ((M1)-style: 1/|A| per arm at each decision),
# root = r=10 periastron of [10,20], a=seg. Exact rationals; exhaustive (no sampling, no seed).
# Also: reachable-orbit census with several stuck-orbit definitions, to locate 14,477 vs 14,478.
import os, sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from kr import orbit_EL, target, admissible, classify
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import numpy as np
c=float(sys.argv[1]) if len(sys.argv)>1 else 0.01
E0,L0=orbit_EL(10,20)

@lru_cache(maxsize=None)
def edges_at(r,E,L):
    """admissible jump targets from turning point r of orbit (E,L)"""
    out=[]
    for sg in (1,-1):
        T=target(r,sg,c,E,L)
        if T is None: continue
        rp,E2,L2,_=T; ok,kind,lo,hi=admissible(r,rp,E2,L2)
        if ok: out.append((rp,E2,L2,kind,lo,hi,sg))
    return tuple(out)
def other(r,E,L):
    k,lo,hi=classify(r,E,L); assert k=='bound'
    if abs(r-lo)<1e-9*r: return hi
    assert abs(r-hi)<1e-9*r; return lo

@lru_cache(maxsize=None)
def law(r,E,L):
    """History about to be at turning point r (a decision if r carries an edge), orbit (E,L).
    Returns (dict jumps->prob, expected decisions, set of terminal kinds). Exact."""
    x=r; y=other(r,E,L)
    ex=edges_at(x,E,L); ey=edges_at(y,E,L)
    assert len(ex)<=1 and len(ey)<=1, "m<=1 violated"
    if not ex and not ey:
        return {0:F(1)}, F(0), ('stuck',)
    # decision sequence alternates x,y,x,y,... skipping points without an edge; each decision 1/2 jump
    # P(first jump at x), P(at y), expected decisions until first jump
    if ex and ey:  # decisions at every visit: jump at x w.p. 2/3, at y w.p. 1/3; E[decisions]=2
        branches=[(F(2,3),ex[0]),(F(1,3),ey[0])]
    else:
        branches=[(F(1),(ex or ey)[0])]
    Edec=F(2)
    dist={}; kinds=set(); Esub=F(0)
    for p,(rp,E2,L2,kind,lo,hi,sg) in branches:
        if kind=='bound':
            d2,e2,k2=law(other(rp,E2,L2),E2,L2)   # jump-reached state does not branch; next decision point is the other tp
        else:
            d2,e2,k2={0:F(1)},F(0),(kind,)
        for j,q in d2.items(): dist[j+1]=dist.get(j+1,0)+p*q
        Esub+=p*e2; kinds|=set(k2)
    return dist, Edec+Esub, tuple(sorted(kinds))

dist,Ed,kinds=law(10.0,E0,L0)
print("c=%g exact jump-count law (EPP1, (a)):"%c)
for j in sorted(dist): print("  P(J=%d) = %s ~ %.6g"%(j,dist[j] if dist[j].denominator<10**12 else '(big rational)',float(dist[j])))
print("  sum =",sum(dist.values()),"; E[J] = %.6f ; E[decisions] = %.6f ; terminal kinds %s"%(float(sum(j*q for j,q in dist.items())),float(Ed),kinds))

# census of reachable orbits (orbit = (lo,hi)), as in g154/agraph.py
def key(lo,hi,nd=9): return (round(lo,nd),round(hi,nd))
seen={}; fr=[(10.0,20.0,E0,L0)]; seen[key(10,20)]=(10.0,20.0,E0,L0)
while fr:
    nf=[]
    for lo,hi,E,L in fr:
        for rs in (lo,hi):
            for rp,E2,L2,kind,a,b,sg in edges_at(rs,E,L):
                if kind!='bound': continue
                k=key(a,b)
                if k not in seen: seen[k]=(a,b,E2,L2); nf.append((a,b,E2,L2))
    fr=nf
cnt=Counter()
for k,(lo,hi,E,L) in seen.items():
    el=edges_at(lo,E,L); eh=edges_at(hi,E,L)
    alle=el+eh
    cnt['orbits']+=1
    if not alle: cnt['stuck: no admissible edge']+=1
    if not [e for e in alle if e[3]=='bound']: cnt['stuck: no admissible bound edge']+=1
    if alle and not [e for e in alle if e[3]=='bound']: cnt['only non-bound admissible edges']+=1
    if el and eh: cnt['edges at both turning points']+=1
print("census:",dict(cnt))
# keys at other rounding
for nd in (6,7,8,10,11,12):
    print("  distinct orbits at round(.,%d): %d"%(nd,len({key(v[0],v[1],nd) for v in seen.values()})))
