# Zeno well-posedness: does a Zeno history's limit state exist?

*Standalone note answering the Physics Lead's question on David's (Z-ix) reading (proposed by David, relayed by the Physics Lead, not signed; `notes/zeno-mass-scoping.md`), using #297's method. Written at main `af75d21`; v0.9.1 unedited. Bare § and C pointers are to v0.9.1. (M1) is ruled by David at L3 (relayed, not signed). Gauge, grain, F11, the throat convention and the Zeno pick stay open; this is a well-posedness finding only.*

**Verdict.** v0.9.1 names no topology on $V$, so "exists" is undefined there and (Z-ix) is not yet well-posed. The record holds one candidate: the Fermi-slice topology of `papers/obs-as-a-space.md` (Theorem 16), which is defined but not adopted.
Under it, C8 has no limit and the germless toys have nothing to ask about. C5's jump chains have a limit only when $r_n\to\infty$ (the flat germ) or when $r_n\to r^*$, the self-target radius ("through" only, and only with germs taken modulo "which exterior"). So no partner row (the Zeno note's N-b) becomes redundant.

## 1. Limit notions on record

| Notion | Where | Status |
|---|---|---|
| A topology on $V$ in v0.9.1 | none. §9's (J2) asks for "a named topology on curvelets"; the Zeno note's N-a and plan item 2 mark "exists" ILL | absent |
| Fermi-slice topology: presentations in Fermi coordinates along $u$, modulo $O(3)$; two variants, the inverse-limit topology (each $J^k$ coefficient converges) and the analytic inductive-limit topology | `papers/obs-as-a-space.md` Thm 16; used only to state extras in `closed-graph-r.md`, `open-graph-r.md` and `compact-stars.md` | on record and Hausdorff; not adopted, and not cited by v0.9.1 (that paper's "stateable, not written" refers to a neighbourhood-law for $R$, not to the topology). The theorem states it as a topology on $\mathrm{Obs}$, the set of lumps; its slice fixes $u$, so its points carry $u$, and this note reads it as a topology on $V$ |
| Inverse-limit analyticity along a curve | `papers/geodesic-lifts.md` Thm 3, cited by §5 for curvelets | on record and used; the same topology restricted to one curvelet, so it covers accumulation along a segment only |
| Chart $(r,u^r,v)$ on Schwarzschild $M=1$ germs | #290 A6 ("the germ is determined by $(r,u^r,v)$ up to isometry") | a parametrisation of one family, not a topology on $V$. Inside $r>2$ every Fermi coefficient is analytic in it, so the two agree there; they differ as $r\to\infty$ |
| Closed- or open-graph $R$, compact stars | the three notes above | conditions on $R$ in the Fermi-slice topology, named extras; they give no limit notion of their own |

A candidate metric is also on record (`papers/fermi-distance.md`: a quotient distance built on the inverse-limit variant, "extra packaging of Theorem 16", not adopted). The record calls it "a candidate" and does not prove that it generates the Fermi-slice topology (a standard fact if the slice metric is $O(3)$-invariant). That is owed, not proved; if it holds, the metric gives the same limits. Anything else (a metric generating another topology, a topology through which a limit may leave the slice) would be new.

## 2. Does the limit exist? The record's Zeno examples

- **C35, V0–V2.** These are trees labelled by $\tau$ only, with no germs. The question does not apply. The Zeno note's analogue (a limit state added at each accumulation point) is stipulated, not found.
- **C7.** On the instance under (A) the Zeno set is empty, so there is nothing to ask.
- **C8** (FLRW, $H=2+\sin(1/(1-t))$). The branch points accumulate at the segment endpoint $t=1$, where $K$ is unbounded. The order-2 Fermi coefficients (curvature) do not converge, so there is no limit under either Fermi variant or under Theorem 3. $t=1$ is not a point of the spacetime.
- **C5** (no arrival rule, model without (a); Zeno by §8.2 item 8 under Zeno FD1 option (i), a Lead ruling (2026-10-11, under David's delegation of 12:34 PM ET; relayed, not signed; `reviews/zeno-and-born-readiness-pressure-test.md` §3)). Every target is a turning point with the source's static-frame speed $v$ (#290 T1). So a chain is fixed by its radii, $u_n$ keeps $u^r=0$ and $v$, and no target is circular: an outward target never is, and an inward target would be only at $r=2+v^{-2}=8.75$, which the pinned chains miss by at least $0.0117$ (pin (0)). There are three cases:
  - **Any chain.** Each jump moves $\Delta\ell$ by $\varepsilon(r_n)\ge\varepsilon(2)>0$. So $r_n\to r^*\in(2,\infty)$ forces the late jumps to cross the throat, with $2\Delta\ell(r^*)=\varepsilon(r^*)$, which is #290 (T3)'s self-target. $r_n\to2$ is impossible (pin (4)). Every other chain either has $r_n\to\infty$ or has no limit.
  - **Outward** (C5's own chain, $10\to10.108\to10.217\to10.328$). $r_n\to\infty$, reaching $10^6$ within 180 jumps at $c=0.01$ and 24 at $c=0.1$ (pin (1)). In the chart there is no limit. In the inverse-limit Fermi topology every coefficient is $O(\gamma^2r^{-3-j})\to0$, so the chain converges to the flat germ. That germ is in $V$, with a future timelike $u$, but lies in a different continuation class. For the inductive-limit variant I have not proved that the radii of convergence stay bounded below.
  - **Inward.** Under "stop" the chain ends at the throat window (after 39 jumps at $c=0.1$, 410 at $c=0.01$) and is not Zeno. Under "through" it settles into alternating-side jumps around the near-throat self-target: $r^*=2.00036101764$ ($c=0.1$) and $2.00000360846$ ($c=0.01$), with multipliers $-0.99892$ and $-0.99999$ (the derivative at $\Delta\ell^*$ of the through map $\Delta\ell\mapsto\varepsilon(r)-\Delta\ell$), so it is attracting. At $c=0.1$, $\Delta\ell$ is within $2\times10^{-11}$ of its value at $r^*$ after 20,000 jumps; at $c=0.01$ convergence is slower and was not run to the end (pin (2)). The far self-target $r^*=2786.4692$ is repelling (multiplier $2.007$, pin (3)). The limit is a regular turning-point germ with a future timelike $u$, in the same class, but only modulo "which exterior". If germs keep the exterior label, the chain has two accumulation points and no limit. That is a gauge reading, not picked here.

## 3. What this leaves standing

- On v0.9.1 alone, (Z-ix) stays ILL. It becomes well-posed once a notion is named. The Fermi-slice topology is on record, but using it is a choice v0.9.1 does not make.
- Where a limit exists, the existing rule continues from it: no new rule at $T$, and $R$ and $A(O^u,a)$ are defined there (the Kretschmann rule gives no target at $K=0$, and no inward edge at a self-target, whose target is itself). Where a limit does not exist, no rule is needed at $T$.
- On every example above, histories with no limit remain (C8, most C5 chains, and the toys, where the question does not apply). So N-b's partner still acts, and none of (Z-0)–(Z-viii) becomes redundant. None is made ill-posed beyond what the Zeno note already records.
- C5's chains have mass 0, so no notion changes a weight under (Z-ii), (Z-iii), (Z-vi) or (Z-vii). On C5, (Z-ix) changes only which histories §8.2 item 8 ends. This rests on C5's mass being 0. Where the Zeno mass $z>0$, (Z-ix) can change weights: on C35 ($z=1/2$) the Zeno note's (Z-ix) row shows that a stipulated limit state moves them (to $1/2$, or to undefined, depending on how clause (2) is read). Clause (2) still fails on a continued history (Zeno note).
- Where the answer turns on the notion: outward chains (a flat limit in Fermi, none in the chart). Where it turns on gauge: inward "through" chains. N-a's uniqueness choice bites: all outward chains share one flat limit, and all inward "through" chains with the same $v$ share one $r^*$ germ, so continuation merges histories.

## Pins

`notes/zeno-well-posedness-scripts/`. Run with `sh run.sh` (Python 3.13.5, mpmath 1.3.0; `run.sh` calls `python`). The run is deterministic, with no seed and no $N$. `zwp.py` `1777f0be425d`, `run.sh` `36afcad10523`, `expected/zwp.txt` `2c5def6dcc2b`. The source is the $r=10$ periastron of $[10,20]$, $v=0.3849001795$. The outputs are the radii, jump counts, fixed points and multipliers quoted above.

## Critic questions

1. The Fermi-slice topology was built to state neighbourhood laws for $R$ and is not adopted. Is using it for "exists" a reading of the record, or new structure? Which variant?
2. Outward chains converge, in the Fermi topology, to a germ outside their continuation class. Should "exists" require the limit to lie in the chain's class? The chart notion does this implicitly.
