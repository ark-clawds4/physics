# Curvelet-induced topology on $V$: what curvelet continuity gives for free

*Standalone note answering the Physics Lead's question, prompted by David: can curvelet continuity (Thm 3 of `papers/geodesic-lifts.md`) give $V$ a notion of continuity with no new structure? Written at main `76e9ace`. v0.9.1 is unedited, no option is picked, and the note is neutral relative to #301's (T0)–(T3). Bare § and C pointers are to v0.9.1. (M1) is ruled by David at L3 (relayed, not signed). Gauge, grain, F11, the throat convention and the Zeno pick stay open.*

**Verdict.** Yes, but the result is nearly empty for Zeno. Call $\mathcal T_\gamma$ the final topology on $V$ from all curvelets. It is defined from v0.9.1 §5's curvelets plus the results §5 cites (Prop. 3.2, Thm 3, Cor. 3.1 of `papers/geodesic-lifts.md`), with nothing new. The hypothesis holds: maximal curvelets partition $V$, each one is clopen, and $V$ is a topological disjoint union of points, circles and open intervals. $\mathcal T_\gamma$ is Hausdorff, and indeed metrizable. Every type-(ii) jump is a discontinuity. With finite arm sets, a Zeno history has a limit iff it ends in an infinite repetition of one self-loop $(Q,Q)$ at a single $\tau$. So C5's chains and C8 have no limit. (Z-ix) becomes well-posed but takes its partner's value on every example on record. For Zeno purposes, $\mathcal T_\gamma$ coincides in effect with (T0). Any topology that gives such chains a limit has to be coarser than $\mathcal T_\gamma$, which needs structure that curvelets do not supply: #301's (T1)/(T2), or something new.

## 1. The construction, and what it needs (question 1)

$\mathcal T_\gamma$: $U\subseteq V$ is open iff $\gamma^{-1}(U)$ is open in $I_\gamma$ for every curvelet $\gamma:I_\gamma\to V$. This is the finest topology that makes every curvelet continuous.

**From v0.9.1 alone.** §5 defines $\gamma_{O^u}$ as "the unique curve in $V$ traced by the geodesic from $(p,u)$ in the patch $P(O)$", parametrised by proper time $\tau$ (§5, oriented split, writes $\gamma_{O^u}(\tau)$). Its domain is "the curvelet's maximal analytic domain" (§5), which is open (§6.1) and includes $\tau<0$ (§5, backward pairs). That the curvelet is a function of the class $O^u$, not of a presentation, is stated in §4 ("Lock-side": "the curvelet $\gamma_{O^u}$ that $O^u$ determines"). Uniqueness and analyticity come from the results §5 cites. So the maps, their parametrisation and their domains are all v0.9.1's. Three things are not written in v0.9.1:

1. *How the maximal domain is built.* v0.9.1 names the domain and rules out world-dependent lifetimes, but does not construct it. The natural construction continues $g$ along $\sigma_O$, which matches geodesic-lifts' "wherever both remain analytic". $\mathcal T_\gamma$ does not depend on this choice. Openness of a preimage is a local condition, and every germ is an interior point of the curvelet of a slightly earlier germ. So any convention that gives each germ an open interval of $\tau$ around 0 yields the same topology, and so do forward-only domains $[0,b)$.
2. *The shift property* $\gamma_{\gamma_O(s)}(\tau)=\gamma_O(s+\tau)$, with $I_{\gamma_O(s)}=I_O-s$. This follows from Prop. 3.2 and Cor. 3.1 (§2 below) but is not stated in v0.9.1.
3. *The shape of the components* (§2), which needs item 2 and a short argument.

So $\mathcal T_\gamma$ is well-defined on v0.9.1's definitions together with the results §5 itself cites. What is missing is statements (items 2 and 3), not structure.

## 2. The partition hypothesis, tested

**Claim.** Two maximal curvelets that share a point have the same image.

**Proof.** Suppose $Q=\gamma_O(s)=\gamma_{O'}(s')$. The shifted geodesics $\sigma_O(s+\cdot)$ and $\sigma_{O'}(s'+\cdot)$ start from occurrences of $Q$, with $Q$'s $u$. By Prop. 3.2, each lift coincides with $\gamma_Q$ on a positive interval. By Cor. 3.1 (Theorem 2 of `papers/analytic-split.md`), they coincide wherever both are analytic. Maximality then makes the domains match. $\square$

Theorem 2 does allow distinct analytic curves to meet at an isolated point (geodesic-lifts §2, the "star"). Prop. 3.2 excludes this for geodesic lifts *in $V$*, because the oriented germ carries $u$, and $u$ fixes the geodesic. So the orbits $C=\gamma(I)$ partition $V$. For a curvelet $\gamma'$ of another orbit, $\gamma'^{-1}(C)=\emptyset$, and for $C$'s own curvelets it is the whole domain. So each orbit is clopen, and $V=\bigsqcup C$ topologically, with each $C$ carrying the quotient topology from $I$.

**Shapes.** Suppose $\gamma(s)=\gamma(t)$ with $s<t$. By the shift property, $\gamma$ has period $t-s$, and $I$ is invariant under that translation, so $I=\mathbb R$. The periods form a subgroup $P\subseteq\mathbb R$.

If $P$ were dense, then for each $k$ the $O(3)$-invariant polynomials of the order-$k$ Fermi coefficients along $\sigma$ would be analytic functions of $\tau$ (Thm 3) that are $P$-periodic. They would therefore be constant. Invariants separate the orbits of a compact group, so every $\gamma(\tau)$ would equal $\gamma(0)$, meaning $\gamma$ is constant. (This is my argument, not on record; it uses Thm 3 only as a tool.) So there are three cases:

| $P$ | Component | Instances on record |
|---|---|---|
| $\mathbb R$ (constant curvelet) | a point | locally symmetric lumps: Minkowski, de Sitter, ESU, Cahen–Wallach (§6.1, C19, C28); Schwarzschild circular geodesics (C21's circular locus; staticity and spherical symmetry carry each point and tangent to any other) |
| $T\mathbb Z$, $T>0$ | a circle $\mathbb R/T\mathbb Z$ | bound non-circular Schwarzschild orbits. The germ recurs at successive periastra (#292 case 2); for $X'$ on $[9.8926,18.7504]$, $T=400.528$ (C6) |
| $\{0\}$ | an open interval, homeomorphic to $I$ | plunging and scattering orbits; comoving FLRW observers, including C8's, whose domain ends at the singular time |

**Gauge.** The partition and the shapes above are for v0.9.1's identity: germs modulo pointed analytic diffeomorphism, with $u$ taken modulo isotropy (§4). Under other readings:

- *Raw presentations, no quotient.* A curvelet does not pick one presentation per $\tau$, so the maps are not defined without a choice along $\sigma$. The canonical choice, Fermi normal form modulo $O(3)$, gives back $V$'s points.
- *"Which exterior" kept* (#301 (T3)). Points are finer, but no curvelet crosses between regions I and III. The partition and the shapes are unchanged, and the C5 states of §5 stay in pairwise distinct components.
- *World-anchored labels* (pointed worlds). Circles and points would unwind into lines. That is not v0.9.1's $V$, and using a particular world in this way would be E-smuggling (§4).
- *Lumps without $u$* ($\mathrm{Obs}$). The partition fails: projected curvelets with different $u$ meet at a shared lump. See §7.

## 3. Hausdorff, T1, metrizable (question 2)

Each component is a point, a circle or an open interval, all Hausdorff. A disjoint union of Hausdorff spaces is Hausdorff, so $\mathcal T_\gamma$ is Hausdorff and therefore T1. It is also metrizable with no new structure. Take $d=\min(1,|s-t|)$ along an interval component, $\min(1,\text{arc distance})$ on a circle, and $d=1$ across components. This metric is lock-side, since it uses only proper time along the curvelet. $\mathcal T_\gamma$ is locally compact but not separable, since it has uncountably many components.

## 4. Jumps (question 3)

Read a history's trace as right-continuous (#292 D1). At a jump from $O$ to $O'$, the left limit is $O$ and the value is $O'$, so the trace is continuous there iff $O'=O$.

- *Target on another curvelet.* Discontinuous: $O'$ lies in a different clopen component.
- *Target on the same curvelet at $\tau>0$.* This is type (i) (§5), so it is not a jump, and §8.2 item 3 removes it. On a circle every point of the component is at some $\tau>0$, so no type-(ii) pair stays on a circle. On a point component there is no pair at all.
- *Same curvelet at $\tau<0$ only* (a backward pair, which v0.9.1 neither admits nor excludes). Discontinuous: $\gamma(s)\neq\gamma(s-d)$ in a Hausdorff interval.
- *Self-loop $(O,O)$.* There is no change of state, so the trace is continuous in any topology. #292's three cases are: under (a), excluded; at a recurrent germ, type (i) and removed (this is the circle case); otherwise it survives unless $R$ is irreflexive, a named extra. On the Kretschmann rule under "continue through", self-targets occur only at the $\varepsilon=2\Delta\ell$ apastra ($r_0=2786.4692$ and $\approx2.000361$ at $c=0.1$, #290 (T3)).

So under $\mathcal T_\gamma$, every type-(ii) jump other than a self-loop is a discontinuity. v0.9.1 §5's "discontinuous in oriented observer space", C10 and the other "discontinuous" hits that #303 counts as ill-posed would become true statements. I have not re-run #303's classification.

## 5. Limits: C5 and C8 (question 4)

In a disjoint union, a sequence converges iff it is eventually in one component and converges there.

- **C5 near-throat chain ("through", $c=0.1$, from $r=10$).** Every state is a turning-point germ with the same $v=0.3849001795$. So its angular momentum is $L=rv/\sqrt{1-v^2}$, which is constant along a curvelet. Distinct radii therefore put states on distinct curvelets. Over 20,000 jumps, the 20,001 values $L_n$ are pairwise distinct, with a minimum gap of $2.5\times10^{-16}$, and none equals $L^*=0.834208210991$ (the closest is $1.2\times10^{-13}$ away). This is pin (2). No component holds a tail of the chain, so the chain has no limit, under either (T3) reading. In particular it does not converge to the germ at $r^*=2.00036101764$, whose component is open and contains no $O_n$ in the pinned range.
- **C5 outward chain.** Its radii increase strictly (pin (3)), so its states are on distinct curvelets and it has no limit. Under (T1) it converges to the flat germ (#299).
- **C8.** Here branch points accumulate along one comoving curvelet as $t\to1$, the end of its domain. As $\tau$ approaches the end of the domain, $\gamma(\tau)$ leaves every compact subset of its interval component, and the other components are open and disjoint from it. So there is no limit, as under every option in #301.

| | (T0) | (T1)/(T2), identify exteriors | (T1)/(T2), labels kept | $\mathcal T_\gamma$ |
|---|---|---|---|---|
| C5 inward, "through" | not asked; ends | germ at $r^*$ | none (two accumulation points) | none |
| C5 outward | not asked; ends | flat germ (inverse-limit) | flat germ | none |
| C8 | not asked; ends | none | none | none |

**Relation to #301.** By Thm 3, each curvelet is continuous into (T1)'s inverse-limit variant: Fermi coordinates along $\sigma$, re-centred at $\sigma(\tau)$, are Fermi coordinates for $(\sigma(\tau),\dot\sigma(\tau))$ up to $O(3)$. Theorem 16 is stated for $\mathrm{Obs}$ and is read on $V$ as in #299, and I take this step as immediate. Given that, $\mathcal T_\gamma$ is finer than (T1): every $\mathcal T_\gamma$-limit is a (T1)-limit, but not conversely. (T3) is idle under $\mathcal T_\gamma$. For Zeno purposes $\mathcal T_\gamma$ coincides in effect with (T0) on every example on record. It differs only formally ("exists" is defined) and at self-loop tails (§6).

## 6. (Z-ix) (question 5)

**Proposition.** Assume finite arm sets (as EPP1's equal shares need), sources in $V^\tau$ (§8.2 item 1), and $V^\tau$ discrete along each curvelet in its open domain (§6.1). Then a Zeno history converges in $\mathcal T_\gamma$ iff, from some decision on, it repeats a single self-loop $(Q,Q)$ at one $\tau$. Its limit is then $Q$.

**Proof sketch.** Suppose the history converges to $Q$. Then its states lie eventually in $Q$'s component $C$. If $C$ is a point component, $s\circ\gamma$ is constant, so $V^\tau\cap C=\emptyset$ and there are no decisions, which is impossible. Otherwise, choose a window $\gamma((s^*-\delta,s^*+\delta))$ around $Q=\gamma(s^*)$ that contains no slice point other than $Q$, no target of $Q$'s finite star other than $Q$, and (on a circle) has $2\delta<T$. Eventually every state is in the window, so every decision is at $Q$. A segment arm leaves the window before the next slice point, and a jump to any other target leaves it too. Only the self-loop remains. The converse is immediate. $\square$

So (Z-ix) becomes well-posed, and N-a's choices are met automatically: membership ($Q\in V$), uniqueness (Hausdorff) and reachability ($Q$ is visited). Its content is this: **only self-loop tails are continued, and every other Zeno history ends.** That includes every history with infinitely many jumps across distinct curvelets, which is the Lead's guess, and also those confined to one curvelet. Self-loop tails do not occur under (a), at recurrent germs, or under irreflexivity (#292 cases 1–3). On the Kretschmann rule they could arise only at a self-target germ reached by a jump, without (A). The pinned chain never lands on one in 20,000 jumps (pin (2)), and I have not shown that any chain does. Continuing from such a $Q$ under the same rule re-enters the same loop, which is `notes/zeno-mass-scoping.md` question 7.

**Rows affected.** Only the (Z-ix) row: "exists" is now defined, and its values equal its partner's on C5, C8 and the toys (which carry no observer data, Zeno note "On the toys"). (Z-0)–(Z-viii) are defined without a topology and do not change. Plan item 2's ILL flag on (Z-ix) would become WP, conditional on adopting $\mathcal T_\gamma$. #292's D1/D2 are unchanged except at self-loop tails. Without finite stars, for example with the in-patch continuum of soft Prop. 13, the proposition does not apply, and backward jumps along one curvelet could converge.

## 7. Close variants

- *Smooth segments, or compact sub-intervals of curvelets.* Same topology, since openness of a preimage is local.
- *Finite concatenations without jumps (CWS packages).* Same topology: by Cor. 3.1 their path is the curvelet (§5).
- *The same construction on $\mathrm{Obs}$, through $\pi\circ\gamma$* (not on record; sketched). Components are not disjoint, since lumps are shared across $u$. Under identification of the exteriors, the C5 chain's lumps would converge to the $r^*$ lump: a radial geodesic through that lump sweeps an interval of $r$ around $r^*$. But this gives $V$ no Hausdorff topology. Pulled back along $V\to\mathrm{Obs}$, all $u$ at one lump become inseparable, and limits are not unique.
- *Making every history continuous* (the final topology from traces with jumps). This depends on $R$, and it is not Hausdorff once an edge's source is reached along a segment. Any open set around the target must then contain the curvelet just before the source, and so must any open set around the source.

## 8. Options and costs (no pick)

- **Adopt $\mathcal T_\gamma$.** It needs no new structure, is Hausdorff and metrizable, and turns §5's "discontinuous" into a theorem. Cost: for Zeno purposes it is (T0) with "exists" defined. Item 8's "ends there" stays unconditional except at self-loop tails, and David's reading continues nothing on record.
- **A coarser Hausdorff topology in which chains like C5's converge.** This needs structure that curvelets do not supply. That is #301's (T1)/(T2), with (T3) on top, at the costs #301 lists, or something new.
- **A coarser topology built only from record objects** ($\mathrm{Obs}$-pullback, or making histories continuous). It is not Hausdorff, its limits are not unique, and the second version depends on $R$.
- **(T0)** as in #301.

## Pins

`notes/curvelet-induced-topology-scripts/`. Run with `sh run.sh` (Python 3.13.5, mpmath 1.3.0; `run.sh` calls `python`). The run is deterministic, with no seed and no $N$, at `mp.dps=40`. `cit.py` `a19b8a42d22a`, `run.sh` `76c334e5085e`, `expected/cit.txt` `0b896744278f`. `ell`, `eps`, `rof` and the jump are those of #299's `zwp.py`, taken from #290. Pin (1) gives $r^*$ and $L^*$, pin (2) the chain's distinct $L_n$, and pin (3) the monotone outward radii.

## Critic questions

1. The proposition needs finite arm sets. Is that a commitment of v0.9.1 (EPP1's equal shares), or only of the Kretschmann rule? If continuum stars are allowed, does $\mathcal T_\gamma$ still decide (Z-ix)?
2. Should the dense-period argument of §2 be proved in full in a paper, or is it enough that every instance on record falls into one of the three listed cases?
