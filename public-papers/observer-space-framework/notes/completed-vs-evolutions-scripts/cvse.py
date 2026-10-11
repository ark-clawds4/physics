# Completed histories vs Paper 1 evolutions: is the map from decision paths (D2) to proper-time traces (D1) injective
# on the reachable part of the Kretschmann rule? It is injective iff no reachable decision has an arm whose target is the
# source germ itself (a self-loop) or two arms with one target. Schwarzschild M=1, instance [10,20], double precision
# (same rule, target map and (a) test as notes/turning-type-lemma-scripts/censusf286.py; dedupe key 10 significant digits).
# A target germ equals the source germ iff r' = r0 (same static speed v is kept by the jump), so we record min |r'-r0|/r0
# over all arms, and min |r1'-r2'|/r0 between the two edge targets at a decision.
# Usage: python cvse.py MODEL C DEPTH CONV   MODEL in {a, noa}; CONV in {stop, through}; DEPTH = BFS depth cap.
import sys, math
def ell(r): return math.sqrt(r*(r-2))+2*math.log((math.sqrt(r)+math.sqrt(r-2))/math.sqrt(2))
def target(r,sg,c,conv):
    eps=c*r**1.5/48**0.25; goal=ell(r)+sg*eps; through=False
    if goal<=0:
        if conv=='stop' or goal==0: return None
        goal=-goal; through=True
    x=max(r+sg*eps,2.0+1e-12) if not through else r
    for _ in range(200):
        xn=x-(ell(x)-goal)/math.sqrt(x/(x-2))
        if xn<=2: xn=2+(x-2)/2
        if abs(xn-x)<=1e-15*x: x=xn; break
        x=xn
    return x,through
def EL(a,b):
    p=2*a*b/(a+b); e=(b-a)/(b+a)
    return math.sqrt((p-2-2*e)*(p-2+2*e)/(p*(p-3-e*e))), math.sqrt(p*p/(p-3-e*e))
def classify(rp,E,L):
    a=E*E-1; q1=2+a*rp; q0=-L*L+q1*rp; disc=q1*q1-4*a*q0
    others=sorted([(-q1-math.sqrt(disc))/(2*a),(-q1+math.sqrt(disc))/(2*a)]) if (a!=0 and disc>=0) else ([] if a!=0 else [-q0/q1])
    g=-(2/rp**2)*(1+L*L/rp**2)+(1-2/rp)*(2*L*L/rp**3)
    if g>0:
        hi=[x for x in others if x>rp]
        return ('peri-bound',rp,min(hi)) if (E<1 and hi) else ('peri-unbound',rp,math.inf)
    lo=[x for x in others if 2<x<rp]
    return ('apo-bound',max(lo),rp) if lo else ('apo-plunge',2.0,rp)
def main(model,c,depth,conv):
    E,L=EL(10.0,20.0); key=lambda lo,hi:(f'{lo:.9e}',f'{hi:.9e}')
    seen={key(10.0,20.0)}; fr=[(10.0,20.0,E,L)]; d=0
    dec=0; arms=0; selfloop=0; same=0; through=0; mins=math.inf; minpair=math.inf; amax=20.0
    while fr and d<depth:
        nf=[]
        for lo,hi,E,L in fr:
            for r0 in (lo,hi):
                tg=[]
                for sg in (1,-1):
                    t=target(r0,sg,c,conv)
                    if t is None: continue
                    rp,th=t; through+=th
                    E2=E*math.sqrt((1-2/rp)/(1-2/r0)); L2=L*rp/r0; kind,a_,b_=classify(rp,E2,L2)
                    ok=(a_<=r0<=b_) and rp!=r0
                    if model=='a' and not ok: continue
                    tg.append(rp); mins=min(mins,abs(rp-r0)/r0); selfloop+= abs(rp-r0)<=1e-9*r0
                    if kind in ('peri-bound','apo-bound'):
                        k=key(a_,b_)
                        if k not in seen: seen.add(k); nf.append((a_,b_,E2,L2)); amax=max(amax,b_)
                if tg:                                  # a decision: continue arm + edges in force
                    dec+=1; arms+=1+len(tg)
                    if len(tg)==2:
                        minpair=min(minpair,abs(tg[0]-tg[1])/r0); same+= abs(tg[0]-tg[1])<=1e-9*r0
        fr=nf; d+=1
    print(f'model={model} c={c} conv={conv} depth={d}{" (exhausted)" if not fr else " (capped)"}: orbits {len(seen)}, '
          f'decisions {dec}, arms {arms}, self-loops {selfloop}, coincident edge targets {same}, through-throat edges {through}, '
          f'min |r\'-r0|/r0 {mins:.6g}, min |r1\'-r2\'|/r0 {minpair if minpair<math.inf else float("nan"):.6g}, max apastron {amax:.6g}')
if __name__=='__main__':
    main(sys.argv[1],float(sys.argv[2]),int(sys.argv[3]),sys.argv[4])
