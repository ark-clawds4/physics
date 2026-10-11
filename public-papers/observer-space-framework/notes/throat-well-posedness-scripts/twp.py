# Is the far-side target of a through-throat Kretschmann jump a well-defined germ? Schwarzschild M=1, Kruskal (T,X).
# Deterministic (no seed). Needs mpmath and sympy.
import mpmath as mp, sympy as sp
mp.mp.dps = 40
# (1) Metric g = F(r)(-dT^2+dX^2) + r^2 dOmega^2, F = (32/r) e^{-r/2}, (r/2-1) e^{r/2} = X^2-T^2 =: z, so r = 2(1+W(z/e)).
#     r(z) is analytic at z=0 (the bifurcation sphere); its only singularity is the branch point z=-1, i.e. r=0.
z = sp.symbols('z')
rz = 2*(1 + sp.LambertW(z/sp.E))
ser = sp.series(rz, z, 0, 6).removeO()
print('(1) r(z) Taylor at z=0:', sp.nsimplify(sp.expand(ser)))
print('    singular point of r(z): z =', sp.solve(sp.Eq(z/sp.E, -1/sp.E), z), '-> r =', 2*(1 + sp.LambertW(-1/sp.E)))
print('    at the bifurcation sphere: F(2) =', sp.nsimplify(32/2*sp.exp(-1)), '; K(2) = 48/2^6 =', sp.Rational(48, 64))
# (2) T=0 is totally geodesic, and the unit normal n = F^{-1/2} d_T and e_phi = r^{-1} d_phi are parallel along the radial line T=0.
T, X, th, ph = sp.symbols('T X theta phi'); Fz = sp.Function('F'); Rz = sp.Function('R')
F = Fz(X**2 - T**2); R = Rz(X**2 - T**2); x = [T, X, th, ph]
g = sp.diag(-F, F, R**2, R**2*sp.sin(th)**2); gi = g.inv()
Gam = lambda a, b, c: sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in range(4))/2)
at0 = lambda e: sp.simplify(e.subs(T, 0))
print('(2) at T=0: Gamma^T_XX =', at0(Gam(0, 1, 1)), ', Gamma^theta_XX =', at0(Gam(2, 1, 1)), ', Gamma^phi_XX =', at0(Gam(3, 1, 1)), '(the radial line T=0 is a geodesic through X=0)')
n = [1/sp.sqrt(F), 0, 0, 0]; ephi = [0, 0, 0, 1/(R*sp.sin(th))]
cov = lambda V: [at0(sp.diff(V[a], X) + sum(Gam(a, 1, b)*V[b] for b in range(4))) for a in range(4)]
print('    D_X n at T=0:', cov(n), '; D_X e_phi at T=0:', cov(ephi))
# (3) Integrate proper length along T=0 from region I through X=0 into X<0 (region III), compare with the reflection formula.
def ell(r): r = mp.mpf(r); return mp.sqrt(r*(r-2)) + 2*mp.log((mp.sqrt(r) + mp.sqrt(r-2))/mp.sqrt(2))
def eps(r, c): return mp.mpf(c)*mp.mpf(r)**mp.mpf(1.5)/mp.mpf(48)**mp.mpf(0.25)
rofX = lambda Xv: 2*(1 + mp.lambertw(Xv**2/mp.e).real)
sqF = lambda Xv: mp.sqrt(32/rofX(Xv)*mp.exp(-rofX(Xv)/2))
for c, r0 in (('0.1', 3000), ('0.1', 1000)):           # #290's through-throat examples (r'=3227.216103 beyond; 189.87 inside)
    c = mp.mpf(c); e = eps(r0, c); s0 = mp.asinh(mp.sqrt((mp.mpf(r0)/2 - 1)*mp.exp(mp.mpf(r0)/2)))
    L = lambda s1: mp.quad(lambda s: sqF(mp.sinh(s))*mp.cosh(s), mp.linspace(s1, s0, 40))   # proper length from X=sinh(s1) to the source
    rp_formula = mp.findroot(lambda r: ell(r) - (e - ell(r0)), (mp.mpf(2) + mp.mpf('1e-20'), 10*mp.mpf(r0)), solver='anderson')
    s1 = -mp.asinh(mp.sqrt((rp_formula/2 - 1)*mp.exp(rp_formula/2)))                        # far-side point X<0 at radius r'
    print(f'(3) c={mp.nstr(c,3)} r0={r0}: eps={mp.nstr(e,12)}, Delta ell(r0)={mp.nstr(ell(r0),12)}, reflection formula r\'={mp.nstr(rp_formula,12)}; '
          f'Kruskal proper length from X={mp.nstr(mp.sinh(s1),4)} (<0, far exterior) through X=0 to the source = {mp.nstr(L(s1),12)}, |minus eps|={mp.nstr(abs(L(s1)-e),2)}')
