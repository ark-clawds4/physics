# Schwarzschild M=1 tools for the Kretschmann +-eps n rule (v0.6 §5.4), (a)-test via F(O).
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
K=lambda r: 48.0/r**6
THROAT='cross'   # 'cross' (Kruskal continuation) or 'none' (target undefined)
def s(r): return np.sqrt(r*(r-2))+2*np.log(np.sqrt(r)+np.sqrt(r-2))   # proper radial distance on t=const (ds=dr/sqrt(1-2/r))
def orbit_EL(r1,r2):
    p=2*r1*r2/(r1+r2); e=(r2-r1)/(r2+r1)
    L2=p**2/(p-3-e**2); E2=(p-2-2*e)*(p-2+2*e)/(p*(p-3-e**2)); return np.sqrt(E2),np.sqrt(L2)
def rdot2(r,E,L): return E**2-(1-2/r)*(1+L**2/r**2)
def realroots(E,L):
    rt=np.roots([E**2-1,2,-L**2,2*L**2]); return np.sort(rt[np.abs(rt.imag)<1e-9].real)
def frame(r,E,L):  # static-frame components at a turning point (u^r=0)
    return E/np.sqrt(1-2/r), L/r
def target(r,sign,c,E,L):
    eps=c*K(r)**-0.25
    d=s(r)+sign*eps-s(2.0)          # signed proper distance from the bifurcation sphere along t=const
    if d<0:
        if THROAT=='none': return None
        d=-d                          # continues into the other exterior (region III); mirror isometry X->-X maps it back to region I
    rp=brentq(lambda x: s(x)-s(2.0)-d,2+1e-12,max(1e12,10*d+10),xtol=1e-13)
    ut,up=frame(r,E,L)
    return rp, np.sqrt(1-2/rp)*ut, rp*up, eps
def classify(rp,E,L):
    """Return (kind, lo, hi): past/future r-range of the geodesic through turning point rp.
    kind: 'bound' (range [r1,r2]), 'plunge' (rp is apastron of plunge from white hole: range (0,rp]),
          'unbound' (rp periastron, escapes: range [rp,inf))."""
    h=1e-7*rp
    above=rdot2(rp+h,E,L)>0; below=rdot2(rp-h,E,L)>0
    rts=[x for x in realroots(E,L) if x>0]
    if above and not below:  # periastron
        higher=[x for x in rts if x>rp*(1+1e-9)]
        if E<1 and higher: return 'bound',rp,min(higher)
        return 'unbound',rp,np.inf
    if below and not above:  # apastron
        lower=[x for x in rts if x<rp*(1-1e-9)]
        if lower and max(lower)>2 and rdot2((max(lower)+rp)/2,E,L)>0: return 'bound',max(lower),rp
        return 'plunge',0.0,rp
    return 'degenerate',rp,rp
def admissible(rs,rp,E2,L2):
    """(a): target's own curvelet passes through the source lump (radius rs) in its past (F(O) test)."""
    kind,lo,hi=classify(rp,E2,L2)
    return (lo-1e-12<=rs<=hi+1e-12) and abs(rp-rs)>1e-12, kind,lo,hi
def half_period(r1,r2,E,L):
    f=lambda chi: 0
    # tau from r1 to r2 via r=(A - B cos chi)
    A=(r1+r2)/2; B=(r2-r1)/2
    rts=realroots(E,L); r3=min(rts)
    g=lambda chi: np.sqrt((A-B*np.cos(chi))**3/((1-E**2)*((A-B*np.cos(chi))-r3)))
    return quad(g,0,np.pi,epsabs=1e-12,epsrel=1e-12)[0]
