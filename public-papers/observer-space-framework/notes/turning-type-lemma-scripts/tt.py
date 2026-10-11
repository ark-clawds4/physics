# Turning-type lemma (#203): core functions, Schwarzschild M=1, mpmath. Self-contained (cross-checked against g201/r1.py).
# Rule: at a turning point r (u^r=0) with static-frame tangential speed v, jump along t=const by proper radial length
# eps=c*r^(3/2)/48^(1/4); u parallel-transported => static-frame speed v kept; target is a turning point with the same v.
# (a): target geodesic reaches the source radius in its past and target != a germ of the source's forward curvelet.
import mpmath as mp
mp.mp.dps=60
def ell(r): r=mp.mpf(r); return mp.sqrt(r*(r-2))+2*mp.log((mp.sqrt(r)+mp.sqrt(r-2))/mp.sqrt(2))   # l(r)-l(2)
def eps(r,c): return mp.mpf(c)*mp.mpf(r)**mp.mpf(1.5)/mp.mpf(48)**mp.mpf(0.25)
def EL_from_rv(r,v): r=mp.mpf(r); g=1/mp.sqrt(1-v**2); return mp.sqrt(1-2/r)*g, r*g*v
def v_from_EL(r,E,L): w=L/r; return w/mp.sqrt(1+w**2)            # tangential static speed at a turning point
def EL_orbit(a,b):  # bound orbit with turning points a<b
    a=mp.mpf(a); b=mp.mpf(b); p=2*a*b/(a+b); e=(b-a)/(b+a)
    return mp.sqrt((p-2-2*e)*(p-2+2*e)/(p*(p-3-e**2))), mp.sqrt(p**2/(p-3-e**2))
def rdot2(r,E,L): return E**2-(1-2/r)*(1+L**2/r**2)
def target(r,sign,c,throat='stop'):
    """radius reached by the spacelike radial geodesic; returns (r', through_throat) or None if undefined."""
    r=mp.mpf(r); goal=ell(r)+sign*eps(r,c); through=False
    if goal<=0:
        if throat=='stop' or goal==0: return None
        goal=-goal; through=True
    lo,hi=(r,r+eps(r,c)+1) if (goal>=ell(r)) else (mp.mpf(2),r)
    rp=mp.findroot(lambda x: ell(x)-goal,(lo,hi),solver='anderson')
    return rp,through
def classify(rp,E,L):
    """kind of the turning point rp and radial range [lo,hi] of the connected component of rdot^2>=0 containing rp."""
    a,b,cc,d=E**2-1,mp.mpf(2),-L**2,2*L**2         # r^3 rdot^2 = a r^3 + b r^2 + cc r + d
    q1=b+a*rp; q0=cc+q1*rp
    disc=q1**2-4*a*q0
    others=sorted([(-q1-mp.sqrt(disc))/(2*a),(-q1+mp.sqrt(disc))/(2*a)]) if (a!=0 and disc>=0) else ([] if a!=0 else [-q0/q1])
    g=-(2/rp**2)*(1+L**2/rp**2)+(1-2/rp)*(2*L**2/rp**3)       # d(rdot^2)/dr
    if g>0:
        hi=[x for x in others if x>rp]
        return ('peri-bound',rp,min(hi)) if (E<1 and hi) else ('peri-unbound',rp,mp.inf)
    if g<0:
        lo=[x for x in others if x<rp and x>2]
        return ('apo-bound',max(lo),rp) if lo else ('apo-plunge',mp.mpf(2),rp)
    return ('circular',rp,rp)
def edge(r,sign,c,v,throat='stop'):
    t=target(r,sign,c,throat)
    if t is None: return None
    rp,through=t; E2,L2=EL_from_rv(rp,v); kind,lo,hi=classify(rp,E2,L2)
    ok = (lo<=r<=hi) and rp!=r       # rp==r only via the throat: same oriented germ as the source, on its own curvelet
    return dict(rp=rp,through=through,kind=kind,lo=lo,hi=hi,ok=ok,E=E2,L=L2,margin=v**2-1/(rp-2))
