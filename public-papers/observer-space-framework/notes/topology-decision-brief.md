# What makes two observer states "close"? Decision brief for David

**Status:** decision brief, neutral. It makes no pick, has no lean and gives no recommendation; the call is David's. Written at main `f7acfac`; nothing in `versions/` or `papers/` is edited. Sources are cited by path; numbers are #299's pins (`notes/zeno-well-posedness.md`, `zwp.py` `1777f0be425d`), and nothing new is computed. Options are listed in the order the Physics Lead gave them; the order implies no ranking.

## 1. The question

David's (Z-ix) reading says an observer continues from a Zeno history's limit state *if that state exists* (relayed, not signed; `notes/zeno-mass-scoping.md`). "Limit" needs a notion of which observer states are close, that is, a topology on $V$. v0.9.1 names none, so (Z-ix) is not yet well-posed (#299; plan item 2). This brief sets out the options the record supports.

**Where it matters.** On the instance under the arrival rule (A) there are no Zeno histories (C7), so no option changes any instance figure. The question bites in the model without (a) and without (A) (C5's jump chains), and on singular endpoints such as C8.

**The example, used for every option.** A C5 jump chain at $c=0.1$, all at one value of $\tau$, jumping inward under the throat convention "continue through" (§7, C37). Near the throat its jumps cross back and forth between the two exteriors, and its radius settles on $r^*=2.00036101764$, the near-throat self-target: after 20,000 jumps it is within $2\times10^{-11}$ of $r^*$ in proper radial distance (#299 pin (2)). Each state is a regular turning-point germ with the same static-frame speed $v=0.3849$. Under "stop" the chain ends at the throat and is not a Zeno history at all, so the example exists only under "through".

## 2. The options

**(T0) No topology: Zeno histories end, as now** (§8.2 item 8, v0.9.1 as written).
- *Case.* No new structure. Item 8 is a stated clause; every Zeno-mass reading (Z-0)–(Z-viii) is defined without a topology.
- *Cost.* (Z-ix) stays ill-posed, so David's reading cannot act. The example ends even though its radius visibly converges to a regular germ.
- *Example.* The history ends at its accumulation; no limit is asked for.
- *Settles / leaves open.* Settles nothing; (Z-ix) reduces to its partner (Zeno note N-b). (Z-0)–(Z-viii), gauge, grain and F11 stay open. #292's D1/D2 count Zeno paths as ended, unchanged.

**(T1) The Fermi-slice topology** (`papers/obs-as-a-space.md`, Theorem 16): put each germ in Fermi coordinates along its $u$; two states are close when their coefficients are.
- *Case.* On record, Hausdorff (so limits are unique), already used to state four named extras (closed- and open-graph $R$, compact stars, Fermi distance). It makes (Z-ix) well-posed, and inside $r>2$ it agrees with the $(r,u^r,v)$ parameters the numerics use.
- *Cost.* Adopts structure the record named but did not adopt; Theorem 16 is stated for $\mathrm{Obs}$ and is read here on $V$ (#299). Two variants: *inverse-limit* (each coefficient converges), where a limit can be a formal jet that is not a germ at all (Prop. 14 there), so membership in $V$ is checked separately; and *inductive-limit* (convergence with a common radius), which keeps limits analytic but owes proofs, including the outward chain's flat limit (#299). N-a's other choices (reachability, uniqueness) and clause (2)'s reading stay owed.
- *Example.* Converges to the germ at $r^*$, a regular germ with future timelike $u$ (shown for the inverse-limit variant in #299; owed for the inductive-limit one). The topology is built on germs modulo pointed diffeomorphism, so it does not see which exterior a state is in.
- *Settles / leaves open.* "Exists" becomes defined; its partner still acts on histories with no limit (C8, most C5 chains), so (Z-0)–(Z-viii) all stay open. Gauge as a named home, grain (rounding is a grain, `papers/fermi-distance.md`) and F11 stay open. Under D1/D2, Zeno paths with a limit are continued, and chains sharing a limit merge, which #292 does not treat.

**(T2) A Fermi-slice distance** (`papers/fermi-distance.md`).
- *Accurately:* not a separate topology. The record builds it as a quotient metric from the inverse-limit topology and calls it "extra packaging of Theorem 16"; any metric generating that topology is "the same kind of scale". So it is a metrization of (T1)'s inverse-limit variant and has the same limits (#300 N1). The record gives no metric for the inductive-limit variant.
- *Case.* Everything in (T1)'s inverse-limit variant, plus a number for "how close", so limits can be stated as distances and rates.
- *Cost.* Adopts a specific metric on top of (T1); which compatible metric is a further choice that changes no limit. Theorem 24 there: it is a continuous scale and gives no slice, clock or generation.
- *Example.* As (T1), inverse-limit variant: converges to the germ at $r^*$, with distance going to 0.
- *Settles / leaves open.* As (T1); in addition it fixes nothing that (T1) leaves open.

**(T3) Germs identified across exteriors, or not** (#297, #299). This is not a topology but a choice of what the points are, and it applies on top of any notion above.
- *Case for identifying.* It is v0.9.1's stated identity: germs modulo pointed diffeomorphism (§4), and "'Which exterior' is not a property of the target" (§7). With it, the example has one limit.
- *Case for keeping the label.* It keeps a distinction a completed spacetime draws (regions I and III) and leaves gauge fully open. With it, the example alternates between two accumulation points and has no limit.
- *Cost.* Either way it touches the open gauge question (`papers/obs-as-a-space.md`: gauge as a named home stays open); keeping labels also needs a $V$ finer than §4's.
- *Settles / leaves open.* Decides whether "through" chains near the throat have limits; nothing else. C37's wording (plan item 12) is unaffected: the through-throat target exists by continuation, not by a limit (#297).

## 3. What is not being decided

Which Zeno reading (Z-0)–(Z-ix) to adopt; the throat convention; gauge as a named home; grain; F11; any law of $R$; (M1), which is ruled. Choosing (T1) or (T2) defines "exists" for (Z-ix); it does not adopt (Z-ix), and N-a's other choices stay open.

## 4. Where the record is unclear

1. Theorem 16 is stated for $\mathrm{Obs}$ (lumps); its slice carries $u$, and #299 reads it on $V$. The record has no separate statement for $V$.
2. Under the inverse-limit variant, the record does not say whether a limit that is not a convergent jet counts as "not existing" or as a state outside $V$.
3. The record does not say whether "exists" should require the limit to lie in the chain's continuation class (#299's second critic question).
