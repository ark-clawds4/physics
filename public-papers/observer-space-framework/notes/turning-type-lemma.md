# The turning-type lemma (#203)

*Standalone note. It does not edit v0.9.1, and whether it enters v0.10 stays open under F11. Terms are those of v0.9.1 on main at `4d1fb11`: vertex, the Kretschmann rule and the throat convention (§7), (a) in lock-side form (§8.2), and C30, C31, C33, C37, C38. Terms used before §1 (turning type, interior side, $\varepsilon$, $\Delta\ell$, $m$, *stop*, *through*) are defined there. Scripts and pins are in §5.*

**Verdict: the lemma holds as #203 states it, with the throat proviso, and extends up to $\varepsilon\le2\Delta\ell$. Only the unqualified form is refuted.**

The lemma holds at every periastron, for every $c>0$ and under either throat convention. At an apastron it holds when the inward path stays short of the bifurcation sphere. Past the sphere the inward edge is undefined under the named alternative ("stop"); under the proposed default ("continue through") it still fails (a) up to $\varepsilon\le2\Delta\ell(r_0)$ ($\varepsilon=\Delta\ell$ excluded).

Under the proposed default ("continue through") its unqualified form is **refuted** at apastra with $\varepsilon(r_0)>2\Delta\ell(r_0)$. #203's derivation bullet carries the proviso "provided the jump does not reach the throat" (`reviews/v0.8-prose-claude-pressure-test.md`), and in that form the lemma holds without exception. The refuted form is the unqualified one in #203's "precise correct claim" and in item 1 of the v0.10 plan (#285). There the inward target lands beyond $r_0$, it can pass (a), and $m=2$. For bound sources this case means $r_a>2786.4692$ ($c=0.1$) or $r_a>277{,}152.58$ ($c=0.01$).

The mechanism, that the target keeps its turning type, is correct whenever the target lands on the interior side. In the counterexample the type is still kept; what flips is the side the target lands on.

## 1. Terms

Schwarzschild $M=1$. We use $f=1-2/r$, $V(r)=f\,(1+L^2/r^2)$ and $\dot r^2=E^2-V$. We write $\Delta\ell(r)=\ell(r)-\ell(2)=\sqrt{r(r-2)}+2\ln\big((\sqrt r+\sqrt{r-2})/\sqrt2\big)$ for proper radial distance from the bifurcation sphere on $t=$ const.

- **Turning point.** A point of a timelike geodesic with $u^r=0$ and $r_0>2$. Its static-frame tangential speed is $v\in[0,1)$, with $E=\sqrt f\,\gamma$, $L=r\gamma v$ and $\gamma=(1-v^2)^{-1/2}$.
  - On a non-circular geodesic it is a vertex (C38: $dK/d\tau\propto u^r$, and the zero is isolated).
  - **Circular orbits are excluded.** This includes ISCO $r=6$ and the unstable orbits $3<r<6$. Their $K$ is constant, so they have no vertex, and turning type is not defined for them.
  - An asymptotic (homoclinic) approach to an unstable circular orbit is not a turning point.
- **Turning type** (defined here). A turning point is a *periastron* if $V'(r_0)<0$ and an *apastron* if $V'(r_0)>0$.
  - With $L=r\gamma v$, $V'(r)=2\gamma^2\big(1-v^2(r-2)\big)/r^2$ (identity (I)).
  - So the turning point is a periastron iff $v^2>1/(r_0-2)$ and an apastron iff $v^2<1/(r_0-2)$.
  - Every turning point with $r_0\le3$ is an apastron.
- **Interior side.** $r>r_0$ at a periastron and $r<r_0$ at an apastron: the side on which the orbit's own radial range lies.
- **The jump** (§7). $\varepsilon(r_0)=c|K|^{-1/4}=c\,r_0^{3/2}/48^{1/4}$.
  - At $u^r=0$, $\hat n=\pm e_{\hat r}$, and the path is the radial line at constant $t,\theta,\varphi$.
  - The **into-range edge** is the outward edge at a periastron and the inward edge at an apastron. This is #203's "edge into the orbit's radial range (outward at a periastron, inward at an apastron)", which #203 defines by direction. Reading "into the range" as where the target lands differs from it only in the throat exception below. The other edge is the **away** edge.
- **Throat** (C37, with the near-throat window of #238).
  - The inward path meets the bifurcation sphere iff $\varepsilon(r_0)\ge\Delta\ell(r_0)$. For $c=0.1$ that means $r_0>705.155$ or $2<r_0<2.00145$; for $c=0.01$, $r_0>69{,}303.7$ or $2<r_0<2.0000144$.
  - The two windows merge, so that every inward path meets the sphere, for $c\ge c^*=\max_r 48^{1/4}\Delta\ell(r)/r^{3/2}=1.55721$, attained at $r=3.2698$.
  - *Through*: $\Delta\ell(r')=\varepsilon-\Delta\ell(r_0)$, with the same static speed. *Stop*: the target is undefined.
  - At equality the path ends on the sphere, where the static frame degenerates. The target is then undefined under both conventions, and the case is excluded.
- **(a)**: $O'^{u'}\in F(O)\setminus\{\gamma_{O^u}(\tau):\tau\ge0\}$.
- **$m$**: the number of (a)-admissible edges of the rule at the vertex, so that $|B_R|=1+m$ under (a).
- **Bound source.** $E<1$ and both turning points exist. Then $p>6+2e$, where $p$ is the semi-latus rectum and $e$ the eccentricity ($r_{p,a}=p/(1\pm e)$), so $r_p>4$ and $r_a>6$ (Cutler, Kennefick & Poisson, Phys. Rev. D 50, 3816 (1994)), and no bound turning point lies in a near-throat window. The theorem itself needs no boundedness, so plunging and unbound sources are covered too.

## 2. Statement

**Theorem.** Let $O^u$ be a turning point at $r_0>2$ of a non-circular timelike geodesic with speed $v$. Let $O'^{u'}$ be the target of either edge, where defined, at radius $r'$. Let $c>0$.

- **(T1) Speed kept.** $O'^{u'}$ is the turning point at $r'$ with the same $v$: $E'=\sqrt{f(r')}\,\gamma$ and $L'=r'\gamma v$.
- **(T2) Type kept on the interior side.** Suppose $r'$ lies strictly on the interior side of $r_0$. Then $O'$ has the source's turning type and is never circular. Its whole radial range lies strictly on that side, so the edge fails (a). If $r'=r_0$, the target is $O^u$ itself, and the edge fails (a).
- **(T3) Landing.** The outward edge at a periastron lands on the interior side.
  - At an apastron the inward edge does so if $\varepsilon<\Delta\ell(r_0)$.
  - If $\varepsilon>\Delta\ell(r_0)$, the edge is undefined under *stop*.
  - Under *through* it lands at $r'<r_0$, $r'=r_0$ or $r'>r_0$ according as $\varepsilon<$, $=$ or $>\,2\Delta\ell(r_0)$.

**Corollary (the #203 lemma: the proviso form, extended).** The into-range edge fails (a) at every periastron. At every apastron it fails (a) or is undefined (under *stop* when the path meets the sphere, and at $\varepsilon=\Delta\ell$), except under *through* with $\varepsilon(r_0)>2\Delta\ell(r_0)$. So $m\le1$ at every vertex outside that exception.

**Counterexample (to the unqualified form; the exception is real).**

- **$c=0.1$.** Take the bound orbit with apastron $r_0=3000$ and $v=0.0015$, so that its periastron is $7.410741$, $E=0.9996677357$ and $L=4.5000051$.
  - The inward edge goes through the throat to $r'=3227.216103$, an apastron with range $[9.1941635,\,3227.2161]\ni3000$. It **passes**.
  - The outward edge goes to $r'=9241.561739$, with range $[95.027248,\,9241.5617]$. It passes.
  - So $m=2$.
- **$c=0.01$.** With $r_0=300{,}000$ and $v=1.5\times10^{-5}$, the inward target is at $r'=324{,}244.03$ with range $[9.2783607,\dots]$. It passes, and so does the outward edge.
- **Threshold.** The bound in $\varepsilon=2\Delta\ell$ is $r_0>2786.4692$ ($c=0.1$) or $r_0>277{,}152.58$ ($c=0.01$). It grows like $4\sqrt{48}/c^2$ as $c\to0$, so the exception exists at every $c>0$. Near the throat it also covers $2<r_0<2.000361$ ($c=0.1$) and $2<r_0<2.0000036$ ($c=0.01$), where no bound turning point lies.
- **Not every beyond-landing passes.** In S2 (§4), 6 of 352 beyond-landings fail, 3 of them with a change of type. A through-throat path can also land inside: at $r_0=1000$, $v=0.0045$, $c=0.1$, $\Delta\ell<\varepsilon<2\Delta\ell$, so the target lands inside at $189.87$ (the apastron of a plunging orbit) and fails. Sampled cases with $\varepsilon>2\Delta\ell$ almost always pass (§4).

## 3. Proof sketch (details in Appendix A)

**(T1).** $\nabla K$ is radial and orthogonal to $u$ when $u^r=0$. The radial line is a geodesic, and the static frame $f^{-1/2}\partial_t,\ r^{-1}\partial_\varphi$ is parallel along it (sympy). So $(\gamma,v)$ and $u'^r=0$ are kept. Through the throat, the same holds by the convention.

**(T2), periastron.**

1. For $r'>r_0$, $v^2>1/(r_0-2)>1/(r'-2)$, so $V'_{L'}(r')<0$ by (I) and the target is a periastron.
2. $r'$ is the left endpoint of its component of $\{V\le E'^2\}$, because $V'(r')\ne0$. So the target orbit keeps $r\ge r'>r_0$ in both time directions.
3. Since $E'/E=\sqrt{f(r')/f(r_0)}\neq1$, $O'$ is not on $\gamma_{O^u}$. So (a) holds iff the target's past curvelet meets the lump $O$, that is, the radius $r_0$ (lumps at $r>2$ are labelled by $r$, since $K=48/r^6$).
4. In any connected real-analytic world the continuation along the geodesic is locally Schwarzschild $M=1$, with $E',L'$ conserved. So $r(\tau)$ obeys $\dot r^2=E'^2-V$ and never reaches $r_0$. If the world ends sooner, the range only shrinks.

**(T2), apastron.** Symmetric, with $r\le r'<r_0$. The component may continue to $r<2$ (a past plunge into the white-hole region), which is still below $r_0$.

**(T2), $r'=r_0$.** Equal $(r,\,u^r=0,\,v)$ gives the same oriented germ, which is $\gamma_{O^u}(0)$ and is excluded.

**(T3).** $\Delta\ell$ is increasing.

**Edge cases.**

- A circular target needs $v^2=1/(r'-2)$, which is impossible on the interior side.
- Plunging and unbound targets are covered.
- If $r_0\le3$, the turning point is an apastron, which is covered.
- For large $c$ only the throat condition matters.
- Near ISCO and near the separatrix, the source margin $|v^2-1/(r_0-2)|$ can be tiny. The target margin exceeds it by $|1/(r_0-2)-1/(r'-2)|>0$.
- The away edge is unconstrained. Its type can change (C33 census: 12,055 apastron-outward targets are periastra), and it can pass or fail.

## 4. Numerics (classifier: deflated cubic plus the analytic sign of $V'$)

**Census** (C33's (a)-restricted reach from $[10,20]$; `census.py` (with `r1.py`, both from the box's `g201`) for $c=0.1,0.01$; its double-precision port `censusf286.py` for $c=0.001$, which reproduces the $c=0.1$ and $c=0.01$ rows exactly and re-decides near-tie edges in mpmath, of which there were none):

| $c$ | orbits | into-range edges | pass | type kept | $m\le1$ | stuck | throat |
|---|---|---|---|---|---|---|---|
| 0.1 | 3 | 6 | 0 | 6/6 | all | 2 | 0 |
| 0.01 | 29,119 | 58,238 | 0 | all | all 58,238 | 14,478 | 0 |
| 0.001 (capped) | 4,140,195 expanded | 8,280,390 | 0 | all | all ($m=1$) | 0 | 0 |

At $c=0.001$ the census is **not exhaustive**. The reachable set roughly doubles at each BFS depth (8,254,910 orbits found by depth 22, none stuck), and depth 23 exceeded memory. The row covers every orbit to depth 21, and the maximum apastron found is $20.7284$.

**Pinned sample** (`sample286.py 20000 20000`, seed 286, $N=20{,}000$ per scheme; the script's default is 4,000). The constant $c$ is log-uniform on $[0.001,0.2]$. Each turning point gets both edges under both conventions.

- **S1: bound orbits**, 40,000 turning points.
  - *Stop.* 30,553 interior landings, all type-kept with the correct margin sign, all fail. 9,447 targets are undefined. $m\le1$ throughout.
  - *Through.* 31,756 interior landings (1,203 of them via the throat), all type-kept, all fail. 8,244 land beyond $r_0$, and all 8,244 pass. These are exactly the orbits with $\varepsilon(r_a)>2\Delta\ell(r_a)$, and $m=2$ at exactly those 8,244 turning points.
- **S2: arbitrary turning points**, 20,000, with $r_0\in(2+10^{-4},\,2+10^5)$ and $v$ uniform.
  - Interior landings: 19,180 under *stop* and 19,648 under *through*. All fail, all with the type kept.
  - Beyond landings: 352. Of these, 346 pass and 6 fail (3 of the 6 change type). $m=2$ at 345.

**High precision** (`boundary286.py`, mpmath dps 60): 41 orbits, namely near-circular ($r_{p,a}=r_c(1\mp\delta)$, $\delta$ down to $10^{-40}$), near-separatrix $p-(6+2e)$ down to $10^{-40}$ for $e$ from $10^{-6}$ to $0.9$, near-ISCO, and near-marginal. Each was run at $c\in\{0.001,0.01,0.1,0.2\}$.

- 0 violations.
- The smallest gap between $r_0$ and the target's range is $0.00215$ (near-marginal, $c=0.001$).
- Near-separatrix gaps do not change with $p-(6+2e)$.
- 2 near-marginal apastra ($r_a\sim8\times10^6$) reach the throat and are undefined under *stop*.

## 5. $m\le1$ and C33

What the corollary makes a theorem:

- $m\le1$ at every periastron.
- $m\le1$ at every apastron with $\varepsilon\le2\Delta\ell$.
- $m\le1$ at every vertex under *stop*.

C33's "$m\le1$ at every turning point" at $c=0.01$ therefore follows from the theorem together with one computed C33 fact, maximum apastron $25.37$. That value lies below $69{,}303.7$, the $c=0.01$ throat bound (C37), so no reachable path reaches the throat and the result holds under either convention. At $c=0.1$ the maximum apastron is $23.24<705.155$.

What it does not give: the counts (29,119 orbits, 14,478 stuck), the chain bound 14, acyclicity, transience, countability, or the exact jump-count law. $m\le1$ caps the arms at 2 per decision, but a decision recurs at every radial period. Countability needs every history to make finitely many jumps, and that remains a computed C33 result.

In the model without (a), the theorem says only which edge fails (a). It sets no law.

**Pins** (sha256 of the committed files, first 12 hex digits; the scripts, their invocations and expected outputs are in [`turning-type-lemma-scripts/`](turning-type-lemma-scripts/) next to this note):

| file (in `turning-type-lemma-scripts/`) | sha256 |
|---|---|
| `tt.py` | `6c23692a996f` |
| `proof286.py` | `e9642208c993` |
| `throat286.py` | `171031300b0c` |
| `boundary286.py` | `42130bed3df5` |
| `sample286.py` | `087958fcac9d` |
| `census286.py` | `ce3010b2b2b1` |
| `censusf286.py` | `611781f6eda5` |
| `census.py` | `97659775a495` |
| `r1.py` | `edd8c89b2216` |
| `c33r.py` | `de23f0b87f47` |
| `c33x.py` | `517945e54b19` |
| `kr.py` | `0432cc20f56a` |

The RNG is Python's `random.Random(286)`. The task brief (not in this repository) names `g183/c33r.py`, which does not exist; the robust classifier was `g168/c33r.py` on the shared box, and the committed copy `turning-type-lemma-scripts/c33r.py` (with `c33x.py` and `kr.py`) supersedes that pointer. Its method (a deflated cubic plus the analytic sign of $V'$) is the one used here.

## Appendix A. Proof details

**A1. Identity (I).** $V'(r)=2(r^2-L^2(r-3))/r^4$. Substituting $L=r\gamma v$ and $1+\gamma^2v^2=\gamma^2$ gives $V'=2\gamma^2(1-v^2(r-2))/r^2$. At a turning point $E^2=V(r_0)=f\gamma^2$, consistent with $E=\sqrt f\gamma$ (all sympy-verified, `proof286.py`).

**A2. Transport.** In equatorial Schwarzschild coordinates, $\Gamma^a_{rr}$ is nonzero only for $a=r$, so $t,\theta,\varphi=$ const is a geodesic. Also $\nabla_r(f^{-1/2}\partial_t)=0$ and $\nabla_r(r^{-1}\partial_\varphi)=0$ (sympy). So the static-frame components of $u$ are constant along the path, and at $r'$ we have $u'=\gamma(e_{\hat t}+v\,e_{\hat\varphi})$.

**A3. Type.** Write $g(r)=1-v^2(r-2)$, which is strictly decreasing in $r$ for $v>0$ and positive for $v=0$.

- Periastron: $g(r_0)<0$ and $r'>r_0$ give $g(r')<0$.
- Apastron: $g(r_0)>0$ and $r'<r_0$ give $g(r')>0$.
- In both cases $g(r')\ne0$, so the target is not circular.

**A4. Range.** $\dot r^2=E'^2-V$ vanishes at $r'$, and $V'(r')\neq0$. So $\{r:\ V(r)\le E'^2\}$ near $r'$ is a one-sided interval ending at $r'$. A timelike geodesic's $r(\tau)$ is $C^1$, and $\ddot r=-V'/2$ is nonzero at $r'$, so the orbit stays in the connected component on that side. The component lies in $[r',\infty)$ (periastron) or in $(0,r']$ (apastron; across $r=2$ the past motion is in the white-hole region, where $r$ keeps decreasing). It does not contain $r_0$.

**A5. World independence.** (a) is lock-side, so it is tested on the target's own curvelet, which is the same in every world (Prop. 3.2 of `papers/geodesic-lifts.md`). Along the curve, the analytic continuation of the germ carries the local Killing fields $\partial_t,\partial_\varphi$. The quantities $E',L'$ are therefore constants of the continued motion, and the radial equation is unchanged. A world in which the geodesic ends earlier realises a subset of the range.

**A6. Equal radius.** $r'=r_0$ and the same $v$ give the same oriented germ: the germ is determined by $(r,u^r,v)$ up to isometry. Through the throat the static Killing field changes time orientation, but the germ modulo pointed diffeomorphism does not. This germ is $\gamma_{O^u}(0)$, which (a) excludes.
