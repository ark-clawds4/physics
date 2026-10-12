# Curvelet-induced topology on $V$: what curvelet continuity gives for free

*Answers David's question, relayed by the Physics Lead (not signed; the exchange is not recorded in this repository): can curvelet continuity (Thm 3 of `papers/geodesic-lifts.md`) give $V$ continuity with no new structure? Written at main `76e9ace`; prior work and references added at main `8bca97f`; v0.9.1 unedited; no pick; neutral relative to #301's (T0)–(T3). Bare § and C pointers are to v0.9.1. Gauge, grain, F11, the throat convention and the Zeno pick stay open.*

**Verdict.** Yes, but it is nearly empty for Zeno. The final topology from all curvelets, presented here as a fifth option, (T4) "the curvelet-induced topology, no new structure", needs only §5's curvelets and the results §5 cites (Prop. 3.2, Thm 3, Cor. 3.1 of `papers/geodesic-lifts.md`). It splits $V$ into clopen points, circles and open intervals, is Hausdorff and metrizable, and makes non-self-loop jumps discontinuous. With finite arm sets, a Zeno history has a limit iff it ends by repeating one self-loop $(Q,Q)$ at a single $\tau$. So C5's chains and C8 have no limit, and (Z-ix) (David's reading, relayed, not signed; `notes/zeno-mass-scoping.md`) is well-posed but equals its partner on every example on record: for Zeno limits on those examples, in effect (T0). Convergence of such chains needs a coarser topology: #301's (T1)/(T2) or something new.

## 1. Well-defined? (question 1)

$U\subseteq V$ is open iff $\gamma^{-1}(U)$ is open in $I_\gamma$ for every curvelet $\gamma:I_\gamma\to V$. v0.9.1 supplies the maps (§5: the curve traced by the geodesic from $(p,u)$ in $P(O)$, parametrised by $\tau$), their open maximal analytic domains (§5, §6.1; including $\tau<0$), and their dependence on the class $O^u$ alone (§4, "Lock-side"). Not written in v0.9.1:

1. *How the maximal domain is built.* (T4) does not depend on it: openness is local, and each germ is interior to an earlier germ's curvelet, so any open-interval convention, or forward-only $[0,b)$, gives the same topology.
2. *The shift property* $\gamma_{\gamma_O(s)}(\tau)=\gamma_O(s+\tau)$, $I_{\gamma_O(s)}=I_O-s$ (Prop. 3.2, Cor. 3.1).
3. *The component shapes* (next section).

What is missing is statements, not structure.

**Prior work.** The construction is standard: the finest topology making a family of curves continuous is the D-topology of diffeology for one-dimensional plots (Iglesias-Zemmour 2013, art. 2.8; Christensen, Sinnamon and Wu 2014, Thm 3.7) and, for all smooth curves, the $c^\infty$-topology (Kriegl and Michor 1997, 2.12). On spacetime its analogues are Zeeman's (1967), Göbel's (1976) and the Hawking–King–McCarthy path topology (1976; see Low 2016), where the curves cross and fill open sets. On $V$ the curvelets do not cross, so the result is a formal analogue of the leaf topology of a one-dimensional flow. The nearest flow on record is the inertial-observer (Reeb) flow on Gielen and Wise's observer space (2013, §3.1), a different construction: its points are 4-velocities, not analytic germs, and $V$ is not their 7-manifold (§4, §12; §2: "It is not Stoica, not Gielen–Wise and not Larsson", FW4 in `versions/v0.10-changelog.md` §2c). What this note adds is carrying the construction out on $V$ via Thm 3, and the consequence for Zeno histories.

## 2. The partition hypothesis

**Claim.** Maximal curvelets sharing a point $Q$ have the same image: both shifted lifts start from $Q$ with its $u$, so each equals $\gamma_Q$ on a positive interval (Prop. 3.2), hence wherever both are analytic (Cor. 3.1, from Theorem 2 of `papers/analytic-split.md`). $\square$ Theorem 2 allows isolated meetings (geodesic-lifts §2, the "star"); in $V$, $u$ fixes the geodesic and excludes them.

So the orbits $C=\gamma(I)$ partition $V$, each clopen (other orbits' curvelets have empty preimage), and $V=\bigsqcup C$, each $C$ with the quotient topology from $I$.

**Shapes.** If $\gamma(s)=\gamma(t)$, $s<t$, the shift property makes $\gamma$ $(t-s)$-periodic with $I=\mathbb R$; periods form a subgroup $P$. If $P$ were dense, the $O(3)$-invariants of each order of Fermi coefficients along $\sigma$ would be analytic (Thm 3) and $P$-periodic, hence constant; invariants separate orbits of a compact group, and by compactness of $O(3)$ one rotation matches every order at once, so $\gamma$ would be constant. The same step shows $P$ is the common period group of continuous functions, hence closed: $\{0\}$, $T\mathbb Z$ or $\mathbb R$, and a dense proper $P$ cannot occur (isometries generating a non-closed subgroup make $\gamma$ constant). *This argument is this note's own, not on record.*

That a period group of a continuous map into a Hausdorff space is closed, and that the closed subgroups of $\mathbb R$ are $\{0\}$, $T\mathbb Z$ and $\mathbb R$, are standard (e.g. Bourbaki, *General Topology*). The excluded case, a dense period group, gives the indiscrete quotient, as in the irrational-torus example of diffeology (Iglesias-Zemmour 2013, exercise on irrational tori).

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

Yes, and every point is closed (a disjoint union of points, circles and intervals). Metrizable without new structure: $\min(1,|s-t|)$ on intervals, $\min(1,\text{arc distance})$ on circles, 1 across components (lock-side). Locally compact, not separable.

## 4. Jumps (question 3)

With #292's right-continuous trace, a jump $O\to O'$ is continuous iff $O'=O$:
- *Another curvelet:* discontinuous.
- *Same curvelet, $\tau>0$:* type (i), not a jump (item 3). So no type-(ii) pair stays on a circle or a point.
- *Same curvelet, $\tau<0$ only* (backward; undecided in v0.9.1): discontinuous, as $\gamma(s)\neq\gamma(s-d)$ in a Hausdorff interval.
- *Self-loop $(O,O)$:* continuous in any topology. #292: excluded under (a); type (i) at recurrent germs (circles); otherwise kept unless $R$ is irreflexive (a named extra). On the Kretschmann rule under "continue through", self-targets occur only at turning points with $\varepsilon=2\Delta\ell$ ($r_0=2786.4692$ and $\approx2.000361$ at $c=0.1$; #290, under its hypothesis that $\Delta\ell$ is increasing). At a recurrent germ (a bound orbit, a circle) the pair is type (i) and not in $R$ (item 3), so a self-loop needs a non-recurrent turning point there: at the C5 speed, the unbound periastron at $r_0=2786.47$ or the plunging apastron at $r^*$.

§5's "discontinuous in oriented observer space", C10 and #303's other "discontinuous" hits become true (#303 not re-run).

## 5. Limits (question 4)

A sequence converges iff eventually in one component and convergent there.
- **C5 near-throat chain ("through", $c=0.1$, from $r=10$).** States are turning points with $v=0.3849001795$, so $L=rv/\sqrt{1-v^2}$, constant along curvelets, separates them. Over 20,000 jumps the 20,001 values $L_n$ are pairwise distinct (minimum gap $2.5\times10^{-16}$), and none equals $L^*=0.834208210991$ (closest $1.2\times10^{-13}$) (pin (2)). No limit under either (T3) reading, in particular not the germ at $r^*=2.00036101764$.
- **C5 outward chain.** Radii strictly increasing (pin (3)): no limit. (T1) gives the flat germ (#299).
- **C8.** Accumulation is at $t\to1$, the domain's end, where $\gamma$ leaves every compact subset: no limit.

| | (T0) | (T1)/(T2), identify exteriors | (T1)/(T2), labels kept | (T4) |
|---|---|---|---|---|
| C5 inward, "through" | not asked; ends | germ at $r^*$ | none (two accumulation points) | none |
| C5 outward | not asked; ends | flat germ (inverse-limit) | flat germ (inverse-limit) | none |
| C8 | not asked; ends | none | none | none |

By Thm 3 each curvelet is continuous into (T1)'s inverse-limit variant (re-centred Fermi coordinates along $\sigma$; Theorem 16 read on $V$ as in #299; taken as immediate), so (T4) is finer than (T1) and (T3) is idle. For Zeno limits it matches (T0) in effect on every recorded example (C5, C8, the toys), differing in defining "exists" and at self-loop tails. As a topology it is not (T0): it makes non-self-loop jumps discontinuous, and it is listed separately as (T4).

## 6. (Z-ix) (question 5)

**Proposition.** Assume finite arm sets (v0.9.1's default: "The default is finite stars", §9), sources in $V^\tau$ (§8.2 item 1), and $V^\tau$ discrete along each curvelet in its open domain (§6.1). A Zeno history converges in (T4) iff it eventually repeats one self-loop $(Q,Q)$ at one $\tau$; its limit is then $Q$.

*Sketch.* The tail lies in $Q$'s component $C$; a point component has no slice points. Otherwise take a window around $Q$ with no other slice point or star target (and $2\delta<T$ on a circle): late decisions are all at $Q$, segments and other jumps leave the window, so only the self-loop remains. The converse is immediate. $\square$

So (Z-ix) is well-posed, N-a's choices (membership, uniqueness, reachability) hold automatically, and **only self-loop tails are continued**: histories with infinitely many jumps across distinct curvelets, and those confined to one, all end. Such tails are absent under (a), at recurrent germs, or under irreflexivity (#292 cases 1–3). On the Kretschmann rule they need a self-target reached by a jump, without (A) (strict alternation, §8.2 item 2, under which a jump is always followed by a segment of positive proper time); the pinned chain hits none in 20,000 jumps, and I have not shown any chain does. Continuing from $Q$ re-enters the loop (`notes/zeno-mass-scoping.md` question 7).

**Rows affected.** Only (Z-ix): "exists" is defined, and its values equal its partner's on C5, C8 and the toys. (Z-0)–(Z-viii) are unchanged; plan item 2's ILL flag on (Z-ix) would become WP if (T4) were adopted. #292's D1/D2 change only at self-loop tails. With continuum stars (soft Prop. 13) the proposition fails, and backward jumps along one curvelet could converge.

**Close variants.** Smooth segments, compact sub-intervals and CWS packages (Cor. 3.1) give the same topology. On $\mathrm{Obs}$ via $\pi\circ\gamma$ (not on record; sketched), components overlap, and with exteriors identified C5's lumps converge to the $r^*$ lump (a radial geodesic sweeps $r$ around $r^*$); pulled back to $V$, all $u$ at one lump become inseparable. Making every history continuous depends on $R$ and is not Hausdorff once an edge's source is reached along a segment.

Zeno behaviour of this kind (infinitely many jumps at one $\tau$) is the "static" Zeno of hybrid systems (Simić, Johansson, Lygeros and Sastry 2005, Def. 2.10), whose "hybrifold" glues each jump's start to its end (Def. 3.1), much as the continuous-history variant above does. Continuing runs past a Zeno point is studied in Ames, Zheng, Gregg and Sastry (2006). In finer path topologies on spacetime, limit-curve theorems likewise fail (Low 2016; Papadopoulos and Papadopoulos 2019; compare Minguzzi 2008).

## 7. Options and costs (no pick)

- **(T4) The curvelet-induced topology, no new structure.** Hausdorff and metrizable; §5's "discontinuous" becomes a theorem. Cost: for Zeno it is (T0) with "exists" defined; item 8's "ends there" stays unconditional except at self-loop tails, and (Z-ix) continues nothing on record.
- **(T1)/(T2), with (T3) on top: a coarser Hausdorff topology where C5-type chains converge.** Needs structure curvelets lack, at #301's costs; or something new.
- **Coarser, from record objects only** ($\mathrm{Obs}$-pullback, continuous histories). Not Hausdorff; the second depends on $R$.
- **(T0)** as in #301.

## Pins

`notes/curvelet-induced-topology-scripts/`. `sh run.sh` (Python 3.13.5, mpmath 1.3.0; calls `python`); deterministic, no seed, `mp.dps=40`. `cit.py` `a19b8a42d22a`, `run.sh` `76c334e5085e`, `expected/cit.txt` `0b896744278f`. `ell`, `eps`, `rof` and the jump are #299's, from #290. Pins: (1) $r^*$, $L^*$; (2) distinct $L_n$; (3) monotone outward radii.

## Critic questions

1. The proposition uses v0.9.1's default of finite stars (§9). Does that default bind every $R$, or only the Kretschmann rule? With continuum stars, does (T4) still decide (Z-ix)?
2. Should the dense-period argument be proved in full, or is it enough that every recorded instance falls in one of the three cases?

## References (prior work)

Compiled by Literature (`refs.md`, 2026-10-11; not in this repository) at David's request of 2026-10-11, 5:57 PM ET (relayed, not signed). Marks are Literature's: **[V-text]** the text itself was read; **[V-meta]** the DOI or arXiv metadata was checked, but the content comes from the abstract or a secondary source; **[U]** unverified. Further reading, not cited in the text: entry 1 (Zeeman 1964), entry 5's comment (Agrawal and Sinha 2026), entry 11 (Dugger), entry 12 (Fajstrup and Rosický) and entry 14 (Hohmann).

1. [V-meta] Zeeman, E. C., "Causality implies the Lorentz group", *J. Math. Phys.* 5(4), 490–493 (1964), doi:10.1063/1.1704140.
2. [V-meta] Zeeman, E. C., "The topology of Minkowski space", *Topology* 6(2), 161–170 (1967), doi:10.1016/0040-9383(67)90033-X.
3. [V-meta] Göbel, R., "Zeeman topologies on space-times of general relativity theory", *Commun. Math. Phys.* 46(3), 289–307 (1976), doi:10.1007/BF01609125.
4. [V-meta] Hawking, S. W., King, A. R., McCarthy, P. J., "A new topology for curved space–time which incorporates the causal, differential, and conformal structures", *J. Math. Phys.* 17(2), 174–181 (1976), doi:10.1063/1.522874.
5. [V-text] Low, R. J., "Spaces of paths and the path topology", *J. Math. Phys.* 57(9), 092503 (2016), doi:10.1063/1.4963144. Comment [V-meta]: Agrawal, G., Sinha, S., *J. Math. Phys.* 67(1), 014101 (2026), doi:10.1063/5.0275357.
6. [V-meta] Papadopoulos, K., Papadopoulos, B. K., "Space-time singularities vs. topologies in the Zeeman–Göbel class", *Gravit. Cosmol.* 25(2), 116–121 (2019), doi:10.1134/S0202289319020117, arXiv:1712.03270.
7. [V-meta] Minguzzi, E., "Limit curve theorems in Lorentzian geometry", *J. Math. Phys.* 49(9), 092501 (2008), doi:10.1063/1.2973048, arXiv:0712.3942.
8. [V-text] Iglesias-Zemmour, P., *Diffeology*, Math. Surveys Monogr. 185, AMS (2013), doi:10.1090/surv/185, art. 2.8 (D-topology). The article number and the irrational-torus exercise (no. 55) were checked in the author's posted revised edition, not the AMS print; the print numbering is [U].
9. [V-text] Christensen, J. D., Sinnamon, G., Wu, E., "The D-topology for diffeological spaces", *Pacific J. Math.* 272(1), 87–110 (2014), doi:10.2140/pjm.2014.272.87, arXiv:1302.2935, Thm 3.7.
10. [V-text] Kriegl, A., Michor, P. W., *The Convenient Setting of Global Analysis*, Math. Surveys Monogr. 53, AMS (1997), doi:10.1090/surv/053, 2.12 and 27.4.
11. [V-text] Dugger, D., "Notes on Delta-generated spaces", unpublished notes (2003), https://pages.uoregon.edu/ddugger/delta.pdf, Def. 1.2.
12. [V-meta] Fajstrup, L., Rosický, J., "A convenient category for directed homotopy", *Theory Appl. Categ.* 21, 7–20 (2008). Metadata only; not opened.
13. [V-text] Gielen, S., Wise, D. K., "Lifting general relativity to observer space", *J. Math. Phys.* 54, 052501 (2013), arXiv:1210.0019, doi:10.1063/1.4802878 (v0.9.1's References entry), §3.1 (Reeb flow on observer space).
14. [V-meta] Hohmann, M., "Extensions of Lorentzian spacetime geometry: From Finsler to Cartan and vice versa", *Phys. Rev. D* 87, 124034 (2013), doi:10.1103/PhysRevD.87.124034, arXiv:1304.5430.
15. [V-meta] Bourbaki, N., *General Topology, Chapters 5–10*, Springer (1989), doi:10.1007/978-3-642-61703-4. Cited without a section; the location is [U].
16. [V-text] Simić, S. N., Johansson, K. H., Lygeros, J., Sastry, S., "Towards a geometric theory of hybrid systems", *Dyn. Contin. Discrete Impuls. Syst. Ser. B* 12(5–6), 649–687 (2005), Defs. 2.10 and 3.1. No DOI was found.
17. [V-meta] Ames, A. D., Zheng, H., Gregg, R. D., Sastry, S., "Is there life after Zeno? Taking executions past the breaking (Zeno) point", *Proc. 2006 American Control Conference*, doi:10.1109/ACC.2006.1656623. Abstract only.
