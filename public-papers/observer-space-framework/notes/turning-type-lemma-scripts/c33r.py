# Re-run c33x.py (exact EPP1 jump-count law + orbit census, (a)-restricted rule, c=0.01) with a robust classifier:
# the target's own radius rp is a known root of rdot^2 (it is a turning point by construction), so the cubic
# (E^2-1) r^3 + 2 r^2 - L^2 r + 2 L^2 is deflated by (r - rp) in 50-digit arithmetic and the remaining quadratic solved;
# periastron/apastron is decided by the analytic sign of d(rdot^2)/dr at rp. Float inputs are taken as exact.
# Everything else (target map, admissibility tolerances, EPP1 weights) is as in kr.py / c33x.py.
import os, sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp, kr
mp.mp.dps=50
_old=kr.classify
def classify_robust(rp,E,L):
    r=mp.mpf(rp); E=mp.mpf(E); L=mp.mpf(L)
    a,b,c_,d=E**2-1,mp.mpf(2),-L**2,2*L**2
    # synthetic division by (r - rp): a r^2 + (b + a rp) r + (c + (b + a rp) rp); remainder should be ~0
    q2=a; q1=b+a*r; q0=c_+q1*r
    disc=q1**2-4*q2*q0
    others=[]
    if disc>=0:
        s=mp.sqrt(disc); others=sorted([(-q1-s)/(2*q2),(-q1+s)/(2*q2)]) if q2!=0 else [-q0/q1]
    dV=(2/r**2)*(1+L**2/r**2)-(1-2/r)*(2*L**2/r**3)     # d/dr of (1-2/r)(1+L^2/r^2)
    drd=-dV                                             # d(rdot^2)/dr
    if drd>0:   # periastron: motion is outward of rp
        higher=[x for x in others if x>r*(1+mp.mpf('1e-12'))]
        if E<1 and higher: return 'bound',float(r),float(min(higher))
        return 'unbound',float(r),np.inf
    if drd<0:   # apastron
        lower=[x for x in others if x<r*(1-mp.mpf('1e-12'))]
        if lower and max(lower)>2: return 'bound',float(max(lower)),float(r)
        return 'plunge',0.0,float(r)
    return 'degenerate',float(r),float(r)
kr.classify=classify_robust
sys.argv=[sys.argv[0],sys.argv[1] if len(sys.argv)>1 else '0.01']
import runpy
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)),'c33x.py'),run_name='__main__')
# how many classifications differ from kr.classify on the targets met
