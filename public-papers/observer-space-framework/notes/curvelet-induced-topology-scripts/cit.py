# Curvelet-induced topology: are the states of C5's c=0.1 jump chains on pairwise distinct curvelets?
# Deterministic (no seed). Needs mpmath. ell, eps, rof and the jump as in zeno-well-posedness-scripts/zwp.py (#299), from #290's tt.py.
# Every target is a turning point (u^r=0) with the source's static-frame speed v (#290 T1). At a turning point the static-frame
# velocity is tangential, so the conserved angular momentum is L = r v / sqrt(1-v^2). L is constant along a curvelet, so states
# with distinct L lie on distinct curvelets (distinct components of the final topology). With v fixed, distinct r gives distinct L.
import mpmath as mp
mp.mp.dps = 40
def ell(r): r = mp.mpf(r); return mp.sqrt(r*(r-2)) + 2*mp.log((mp.sqrt(r) + mp.sqrt(r-2))/mp.sqrt(2))
def eps(r, c): return mp.mpf(c)*mp.mpf(r)**mp.mpf(1.5)/mp.mpf(48)**mp.mpf(0.25)
def rof(D):
    f = lambda y: y*mp.sqrt(2 + y**2) + 2*mp.asinh(y/mp.sqrt(2)) - D
    y = mp.findroot(f, D/(2*mp.sqrt(2)) if D < 3 else mp.sqrt(D))
    return 2 + y**2
def step(D, s, c, throat):
    e = eps(rof(D), c); g = D + s*e
    if g > 0: return g
    return None if throat == 'stop' or g == 0 else -g
a, b = mp.mpf(10), mp.mpf(20); p = 2*a*b/(a+b); e_ = (b-a)/(b+a); Lp = mp.sqrt(p**2/(p-3-e_**2)); v = (Lp/a)/mp.sqrt(1 + (Lp/a)**2)
gv = v/mp.sqrt(1 - v**2)
print('v =', mp.nstr(v, 10), '; check: L at r=10 from v equals the orbit L of [10,20]:', mp.nstr(10*gv, 12), mp.nstr(Lp, 12))
c = mp.mpf('0.1')
Ds = mp.findroot(lambda D: eps(rof(D), c) - 2*D, eps(2, c)/2); rs = rof(Ds); Ls = rs*gv
print('(1) c=0.1 near-throat self-target r* =', mp.nstr(rs, 12), ', L* =', mp.nstr(Ls, 12))
D = ell(10); Ls_list = [10*gv]
for n in range(20000):
    D = step(D, -1, '0.1', 'through'); Ls_list.append(rof(D)*gv)
srt = sorted(Ls_list)
gap = min(srt[i+1] - srt[i] for i in range(len(srt) - 1))
print('(2) inward through chain from 10, 20,000 jumps: 20,001 states; min gap between sorted L_n =', mp.nstr(gap, 4),
      '; min |L_n - L*| =', mp.nstr(min(abs(x - Ls) for x in Ls_list), 4), '; last r =', mp.nstr(Ls_list[-1]/gv, 12))
D = ell(10); rr = [mp.mpf(10)]
while rr[-1] < 10**6:
    D = step(D, 1, '0.1', 'stop'); rr.append(rof(D))
print('(3) outward chain from 10 (C5): radii strictly increasing over', len(rr) - 1, 'jumps:', all(rr[i+1] > rr[i] for i in range(len(rr) - 1)))
