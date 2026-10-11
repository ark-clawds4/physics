# Completed histories versus Paper 1's evolutions

*Standalone note on v0.10 plan item 3 (#285), at main `5e05692`; v0.9.1 unedited. (M1) is cited as ruled at L3; the Zeno readings, throat convention, F11, gauge and grain stay open and unpicked.*

v0.9.1 §12 reads C16 and C33 as facts about Paper 1's evolutions, but Paper 1 §4 states identity for curves parametrised by proper time, and histories are segments joined by jumps that carry no $\tau$ (§8.2 item 2): the plan's ILL flag. Paper 1 defines no $\sim$-equivalence (the symbol appears, for curves, in `papers/analytic-split.md`). So the criterion comes first.

## 1. Two definitions

A *completed history* is a maximal path from the root (§9). A path that item 8 ends at a Zeno accumulation is one too.

**D1 (trace).** $x_h(\tau)$ is the oriented germ that $h$ occupies at accumulated proper time $\tau$, on $[0,T_h)$. The trace is two-valued at a jump; here it is taken right-continuous. $h\approx_1h'$ iff $x_h=x_{h'}$ on the common domain.

- *Grounds:* Paper 1 §4 ("the same until the simply-connected analytic patches disagree", not reopened); the jet–patch lock (Paper 1 §2; `papers/analytic-patch-from-jet.md`, Theorems A–B), so patches disagree iff germs do; $u$ as Paper 1's time direction (v0.9.1 §4); §6.2 (ending and continuing are one evolution, encoded by "common domain"); $E(O)$ not folded into $\sim$, so worlds make no evolutions.
- *Cost:* "curve" is extended to a trace with jumps that carry no $\tau$.

**D2 (decision path).** $h\approx_2h'$ iff they take the same arm at every decision, that is, §8.2 item 5 applied along the history. Completed histories are then the maximal paths of the decision tree, where the (M1) path measure lives (§9).

- *Grounds:* §8.2 items 5–7 and C11; delayed forks (`papers/type-ii-adopted.md`, Definition 8 and Proposition 12).

## 2. How they relate

**Proposition.** Suppose $h$ and $h'$ first differ at a decision $(O^u,\mathrm{seg})$ at time $\tau_0$. Then their traces split at $\tau_0$, unless one arm continues and the other is a self-loop $(O^u,O^u)\in R$. Hence D2-classes map onto D1-classes, one-to-one iff no reachable decision carries a self-loop.

Three cases:

1. **Under (a), for every $R$.** (a) excludes $\{\gamma_{O^u}(\tau):\tau\ge0\}\ni O^u$.
2. **At recurrent germs.** If $\gamma_{O^u}$ returns to $O^u$ at some $\tau>0$ (successive periastra, §8.2), then $(O^u,O^u)$ is a type-(i) pair, and §8.2 item 3 removes it. This reads a type-(i) pair as any $(O^u,\gamma_{O^u}(\tau))$ with $\tau>0$.
3. **Otherwise.** Irreflexivity of $R$ is needed, which is a named extra and not adopted (`papers/irreflexive-r.md`).

The jump convention is immaterial: curvelets agreeing on $(0,\delta)$ agree at $0$ (Theorem 2 of `papers/analytic-split.md`).

**Kretschmann rule.** A target is the source germ iff $r'=r_0$. A direct path never gives this. Under "continue through", a through-throat path gives it only at apastra with $\varepsilon=2\Delta\ell$ (#290 (T3); $r_0=2786.4692$ at $c=0.1$). A decision there is reached along a segment, so it sits on a bound orbit (a plunging orbit's apastron is reached only by the jump that lands on it). The germ is therefore recurrent, and case 2 applies. **So D1 and D2 coincide on the Kretschmann rule**, with or without (a), under either throat convention.

## 3. What each makes true or false

| Claim | D1 | D2 |
|---|---|---|
| Completed histories are one-to-one with evolutions | True iff no reachable self-loop (cases 1–3); otherwise many-to-one | True by construction |
| C16 (a continuum without (a)) | True: its arms are continue or an edge to $f(r)\neq r$ | True |
| C33 (countable under (a)) | True | True |
| Paper 1 §5's antecedent on the instance | Fails without (a), holds under (a) | Same |
| (M1) weight of an evolution | The sum over its D2-classes; it differs from the path weight only at surviving self-loops | The path weight |
| Toys with no germs (C35, V0–V2) | Undefined | Defined |

D1 is a quotient of D2: D2 countable implies D1 countable, not conversely.

**Zeno histories (no reading picked).** A Zeno history is one completed history, ended by item 8. Distinct ones differ at some decision, so both definitions separate them where germs exist.

- **Mass only:** (Z-0)/(Z-i), (Z-ii), (Z-iii), per-vertex (Z-iv), (Z-v), (Z-vi) and (Z-viii). These change neither identity nor countability.
- **(Z-vii)** prunes arms that carry only Zeno histories. On C35 the uncountably many D2 Zeno histories below $Y$ shrink to $\{X\}$, so countability can depend on the reading where $z>0$.
- **(Z-ix)** continues a history where a limit state $T$ exists.
  - Under D1 the trace runs past $T$, and by §6.2 the ended and continued forms are one evolution.
  - Under D2, "maximal path" would need more than $\omega$ decisions. This is routed around by indexing the continued history as a pair: the $\omega$-path to $T$, then a path from $T$.
  - Histories with no limit take the partner row.
- **The instance has no Zeno histories (C7).**

## 4. Options and costs (no pick)

- **D1.**
  - *For:* it is Paper 1's own premise; it is blind to the world and to the arrival flag, as Paper 1's object is; it handles (Z-ix) natively.
  - *Cost:* the extended "curve"; per-evolution (M1) sums and toys (table); case 3 needs a named extra.
- **D2.**
  - *For:* (M1), C11, C16 and C33 already use it, and it is defined on toys.
  - *Cost:* "match" is true by construction; it counts the arrival flag, which exceeds Paper 1's object (T1); under (Z-ix) it needs paths longer than $\omega$.

## 5. Pins

Scripts are in [`completed-vs-evolutions-scripts/`](completed-vs-evolutions-scripts/).

- **Run:** `sh run.sh`, with Python 3.13.5 and the standard library only. The run is deterministic, so there is no seed or $N$.
- **Expected output:** `expected/cvse.txt`, byte for byte.
- **sha256 (first 12 hex digits):** `cvse.py` `9c11df39fe7d`, `run.sh` `3eea1ec3f8cb`, `expected/cvse.txt` `e0787dee6204`.
- **Method:** `turning-type-lemma-scripts/censusf286.py`'s rule and (a) test, from $[10,20]$: exhaustive under (a) at $c=0.1$ and $0.01$; without (a), BFS depth 8, "stop" and "through".
- **Results:** 0 self-loops and 0 coincident edge targets in every run.
  - Under (a) at $c=0.01$: 29,118 turning points with an admissible edge, on 29,119 orbits.
  - Without (a), $c=0.1$, depth 8, "through": 10,092 decisions, 240 edges through the throat, minimum $|r'-r_0|/r_0=0.000882$.

## Critic questions

1. Is D1's right-continuous trace a faithful reading of Paper 1's "curve parametrised by proper time"? Or does a jump that carries no $\tau$ already break §4, so that neither definition is Paper 1's?
2. Case 2 treats a recurrent self-loop as a type-(i) pair. Is that intended, or is it a type-(ii) edge whose only effect is to change the arrival flag?
3. Where $z>0$, countability depends on the Zeno reading through (Z-vii). Should C33's "countable" be stated before excision or after it?
