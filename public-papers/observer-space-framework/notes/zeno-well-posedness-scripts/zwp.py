# Zeno well-posedness: limits of C5-type jump chains (no arrival rule, model without (a)), Schwarzschild M=1, Kretschmann rule.
# Deterministic (no seed). Needs mpmath. ell, eps and the jump as in turning-type-lemma-scripts/tt.py (#290).
# Every target is a turning point (u^r=0) with the source's static-frame speed v (#290 T1), so a chain is fixed by its radii.
import mpmath as mp
mp.mp.dps = 30
def ell(r): r = mp.mpf(r); return mp.sqrt(r*(r-2)) + 2*mp.log((mp.sqrt(r) + mp.sqrt(r-2))/mp.sqrt(2))   # Delta ell(r)
def eps(r, c): return mp.mpf(c)*mp.mpf(r)**mp.mpf(1.5)/mp.mpf(48)**mp.mpf(0.25)
def rof(D):                                   # inverse of Delta ell on r>2 (D>0), solved in y=sqrt(r-2)
    f = lambda y: y*mp.sqrt(2 + y**2) + 2*mp.asinh(y/mp.sqrt(2)) - D
    y = mp.findroot(f, D/(2*mp.sqrt(2)) if D < 3 else mp.sqrt(D))
    return 2 + y**2
def step(D, s, c, throat):                    # one jump from Delta ell = D; s=+1 outward, -1 inward
    e = eps(rof(D), c); g = D + s*e
    if g > 0: return g
    return None if throat == 'stop' or g == 0 else -g          # through: land on the far side at Delta ell = -g
# instance periastron r=10 of [10,20]: static-frame speed v
a, b = mp.mpf(10), mp.mpf(20); p = 2*a*b/(a+b); e_ = (b-a)/(b+a); L = mp.sqrt(p**2/(p-3-e_**2)); v = (L/a)/mp.sqrt(1 + (L/a)**2)
print('v at the r=10 periastron of [10,20]:', mp.nstr(v, 10), '; circular speed v_c(r)=(r-2)^(-1/2) at r=10:', mp.nstr(1/mp.sqrt(8), 10), '(v>v_c, and v_c falls with r: no outward target is circular)')
rc = 2 + 1/v**2                               # the one radius where a target with speed v would be circular (v = v_c)
for c in ('0.1', '0.01'):
    D = ell(10); best = mp.inf
    while D is not None:
        best = min(best, abs(rof(D) - rc)); D = step(D, -1, c, 'stop')
    print(f'(0) c={c}: circular radius 2+1/v^2={mp.nstr(rc, 10)}; the inward chain from 10 (until it ends under stop) misses it by at least {mp.nstr(best, 6)}')
# (1) outward chains (C5): r_n -> infinity
for c in ('0.01', '0.1'):
    D = ell(10); rs = [mp.mpf(10)]; n = 0; marks = {}
    while rs[-1] < mp.mpf(10)**6:
        D = step(D, 1, c, 'stop'); rs.append(rof(D)); n += 1
        for m in (100, 1000, 10**4, 10**5):
            if m not in marks and rs[-1] > m: marks[m] = n
    print(f'(1) c={c} outward chain from 10: first radii', [mp.nstr(x, 8) for x in rs[1:4]], '; steps to exceed 1e2,1e3,1e4,1e5,1e6:', [marks[m] for m in (100, 1000, 10**4, 10**5)] + [n],
          '; K=48/r^6 at the last radius', mp.nstr(48/rs[-1]**6, 3), '; static-frame Riemann components 2/r^3 (times gamma^2<=', mp.nstr(1/(1-v**2), 6), '):', mp.nstr(2/rs[-1]**3, 3))
# (2) inward chains: under 'stop' they end at the throat window; under 'through' they settle on the near-throat self-target radius
for c in ('0.1', '0.01'):
    cm = mp.mpf(c)
    Ds = mp.findroot(lambda D: eps(rof(D), cm) - 2*D, eps(2, cm)/2); rs_ = rof(Ds)
    mult = mp.diff(lambda D: eps(rof(D), cm), Ds) - 1          # derivative of D -> eps - D at the fixed point
    Dst = ell(10); n = 0
    while True:
        nx = step(Dst, -1, c, 'stop')
        if nx is None: break
        Dst = nx; n += 1
    print(f'(2) c={c}: self-target Delta ell*={mp.nstr(Ds, 12)}, r*={mp.nstr(rs_, 12)}, multiplier {mp.nstr(mult, 8)} (|.|<1: attracting); under stop the inward chain from 10 ends after {n} jumps at r={mp.nstr(rof(Dst), 10)} (inward edge undefined)')
    D = ell(10); n = 0; hist = []
    while n < 20000:
        D = step(D, -1, c, 'through'); n += 1
        if n in (1000, 5000, 10000, 20000): hist.append((n, mp.nstr(rof(D), 12), mp.nstr(abs(D - Ds), 3)))
    print('    under through, the inward chain from 10 (n, r_n, |Delta ell_n - Delta ell*|):', hist)
# (3) the far self-target radius at c=0.1 is repelling
c = mp.mpf('0.1'); Df = mp.findroot(lambda D: eps(rof(D), c) - 2*D, ell(2786)); print('(3) c=0.1 far self-target r*=', mp.nstr(rof(Df), 10), 'multiplier', mp.nstr(mp.diff(lambda D: eps(rof(D), c), Df) - 1, 8), '(|.|>1: repelling)')
# (4) any chain with r_n -> r* in (2,inf): same-side jumps move Delta ell by eps(r_n) -> eps(r*) > 0, so late jumps all cross the throat, forcing 2 Delta ell(r*) = eps(r*).
#     r_n -> 2 is impossible: eps(2) > 0.
print('(4) eps(2) =', mp.nstr(eps(2, '0.1'), 10), '(c=0.1),', mp.nstr(eps(2, '0.01'), 10), '(c=0.01)')
