# From-scratch recomputation (no import of kr.py / c33r.py) of the Kretschmann +-eps rule's edges and the (a) test,
# Schwarzschild M=1, bound orbit [10,20], c in {0.1, 0.01, 0.001}. mpmath, 40 digits.
# Rule (v0.8 §5.4): at a turning point r (u^r=0), jump along t=const by proper radial distance eps=c*K^(-1/4), K=48/r^6,
# outward (+) or inward (-), static-frame velocity components preserved: E'=E*sqrt((1-2/r')/(1-2/r)), L'=L*r'/r.
# (a) (v0.8 §4.2): target O'^{u'} in F(O)\gamma_{O^u}, i.e. the target's own geodesic reaches the source radius r_s in
# its past; for a turning-point target this is r_s in the radial range of the target's orbit, r' != r_s.
import mpmath as mp
mp.mp.dps=40
def EL(r1,r2):
    r1=mp.mpf(r1); r2=mp.mpf(r2); p=2*r1*r2/(r1+r2); e=(r2-r1)/(r2+r1)
    return mp.sqrt((p-2-2*e)*(p-2+2*e)/(p*(p-3-e**2))), mp.sqrt(p**2/(p-3-e**2))
def V(r,E,L): return E**2-(1-2/r)*(1+L**2/r**2)          # rdot^2
def dV(r,E,L): return mp.diff(lambda x: V(x,E,L), r)
def s(r): return mp.sqrt(r*(r-2))+2*mp.log(mp.sqrt(r)+mp.sqrt(r-2))
def target(r,sign,c,E,L):
    eps=c*(48/r**6)**(-mp.mpf(1)/4); goal=s(r)+sign*eps
    assert goal>s(mp.mpf(2))                                 # throat never reached for these cases
    rp=mp.findroot(lambda x: s(x)-goal, r+sign*eps*mp.sqrt(1-2/r))
    return rp, E*mp.sqrt((1-2/rp)/(1-2/r)), L*rp/r, eps
def orbit(rp,E,L):
    """type of turning point rp and radial range of the geodesic through it (roots of (E^2-1)r^3+2r^2-L^2r+2L^2)."""
    a,b,c_,d=E**2-1,mp.mpf(2),-L**2,2*L**2
    q1=b+a*rp; q0=c_+q1*rp; rem=d+q0*rp                     # deflate by (r-rp)
    disc=q1**2-4*a*q0; others=sorted([(-q1-mp.sqrt(disc))/(2*a),(-q1+mp.sqrt(disc))/(2*a)]) if disc>=0 else []
    g=dV(rp,E,L)
    if g>0:  # periastron
        hi=[x for x in others if x>rp*(1+mp.mpf('1e-20'))]
        return ('peri-bound',rp,min(hi)) if (E<1 and hi) else ('peri-unbound',rp,mp.inf)
    lo=[x for x in others if x<rp*(1-mp.mpf('1e-20'))]
    if lo and max(lo)>2 and V((max(lo)+rp)/2,E,L)>0: return ('apo-bound',max(lo),rp)
    return ('apo-plunge',mp.mpf(0),rp)
def edge(rs,sign,c,E,L):
    rp,E2,L2,eps=target(rs,sign,c,E,L); kind,lo,hi=orbit(rp,E2,L2)
    return dict(rp=rp,kind=kind,lo=lo,hi=hi,ok=(lo<=rs<=hi) and rp!=rs,eps=eps,E=E2,L=L2)
if __name__=='__main__':
    E,L=EL(10,20)
    print('orbit [10,20]: E=%s L=%s; rdot^2(10)=%s rdot^2(20)=%s; dV(10)=%s dV(20)=%s'%(mp.nstr(E,12),mp.nstr(L,12),mp.nstr(V(mp.mpf(10),E,L),3),mp.nstr(V(mp.mpf(20),E,L),3),mp.nstr(dV(mp.mpf(10),E,L),6),mp.nstr(dV(mp.mpf(20),E,L),6)))
    for c in ('0.1','0.01','0.001'):
        c=mp.mpf(c)
        for rs,name in ((10,'periastron'),(20,'apastron')):
            for sg,d in ((1,'outward'),(-1,'inward')):
                e=edge(mp.mpf(rs),sg,c,E,L)
                print(f"c={mp.nstr(c,3):5s} {name:10s} r={rs} {d:7s} eps={mp.nstr(e['eps'],8):10s} target r'={mp.nstr(e['rp'],10):14s} {e['kind']:12s} orbit [{mp.nstr(e['lo'],8)}, {mp.nstr(e['hi'],8)}]  (a): {'PASS' if e['ok'] else 'FAIL'}")
    # C6's X': inward c=0.01 target of the r=10 periastron, then its own outward edge
    x=edge(mp.mpf(10),-1,mp.mpf('0.01'),E,L)
    xo=edge(x['rp'],1,mp.mpf('0.01'),x['E'],x['L']); xi=edge(x['rp'],-1,mp.mpf('0.01'),x['E'],x['L'])
    print("C6 X' r=%s: outward target %s %s -> %s; inward target %s %s -> %s"%(mp.nstr(x['rp'],8),mp.nstr(xo['rp'],8),xo['kind'],'PASS' if xo['ok'] else 'FAIL',mp.nstr(xi['rp'],8),xi['kind'],'PASS' if xi['ok'] else 'FAIL'))
    # inward chain at c=0.01 from the periastron (§4.2: admissible 12 steps, fails at step 13, target 8.7383)
    r,E2,L2=mp.mpf(10),E,L
    for k in range(1,15):
        e=edge(r,-1,mp.mpf('0.01'),E2,L2)
        if not e['ok'] or k>=12: print('  inward chain step %d: source %s -> target %s %s [%s, %s] %s'%(k,mp.nstr(r,8),mp.nstr(e['rp'],8),e['kind'],mp.nstr(e['lo'],6),mp.nstr(e['hi'],6),'PASS' if e['ok'] else 'FAIL'))
        if not e['ok']: break
        r,E2,L2=e['rp'],e['E'],e['L']
