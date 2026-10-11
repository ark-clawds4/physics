**SCOPING ONLY, NOT A CLAIM.**

# Born-rule readiness: is it too early to ask?

Authors: Geometry, co-written with Literature (the obstacles in §1 are Literature's, lightly edited)
Date: 2026-09-28
Question (David): "is it too early to ask whether the Born rule is on the horizon?" No paper or essay edits; no choice of (M1)/(M2) or T1/T2/T3; no law of $R$; nothing put in by hand ($|a|^2$ appears only as the literature's target); Paper 1's object untouched; type (ii) abandonable.

**Answer.** Too early for any claim; the right time to frame the question. The framework cannot yet state a Born question: it has no amplitudes to attach $|a|^2$ to, no law of $R$ to produce a tree, and no measurement model saying which arms are "the same outcome". But it can now say what would have to exist for outcome counting to give anything other than uniform branch counting, which orders the §9 open items (§3), and one cheap test can run now.

---

## 1. The conditions

### 1.1 Obstacles in the literature (co-written with Literature)

For each approach: (i) the premise that takes it from counting to $|a|^2$ weights, stated as a condition a branch measure $\mu$ would have to meet; (ii) the standard objection; (iii) a citation.

**1. Deutsch–Wallace decision theory.**
(i) Rational preferences over quantum bets that are indifferent to branching which leaves payoffs unchanged. As a condition, $\mu$ must be (a) invariant under unitary symmetries that swap equal-amplitude branches, and (b) unchanged when a branch splits into sub-branches with the same payoff (fine-graining invariance). Together with the other rationality axioms, these fix the weights at $|a|^2$.
(ii) Condition (b) excludes branch counting by assumption, since counting is exactly the rule that changes under splitting. The rival is ruled out by an axiom, not an argument (Dizadji-Bahmani 2015). Deutsch's original derivation was also charged with a hidden probabilistic assumption (Barnum et al. 2000).
(iii) Deutsch (1999).

**2. Zurek envariance.**
(i) If a swap of system outcomes can be undone by a counter-swap on the environment alone, those outcomes are equiprobable. Unequal (rational) amplitude ratios are fine-grained through an ancilla into equal-amplitude states, and their probabilities are summed. As a condition, $\mu$ depends only on the system's reduced state, gives envariantly swappable outcomes equal weight, and is additive under fine-graining (plus continuity for irrational ratios).
(ii) The circularity charge: the link from state to probability, additivity, and "equal amplitude" as the unit of fine-graining are unstated assumptions that already encode the amplitude measure (Schlosshauer and Fine 2005).
(iii) Zurek (2005).

**3. Saunders and Vaidman: branch counting versus self-location.**
(i) *Saunders:* decoherent histories are regrouped into equal-norm units, and probability is the ratio of unit counts. As a condition, $\mu$ is a ratio of counts of equal-norm units that depends on the state and is continuous in the norm topology. *Vaidman:* between decoherence and observation, an observer is uncertain which branch they are on, and credence follows each branch's postulated "measure of existence" (Vaidman 2012). *Sebens–Carroll* replace the postulate with the condition that credence depends only on the observer's local reduced state, not on changes confined to the environment (Sebens and Carroll 2018).
(ii) Question-begging: equal-norm units are in effect taken as equiprobable. Saunders raises this objection himself and replies to it (Saunders 2021, §8). On the self-location side, Vaidman's measure is postulated, so self-location explains what the probability *means*, not its values. Whether Sebens–Carroll's locality principle is independently motivated is disputed: Dawid and Friederich (2022) argue that Sebens and Carroll's ESP-QM is not a less general version of the plausible Epistemic Separability Principle and can be motivated only by quantum mechanics' empirical success, Born rule included, so it cannot serve as a premise for deriving the Born rule (see also Kent 2015, who questions whether self-locating uncertainty makes sense in the universal wave function).
(iii) Saunders (2021), §§7–8.

**4. The measure problem: counting versus weighting.**
(i) Counting needs a finite branch number for each outcome, fixed by the state, whose ratios survive refinement of the coarse-graining and change only when the amplitudes do. As a condition, a count-based $\mu$ needs a privileged grain, or a limit that does not depend on the grain.
(ii) The incoherence objection: decoherence is approximate, so there is no finest branching structure and no fact about how many branches there are. Counts also change under irrelevant further splitting, and with an infinite count the ratios depend on the regulator.
(iii) Wallace (2012), §5.8.1 ("Branch counting").

### 1.2 What each premise becomes in the framework

Objects: the tree of evolutions on $(V,R)$; branch points (decisions on the slice $V^\tau$ with $\mathrm{succ}_R\neq\emptyset$); states $(O^u,a)$ with arrival flag $a$; EPP1 = (M1), the named postulate giving each arm an equal share; (M2), Paper 1's count at a named cut; depth or proper-time cuts.

| Premise | Condition on the framework's objects | Statable now? | Extra structure needed |
|---|---|---|---|
| DW (a): swap symmetry | A lock-side automorphism of $(V,R)$ exchanging two arms forces equal weight | Automorphism, yes; "equal amplitude", **no**. EPP1 and (M2) already weight all arms equally, symmetric or not, so the premise is idle | An amplitude-like invariant on arms |
| DW (b): fine-graining invariance | A prefix's weight is unchanged by *later* splitting of a descendant, and by *same-vertex* splitting of an arm into two with the same outcome | Later splitting, yes: (M1) meets it, (M2) fails (P7). Same-vertex splitting needs an outcome labelling, which does not exist (v0.6 §6 is an informal picture, not ontology; matter open); given one, both fail (P7) | A measurement model; agents (the observer is a germ) |
| Zurek: envariance; reduced-state dependence | Weights depend only on $(O^u,a)$ and $R$; outcomes swappable by an "environment" operation get equal weight | Locality half, yes (Obs-local; EPP1 meets it). Swap half, **no**: no system ⊗ environment split, since the germ fixes a whole patch. A union of ensembles $E_W$ is a set, not a Hilbert space: no superposition, inner product or reduced state | A tensor-factorised state space: new theory, not a reading of the lock |
| Saunders: equal-norm units | (M2) counts evolutions at a cut, at the grain fixed by $R$ and the slice | Counting, yes; "equal norm", **no** | A norm on evolutions |
| Vaidman / Sebens–Carroll: self-location | The co-existence weight is the "measure of existence" slot | Slot, yes (EPP1 or (M2) fills it by postulate). Post-branching uncertainty, **no**: distinct arms are distinct germs, so the germ fixes its arm; an observer coarser than the germ breaks the lock | Nothing lock-compatible; the flag $a$ is the only non-germ datum |
| Measure problem: grain or grain-free limit | Branch points are discrete per history (hard gate); (M2) needs a named cut; counts → per-vertex weights iff siblings are asymptotically balanced (C15) | **Yes, fully**: the one premise statable now | none, to state it |

**Where $|a|^2$ would attach: nowhere, today.** Every computable weight is a combinatorial function of a tree (plus a cut for (M2)). No amplitudes, phases or interference exist, so histories never cancel. A hand-drawn tree matching $|a|^2$ is Paper 1's trivial scheme (v0.6 §8). Amplitude structure would be a new postulate; reverse-engineering the path integral is out of scope, as is the action-principle route hoped for in `old-manuscripts/2007-10-20-OutcomeCounting.pdf`.

**How (M1) and (M2) bear on a Born question (neither chosen).**
- **(M1)** *For:* indifferent to later splitting, a DW-type property (P7); state-local, like Sebens–Carroll; cut-free. *Costs:* every single-decision weight is an equal share, so non-uniform outcome weights can come only from tree shape, i.e. the law of $R$; a named postulate (note 9); one chosen product measure on a continuum (C16, P6); in the countable (a) case, weights $2^{-k}$ meet Paper 1 §6's refusal case (C33).
- **(M2)** *For:* literally branch counting, Saunders's slot; carries Paper 1's uniqueness thesis at the cut. *Costs:* fails fine-graining invariance (P7; SHPMP's cut objection); needs a cut on infinite sets, and under (a) no uniform countably additive measure exists; the MERW hazard (path counting yields a squared-eigenvector density a referee may read as Born: a hazard, not a route; C36); a named cut (note 9).

---

## 2. Do the existing toys lean either way?

No. None has amplitudes or interference, so none bears on Born; they bear on counting versus weighting and on countability.

- **V\*/Option F (continuum result).** Under the public ensemble, extend-vs-not marks a continuum of vertex times (Minkowski minus a point: lifetimes fill $(0,\infty)$, C24). *Shows:* without a lock-side slice there is no grain, so neither counting nor EPP1 is defined (premise 4 failing at its root). *Does not show:* anything about weights. *Pin:* analytic; nothing to re-run.
- **$|B|\ge2$ toy** (`papers/B-ge2-minimal-toy.md`, retired to a digraph fact). *Shows:* its two arms (Minkowski continuation; type-(ii) jump to a dust FLRW germ) differ in lock-side invariants ($K=0$ vs $80/27$, P8), so no germ symmetry swaps them, yet EPP1 would weight them equally: the equality is postulated, and envariance has nothing to act on. The arm count itself depends on the isotropy quotient (3 vs 2, C9, P9). *Does not show:* any weight; none is assigned.
- **20-decision bound computation** (Kretschmann rule as stated, unadopted, without (a)). *Shows:* with $m=2$ jump arms per bound decision the jump share is $2/3$ in expectation (0.6672); at $c=0.1$, 6.58% remain bound after 20 decisions and leavers leave after 5.90 decisions on average; at $c=0.01$, 99.94% (P1, P2). These are branch-count consequences of a regular 3-star, and they move with the rule's constant $c$, not with anything amplitude-like. *Does not show:* Born; it shows jump dominance, which blocks stable records before any Born comparison.
- **(a)-transient.** *Shows:* $m\le1$, so the jump share is 1/2 while branching lasts (0.5015, 0.4999); one jump at $c=0.1$; 12–14 jumps (exact EPP1 law, #169), chain ≤14, 29,119 orbits and 14,478 stuck at $c=0.01$ (P3–P5); completed histories countable. This bears on the measure: (M1) gives unequal weights $2^{-k}$; (M2) has no uniform countably additive measure. *Does not show:* anything about $|a|^2$.

### Pins (all re-run for this note, 2026-09-28)

Python 3.13.5, numpy 2.5.3, scipy 1.18.1, sympy 1.14.0 (venv `/workspace/g128/venv`). Units $G=c=1$, $M=1$. The orbit is $[10,20]$, with $E=0.969087$ and $L=4.170288$. The library is `/workspace/g154/kr.py` with `THROAT='cross'`. As in #155 and #157, scripts stay on the shared machine (the repo holds no scripts); SHA-256 prefixes below.

| Pin | Script and arguments | Seed | Output (confirmed) |
|---|---|---|---|
| P1 | `g154/sim.py 0.1 stated 200000 20 7 cross` | 7 | jump share 0.6672; bound after 20 decisions 0.0658 (SE 0.0006); leavers' mean 5.902 decisions |
| P2 | `g154/sim.py 0.01 stated 20000 20 3 cross` | 3 | jump share 0.6669; bound 0.9994 (SE 0.0002) |
| P3 | `g154/agraph.py 0.1` | none (exact) | 3 reachable orbits; 0 turning points with 2 admissible edges; longest chain 1 |
| P4 | `g154/agraph.py 0.01` | none (exact) | 29,119 orbits; 0 turning points with 2 edges; 14,478 stuck (#169; the script's 14,477 is a classifier rounding artefact); longest chain 14 |
| P5 | `g154/along.py` ($N=20{,}000$ each) | 5 | $c=0.1$: 1 jump in all histories, share 0.5015; $c=0.01$: 13 jumps (3,169) or 14 (16,831), share 0.4999 |
| P6 | `g154/c16.py` | none (exact) | $a=9.892616$, $b=10.107529$; min derivative 1.098432; image inside $[a,b]$: True |
| P7 | `born/pins/fg.py` | none (exact) | $w(A)$: base (M1) 1/2, (M2) 1/2; later split (M1) 1/2, (M2) 1/3; same-vertex split (M1) 1/3, (M2) 1/3 |
| P8 | `born/pins/flrw_k.py` | none (symbolic) | $K_{\rm FLRW}(0)=80/27\approx2.963$; $K_{\rm Mink}=0$ |
| P9 | `g128/misc.py` (item 3) | fixed | $\lvert B\rvert=3$ unquotiented, 2 modulo isotropy; $\dim H^3=3$ |

SHA-256 prefixes: kr `0432cc20`, sim `df306f17`, agraph `edf42d6e`, along `750def92`, c16 `dd6f6a0b`, misc (g128) `f131b3de`, fg `c83641c9`, flrw_k `3ee6f263`. New scripts: `fg.py` computes $w(A)$ under (M1) (product of $1/\deg$ over ancestors) and (M2) (fraction of depth-2 leaves) on three trees: base $\{A\to A_1, B\to B_1\}$; later split $B\to\{B_1,B_2\}$; same-vertex split adding $B'\to B'_1$ at the root. `flrw_k.py` evaluates $K=12[(\ddot a/a)^2+(\dot a/a)^4]$ for $a=(1-t)^{2/3}$ at $t=0$ in sympy.

---

## 3. What would settle it, in what order, and one cheap test

**Gating order** (§9 open items; each is needed before the next means anything):

0. **Keeping type (ii).** Abandoned, $|B|=1$ (CWS singleton): no weights to ask about.
1. **Law of $R$ and the slice**, with motivation among admissible pairs (else Bertrand). No tree without them.
2. **Jump dominance, (J1) or (J2).** Failing both gives jump-dominated histories (P1) and no stable records.
3. **(a) versus (b), and arrival semantics (T1).** Countable versus continuum histories; where EPP1 applies.
4. **The measure (M1)/(M2)**, with completed-vs-cut, the Zeno-mass convention and the weight's reading: per-vertex shares or counts.
5. **A measurement model, including matter.** Without "same outcome", neither DW (b) nor any frequency comparison is statable.
6. **Amplitude-like structure**: whether some germ or $R$ invariant plays the literature's $|a|^2$ role (the Hope "weights forced"). Born enters only here.

The measure-problem premise can be worked on now; everything else waits on gates 1–5.

**One cheap next test: continuous response.**
- *Question:* can a uniform, local, no-case-list rule make an outcome's weight depend on a continuous germ parameter while every single-decision branch count is identical?
- *Setup:* the worked Kretschmann rule as stated (unadopted), $c=0.1$, `kr.py` with `THROAT='cross'`; bound orbits with apastron 20 and periastron $r_p\in\{9.00,9.01,\dots,11.00\}$ (201 germs), starting at periastron. Outcome fixed in advance: $X_n$ = "still bound after $n$ decisions", $n=1,\dots,10$.
- *Computation:* exact enumeration memoised on the orbit $(r_{\min},r_{\max})$, at most $3^{10}$ paths, no sampling. $w_n^{M1}(r_p)$ = EPP1 weight of the bound depth-$n$ paths; $w_n^{M2}(r_p)$ = bound fraction of the depth-$n$ cut, dead ends kept (v0.6 §7). Depth counts decisions (jump-reached states do not branch under (A)); log $|A|$ at every decision to confirm it is 3.
- *PASS:* for some $n\le10$, $w_n^{M1}$ or $w_n^{M2}$ takes at least two values across the grid, with $|A|=3$ at every bound decision. *FAIL:* both constant in $r_p$ for all $n\le10$ (or $|A|\ne3$ somewhere, which voids the test).
- *PASS would show* that weights are counting at a grain set by $R$ and that a germ parameter can enter through tree shape alone. It would **not** show Born, $|a|^2$ or interference: the rule is unmotivated, the outcome is a picture, and at finite $n$ every $w_n^{M1}\in3^{-n}\mathbb Z$, so continuous response exists only as a limit (premise 4's grain problem, concretely). Whether (M1) and (M2) respond differently is a readout, not a choice.
- *FAIL would show* that on this instance weights are blind to the germ within the family, so Born-type state dependence would need an $R$ whose tree shape varies with the germ; it says nothing about other rules.
- *Cost:* one script, minutes; no postulate, no law of $R$. Not run for this note.

---

## References

- Barnum, H., Caves, C. M., Finkelstein, J., Fuchs, C. A., and Schack, R. (2000). Quantum probability from decision theory? *Proc. R. Soc. Lond. A* 456, 1175–1182.
- Dawid, R., and Friederich, S. (2022). Epistemic separability and Everettian branches: a critique of Sebens and Carroll. *Brit. J. Phil. Sci.* 73(3), 711–721. doi:10.1093/bjps/axaa002.
- Deutsch, D. (1999). Quantum theory of probability and decisions. *Proc. R. Soc. Lond. A* 455, 3129–3137.
- Dizadji-Bahmani, F. (2015). The probability problem in Everettian quantum mechanics persists. *Brit. J. Phil. Sci.* 66(2), 257–283.
- Kent, A. (2015). Does it make sense to speak of self-locating uncertainty in the universal wave function? Remarks on Sebens and Carroll. *Found. Phys.* 45(2), 211–217. doi:10.1007/s10701-014-9862-5.
- Saunders, S. (2021). Branch-counting in the Everett interpretation of quantum mechanics. *Proc. R. Soc. A* 477, 20210600.
- Schlosshauer, M., and Fine, A. (2005). On Zurek's derivation of the Born rule. *Found. Phys.* 35, 197–213.
- Sebens, C. T., and Carroll, S. M. (2018). Self-locating uncertainty and the origin of probability in Everettian quantum mechanics. *Brit. J. Phil. Sci.* 69(1), 25–74.
- Vaidman, L. (2012). Probability in the many-worlds interpretation of quantum mechanics. In Y. Ben-Menahem and M. Hemmo (eds.), *Probability in Physics*, Springer, 299–311.
- Wallace, D. (2012). *The Emergent Multiverse*. Oxford University Press, §5.8.1.
- Zurek, W. H. (2005). Probabilities from entanglement, Born's rule $p_k=|\psi_k|^2$ from envariance. *Phys. Rev. A* 71, 052105.
- Framework: `versions/v0.6-prose.md` §§7–9, App. A (C9, C15, C16, C24); `versions/v0.7-outline.md` App. A (C33, C36); `papers/B-ge2-minimal-toy.md`; `papers/Vstar-extend-vs-not.md`.

---

## v0.9 refresh (2026-10-10)

**See also (2026-10-10):** `../notes/born-litmus-test.md` records David's open question on how to tell whether the Born rule genuinely emerges rather than being written in by hand, with his L3 working answer (litmus tests LT1–LT4).

**Read at:** main `b327a7b`, `versions/v0.9-prose.md` (current) and `notes/zeno-mass-scoping.md` as merged with #245's strings 1–4. **Scope:** the old map above is re-mapped against v0.9. One line above this section changed in the same merge: l.46's "(§6 is a cartoon; matter open)" became "(v0.6 §6 is an informal picture, not ontology; matter open)" (#247's F-string A). Nothing else above is edited. Every C-row figure quoted here was checked against v0.9's Appendix A by script (`brr_check.py`, Pins). No pin was in doubt, so nothing was recomputed. **Revised** against main `56ad9b7` with the items of #258 confirmed or qualified in `zeno-and-born-readiness-pressure-test.md`; figures the revision adds are recomputed or checked there. **Revised** against main `2d2e4be` for (M1) ruled by David at L3 (relayed, not signed; v0.9.1 §11, #269/#272): gap 4's Open, Waits on and Cost cells only.

### Gaps before a Born-type question can be posed

The gaps follow the old gating order (§3 above, gates 0–6). The order is not strict. Gap 4's §9 proofs (C13, C15, C36) need no $R$. Gaps 3 and 4 depend on each other: C5's per-history failure leaves a model with no arrival rule without an EPP1 domain under (Z-0)/(Z-i), but not under (Z-ii), (Z-iii), (Z-vi) or (Z-vii), where C5's chains are a Zeno set of mass $0$; and C33's countability changes the costs of (M1) and (M2). Gap 2's figures are EPP1 quantities (C17, C34). "Waits on" lists the named open calls and, for gap 4, the Zeno-mass options of `notes/zeno-mass-scoping.md`, which are a note's options, not calls ((Z-0) and (Z-iv)–(Z-viii) are not in v0.9). Whether they stay listed here is left to David (#259 pressure test, FD2).

| Gap | Settled in v0.9 (row, pin) | Open (v0.9 pointer) | Waits on | Cost |
|---|---|---|---|---|
| 0. Keep type (ii) | CWS singleton, one curvelet class (C28, §8.1) | $R\ne\emptyset$, a working Postulate (§8.2, Option E residue; §11) | "Without being fully deterministic" (existence/permission); T3 | Abandoning it gives $\lvert B\rvert=1$ and no weights. Keeping it rests on a postulate that cannot be derived |
| 1. Law of $R$, slice, motivation | $R\subseteq V^\tau\times V$, a declared constraint on sources with named-extra status (§8.2 item 1); the slice is blind on Minkowski/dS/ESU for every lock-side scalar (C19), and on flat ΛCDM for $K$, $g^{ab}R_{ab}$ and $R_{ab}R^{ab}$ (C18); there the choice of scalar matters (C23); no-Zeno is a named clause (C8); the worked rule is stated and uniform but unmotivated (C26) | §8.2 item 1 constrains only $R$'s sources. The §8.4 motivation clause is unmet (Bertrand over (slice, rule) pairs). Hard-gate clause (1): a law must give finite stars, or countable ones with a named exhaustion (§8.3; §9 *Exhaustion*; §11); lock-side candidates give trivial maps or a continuum of successors (§8.5), and (a) selects no countable star (§8.2, C4) | T3 / #139 (a) | A law, plus a motivation within an independently named class; the slice scalar is a second free choice |
| 2. Jump dominance | The stated rule fails (J1) and (J2): pure-geodesic weight $3^{-10}=1.69\times10^{-5}$ (C17); jump share 0.6672, 0.0658 still bound (C34). The (a)-restriction meets late-window (J1) and fails (J2) (C33, §9) | No §8 item; (J1)/(J2) is a §9 constraint, and §11 asks whether any $R$ meets them | T3 / #139 (a) | (J2) needs a named topology on curvelets; (J1) is window-dependent |
| 3. Realisation (a)/(b); arrival | Without an arrival rule clause (2) fails per history (C5); whether that leaves EPP1 without a domain depends on the Zeno-mass convention (gap 4). Under (A) the process is Markov only on $(O^u,a)$ (C6). (a) is lock-side (C30). For the worked rule on the instance, completed histories are countable under its (a)-restriction (C33: 29,119 orbits, 14,478 stuck) and a continuum in the model without (a) (C16); (a) itself selects no countable star (§8.2, C4). Under (a) the throat thresholds are not reached; without (a) the rule needs a throat convention (C37) | §8.2 item 7, (A), a working Postulate; (a) versus (b) (§8.2, §8.4) | T1; F7 ((B) scope; labelling of (A)); F11 (the #203 lemma would make C33's $m\le1$ a theorem and adds a physics claim about the unadopted example); #139 (a) for the proper-time part | T1's enlarged state, or a replacement for (A); under the worked rule's (a)-restriction, branching on the instance is transient (C33), which v0.9 keeps apart from (a) in general (§2) |
| 4. Measure | Unequal per-vertex weights (C12: $1/6$, $1/2$ against counts $1/4$). Proofs in §9: cut criterion (C13), limit iff (C15), MERW iff (C36). Proper-time cuts can disagree (C14: $2/3$ against $1/2$). Finite cuts on the instance (C29; C7: $111.59$). Zeno toy (C35: mass $1/2$). Exact law of the worked rule's (a)-restriction on the instance at $c=0.01$: $26/3^{12}$, $9338/3^{10}$, $447373/3^{12}$, 27.68 decisions (C33) | §8.3 Zeno-mass convention (which includes clause (2)'s range, before or after item 8's excision, and, after it, whether the excised mass is kept or conditioned away; options in `notes/zeno-mass-scoping.md`); (M1)/(M2), ruled (M1) at L3 (relayed, not signed; #269/#272); completed versus cut, which agree under (M1) where no Zeno history passes (finite stars, dead ends kept in the cut; its cut weights are then the marginals of its measure on completed histories, §9); where one does, agreement turns on the Zeno-mass convention (under (Z-ii) they agree; under (Z-iii) the conditioned measure gives $X$ $1$ against the cut's $1/2$, C35; under (Z-i) neither is defined), while whether finite graph paths are Paper 1's countable evolutions stays open; and the reading of the weight (§11) | (M1)/(M2): ruled (M1) at L3 (relayed, not signed; #269/#272); T2 and #139 (b): the ruling selects T2's per-step side, and whether T2 and #139 (b) are closed stays open; F9, F10; F5 (MERW-hazard wording); F6 (who is credited for §11's (M2) cut objection, Wallace 2007 or SHPMP 2008); (Z-0)–(Z-viii) (under the ruling, counting (Z-iv) is dropped and (Z-iii)/(Z-vii) are narrowed, `notes/zeno-mass-scoping.md`) | As in §11's symmetric cost lines (kept under the ruling as the record of the trade), plus the note's (d) cost for each reading: (Z-0)/(Z-i) need a per-state no-Zeno proof (C7 supplies it on the instance), and one measure-zero Zeno history leaves weights undefined; (Z-ii) needs an existence citation (already referenced) and a scoped item 8, and clause (2) and item 8 then change no weight; (Z-iii) needs the tail mass $z$, an infinite-horizon quantity that may lack a closed form, is undefined at $z=1$, reads $R$ ahead, and gives the arms at one vertex unequal weights; counting (Z-iv) (dropped under the (M1) ruling; kept as a record) needs a cut family and a proof that the limit exists, and can fail to converge; (Z-v) needs one lemma, and stating it fixes a value once the weight type is fixed, which is a choice in itself; (Z-vi) needs (Z-ii)'s existence citation and is defined only where $z=0$; (Z-vii) reads $R$ to infinite depth, changes the arm set in force, is undefined where no non-Zeno history passes, and does not in general remove the Zeno mass; (Z-viii) needs no lemma, and stating it is a choice in itself that fixes no single value |
| 5. Measurement model, matter | No measurement model. §4 "Measurement, informally (not ontology)": no picture is used, and matter is open. One named constraint bears on any later model: under the example slice, a freely falling near-flat laboratory in a Schwarzschild exterior has its $K$-vertices exactly at its radial turning points, so its branch opportunities are fixed by its own free fall, not by anything an experiment does; a supported laboratory lies outside the model while matter is open (§6.1, C38) | No §8 item; §4, §11 (matter). Coupled to the mapping choice inside §11's "Which Bell premise" call ("if co-existing arms count as outcomes"), and to (a) versus (b): (a) forbids the cross-continuation jumps, "the ones a measurement picture would want" (§8.2) | No listed call | An outcome labelling ("same outcome") and matter fields, beyond the lock; for any frequency comparison, also a stated link from weights to frequencies (§8.4 lists "a typicality rule", with "a law of $R$" and "work on circularity", for its later bar) |
| 6. Amplitude-like structure | None. The circularity wall (§10, Paper 1 §8 verbatim). The MERW hazard is a hazard, not a route (C36) | No §8 item; §11 Hope "weights forced"; §8.4's later bar | #139 (e); F5 | A new postulate; a tree drawn by hand to fit a target weight is Paper 1's trivial scheme |

**Premise status since the old map (§1.2).**
- **The measure-problem premise** is now backed by §9 proofs: the cut criterion, the limit iff and the MERW iff.
- **The cheap test of §3** has been run (stale item 7). On that instance (unadopted rule, $c=0.1$, one orbit family) a germ parameter enters the weights through tree shape alone ($|A|=3$ at every decision; only the kinds of jump targets change), as step functions at finite $n$ (scan §5). That weights can depend on nothing but the tree is §1.2's structural point, not a scan result. No continuous limit is shown.
- **The DW, Zurek, Saunders and Vaidman rows are unchanged in status,** with three notes. The DW (a) row's "EPP1 and (M2) already weight all arms equally" is wrong for (M2), which weights the evolutions at its cut equally, not the arms (C12's depth-2 count gives arm $A$ $3/4$ and arm $B$ $1/4$); arms swapped by an automorphism still get equal counts at any cut the automorphism preserves, so "idle" needs rewording, not reversal. The Zurek row's locality half is met as Obs-locality on $(O^u,a)$; v0.9 §10 adds that the flag is not lock-side, that it bears only on whether EPP1 applies, not on the weights it gives, and that how to resolve this is open call T1. The Zurek row's $E_W$ is v0.9's $E_{\mathcal W}$ (#229 N22).

### Stale in the old map (line numbers at `b327a7b`; listed, not edited)

1. **l.9, l.91:** "§9 open items" is now v0.9 §11.
2. **l.41:** "branch points (decisions on the slice $V^\tau$ with $\mathrm{succ}_R\neq\emptyset$)". v0.9 §8.3 defines a branch point as a state $(O^u,a)$ with $\lvert A(O^u,a)\rvert\ge2$, so jump-reached states are not branch points (§8.2 item 7).
3. **l.46** (DW (b) row): "§6" means v0.6 §6, now v0.9 §4 "Measurement, informally (not ontology)". At `b327a7b` the row also used a word on Literature's forbidden list; #246's merge replaced it, and the row now says "v0.6 §6" itself, so only the pointer to v0.9 §4 remains live.
4. **l.52:** "(v0.6 §8)" is now v0.9 §10.
5. **l.78 (P4):** the row names `g154/agraph.py 0.01`, which prints 14,477 stuck under `kr.classify` (the row itself flags this as a classifier artefact). The pinned 14,478 is the corrected-classifier figure (`g168/c33r.py`, `f9e9c31b`; #169, #173), which C33 now pins. Both scripts give 29,119 orbits. The pin row names only the uncorrected script.
6. **l.106:** "dead ends kept (v0.6 §7)" is now v0.9 §9 *Dead ends*.
7. **l.110:** "Not run for this note" no longer holds. The test ran in `born-rule-readiness-scan.md` (#165): PASS, first at $n=4$.
   - #174's hardened classifier relabelled 77 of 1,505,887 targets and changed values at 31 germs for $n\ge6$ only. $n\le5$ is unchanged, so the read stands.
8. **l.127:** the v0.6-prose §§7–9 pointers are now v0.9 §§9–11, and the v0.6-prose / v0.7-outline App. A pointers are now v0.9 App. A. The numbers carry over. C9, C24 and C33 keep their claims (C33's stuck count is item 5). Three claims changed: C15 (v0.6's "cofinal constancy sufficient" is now constancy of $D$ at every depth from some depth on, #229 R3), C16 (v0.6's "numerical evidence, not a proof" is now a proof) and C36 (v0.7-outline's "only in the long-path limit" is now "in general only", #229 R2).
9. **Gate 4 (l.97):** "the Zeno-mass convention" now has the options (Z-0)–(Z-viii) of `notes/zeno-mass-scoping.md`. The same item's "the weight's reading: per-vertex shares or counts" can be read as restating (M1)/(M2); in v0.9 §§9, 11 (as in v0.6 §9) the reading of the weight is co-existence (working Postulate, revisable) versus chance (defined), the sense gap 4 uses.
10. **Unchanged and consistent with v0.9:** P1, P2 (C34); P5 (C33); P6 (C16, where $1.098432$ appears as $1.0984$); P9 (C9: 3 unquotiented, 2 modulo isotropy). P3's "longest chain 1" at $c=0.1$ is C33's "no post-jump orbit has an (a)-admissible edge: one jump a.s."; P3's orbit count (3), P7 and P8 have no v0.9 row.

11. **l.56, l.67:** "(M2) ... under (a) no uniform countably additive measure exists" and "(M2) has no uniform countably additive measure" keep the wording that #229 R1 corrected. Counting measure is uniform and countably additive; what fails, in v0.9 §11's words after Paper 1 §6, is that "a countably infinite set carries no countably additive probability measure that gives each point the same positive weight". "Under (a)" is also C33's (a)-restriction on the instance.
12. **l.66, l.67:** "the jump share is $2/3$ in expectation" and "the jump share is 1/2 while branching lasts" are v0.7 wording. v0.9 states $2/3$ and $1/2$ as ratios of expectations (Wald's identity), gives 0.6672, 0.5015 and 0.4999 as pooled shares, and says a single history's jump share differs (§9, C33, C34).

### Critic questions

1. The order is not strict: gaps 3 and 4 form a cycle through C5 and the Zeno convention, and through C33's countability. Should they be stated as one gap, or kept apart with the coupling named?
2. Countability (C33) sharpens a cost of (M1) and leaves (M2)'s cut cost in place (§11). Does it move any old-map premise from "not statable" to "statable"?
3. Are gaps 5 and 6 independent, or does any outcome labelling already presuppose amplitude-like structure?
4. After the scoping of C18, C33, C16 and C5 here, is any C-row cited (e.g. C29, C7, C38) still used beyond its instance?
5. The #174 relabelling (71 of 77 targets at $r>10^4$) had no 60-digit parent-state recomputation. Does that leave the $n\ge6$ scan values at the 31 changed germs resting on the hardened classifier alone?

### Pins

`/workspace/g246/brr_check.py` (SHA-256 `e95ac2a63fadaaa7378d1a909cadc4cde5e3a0620477661531369a82c30773d1`) checks every C-row figure quoted above against `versions/v0.9-prose.md` at `b327a7b`. It also checks the old map's line pointers. The revision's added figures are checked by the scripts pinned in `zeno-and-born-readiness-pressure-test.md` (`numcheck.py`).
