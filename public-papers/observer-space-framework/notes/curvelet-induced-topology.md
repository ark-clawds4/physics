# Curvelet-induced topology on $V$: what curvelet continuity gives for free

*Answers the Physics Lead's question, prompted by David: can curvelet continuity (Thm 3 of `papers/geodesic-lifts.md`) give $V$ continuity with no new structure? Written at main `76e9ace`; v0.9.1 unedited; no pick; neutral relative to #301's (T0)–(T3). Bare § and C pointers are to v0.9.1. Gauge, grain, F11, the throat convention and the Zeno pick stay open.*

**Verdict.** Yes, but it is nearly empty for Zeno. The final topology $\mathcal T_\gamma$ from all curvelets needs only §5's curvelets and the results §5 cites (Prop. 3.2, Thm 3, Cor. 3.1 of `papers/geodesic-lifts.md`). It splits $V$ into clopen points, circles and open intervals, is Hausdorff and metrizable, and makes non-self-loop jumps discontinuous. With finite arm sets, a Zeno history has a limit iff it ends by repeating one self-loop $(Q,Q)$ at a single $\tau$. So C5's chains and C8 have no limit, and (Z-ix) is well-posed but equals its partner on every example on record: in effect (T0). Convergence of such chains needs a coarser topology: #301's (T1)/(T2) or something new.

## 1. Well-defined? (question 1)

$U\subseteq V$ is open iff $\gamma^{-1}(U)$ is open in $I_\gamma$ for every curvelet $\gamma:I_\gamma\to V$. v0.9.1 supplies the maps (§5: the curve traced by the geodesic from $(p,u)$ in $P(O)$, parametrised by $\tau$), their open maximal analytic domains (§5, §6.1; including $\tau<0$), and their dependence on the class $O^u$ alone (§4, "Lock-side"). Not written in v0.9.1:

1. *How the maximal domain is built.* $\mathcal T_\gamma$ does not depend on it: openness is local, and each germ is interior to an earlier germ's curvelet, so any open-interval convention, or forward-only $[0,b)$, gives the same topology.
2. *The shift property* $\gamma_{\gamma_O(s)}(\tau)=\gamma_O(s+\tau)$, $I_{\gamma_O(s)}=I_O-s$ (Prop. 3.2, Cor. 3.1).
3. *The component shapes* (next section).

What is missing is statements, not structure.

## 2. The partition hypothesis

**Claim.** Maximal curvelets sharing a point $Q$ have the same image: both shifted lifts start from $Q$ with its $u$, so each equals $\gamma_Q$ on a positive interval (Prop. 3.2), hence wherever both are analytic (Cor. 3.1, from Theorem 2 of `papers/analytic-split.md`). $\square$ Theorem 2 allows isolated meetings (geodesic-lifts §2, the "star"); in $V$, $u$ fixes the geodesic and excludes them.

So the orbits $C=\gamma(I)$ partition $V$, each clopen (other orbits' curvelets have empty preimage), and $V=\bigsqcup C$, each $C$ with the quotient topology from $I$.

**Shapes.** If $\gamma(s)=\gamma(t)$, $s<t$, the shift property makes $\gamma$ $(t-s)$-periodic with $I=\mathbb R$; periods form a subgroup $P$. If $P$ were dense, the $O(3)$-invariants of each order of Fermi coefficients along $\sigma$ would be analytic (Thm 3) and $P$-periodic, hence constant; invariants separate orbits of a compact group, so $\gamma$ would be constant. *This argument is mine, not on record.*

| $P$ | Component | Instances on record |
|---|---|---|
| $\mathbb R$ (constant) | point | locally symmetric lumps: Minkowski, de Sitter, ESU, Cahen–Wallach (§6.1, C19, C28); Schwarzschild circular geodesics (C21's circular locus) |
| $T\mathbb Z$, $T>0$ | circle | bound non-circular Schwarzschild orbits, recurring at successive periastra (#292 case 2); $X'$ on $[9.8926,18.7504]$, $T=400.528$ (C6) |
| $\{0\}$ | open interval | plunging and scattering orbits; comoving FLRW observers, including C8's |

**Gauge.** The above uses v0.9.1's identity (§4).
- *Raw presentations.* The maps need a presentation chosen along $\sigma$; Fermi normal form modulo $O(3)$ gives back $V$.
- *"Which exterior" kept* (#301 (T3)). No curvelet crosses regions I/III; nothing changes.
- *World-anchored labels.* Circles and points unwind into lines; not v0.9.1's $V$, and E-smuggling (§4).
- *$\mathrm{Obs}$ (no $u$).* Projected curvelets meet at shared lumps; no partition (close variants, below).

## 3. Hausdorff (question 2)

Yes, and T1 (a disjoint union of points, circles and intervals). Metrizable without new structure: $\min(1,|s-t|)$ on intervals, $\min(1,\text{arc distance})$ on circles, 1 across components (lock-side). Locally compact, not separable.

## 4. Jumps (question 3)

With #292's right-continuous trace, a jump $O\to O'$ is continuous iff $O'=O$:
- *Another curvelet:* discontinuous.
- *Same curvelet, $\tau>0$:* type (i), not a jump (item 3). So no type-(ii) pair stays on a circle or a point.
- *Same curvelet, $\tau<0$ only* (backward; undecided in v0.9.1): discontinuous, as $\gamma(s)\neq\gamma(s-d)$ in a Hausdorff interval.
- *Self-loop $(O,O)$:* continuous in any topology. #292: excluded under (a); type (i) at recurrent germs (circles); otherwise kept unless $R$ is irreflexive (a named extra). On the Kretschmann rule under "continue through", self-targets occur only at the $\varepsilon=2\Delta\ell$ apastra ($r_0=2786.4692$ and $\approx2.000361$ at $c=0.1$, #290 (T3)).

§5's "discontinuous in oriented observer space", C10 and #303's other "discontinuous" hits become true (#303 not re-run).

## 5. Limits (question 4)

A sequence converges iff eventually in one component and convergent there.
- **C5 near-throat chain ("through", $c=0.1$, from $r=10$).** States are turning points with $v=0.3849001795$, so $L=rv/\sqrt{1-v^2}$, constant along curvelets, separates them. Over 20,000 jumps the 20,001 values $L_n$ are pairwise distinct (minimum gap $2.5\times10^{-16}$), and none equals $L^*=0.834208210991$ (closest $1.2\times10^{-13}$) (pin (2)). No limit under either (T3) reading, in particular not the germ at $r^*=2.00036101764$.
- **C5 outward chain.** Radii strictly increasing (pin (3)): no limit. (T1) gives the flat germ (#299).
- **C8.** Accumulation is at $t\to1$, the domain's end, where $\gamma$ leaves every compact subset: no limit.

| | (T0) | (T1)/(T2), identify exteriors | (T1)/(T2), labels kept | $\mathcal T_\gamma$ |
|---|---|---|---|---|
| C5 inward, "through" | not asked; ends | germ at $r^*$ | none (two accumulation points) | none |
| C5 outward | not asked; ends | flat germ (inverse-limit) | flat germ | none |
| C8 | not asked; ends | none | none | none |

By Thm 3 each curvelet is continuous into (T1)'s inverse-limit variant (re-centred Fermi coordinates along $\sigma$; Theorem 16 read on $V$ as in #299; taken as immediate), so $\mathcal T_\gamma$ is finer than (T1) and (T3) is idle. For Zeno it matches (T0) in effect on every recorded example, differing only in defining "exists" and at self-loop tails.

## 6. (Z-ix) (question 5)

**Proposition.** Assume finite arm sets (as EPP1's equal shares need), sources in $V^\tau$ (§8.2 item 1), and $V^\tau$ discrete along each curvelet in its open domain (§6.1). A Zeno history converges in $\mathcal T_\gamma$ iff it eventually repeats one self-loop $(Q,Q)$ at one $\tau$; its limit is then $Q$.

*Sketch.* The tail lies in $Q$'s component $C$; a point component has no slice points. Otherwise take a window around $Q$ with no other slice point or star target (and $2\delta<T$ on a circle): late decisions are all at $Q$, segments and other jumps leave the window, so only the self-loop remains. The converse is immediate. $\square$

So (Z-ix) is well-posed, N-a's choices (membership, uniqueness, reachability) hold automatically, and **only self-loop tails are continued**, which is stronger than the Lead's guess: it also covers histories confined to one curvelet. Such tails are absent under (a), at recurrent germs, or under irreflexivity (#292 cases 1–3). On the Kretschmann rule they need a self-target reached by a jump, without (A); the pinned chain hits none in 20,000 jumps, and I have not shown any chain does. Continuing from $Q$ re-enters the loop (`notes/zeno-mass-scoping.md` question 7).

**Rows affected.** Only (Z-ix): "exists" is defined, and its values equal its partner's on C5, C8 and the toys. (Z-0)–(Z-viii) are unchanged; plan item 2's ILL flag on (Z-ix) would become WP if $\mathcal T_\gamma$ were adopted. #292's D1/D2 change only at self-loop tails. With continuum stars (soft Prop. 13) the proposition fails, and backward jumps along one curvelet could converge.

**Close variants.** Smooth segments, compact sub-intervals and CWS packages (Cor. 3.1) give the same topology. On $\mathrm{Obs}$ via $\pi\circ\gamma$ (not on record; sketched), components overlap, and with exteriors identified C5's lumps converge to the $r^*$ lump (a radial geodesic sweeps $r$ around $r^*$); pulled back to $V$, all $u$ at one lump become inseparable. Making every history continuous depends on $R$ and is not Hausdorff once an edge's source is reached along a segment.

## 7. Options and costs (no pick)

- **Adopt $\mathcal T_\gamma$.** No new structure; Hausdorff and metrizable; §5's "discontinuous" becomes a theorem. Cost: for Zeno it is (T0) with "exists" defined; item 8's "ends there" stays unconditional except at self-loop tails, and (Z-ix) continues nothing on record.
- **A coarser Hausdorff topology where C5-type chains converge.** Needs structure curvelets lack: #301's (T1)/(T2) (with (T3)) at #301's costs, or something new.
- **Coarser, from record objects only** ($\mathrm{Obs}$-pullback, continuous histories). Not Hausdorff; the second depends on $R$.
- **(T0)** as in #301.

## Pins

`notes/curvelet-induced-topology-scripts/`. `sh run.sh` (Python 3.13.5, mpmath 1.3.0; calls `python`); deterministic, no seed, `mp.dps=40`. `cit.py` `a19b8a42d22a`, `run.sh` `76c334e5085e`, `expected/cit.txt` `0b896744278f`. `ell`, `eps`, `rof` and the jump are #299's, from #290. Pins: (1) $r^*$, $L^*$; (2) distinct $L_n$; (3) monotone outward radii.

## Critic questions

1. The proposition needs finite arm sets. Is that a commitment of v0.9.1 (EPP1's equal shares), or only of the Kretschmann rule? With continuum stars, does $\mathcal T_\gamma$ still decide (Z-ix)?
2. Should the dense-period argument be proved in full, or is it enough that every recorded instance falls in one of the three cases?
