# (M1) versus (M2): decision brief for David

David ruled (M1) at 11:45 PM ET on 2026-10-10 (relayed via Ontology's chat, not signed; not otherwise recorded in the repository), after reading this brief at head a39a1d7, before #267 and Literature's check were applied. Hold level, set by David at 11:46 PM ET (relayed via Physics Lead): "Record (M1) as my choice at L3, strong opinion, weakly held, open to reversal if the analysis turns against it."

**Status:** decision brief, neutral. It makes no pick, has no lean and gives no recommendation: the call is David's alone. It is not a claim of v0.9, and nothing in `versions/`, the essays or `papers/` is edited. It was read at main `7fab909`. Sources are cited by path and §; proofs are cited, not restated. (M1) is listed first throughout because v0.9 §11 lists it first; the order implies no ranking.

## 1. The question

When an observer's history branches, each branch needs a weight. At main `7fab909`, the record has two candidate rules and has not chosen between them. v0.9 §11 says "**The measure: undecided.**" and "This paper does not choose between them."

- **(M1)** is "Per-vertex EPP1, the working postulate here. It needs no named cut: it is the count at the depth-1 cut anchored at the current state" (`versions/v0.9-prose.md` §11). EPP1 itself is defined in §9: "assign weight $1/|A(O^u,a)|$ to each arm". A history's weight is the product of its shares, $1/D(v)$ with $D(v)=\prod_{w<v}\deg(w)$ (§9).
- **(M2)** is "Return to Paper 1’s count of distinct evolutions at a named cut" (§11). Each evolution reaching the cut $C$ gets $1/|C|$ (§9).
- **Labels.** v0.9 calls (M1) "the working postulate here" (§11), and of EPP1 says "It is adopted as a named postulate" (§9). (M2) carries no such label; v0.9 says it "would carry the uniqueness thesis at that cut" (§11). Both sit under "**The measure: undecided.**" How these labels read is #230 F9, which the record leaves to David.

**Example 1: a 2-arm split, then a 3-arm split (C12).** This is the tree pinned in C12. The root has arms $A$ and $B$; $A$ then splits three ways ($A_1,A_2,A_3$), and $B$ continues as the single arm $B_1$. The cut is at depth 2.
- (M1): $A_i = \tfrac12\cdot\tfrac13=\tfrac16$ for each $i$, and $B_1=\tfrac12\cdot1=\tfrac12$. Total: $3\cdot\tfrac16+\tfrac12=1$.
- (M2): the cut has four evolutions, so each gets $\tfrac14$. Total: $4\cdot\tfrac14=1$.
- Prefix $A$: (M1) gives $\tfrac12$; (M2) gives $3\cdot\tfrac14=\tfrac34$ at depth 2, but $\tfrac12$ at the depth-1 cut. Under (M2), $A$'s weight changes with the cut; under (M1) it does not (§9).

**Example 2: one 3-way decision described two ways** (`notes/born-litmus-test.md`, "Outcome mapping (Lead's draft, pending David)", LT3 bullet; recomputed in `reviews/born-litmus-merw-substitution-pressure-test.md` §1).
- As one decision $\{X,Y,Z\}$: (M1) gives $\tfrac13$ each, and (M2) gives $\tfrac13$ each.
- As two binary decisions, $\{X,W\}$ and then $W\to\{Y,Z\}$: (M1) gives $X=\tfrac12$ and $Y=Z=\tfrac12\cdot\tfrac12=\tfrac14$. (M2) at the depth-2 cut, with dead ends included (§9), has $C=\{X,Y,Z\}$, so it gives $\tfrac13$ each.

Example 1 moves (M2) with the cut and leaves (M1) fixed; Example 2 moves (M1) with the description and leaves (M2) fixed at any cut of depth 2 or more with dead ends included. At the depth-1 cut, (M2) gives $X$ and $W$ $\tfrac12$ each; counting survivors only, $X$ drops out of the depth-2 cut and $Y$, $Z$ get $\tfrac12$ each (§9, *Dead ends*). The general facts are in C13–C15:
- the two rules agree on a cut iff $D$ is constant on it (C13);
- with finite stars, depth counts converge to the per-vertex weights on every cylinder set iff siblings are asymptotically balanced; constancy of $D$ at every depth from some depth on is sufficient, not necessary, and constancy along a cofinal sequence of cuts need not give convergence (§9, *Limit*; C15; #229 R3);
- proper-time cuts can disagree even on generation-regular trees (C14).

Neither example bears on a Born-type question (v0.9 §2).

## 2. Each choice: case, costs, what it opens or closes

| | (M1) | (M2) |
|---|---|---|
| Case for | No named cut. Weights are functions of the current state, which fits Problem note 6 (§11). A prefix's weight is unchanged when the cut moves (§9) and when a descendant later splits (readiness §1.2, pin P7: $\tfrac12$ both times); a same-vertex split into arms with the same outcome moves it, as it moves (M2) (P7: $\tfrac12\to\tfrac13$ under both). The transition kernels define a path measure on completed histories (§9). | Carries Paper 1's thesis at a cut: equal weight to distinct evolutions (§11). It is Paper 1's "countable at a grain" (§11). Its count at a cut of depth 2 or more, dead ends included, is unchanged when a decision is described as two (Example 2); at the depth-1 cut it is not. It fills the branch-counting slot (readiness §1.2). |
| Pedigree (Appendix B) | The per-split rule: applied in MMWI (2006) in the random-walk argument attached to its Fig. 1E; stated as SHPMP 2008's Definition 3, which SHPMP took as its transition rule, tying its other counts to it by axiom. | The count: stated in MMWI (2006, p. 11); path counting, the form of Paper 1's count, in `Strayhorn3` (2006); SHPMP 2008's Definition 2, which SHPMP rejected in its simple form; Paper 1 went back to the count. |
| Costs | A named postulate (note 9). Does not carry Paper 1's uniqueness thesis. One chosen product measure on a continuum without (a) (C16). Unequal weights on co-existing evolutions (C12). In the countable (a) case, $2^{-k}$ at $c=0.1$ on countably many evolutions of one kind: Paper 1 §6's refusal case (C33). Moves when a decision is described as two (Example 2). | A named cut (note 9). The weight depends on the cut (C13, C14; SHPMP's objection, Appendix B). Needs a cut or grain on infinite sets, under (a) too (Paper 1 §6). The MERW hazard (§9, C36). Next-step weights depend on where the cut sits (note 6). Re-anchoring at each state removes this but in general gives up equal weight at a fixed cut (§11; C13). A later split moves it (P7: $\tfrac12\to\tfrac13$). |
| Opens | v0.9's EPP1 figures (C17, C33's exact law, C34) stand as stated (readiness refresh: "Gap 2's figures are EPP1 quantities"). LT3's cut clause, and its later-split reading, are met by construction; a same-vertex split moves (M1) as it moves (M2) (litmus note, Outcome mapping, LT3 bullet; Lead's draft, pending David). | Paper 1's countability thesis, which §12's table marks "Not carried under EPP1". §11 says the reading of the weight is "to be revisited if (M2) is chosen". Equal weight at a fixed cut (§11). LT3's grain clause, in Example 2's form (a cut of depth 2 or more, dead ends included), is met; its cut clause is met where $D$ is constant on the cuts compared (C13) or in the depth limit under asymptotic sibling balance (C15) (litmus note, Outcome mapping, LT3 bullet; Lead's draft, pending David). |
| Closes | Uneven single-decision weights can come only from tree shape, that is, from the law of $R$ (readiness §1.2). The countability thesis stays uncarried (§12 table). | No weight exists before a cut is named. The record does not compute counterparts of the EPP1 figures. Counting (Z-iv) can fail to converge (Zeno note, (d)). |
| Zeno note, (c) | (Z-0)/(Z-i): no weights above any Zeno history. (Z-ii): weights stay functions of the current state; positive weight sits on histories that item 8 ends. (Z-iii)/(Z-vii): weights read $R$ ahead ((Z-vii)'s arm set also departs from $A(O^u,a)$). (Z-vi): as (Z-i) where $z>0$, as (Z-ii) where $z=0$. (Z-ix): needs $A(O^u,a)$ at the limit state; weights above it are unchanged. | (Z-iv) counts: this is (M2)'s cut question, and the value depends on the cut family (C14, C15). (Z-ix): a counting rule is needed beyond a shared limit state. |

## 3. Pending items, and what a choice does to them

- **#230 F10** (`reviews/v0.8.1-prose-full-claude-pressure-test.md` §4: S46, S47, N39–N41) concerns how the two cost lines are balanced. Its options are "apply as a set", "apply none" and "restate the cost lines once". All three assume both lines stay open. Either pick would rewrite §11's (M1)/(M2) items, the T2 row and §12 "Completed evolutions"; the record does not say what F10 becomes then. Deferring leaves F10 as it is.
- **FD3** (`reviews/born-litmus-merw-substitution-pressure-test.md` §3) asks whether LT3 is restated "given its uneven bearing on (M1) and (M2)", and how "irrelevant" is defined. A pick does not answer FD3. The litmus note records its LT3 analysis "so that LT3 is not read as deciding (M1)/(M2)".
- **Readiness gap 4** (`reviews/born-rule-readiness.md`, v0.9 refresh) waits on (M1)/(M2), T2, #139 (b), F5, F6, F9, F10 and the Zeno options.
  - A pick settles the (M1)/(M2) entry.
  - §11 lists #139 (b) as "= T2 and (M1)/(M2)".
  - Left open either way: completed histories versus a cut, the reading of the weight, F5 (MERW wording), F6 (credit for the cut objection) and F9 (status wording).
- **Zeno options (Z-0)–(Z-ix)** (`notes/zeno-mass-scoping.md`): the note's table (c) gives each option's bearing on each side (§2 above).
  - A pick narrows which options act, but chooses none.
  - (Z-v) and (Z-viii) constrain both sides.
  - Under (A), only C35 changes under the options (note, (b)).
- **#229 §5 item 10** (`reviews/v0.8.1-prose-full-claude-opus.md`): trimming. "next-step weights depend on where the cut sits" appears four times, and it is an (M2) cost line, so trimming it would touch F10. That link is this brief's reading: #230 F12 calls item 10 editorial, and #230 §5 ties item 6 (stating the cost lines once) to F10. A pick changes these passages; deferring leaves the trim tied to F10.

## 4. Options beyond a straight pick (record basis cited)

- **(O1) Defer, keeping v0.9's state** (v0.9 §11: "This paper does not choose between them"). Cost: everything in §3 stays open. (M1) keeps the label "working postulate" while the measure is "undecided", a status wording that #230 F9 leaves to David.
- **(O2) Carry both as named alternatives and report results under each.** Basis: the readiness §3 cheap test computes both $w_n^{M1}$ and $w_n^{M2}$ and calls their difference "a readout, not a choice"; §9 compares both at named cuts. Costs:
  - every weight is stated twice, with a cut named for (M2);
  - the paper gets longer, against #229 item 10;
  - FD3 and the Zeno options stay open.
- **(O3) A count re-anchored at a fixed depth greater than 1** (v0.9 §11, "Both rules as counts at a cut"; C13; C36; #169's horizon-$k$ count; #225 item 1.4; #229 R4). Costs:
  - a named depth (note 9);
  - it reads $R$ ahead, so a later split within the anchor depth moves a prefix (P7's tree, two ahead: $\tfrac12\to\tfrac13$, computed in the Geometry check of this brief);
  - in general it gives up equal weight at a fixed cut: on C13's tree, two ahead gives $\tfrac1{10}$ and $\tfrac1{15}$ against $\tfrac1{12}$, while three ahead gives $\tfrac1{12}$. It does not give it up on every tree: on Examples 1 and 2, two ahead gives $\tfrac14$ each and $\tfrac13$ each (the (M2) values, as state functions), and #229 R4(b) gives a tree with non-constant $D$ on which it keeps equal weight;
  - on a finite strongly connected graph, it approaches MERW in the long-path limit (§11, C36).
  It is a family the record describes (anchored counts are state functions at every depth, #169; (M1) is its depth-1 member), not one of §11's two options.
- **(O4) State weight results only where the two rules agree** (§9: at a named cut the rules agree iff $D$ is constant on it, C13; in the depth limit, iff siblings are asymptotically balanced, C15). Costs:
  - a condition on tree shape is a condition on the law of $R$, which is open;
  - C12 and C14 fail it;
  - §11 says "Neither fact is used to decide".
- **(O5) Restate the cost lines once before deciding** (#230 F10, third option; #229 §5 item 6). Cost: this rewrites the balance passages, which is itself F10's decision, and it adds no new fact bearing on the choice.

## 5. Where the record is unclear or conflicts

1. v0.9 §11 calls the cost lines "symmetric". #229 N41 and #230 F10 say they are parallel but do not match item for item.
2. The old readiness map's "(M2) has no uniform countably additive measure" predates #229 R1's correction (refresh, stale item 11). The DW (a) row is wrong for (M2) (refresh, "Premise status").
3. Readiness gap 4 lists Zeno options up to (Z-viii); the note now runs to (Z-ix).
4. T2's sides parallel (M1)/(M2). The record does not say whether a pick also settles T2.
5. The record does not say whether FD3 should be decided before the measure or after it.
6. EPP1 is "adopted as a named postulate" (§9) while the measure is "undecided" (§11). This is #230 F9, left to David.
