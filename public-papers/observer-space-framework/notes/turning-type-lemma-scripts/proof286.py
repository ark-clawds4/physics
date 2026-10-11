# Symbolic checks for the proof (sympy).
import sympy as sp
r,v,L,E=sp.symbols('r v L E',positive=True)
V=(1-2/r)*(1+L**2/r**2)
dV=sp.diff(V,r)
print('dV/dr == 2(r^2-L^2(r-3))/r^4 :', sp.simplify(dV-2*(r**2-L**2*(r-3))/r**4)==0)
g=1/sp.sqrt(1-v**2); Lv=r*g*v
expr=sp.simplify(dV.subs(L,Lv)-2*g**2*(1-v**2*(r-2))/r**2)
print('with L=r*gamma*v: dV/dr == 2 gamma^2 (1 - v^2 (r-2))/r^2 :', sp.simplify(expr)==0)
print('turning-point consistency E^2=V(r) with E=sqrt(f) gamma:', sp.simplify((1-2/r)*g**2-V.subs(L,Lv))==0)
# radial geodesic t=const is spacelike geodesic; static frame transported: E'/E = sqrt(f(r')/f(r)), L'/L = r'/r (same gamma, v)
# parallel transport along the radial spacelike geodesic (t, theta=pi/2, phi const): static frame e_t, e_phi are parallel
t,th,ph=sp.symbols('t theta phi'); X=[t,r,th,ph]; f=1-2/r
g=sp.diag(-f,1/f,r**2,r**2*sp.sin(th)**2); gi=g.inv()
Gam=[[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
def cov_r(Vec): return [sp.simplify((sp.diff(Vec[a],r)+sum(Gam[a][1][b]*Vec[b] for b in range(4))).subs(th,sp.pi/2)) for a in range(4)]
print('nabla_r e_t =',cov_r([1/sp.sqrt(f),0,0,0]),' nabla_r e_phi =',cov_r([0,0,0,1/r]))
print('radial line is a geodesic (Gamma^a_rr only a=r):',[sp.simplify(Gam[a][1][1]) for a in range(4)])
