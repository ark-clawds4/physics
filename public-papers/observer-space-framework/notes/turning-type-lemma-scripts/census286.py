# Exhaustive census of the (a)-restricted rule from [10,20] (C33-style), reusing g201/census.py (corrected classifier,
# deflated cubic + analytic sign of d(rdot^2)/dr). Counts into-range ("toward") edges that pass and turning points with m>=2.
import os, sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import time; c=sys.argv[1]; sys.argv=['x']
import census, r1, mpmath as mp
from collections import Counter
mp.mp.dps=30
t0=time.time()
n,tab,stuck,ex,d=census.reach(mp.mpf(c),True,cap=int(2e6))
toward=sum(v for k,v in tab.items() if k[2]=='toward'); toward_pass=sum(v for k,v in tab.items() if k[2]=='toward' and k[4]=='PASS')
away_pass=sum(v for k,v in tab.items() if k[2]=='away' and k[4]=='PASS')
# m per turning point: only away edges can pass (toward_pass==0 => m<=1)
print(f'c={c}: reachable orbits {n} (depth {d}); turning points {2*n}; into-range edges {toward}, passing {toward_pass}; '
      f'away edges passing {away_pass}; turning points with m>=2: {"0 (no into-range pass)" if toward_pass==0 else "CHECK"}; '
      f'stuck {dict(stuck)}; throat-skipped {dict(census.THROAT)}; {time.time()-t0:.0f}s')
for k,v in sorted(tab.items()): print('  ',k,v)
