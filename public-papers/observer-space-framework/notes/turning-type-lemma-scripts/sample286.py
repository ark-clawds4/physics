# Pinned random sample for the turning-type lemma. seed=286, N per scheme as below, mpmath dps=30.
# Scheme S1 (bound sources): c log-uniform [0.001,0.2]; r_p = 4+e^U (U unif [ln 1e-3, ln 60]) ; eccentricity: with prob 1/2 e log-uniform [1e-6,1], else 1-e log-uniform [1e-8,1],
#   rejected unless stable bound (p>6+2e); r_a = r_p(1+e)/(1-e) (reaches ~1e6+). Both turning points, both edges, both throat conventions.
# Scheme S2 (any turning point): r0 = 2+e^U (U unif [ln 1e-4, ln 1e5]), v unif (0,1) (circular rejected), same c law.
import os, sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import random, collections, tt, mpmath as mp
mp.mp.dps=30
SEED=286; N1=int(sys.argv[1]) if len(sys.argv)>1 else 4000; N2=int(sys.argv[2]) if len(sys.argv)>2 else 4000
rnd=random.Random(SEED); C=collections.Counter()
def ru(a,b): return mp.mpf(rnd.uniform(a,b))
def c_draw(): return mp.e**ru(mp.log(0.001),mp.log(0.2))
def check(scheme,r0,v,c):
    E,L=tt.EL_from_rv(r0,v); kind,lo,hi=tt.classify(r0,E,L)
    if kind=='circular': C[scheme,'circular source skipped']+=1; return
    turn=kind[:4]; into=+1 if turn=='peri' else -1
    for conv in ('stop','through'):
        npass=0
        for sg in (+1,-1):
            e=tt.edge(r0,sg,c,v,conv)
            if e is None: C[scheme,conv,'undefined (throat, stop)']+=1; continue
            side = 'interior' if (e['rp']-r0)*into>0 else ('equal' if e['rp']==r0 else 'exterior')
            if e['ok']: npass+=1
            if sg==into:
                tag='into-range'+(' via throat' if e['through'] else '')
                C[scheme,conv,tag,'lands '+side,'type kept' if e['kind'][:4]==turn else 'type changed:'+e['kind'],'PASS' if e['ok'] else 'FAIL']+=1
                if side=='interior':
                    C[scheme,conv,'interior landing margin sign ok']+= int((e['margin']>0)==(turn=='peri'))
            else:
                C[scheme,conv,'away'+(' via throat' if e['through'] else ''),'PASS' if e['ok'] else 'FAIL']+=1
        C[scheme,conv,f'm={npass}']+=1
    C[scheme,'turning points']+=1
n=0
while n<N1:
    rp=4+mp.e**ru(mp.log(1e-3),mp.log(60)); e=mp.e**ru(mp.log(1e-6),0) if rnd.random()<0.5 else 1-mp.e**ru(mp.log(1e-8),0); p=rp*(1+e)
    if p<=6+2*e: C['S1','rejected (not stable bound)']+=1; continue
    ra=p/(1-e); E,L=tt.EL_orbit(rp,ra); c=c_draw(); n+=1
    C['S1','orbits']+=1; C['S1','orbits with r_a>2786 (c=0.1 threshold scale)']+=int(ra>2786); C['S1','orbits in the through-throat-beyond regime (eps(r_a)>2 ell(r_a))']+=int(tt.eps(ra,c)>2*tt.ell(ra))
    for r0 in (rp,ra): check('S1',r0,tt.v_from_EL(r0,E,L),c)
for _ in range(N2):
    r0=2+mp.e**ru(mp.log(1e-4),mp.log(1e5)); v=ru(0,1); check('S2',r0,v,c_draw())
for k,v in sorted(C.items(),key=str): print(k,v)
