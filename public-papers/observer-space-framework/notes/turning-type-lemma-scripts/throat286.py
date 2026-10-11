# Throat cases of the into-range (inward) edge at an apastron; continue-through convention vs the stop convention.
import os, sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import tt, mpmath as mp
mp.mp.dps=40
h=lambda r,c: tt.eps(r,c)-tt.ell(r)            # >0 iff the inward path from r reaches the bifurcation sphere
for c in ('0.1','0.01'):
    c=mp.mpf(c)
    lo=mp.findroot(lambda r:h(r,c),(mp.mpf(2)+mp.mpf('1e-12'),mp.mpf('2.1')),solver='anderson')
    hi=mp.findroot(lambda r:h(r,c),(mp.mpf(10),mp.mpf(10)**7),solver='anderson')
    t2=mp.findroot(lambda r:tt.eps(r,c)-2*tt.ell(r),(mp.mpf(10),mp.mpf(10)**9),solver='anderson')
    print(f'c={c}: inward path reaches the throat for 2<r<{mp.nstr(lo,8)} and r>{mp.nstr(hi,9)}; lands beyond the source radius (r\'>r) for r>{mp.nstr(t2,9)}')
# c*: smallest c for which the throat is reached at every r>2 (min over r of ell(r)/r^{3/2} * 48^{1/4})
q=lambda r: tt.ell(r)/mp.mpf(r)**mp.mpf(1.5)*mp.mpf(48)**mp.mpf(0.25)
rm=mp.findroot(lambda r: mp.diff(q,r),(mp.mpf(3),mp.mpf(30)),solver='anderson'); print('c* =',mp.nstr(q(rm),12),'at r =',mp.nstr(rm,10),'(for c>=c*, every inward path reaches the throat)')
# bound apastra: r_a>6 for every non-circular stable bound orbit; is the window 2<r<r_- relevant? (r_- vs 4)
# Counterexample search: c=0.1, apastron r0 > t2, v small enough that the source is a bound orbit with a periastron.
for c,r0,v in (('0.1',3000,'0.0015'),('0.1',5000,'0.0009'),('0.1',1000,'0.0045'),('0.01',300000,'0.000015')):
    c=mp.mpf(c); r0=mp.mpf(r0); v=mp.mpf(v); print('c =',c)
    E,L=tt.EL_from_rv(r0,v); kind,lo,hi=tt.classify(r0,E,L)
    ei=tt.edge(r0,-1,c,v,throat='through'); eo=tt.edge(r0,1,c,v,throat='through')
    print(f'source apastron r0={r0}, v={v}: {kind} [{mp.nstr(lo,8)}, {mp.nstr(hi,8)}], E={mp.nstr(E,10)}, L={mp.nstr(L,8)}')
    for nm,e in (('inward(through throat)' if ei and ei["through"] else 'inward',ei),('outward',eo)):
        print(f'   {nm}: r\'={mp.nstr(e["rp"],10)} {e["kind"]} [{mp.nstr(e["lo"],8)}, {mp.nstr(e["hi"],8)}] (a): {"PASS" if e["ok"] else "FAIL"}')
    print('   stop convention inward:', tt.edge(r0,-1,c,v,throat='stop'))
# near-throat subwindow where the through-throat inward target lands beyond r0 (eps > 2*Delta ell): 2<r<r2m
for c in ('0.1','0.01'):
    c=mp.mpf(c); r2m=mp.findroot(lambda r: tt.eps(r,c)-2*tt.ell(r),(mp.mpf(2)+mp.mpf('1e-15'),mp.mpf('2.1')),solver='anderson')
    print(f'c={c}: eps>2*Delta ell also for 2<r<{mp.nstr(r2m,8)} (only apastra exist there; no bound-orbit turning point)')
