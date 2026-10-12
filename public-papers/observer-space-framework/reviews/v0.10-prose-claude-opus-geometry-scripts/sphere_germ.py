#!/usr/bin/env python3
"""Pins for reviews/v0.10-prose-claude-opus-geometry.md (R1, S4).

Schwarzschild M=1 in Kruskal coordinates, equatorial plane:
  g = F(-dT^2 + dX^2) + r^2 dphi^2,  F = 32 e^{-r/2}/r,
  z = X^2 - T^2 = (r/2 - 1) e^{r/2},  r = 2(1 + W(z/e)).
Static Killing field xi = (X d_T + T d_X)/4; E = -g(xi,u), L = r^2 phidot.

(1) Thresholds: roots of eps(r0) = Dl(r0) at c = 0.1 (the eps = Delta-ell corner).
(2) R1: parallel transport of u = gamma(n + v e_phi) along T = 0 from X0 (r0)
    to -X0 (length 2 Dl(r0)), through X = 0, RK4. Reports sqrt(F) u^T, u^X,
    r u^phi at the far end and the max deviation along the way.
(3) S4: the target at eps = Dl(r0) is the germ at T = X = 0 (the bifurcation
    sphere) with u = gamma(n + v e_phi), v kept. Integrate its geodesic to the
    past (RK4, tau from 0 down) until r < 0.5 and report: max z and max r over
    tau < 0, max (T + |X|), norm and E drift, r(tau) vs 2 - gamma^2 tau^2/8
    near tau = 0, and min K = 48/r^6 on the past curvelet against K(r0).
"""
import mpmath as mp
mp.mp.dps = 30
E1 = mp.e

def r_of_z(z):
    return 2*(1 + mp.lambertw(z/E1).real)
def F_of_r(r):
    return 32*mp.exp(-r/2)/r
def Dl(r):
    return mp.sqrt(r*(r-2)) + 2*mp.log((mp.sqrt(r)+mp.sqrt(r-2))/mp.sqrt(2))
def eps(r, c):
    return c*r**mp.mpf(1.5)/mp.mpf(48)**mp.mpf(0.25)

def geom(T, X):
    z = X*X - T*T
    r = r_of_z(z)
    F = F_of_r(r)
    rz = 4*mp.exp(-r/2)/r
    rT, rX = -2*T*rz, 2*X*rz
    Fr = -F*(mp.mpf(1)/2 + 1/r)
    return r, F, rT, rX, Fr*rT, Fr*rX

def accel(T, X, p, Td, Xd, pd):
    r, F, rT, rX, FT, FX = geom(T, X)
    aT = -(FT/(2*F)*Td*Td + 2*FX/(2*F)*Td*Xd + FT/(2*F)*Xd*Xd + r*rT/F*pd*pd)
    aX = -(FX/(2*F)*Td*Td + 2*FT/(2*F)*Td*Xd + FX/(2*F)*Xd*Xd - r*rX/F*pd*pd)
    ap = -2*(rT/r*Td*pd + rX/r*Xd*pd)
    return aT, aX, ap

def rk4(f, y, h):
    k1 = f(y)
    k2 = f([a + h/2*b for a, b in zip(y, k1)])
    k3 = f([a + h/2*b for a, b in zip(y, k2)])
    k4 = f([a + h*b for a, b in zip(y, k3)])
    return [a + h/6*(b + 2*c + 2*d + e) for a, b, c, d, e in zip(y, k1, k2, k3, k4)]

def geo_rhs(y):
    T, X, p, Td, Xd, pd = y
    aT, aX, ap = accel(T, X, p, Td, Xd, pd)
    return [Td, Xd, pd, aT, aX, ap]

def X_of_r(r):
    return mp.sqrt((r/2 - 1)*mp.exp(r/2))

# (1) thresholds
c = mp.mpf('0.1')
f = lambda r: eps(r, c) - Dl(r)
hi = mp.findroot(f, 705)
lo = mp.findroot(f, (mp.mpf('2.0001'), mp.mpf('2.01')), solver='anderson')
print("(1) c=0.1: eps=Dl at r0 = %s and r0 = %s" % (mp.nstr(hi, 10), mp.nstr(lo, 10)))

# (2) R1 transport along T=0 through X=0
def transport(r0, v, N):
    g = 1/mp.sqrt(1 - v*v)
    X0 = X_of_r(r0)
    r, F, *_ = geom(mp.mpf(0), X0)
    # state: X, U^T, U^X, U^phi ; d/ds with k = (0, -F^{-1/2}, 0) (inward)
    def rhs(y):
        X, UT, UX, Up = y
        r, F, rT, rX, FT, FX = geom(mp.mpf(0), X)
        kX = -1/mp.sqrt(F)
        dUT = -(FX/(2*F))*UT*kX            # Gamma^T_TX U^T k^X (+Gamma^T_XX U^X k^X, F_T=0)
        dUX = -(FX/(2*F))*UX*kX            # Gamma^X_XX U^X k^X (Gamma^X_TX=F_T/2F=0)
        dUp = -(rX/r)*Up*kX
        return [kX, dUT, dUX, dUp]
    y = [X0, g/mp.sqrt(F), mp.mpf(0), g*v/r]
    L = 2*Dl(r0); h = L/N; dev = mp.mpf(0)
    for i in range(N):
        y = rk4(rhs, y, h)
        r, F, *_ = geom(mp.mpf(0), y[0])
        dev = max(dev, abs(mp.sqrt(F)*y[1] - g), abs(y[2]), abs(r*y[3] - g*v))
    r, F, *_ = geom(mp.mpf(0), y[0])
    return y[0], X0, mp.sqrt(F)*y[1], y[2], r*y[3], g, g*v, dev

for r0, v, N in [(mp.mpf(10), mp.mpf('0.3'), 400), (mp.mpf('2.0014462'), mp.mpf('0.9'), 400)]:
    Xe, X0, a, b, cc, g, gv, dev = transport(r0, v, N)
    print("(2) r0=%s v=%s: X0=%s -> X_end=%s; sqrtF u^T=%s (gamma=%s), u^X=%s, r u^phi=%s (gamma v=%s); max dev %s" % (
        mp.nstr(r0, 8), v, mp.nstr(X0, 8), mp.nstr(Xe, 8), mp.nstr(a, 12), mp.nstr(g, 12),
        mp.nstr(b, 3), mp.nstr(cc, 12), mp.nstr(gv, 12), mp.nstr(dev, 3)))

# (3) S4 sphere germ, past geodesic
r0 = hi
K0 = 48/r0**6
for v in ['0', '0.01', '0.0377', '0.3849', '0.9']:
    v = mp.mpf(v); g = 1/mp.sqrt(1 - v*v)
    T, X = mp.mpf(0), mp.mpf(0)
    r, F, *_ = geom(T, X)
    y = [T, X, mp.mpf(0), g/mp.sqrt(F), mp.mpf(0), g*v/r]
    L0 = r*r*y[5]
    h = mp.mpf('-0.001'); tau = mp.mpf(0)
    zmax = rmax = TXmax = None; nd = Ed = Ld = mp.mpf(0); quad = mp.mpf(0); Kmin = None; n = 0
    while True:
        y = rk4(geo_rhs, y, h); tau += h; n += 1
        T, X, p, Td, Xd, pd = y
        r, F, *_ = geom(T, X)
        z = X*X - T*T
        zmax = z if zmax is None else max(zmax, z)
        rmax = r if rmax is None else max(rmax, r)
        tx = T + abs(X); TXmax = tx if TXmax is None else max(TXmax, tx)
        nd = max(nd, abs(F*(-Td*Td + Xd*Xd) + r*r*pd*pd + 1))
        Ed = max(Ed, abs(F*(X*Td - T*Xd)/4))
        Ld = max(Ld, abs(r*r*pd - L0))
        K = 48/r**6; Kmin = K if Kmin is None else min(Kmin, K)
        if n <= 50:
            quad = max(quad, abs((2 - r) - g*g*tau*tau/8)/(tau*tau))
        if r < mp.mpf('0.5'):
            break
    print("(3) v=%s L=%s: past to tau=%s (r=%s): max z=%s, max r=%s, max(T+|X|)=%s; |norm+1|<=%s, |E|<=%s, |dL|<=%s; |(2-r)/tau^2 - gamma^2/8| <= %s for |tau|<=0.05; min K=%s > K(r0)=%s: %s" % (
        v, mp.nstr(L0, 8), mp.nstr(tau, 5), mp.nstr(r, 5), mp.nstr(zmax, 5), mp.nstr(rmax, 12),
        mp.nstr(TXmax, 5), mp.nstr(nd, 3), mp.nstr(Ed, 3), mp.nstr(Ld, 3), mp.nstr(quad, 3),
        mp.nstr(Kmin, 8), mp.nstr(K0, 5), Kmin > K0 and zmax < 0 and rmax < 2))
print("(3) K = 48/r^6 at r=2 is 0.75; K(r0) at the two eps=Dl roots: %s, %s (both < 0.75)" % (mp.nstr(48/hi**6, 5), mp.nstr(48/lo**6, 8)))
