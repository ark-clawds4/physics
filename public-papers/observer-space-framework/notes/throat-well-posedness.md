# Throat well-posedness: does the far-side target exist?

*Standalone note answering David's well-posedness question as relayed by the Physics Lead (not recorded in this repository; not signed). Written at main `8e99afd`; v0.9.1 unedited. Bare § and C pointers are to v0.9.1. Gauge, grain, F11, the Zeno readings and the throat convention stay open and unpicked; §2 gives a well-posedness finding only.*

**Verdict.** On v0.9.1 as written, the far-side target of a through-throat jump exists: it is the jet of the same analytic metric, continued through a regular point, with a future timelike $u$, so it is an element of $V$.
So, on this reading, the rule already defines the through-throat target; "stop" would be an additional rule, as §7 already says ("a case clause keyed to an instance feature"). The target is lost only on a reading v0.9.1 does not make: $V$ drawn from the exterior chart alone.

## 1. What the record says

- **$V$** (§4) is the set of oriented germs $O^u$: the infinite jet of a real-analytic Lorentzian metric at a point, with a future unit timelike $u$, modulo pointed analytic diffeomorphism. No chart or global manifold is named. $O$ is presented by the patch $P(O)$ obtained by analytic continuation of its jet. v0.9.1 claims no unique maximal manifold.
- **The rule** (§7) picks targets by geodesic continuation, not by matching $K$. It continues the jet analytically along the spacelike geodesic from $p$ with tangent $\pm\hat n$ for length $\varepsilon$, with $u$ parallel-transported. It uses "analytic continuation along a path; no completed 4-manifold". This is the operation §5 already uses for a curvelet's maximal analytic domain (`reviews/v0.7-outline-geometry.md`, F3).
- **Throat** (§7, C37; #290 §1). At a turning point $u^r=0$, so the inward path is the radial geodesic of the time-symmetric slice. $\hat n=\pm e_{\hat r}$ is orthogonal to $u$ and to the static Killing field, and every $t=$ const slice is the image of $T=0$ under the Killing boost, which fixes the bifurcation sphere. The path is spacelike and crosses no horizon away from the sphere. It meets $r=2$ only at the bifurcation 2-sphere, "a regular point of the continued metric", and it never enters $r<2$. So the "other side" is the far exterior across the Einstein–Rosen bridge, not the black-hole interior. The record defines the through target as the $M=1$ turning-point germ at $r'$, with $\Delta\ell(r')=\varepsilon-\Delta\ell(r)$ and the same static-frame speed. It adds that "which exterior" is not a property of the target.

## 2. Does the state exist?

1. **Same metric, analytic along the path.** In Kruskal coordinates $(T,X)$ the metric is $F(r)(-dT^2+dX^2)+r^2d\Omega^2$ with $F=(32/r)e^{-r/2}$, and $r=2(1+W(z/e))$ with $z=X^2-T^2$ ($W$ the principal Lambert function). Region I ($X>|T|$) is the source's exterior; region III ($X<-|T|$) is the far exterior. This is analytic at $z=0$, and its only singularity is at $z=-1$, which is $r=0$. At the sphere $F=16/e$ and $K=3/4$, so $r=2$ is a coordinate singularity of the Schwarzschild chart, not a curvature one (pin (1); Kruskal 1960, Phys. Rev. 119, 1743; Misner, Thorne & Wheeler 1973, ch. 31, for the Kruskal–Szekeres coordinates and the Einstein–Rosen bridge).
2. **Unique.** Continuation along a fixed path is unique wherever it exists, by the identity theorem. The path is itself fixed by the continued metric. So any analytic world containing a neighbourhood of the path gives the same germ, whether Kruskal or a quotient of it. Under the jet–patch lock (Paper 1 §2; `papers/analytic-patch-from-jet.md`, Theorem B, proved there via complexification), the source germ determines its maximal simply-connected patch $P(O)$. Kruskal is simply connected and realizes the germ, so it immerses in $P(O)$, and the far side lies in it.
3. **Future timelike $u$.** $T=0$ is a geodesic and totally geodesic, and $n=F^{-1/2}\partial_T$ and $e_\varphi$ are parallel along it (pin (2)). So the transported $u=\gamma(n+v\,e_\varphi)$ stays unit, future and timelike, with the same speed. The static Killing field flips time orientation across the sphere; $u$ does not.
4. **The record's formula is the continuation.** The Kruskal proper length from the far point $X<0$ at $r'$, through $X=0$, to the source equals $\varepsilon$. This is checked at #290's two cases: $r'=3227.2161034$ and $r'=189.874728977$ at $c=0.1$ (pin (3)).
5. **Reachability is not required.** No future causal curve runs from region I to region III, but jumps are type (ii) and carry no $\tau$. (a) is the germ-level $F(O)$ test and is blind to which exterior. Under (a) the thresholds are never reached on the instance (C33).

So the state exists. "Stop" is v0.9.1's own named alternative, a case clause keyed to an instance feature (§7). This note neither adopts nor rejects it. It bears on C37's claim text ("the rule needs a throat convention"): on this reading the rule as stated already defines the through target, so a convention is needed only to adopt "stop". By a Lead ruling (2026-10-11; a v0.10 editorial decision within the Lead's remit, prompted by David's 4:00 PM ET question in chat, "If the observer path keeps going through observer-space mathematically, then what's the question?", not under David's delegation and in no FOR DAVID category of #230 §0; relayed, not signed), that wording is superseded on this reading and is to be revised in v0.10 (`notes/v0.10-plan.md` item 12); v0.9.1 is not edited here.

## 3. Readings on which the answer could turn

| Reading | Does the target exist? |
|---|---|
| v0.9.1 as written (germs, continuation along a path) | Yes, unique. "Stop" is an added rule. |
| A completed world $M$ (Kruskal, a quotient) | Yes, the same germ (identity theorem). A world with the sphere punched out lacks the path, but §5 refuses lifetimes set by holes and §4 refuses E-smuggling. |
| $V$ drawn from the exterior chart ($r>2$) only | The path leaves the chart at finite length, and the rule gives no target. A germ at $r'$ still lies in $V$, but only the reflection formula, added as a rule, would select it. So "through" has no target here. |
| Gauge: germs mod pointed diffeomorphism | The far germ equals the near-exterior germ at $r'$ ($X\mapsto-X$, $\theta\mapsto\pi-\theta$). |
| Gauge: "which exterior" kept | It still exists, as a distinct element. Existence does not turn on gauge; only identifications (such as #290 A6) do. |

A vertex *on* the sphere is a separate case: there $\nabla K=0$ and the rule gives no target (§7).

## Pins

`notes/throat-well-posedness-scripts/`. Run with `sh run.sh` (Python 3.13.5, mpmath 1.3.0, sympy 1.14.0; `run.sh` calls `python`). The run is deterministic, with no seed and no $N$. `twp.py` `656757f1c7dc`, `run.sh` `1b51c5ec761f`, `expected/twp.txt` `549d0a9486be`. Expected output: the series and the values $F(2)=16/e$ and $K(2)=3/4$; all Christoffels and covariant derivatives at $T=0$ equal to 0; and the two path lengths equal to $\varepsilon=6242.68717543$ and $1201.40570707$. A third case ($c=0.01$, $r_0=300{,}000$) was run and dropped. With 40 equal subintervals the quadrature was off by about 1.5. This is a resolution artefact at the throat: the subintervals span about $4\times10^3$ in $s$, while the integrand varies on a scale of order 1 near $X=0$. With breakpoints added at the integers in $[-20,20]$, the length equals $\varepsilon=624268.71754317$ at dps 40. The pinned run omits this case.

## Critic questions

1. The standing rule ("continue to whatever state exists") is not quoted from the repository. Its nearest record is David's (Z-ix) sentence, relayed by the Physics Lead and not signed: "But if it can be defined and it does exist, then it follows the same rule that we use everywhere else" (`notes/zeno-mass-scoping.md`). It is stated for an observer's continuation. This note applies it to a type-(ii) target. Is that the intended scope?
2. Does anyone on the record hold the exterior-chart reading? §4 and §7 seem to exclude it. If no one does, the third row can go.
