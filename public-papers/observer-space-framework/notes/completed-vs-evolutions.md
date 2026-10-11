# Completed histories versus Paper 1's evolutions

*A standalone note on item 3 of the v0.10 plan (#285). It makes no edits to v0.9.1 and was read at main `5e05692`. (M1) is ruled at L3 and is cited here. The Zeno readings, the throat convention, F11, gauge and grain stay open; nothing here picks among them. Scripts and pins are in §5.*

**Why a definition comes first.** v0.9.1 reads C16 and C33 as statements about Paper 1's distinct evolutions (§12, *Completed evolutions*): a continuum without (a), and countable under (a). Paper 1 §4 states its identity criterion for *curves parametrised by proper time*. v0.9.1's histories are not such curves: they are segments joined by jumps that carry no $\tau$ (§8.2 item 2). The plan's ILL flag is that Paper 1's "distinct evolution" has no identity criterion on graph paths. So I propose two definitions, each grounded in the record, before comparing anything.

## 1. Two definitions

A *completed history* is a maximal path from the root, finite or infinite (v0.9.1 §9). A path that item 8 of §8.2 ends at a Zeno accumulation counts as one too.

**D1 (trace; Paper 1 §4).** A history $h$ has a *trace* $x_h$. At accumulated proper time $\tau$, $x_h(\tau)$ is the oriented germ $h$ occupies; the trace is defined on $[0,T_h)$ and is right-continuous at jumps. Two histories are D1-equal, $h\approx_1h'$, iff $x_h=x_{h'}$ on the common domain. They split at the first $\tau$ where the traces differ.

Grounds:

- **Paper 1 §4.** Evolutions are "the same until the simply-connected analytic patches disagree". This is a premise that §4 says is not reopened.
- **The jet–patch lock.** By Paper 1 §2 and Theorems A–B of `papers/analytic-patch-from-jet.md`, the germ is equivalent to the patch, so "patches disagree" means "germs differ".
- **Time direction.** Paper 1's time direction is read as $u$ (v0.9.1 §4).
- **Dying is not an arm.** A history that ends and one that continues through the same germs are one evolution (v0.9.1 §6.2). D1's "common domain" encodes this.
- **$E(O)$ is not folded into $\sim$** (`papers/ensemble-labels.md`). So neither world multiplicity nor the world that realises an (a)-edge creates an evolution.

The extension D1 needs is that Paper 1's "curve" becomes a trace with jumps that carry no $\tau$.

**D2 (decision path; v0.9.1 §8.2).** $h\approx_2h'$ iff the two histories take the same arm at every decision. This is item 5's first-edge equivalence applied at each decision along the history. Under D2, completed histories are the maximal paths of the decision tree, which is the space on which the (M1) path measure lives (§9).

Grounds:

- §8.2 items 5–7 and C11.
- Delayed forks as graph paths (`papers/type-ii-adopted.md`, Definition 8 and Proposition 12).
- §9's maximal paths and the (M1) ruling.

Neither definition uses $|a|^2$ or any weight.

## 2. How they relate

**Proposition.** Let $h\not\approx_2h'$ first differ at a decision at the state $(O^u,\mathrm{seg})$ and time $\tau_0$, where they take arms $\alpha\neq\beta$. Then the traces split at $\tau_0$, unless one of the two arms continues and the other is a self-loop $(O^u,O^u)\in R$. Hence:

1. **Onto, and when one-to-one.** The map from D2-classes to D1-classes is onto. It is one-to-one iff no reachable decision carries a self-loop.
2. **Under (a) it is always one-to-one, for every $R$.** (a) excludes $\{\gamma_{O^u}(\tau):\tau\ge0\}$, and that set contains $O^u$.
3. **Recurrent germs.** Suppose $\gamma_{O^u}$ returns to $O^u$ at some $\tau>0$, as successive periastra do (§8.2). Then $(O^u,O^u)$ is a type-(i) pair, and item 3 of §8.2 removes it from $R$. This reads a type-(i) pair as any pair $(O^u,\gamma_{O^u}(\tau))$ with $\tau>0$.
4. **The jump convention is immaterial.** Two curvelets that agree on $(0,\delta)$ agree at $0$, by Theorem 2 of `papers/analytic-split.md`. So the right-continuity convention does not affect any identification.

Elsewhere, one-to-one needs irreflexivity of $R$, which is a named extra that has not been adopted (`papers/irreflexive-r.md`).

**On the Kretschmann rule.** A target is the source germ iff $r'=r_0$. A direct path cannot give this. Under "continue through", a path through the throat gives it only at apastra with $\varepsilon=2\Delta\ell$ (#290 (T3): $r_0=2786.4692$ at $c=0.1$). A decision there is reached along a segment, so it lies on a bound orbit: a plunging orbit's apastron is reached only by the jump that lands on it. The germ is therefore recurrent, and item 3 removes the loop. So D1 and D2 coincide on every reachable decision, under (a) or without it, and under either throat convention.

**Numerics.** No reachable self-loop occurs in the sets explored (§5). The closest approach is $|r'-r_0|/r_0=0.000882$, without (a), at $c=0.1$, under "through".

## 3. What each definition makes true or false

| Claim about completed histories | D1 | D2 |
|---|---|---|
| One-to-one with evolutions | True iff no reachable self-loop: always under (a), and at recurrent germs (item 3). Otherwise many-to-one: a self-loop and the continue arm are one evolution | True by construction |
| C16 (a continuum without (a)) | True. C16's histories choose between continuing and an edge to $f(r)\neq r$, so their traces differ | True |
| C33 (countable under (a)) | True; D1 and D2 coincide there | True |
| Paper 1 §5's antecedent ("distinct evolutions … countable") on the instance | Fails without (a) and holds under (a) | Same |
| (M1) weight of an evolution | The pushforward: a sum over its D2-classes. It differs from the path weight only at reachable self-loops | The path weight |
| Toys with no germs (C35, V0–V2) | Undefined, since a trace needs germs | Defined |

In general D1 is a quotient of D2. So D2 countable implies D1 countable, but D2 uncountable does not imply D1 uncountable. On the Kretschmann instance §12's reading of C16 and C33 as facts about evolutions holds under either definition.

**Zeno histories, under the Zeno-note readings, with no pick.** A Zeno history is one completed history, ended at $\tau^*$ by item 8. Two Zeno histories differ at some decision before $\tau^*$, so they are distinct under both definitions wherever germs exist. The readings then sort as follows.

- **Mass only: (Z-0)/(Z-i), (Z-ii), (Z-iii), (Z-iv) per-vertex, (Z-v), (Z-vi), (Z-viii).** These move or withhold mass. They do not change which histories exist or how they are identified, so countability of the set of evolutions does not move.
- **(Z-vii).** It prunes arms that carry only Zeno histories, so the history set itself changes. On C35, below $Y$, every vertex carries two arms, so under D2 there are uncountably many Zeno histories. (Z-vii) prunes $Y$, and the set shrinks to $\{X\}$. Where $z>0$, countability can therefore depend on the reading.
- **(Z-ix).** Where a limit state $T$ exists, it continues the history.
  - Under D1 the trace extends past $\tau^*$. By §6.2 the ended and the continued forms are one evolution, so (Z-ix) lengthens evolutions and adds none.
  - Under D2 a continued history has $\omega$ decisions before $T$, so "maximal path" needs paths longer than $\omega$. I route around this by indexing a continued history as a pair: the $\omega$-path to $T$, then a path from $T$.
  - Limitless Zeno histories go to (Z-ix)'s partner row.
- **The instance.** It has no Zeno histories (C7), so none of this moves the findings for the Kretschmann rule.

## 4. Options and costs

The two definitions differ only at reachable self-loops that item 3 does not remove, and on toys with no germs. I make no pick.

- **D1.**
  - *For:* it is Paper 1 §4's own premise. Like Paper 1's object, it is blind to the world and to the arrival flag. It handles (Z-ix) natively.
  - *Cost:* it extends "curve" to traces with jumps that carry no $\tau$. The Markov state $(O^u,a)$ is finer than the evolution, so where self-loops survive, (M1) weights per evolution become sums. It is undefined on toys with no germs. Outside (a) and recurrence, being one-to-one needs irreflexivity, a named extra.
- **D2.**
  - *For:* it is the space that (M1), C11, C16 and C33 already use, and it is defined on toys.
  - *Cost:* "completed histories match evolutions" becomes true by construction, because v0.9.1's own construction is imported into Paper 1's criterion. It counts the arrival flag, which exceeds Paper 1's object (T1). It needs paths longer than $\omega$ under (Z-ix).

## 5. Pins

The scripts are in [`completed-vs-evolutions-scripts/`](completed-vs-evolutions-scripts/). They are deterministic, so there is no seed and no $N$. Run `sh run.sh` with Python 3.13.5 (standard library only). The expected output is `expected/cvse.txt`, which should match byte for byte. sha256 (first 12 hex digits): `cvse.py` `9c11df39fe7d`, `run.sh` `3eea1ec3f8cb`, `expected/cvse.txt` `e0787dee6204`.

`cvse.py` uses the rule, target map and (a) test of `turning-type-lemma-scripts/censusf286.py`. It explores the reachable set from $[10,20]$ in two settings:

- under (a), exhaustively, at $c=0.1$ and $c=0.01$;
- without (a), to BFS depth 8, at $c=0.1$ and $c=0.01$, under "stop" and under "through".

In every run there are 0 self-loops and 0 coincident edge targets. Under (a) at $c=0.01$ there are 29,118 turning points with an admissible edge on 29,119 orbits. Without (a) at $c=0.1$, depth 8, "through", there are 10,092 decisions, 240 of their edges go through the throat, and the minimum $|r'-r_0|/r_0$ is $0.000882$.

## Critic questions

1. Is D1's right-continuous trace a faithful reading of Paper 1's "curve parametrised by proper time"? Or does a jump that carries no $\tau$ already break §4's premise, so that neither definition is Paper 1's?
2. Proposition item 3 reads a recurrent self-loop as a type-(i) pair, which item 3 of §8.2 excludes. Is that the intended reading of "type (i)"? Or should a self-loop count as a type-(ii) edge whose only effect is to change the arrival flag?
3. Under (Z-vii), countability of completed histories depends on the Zeno reading wherever $z>0$. Should "completed histories are countable" (C33) be stated relative to the history set before excision, or after it?
