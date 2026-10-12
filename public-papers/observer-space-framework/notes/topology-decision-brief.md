# What makes two observer states "close"? Decision brief for David

**Status:** decision brief, neutral. It makes no pick, has no lean and gives no recommendation; the call is David's. Written at main `f7acfac`; nothing in `versions/` or `papers/` is edited. Bare § and C pointers are to v0.9.1. Sources are cited by path; numbers are #299's pins (`notes/zeno-well-posedness.md`, `zwp.py` `1777f0be425d`) and, for (T4), #305's (`notes/curvelet-induced-topology.md`, `cit.py` `a19b8a42d22a`); nothing new is computed here. Options are listed in the order the Physics Lead gave them, with (T4) added last; the order implies no ranking.

**Revised against main `76e9ace`:** (T4) added from #305.

## 1. The question

David's (Z-ix) reading says an observer continues from a Zeno history's limit state *if that state exists* (relayed, not signed; `notes/zeno-mass-scoping.md`). "Limit" needs a notion of which observer states are close, that is, a topology on $V$. v0.9.1 names none, so (Z-ix) is not yet well-posed (#299; plan item 2). This brief sets out the options the record supports. Two further courses are not listed. One is deferring the choice until (Z-ix) is adopted, which leaves "exists" undefined as (T0) does but does not rule a topology out. The other is any topology or metric not on record, which #299 §1 says "would be new". (T4), from #305, is new to the record but uses no new structure, so it is listed. The $(r,u^r,v)$ chart is a parametrisation of one family, not a topology on $V$ (#299).

**Where it matters.** On the instance under the arrival rule (A) there are no Zeno histories (C7), so no option changes any instance figure. The question bites in the model without (a) and without (A) (C5's jump chains), and on singular endpoints such as C8.

**The example, used for every option.** A C5 jump chain at $c=0.1$, all at one value of $\tau$, jumping inward under the throat convention "continue through" (§7, C37). Near the throat its jumps cross back and forth between the two exteriors, and its radius settles on $r^*=2.00036101764$, the near-throat self-target: after 20,000 jumps it is within $2\times10^{-11}$ of $r^*$ in proper radial distance (#299 pin (2)). Each state is a regular turning-point germ with the same static-frame speed $v=0.3849$. Under "stop" the chain ends at the throat and is not a Zeno history at all, so the example exists only under "through".

## 2. The options

**(T0) No topology: Zeno histories end, as now** (§8.2 item 8, v0.9.1 as written).
- *Case.* No new structure and no owed proofs. Item 8 is a stated clause; every Zeno-mass reading (Z-0)–(Z-viii) is defined without a topology, and v0.9.1 and #292 stand as written. Item 8's "ends there" stays unconditional. With no limit asked for, whether germs are identified across exteriors does not arise for Zeno histories, so no gauge reading is needed.
- *Cost.* (Z-ix) stays ill-posed, so David's reading cannot act. The example ends even though its radius converges ($r_n\to r^*$ in the $(r,u^r,v)$ parameters); whether the germs converge is what a topology would decide. Plan item 2's ILL flag on (Z-ix) stays, and every Zeno history, including any that a later topology would give a limit, takes its partner's value.
- *Example.* The history ends at its accumulation; no limit is asked for. Whether its late jumps cross the throat makes no difference, so (T3)'s question does not arise. C5's chains have mass 0 (#299), so under (Z-ii), (Z-iii), (Z-vi) and (Z-vii) no weight above it moves, as under every option (#299).
- *Settles / leaves open.* Settles nothing; (Z-ix) reduces to its partner (Zeno note N-b). (Z-0)–(Z-viii), gauge, grain and F11 stay open. #292's D1/D2 count Zeno paths as ended, unchanged. C37 and plan item 12 are unaffected, as under every option.

**(T1) The Fermi-slice topology** (`papers/obs-as-a-space.md`, Theorem 16): put each germ in Fermi coordinates along its $u$; two states are close when their coefficients are.
- *Case.* On record, Hausdorff (so limits are unique), already used to state four named extras (closed- and open-graph $R$, compact stars, Fermi distance). It makes (Z-ix) well-posed, and inside $r>2$ it agrees with the $(r,u^r,v)$ parameters the numerics use; the two differ as $r\to\infty$ (#299).
- *Cost.* Adopts structure the record named but did not adopt; Theorem 16 is stated for $\mathrm{Obs}$ and is read here on $V$ (#299). Two variants: *inverse-limit* (each coefficient converges), where the limit in the ambient jet space can be a formal jet that is not a germ (Prop. 14 there: analytic jets are not closed), so membership in $V$ is checked separately; and *inductive-limit* (convergence with a common radius), which keeps limits analytic but owes proofs, including the outward chain's flat limit (#299). N-a's other choices (reachability, uniqueness) and clause (2)'s reading stay owed.
- *Example.* Converges to the germ at $r^*$, a regular germ with future timelike $u$ (shown for the inverse-limit variant in #299; owed for the inductive-limit one). The topology is built on germs modulo pointed diffeomorphism, so it does not see which exterior a state is in.
- *Settles / leaves open.* "Exists" becomes defined; its partner still acts on histories with no limit (C8, most C5 chains), so (Z-0)–(Z-viii) all stay open. Gauge as a named home, grain (rounding is a grain, `papers/fermi-distance.md`) and F11 stay open. Under D1/D2, Zeno paths with a limit are continued, and chains sharing a limit merge, which #292 does not treat.

**(T2) A Fermi-slice distance** (`papers/fermi-distance.md`).
- *Accurately:* not a separate topology. The record builds it as a quotient metric from the inverse-limit topology and calls it "extra packaging of Theorem 16"; any metric generating that topology is "the same kind of scale". The record calls it "a candidate" and does not prove that it generates (T1)'s inverse-limit topology (a standard fact if the slice metric is $O(3)$-invariant). If it does, it is a metrization of that variant and has the same limits (#299 §1). The record gives no metric for the inductive-limit variant.
- *Case.* Everything in (T1)'s inverse-limit variant, plus a number for "how close", so limits can be stated as distances and rates.
- *Cost.* Adopts a specific metric on top of (T1); which compatible metric is a further choice that changes no limit. Theorem 24 there: it is a continuous scale and gives no slice, clock or generation.
- *Example.* As (T1), inverse-limit variant: converges to the germ at $r^*$, with distance going to 0.
- *Settles / leaves open.* As (T1); in addition it fixes nothing that (T1) leaves open.

**(T3) Germs identified across exteriors, or not** (#297, #299). This is not a topology but a choice of what the points are, and it applies on top of any topology in this list.
- *Case for identifying.* It is v0.9.1's stated identity: germs modulo pointed diffeomorphism (§4), and "'Which exterior' is not a property of the target" (§7). With it, the example has one limit.
- *Case for keeping the label.* It keeps a distinction a completed spacetime draws (regions I and III) and leaves gauge fully open. The record states this reading as a gauge option (#297 §3, row "Gauge: 'which exterior' kept"), and gauge as a named home is open (`papers/obs-as-a-space.md`). With it, the example alternates between two accumulation points and has no limit.
- *Cost.* Identifying merges two states that a completed spacetime separates (regions I and III); keeping labels needs a $V$ finer than §4's. Either way it touches the open gauge question (`papers/obs-as-a-space.md`: gauge as a named home stays open).
- *Settles / leaves open.* Decides whether "through" chains near the throat have limits; nothing else. C37's wording (plan item 12) is unaffected: the through-throat target exists by continuation, not by a limit (#297).

**(T4) The curvelet-induced topology, no new structure** (#305): the finest topology on $V$ in which every curvelet is continuous.
- *Case.* Built only from §5's curvelets and the results §5 cites, so it adds no structure. It is Hausdorff and metrizable, and it splits $V$ into clopen points, circles and open intervals, one per maximal curvelet. It makes (Z-ix) well-posed, and it makes §5's "discontinuous in oriented observer space" a theorem for every jump that is not a self-loop, as would any Hausdorff topology in which curvelets are continuous (#303, critic question 1).
- *Cost.* New to the record and not adopted; v0.9.1 does not write the statements it uses (#305 §1), and the exclusion of dense period groups is #305's own argument. Every jump that is not a self-loop is a discontinuity, and states on different curvelets are never close (#305 §§4–5). For Zeno limits on the recorded examples it acts as (T0) does: with finite stars (§9's default; #305's sketch fails with continuum stars), a Zeno history has a limit only if it ends by repeating one self-loop at a single $\tau$, and #305 shows no chain on record that does. It is finer than (T1)'s inverse-limit variant (#305 §5, taken there as immediate), so it gives no limit that variant lacks.
- *Example.* No limit, although its radius converges to $r^*$ (#299 pin (2)). Each state lies on a different curvelet (20,001 distinct values of the conserved angular momentum over 20,000 jumps, #305 pin (2)), and the germ at $r^*$ is in yet another component. This holds whether or not exteriors are identified, so (T3)'s question does not arise.
- *Settles / leaves open.* "Exists" becomes defined, but item 8's "ends there" stays unconditional except at self-loop tails. The partner still acts, so (Z-0)–(Z-viii) all stay open, as do gauge as a named home, grain and F11. #292's D1/D2 change only at self-loop tails.

## 3. What is not being decided

Which Zeno reading (Z-0)–(Z-ix) to adopt; the throat convention; gauge as a named home; grain; F11; any law of $R$; (M1), which David ruled at L3 on 2026-10-10 (relayed, not signed). Choosing (T1), (T2) or (T4) defines "exists" for (Z-ix); it does not adopt (Z-ix), and N-a's other choices stay open.

## 4. Where the record is unclear

1. Theorem 16 is stated for $\mathrm{Obs}$ (lumps); its slice carries $u$, and #299 reads it on $V$. The record has no separate statement for $V$.
2. Under the inverse-limit variant, the record does not say whether a limit that is not a convergent jet counts as "not existing" or as a state outside $V$.
3. The record does not say whether "exists" should require the limit to lie in the chain's continuation class (#299's second critic question).
4. (T4)'s exclusion of dense period groups is #305's own argument, not on record.
