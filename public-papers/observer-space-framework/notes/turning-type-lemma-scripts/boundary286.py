# High-precision (mpmath dps=60) checks of the into-range edge near circular, near ISCO, near the separatrix p=6+2e,
# and near marginally bound (e->1). gap = distance from the source radius to the target's radial range (>0 means (a) fails).
import os, sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import tt, mpmath as mp
mp.mp.dps=60
def run(label,rp,ra,cs=('0.001','0.01','0.1','0.2')):
    E,L=tt.EL_orbit(rp,ra); worst=None
    for c in cs:
        for r0,turn,sg in ((rp,'peri',1),(ra,'apo',-1)):
            v=tt.v_from_EL(r0,E,L); e=tt.edge(r0,sg,mp.mpf(c),v,'stop')
            if e is None: print('  ',label,c,turn,'throat (undefined)'); continue
            gap = e['lo']-r0 if turn=='peri' else r0-e['hi']
            kept = e['kind'].startswith(turn)
            if not (kept and not e['ok'] and gap>0): print('  VIOLATION',label,c,turn,e)
            rec=(gap,label,c,turn,e['kind'],abs(e['margin']))
            worst=rec if worst is None or rec[0]<worst[0] else worst
    return worst
rows=[]
for rc in (7,10,20,100):
    for d in ('1e-5','1e-10','1e-20','1e-40'):
        d=mp.mpf(d); rows.append(run(f'near-circular rc={rc} delta={mp.nstr(d,2)}',rc*(1-d),rc*(1+d)))
for e in ('1e-3','1e-6','0.1','0.5','0.9'):
    for eta in ('1e-5','1e-10','1e-20','1e-40'):
        e_=mp.mpf(e); p=6+2*e_+mp.mpf(eta)
        rows.append(run(f'near-separatrix e={e} p-(6+2e)={eta}',p/(1+e_),p/(1-e_)))
for d in ('1e-5','1e-10','1e-20'):   # near ISCO: e=d, p=6+2e+d
    d=mp.mpf(d); p=6+3*d; rows.append(run(f'near-ISCO e={mp.nstr(d,2)} p=6+3e',p/(1+d),p/(1-d)))
for om in ('1e-3','1e-6'):           # near marginally bound: e=1-om, p=4(1+e)+... (r_p near 4)
    e=1-mp.mpf(om); p=(6+2*e)*mp.mpf('1.0001'); rows.append(run(f'near-marginal e=1-{om}',p/(1+e),p/(1-e),cs=('0.001','0.01')))
print('cases:',len(rows),' violations: see above (none printed => 0)')
for r in sorted(rows,key=lambda x:x[0])[:6]: print(' smallest gaps:',mp.nstr(r[0],6),r[1],'c=',r[2],r[3],r[4],'|margin|=',mp.nstr(r[5],6))
