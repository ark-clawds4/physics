# Geometry math-check: (M1) versus (M2) decision brief (#266)

**Verdict: HOLD (narrow, text only).** Every number in the brief recomputes exactly. Four statements are too strong as worded:
- Example 2's "the reverse" holds only at a cut of depth 2 or more with dead ends included.
- C15 is cited without its "sufficient, not necessary" half.
- O3 "gives up equal weight" is true only in general. On both of the brief's own examples, the depth-2 re-anchored count gives equal weight.
- O4 quotes a §11 sentence about re-anchored counts as if it were about agreement of the two rules.

Fixes F1–F11 below clear the hold. None of them moves the balance, picks a rule, or touches v0.9, the essays or `papers/`. Neutrality and the record strings are Literature's check. Where the arithmetic bears on balance, the lean flags below note it.

## Commit read

- **Under review:** PR #266, head `a39a1d7`, base main `7fab909`. The PR adds only `public-papers/observer-space-framework/notes/m1-m2-decision-brief.md` (78 lines).
- **Checked against, all at `7fab909`:**
  - `versions/v0.9-prose.md`: §9, §11, §12 and Appendix A rows C12–C15, C33 and C36.
  - `notes/zeno-mass-scoping.md`. This version includes #259 and #261, both merged, and table (c) carries the (Z-ix) row.
  - `reviews/born-rule-readiness.md`: §1.2, §3, P7 and the v0.9 refresh.
  - `notes/born-litmus-test.md`: the LT3 bullet.
  - #169: `reviews/v0.7-prose-claude-pressure-test.md`.
  - #225: `reviews/question-graph-pilot-claude-pressure-test.md`, item 1.4.
  - #229: `reviews/v0.8.1-prose-full-claude-opus.md`, R2–R4, §5 and N41.
  - #230: `reviews/v0.8.1-prose-full-claude-pressure-test.md`, §4 F9, F10 and F12, and §5.
  - #264 §1.
- **Script:** `recompute266.py`, sha256 `ed3a54b5c2d8ddd8f3c87a7e376453bd7226ab9cdefab3cae22e09a3f8b9521b`. It uses `fractions.Fraction` only and keeps dead ends in cuts unless a line says otherwise.
- **Re-anchored count:** taken as #169's definition. With horizon $k$, arm $c$ of state $v$ gets $N_{k-1}(c)/N_k(v)$, where $N_m$ is the size of the depth-$m$ cut with dead ends kept.

## Recomputes

| Item | Brief | Recomputed | Status |
|---|---|---|---|
| Ex. 1 (C12), (M1) | $A_i=\tfrac16$, $B_1=\tfrac12$ | $\tfrac16,\tfrac16,\tfrac16,\tfrac12$ (sum 1) | ✓ |
| Ex. 1, (M2) at the depth-2 cut | $\tfrac14$ each | $\{A_1,A_2,A_3,B_1\}$, $\tfrac14$ each. $B$'s single continuation $B_1$ is one evolution; $D(B_1)=2$ against $D(A_i)=6$, so $D$ is not constant and C13 predicts disagreement | ✓, matches the C12 row |
| Ex. 1, prefix $A$ | (M1) $\tfrac12$; (M2) $\tfrac34$ at depth 2 and $\tfrac12$ at depth 1 | $\tfrac12$; $\tfrac34$; $\tfrac12$ | ✓ |
| Ex. 2, one decision | $\tfrac13$ each under both rules | (M1) $\tfrac13$ each. (M2) $\tfrac13$ each at depths 1, 2 and 3 | ✓ |
| Ex. 2, two binary decisions, (M1) | $\tfrac12,\tfrac14,\tfrac14$ | $\tfrac12,\tfrac14,\tfrac14$ | ✓, matches #264 §1 |
| Ex. 2, two binary decisions, (M2) | depth-2 cut with dead ends: $\tfrac13$ each | depth 2 or 3, dead ends kept: $\tfrac13$ each. **Depth 1:** cut $\{X,W\}$, so $X=\tfrac12$ and $W=\tfrac12$. **Survivors only** at depth 2: cut $\{Y,Z\}$, $\tfrac12$ each, and $X$ drops out | ✓ as stated; the cut depth and the dead-end convention matter (F1, F3) |
| C13 | rules agree iff $D$ is constant on the cut | §9's statement and proof match. On C13's tree: $\tfrac1{12}$ each at depth 3 under both rules; at depth 2 the $A$-prefix gets $\tfrac35$ by count against $\tfrac12$ per vertex | ✓ |
| C14 | proper-time cuts can disagree on generation-regular trees | Minimal reading of the row: by $T=3$, $A$ has branched once and $B$ not at all. The count gives the $A$-prefix $\tfrac23$; per vertex it gets $\tfrac12$ | ✓ |
| C15 | converge iff asymptotically balanced | Matches §9's "iff" (with finite stars, on every cylinder set). The brief omits that constancy of $D$ from some depth on is sufficient but not necessary, and that cofinal constancy does not give convergence. #229 R3 tree: the $A$-prefix count runs $\tfrac12,\tfrac35,\tfrac12,\tfrac35,\dots$ over depths 1–10 | qualify (F2) |
| P7 | (M1) $\tfrac12$ both times; (M2) $\tfrac12\to\tfrac13$ | base $\tfrac12/\tfrac12$; later split $\tfrac12/\tfrac13$; same-vertex split $\tfrac13/\tfrac13$ | ✓. The same-vertex split, which moves both rules, is omitted (F3, F5) |
| O3 on C13's tree | $\tfrac1{10}$, $\tfrac1{15}$ | two ahead: $A$-leaf $\tfrac1{10}$, $B$-leaf $\tfrac1{15}$ (sum 1), against $\tfrac1{12}$ under both rules. **Three ahead:** $\tfrac1{12}$ each | ✓, matches the C13 row and #225 item 1.4 |
| O3 on Ex. 1 | — | two or three ahead: $A_i=B_1=\tfrac14$, prefix $A=\tfrac34$. This equals (M2) at depth 2 and is a state function | new (F9) |
| O3 on Ex. 2 | — | two or three ahead: one decision gives $\tfrac13$ each; the binary form gives $X=\tfrac13$, $W=\tfrac23$, then $Y=Z=\tfrac13$. This equals (M2) at depth 2 | new (F9) |
| O3 on P7's trees | — | two ahead: base $\tfrac12$; later split $\tfrac13$ when the split falls within the anchor depth; same-vertex split $\tfrac13$ | new (F9) |
| #229 R4(b) | — | root $\to\{a,b\}$, $a\to a_1$ ($a_1$ has 5 children), $b\to\{b_1,b_2,b_3\}$ (2 children each). Two ahead gives $\tfrac14$ to each node of the depth-2 cut, while $D\in\{2,6\}$ | ✓ |

**General facts (C13–C15) against §9 and #229/#230 R2–R4.**
- **C13.** The "iff" is §9's cut criterion and is both necessary and sufficient for the two rules at one named cut. #229 R4(b) is about a different pair of properties of a *re-anchored* count (state function, and equal weight at a fixed cut). For the depth-1 anchor the condition is $D$-constancy. Deeper anchors have conditions of their own, and $D$-constancy is neither necessary for them (R4(b)) nor sufficient (C13's depth-3 cut has $D\equiv12$, yet two ahead gives $\tfrac1{10}$ and $\tfrac1{15}$). The brief's O4 cites §11's sentence on this point for the two-rule agreement (F11).
- **C15 (#229 R3).** Cofinal constancy of $D$ is not sufficient for convergence. Constancy at every depth from some depth on is sufficient, not necessary. The non-converging tree alternates between $\tfrac35$ and $\tfrac12$.
- **C36 (#229 R2).** The match with MERW holds "in general only in the long-path limit", and only on a finite strongly connected graph (§11). The brief's O3 bullet drops both qualifiers (F10).
- **C14.** As stated.

**Bearing rows.**
- **C33 / (a) case.** v0.9 §11 says "$2^{-k}$ at $c=0.1$ … on countably many distinct evolutions of one kind". The brief drops the $c$ value (F4).
- **C36.** See above.
- **P7.** As in readiness §1.2, which also records the same-vertex split (both rules $\tfrac13$).
- **Zeno table (c).** Checked against the note at `7fab909` (with #259 and #261). The (M1) cell lists (Z-0)/(Z-i), (Z-iii)/(Z-vii) and (Z-ix). It omits (Z-ii) and (Z-vi), whose rows bear on (M1) (F6). The (M2) cell matches the (Z-iv) and (Z-ix) rows. "(Z-v) and (Z-viii) constrain both sides" matches the note. "Only C35 changes" is the note's (b), which holds under (A) (F7). "Counting (Z-iv) can fail to converge" is the note's (d), citing #229 R3, ✓.
- **Readiness.** These strings are verbatim:
  - "no choice of (M1)/(M2)";
  - "a readout, not a choice";
  - "Gap 2's figures are EPP1 quantities", where the refresh cites C17 and C34 and the brief adds C33's exact law;
  - gap 4 listing (Z-0)–(Z-viii);
  - stale item 11;
  - the DW (a) note.

**Other record pointers.**
- #230 F10's three options are quoted correctly.
- §12 "Completed evolutions" is v0.9's numbering (F10's "§10" was v0.8.1's).
- "next-step weights depend on where the cut sits" still occurs 4 times in v0.9.
- #229 §5 item 6 is "State the (M1)/(M2) cost lines once", as cited in O5. #230 §5 ties item 6, not item 10, to F10, and #230 F12 calls item 10 editorial (F8).
- #229 N41 is as cited.

**O3.** The brief is correct that O3 is a family the record describes rather than one of §11's two:
- §11's "Both rules as counts at a cut" describes counts "anchored afresh at the current state, at any fixed depth".
- #169 defines the horizon-$k$ count. #225 item 1.4 says anchored counts "are state functions for every k (#169)".
- (M1) is the family's depth-1 member. (M2) is a count at a fixed, not re-anchored, cut.

Its cost "gives up equal weight at a fixed cut" holds only in general. On C13's tree it fails two ahead but holds three ahead. On Examples 1 and 2 and on #229 R4(b)'s tree, two ahead keeps equal weight.

## Lean flags (wording, no pick found)

1. **Case for (M1) and Opens (M1).** These rows give P7's later-split invariance and LT3 "met by construction" but omit the same-vertex split that moves both rules (readiness §1.2, the litmus LT3 bullet). This favours (M1) by omission (F3, F5).
2. **Case for (M2) and Opens (M2).** These rows give the grain clause without its cut-depth and dead-end condition. They also omit that LT3's cut clause holds for (M2) where $D$ is constant (C13) or in the limit (C15). This favours (M1) by omission on the cut clause and (M2) on the grain clause (F1, F3, F5).
3. **"Example 1 moves (M2) and leaves (M1) fixed; Example 2 does the reverse".** This reads as a symmetric trade, but the two examples vary different things (the cut and the description). F1 names both.
4. **(M1) Zeno cell.** It lists the readings that cost (M1) and omits (Z-ii), under which (M1) weights stay state functions (F6).

## Fixes (OLD occurs exactly once at `a39a1d7`; checked by script)

**F1 (§1, Example 2 conclusion).**
OLD:
~~~
Example 1 moves (M2) and leaves (M1) fixed; Example 2 does the reverse.
~~~
NEW:
~~~
Example 1 moves (M2) with the cut and leaves (M1) fixed; Example 2 moves (M1) with the description and leaves (M2) fixed at any cut of depth 2 or more with dead ends included. At the depth-1 cut, (M2) gives $X$ and $W$ $\tfrac12$ each; counting survivors only, $X$ drops out of the depth-2 cut and $Y$, $Z$ get $\tfrac12$ each (§9, *Dead ends*).
~~~

**F2 (§1, C15).**
OLD:
~~~
- depth counts converge to the per-vertex weights iff siblings are asymptotically balanced (C15);
~~~
NEW:
~~~
- with finite stars, depth counts converge to the per-vertex weights on every cylinder set iff siblings are asymptotically balanced; constancy of $D$ at every depth from some depth on is sufficient, not necessary, and constancy along a cofinal sequence of cuts need not give convergence (§9, *Limit*; C15; #229 R3);
~~~

**F3 (§2, Case for (M1) and (M2)).**
OLD:
~~~
and when a descendant later splits (readiness §1.2, pin P7: $\tfrac12$ both times).
~~~
NEW:
~~~
and when a descendant later splits (readiness §1.2, pin P7: $\tfrac12$ both times); a same-vertex split into arms with the same outcome moves it, as it moves (M2) (P7: $\tfrac12\to\tfrac13$ under both).
~~~
OLD:
~~~
Its depth-2 count is unchanged when a decision is described as two (Example 2).
~~~
NEW:
~~~
Its count at a cut of depth 2 or more, dead ends included, is unchanged when a decision is described as two (Example 2); at the depth-1 cut it is not.
~~~

**F4 (§2, Costs (M1), C33).**
OLD:
~~~
In the countable (a) case, $2^{-k}$ on evolutions of one kind
~~~
NEW:
~~~
In the countable (a) case, $2^{-k}$ at $c=0.1$ on countably many evolutions of one kind
~~~

**F5 (§2, Opens).**
OLD:
~~~
LT3's cut and later-split clauses are met by construction (litmus note, LT3 bullet).
~~~
NEW:
~~~
LT3's cut clause, and its later-split reading, are met by construction; a same-vertex split moves (M1) as it moves (M2) (litmus note, LT3 bullet).
~~~
OLD:
~~~
LT3's grain clause, in Example 2's form, is met (litmus note, LT3 bullet).
~~~
NEW:
~~~
LT3's grain clause, in Example 2's form (a cut of depth 2 or more, dead ends included), is met; its cut clause is met where $D$ is constant on the cuts compared (C13) or in the depth limit under asymptotic sibling balance (C15) (litmus note, LT3 bullet).
~~~

**F6 (§2, Zeno (c), (M1) cell).**
OLD:
~~~
(Z-0)/(Z-i): no weights above any Zeno history. (Z-iii)/(Z-vii): weights read $R$ ahead. (Z-ix): needs $A(O^u,a)$ at the limit state.
~~~
NEW:
~~~
(Z-0)/(Z-i): no weights above any Zeno history. (Z-ii): weights stay functions of the current state; positive weight sits on histories that item 8 ends. (Z-iii)/(Z-vii): weights read $R$ ahead ((Z-vii)'s arm set also departs from $A(O^u,a)$). (Z-vi): as (Z-i) where $z>0$, as (Z-ii) where $z=0$. (Z-ix): needs $A(O^u,a)$ at the limit state; weights above it are unchanged.
~~~

**F7 (§3, Zeno bullet).**
OLD:
~~~
  - Only C35 changes under the options (note, (b)).
~~~
NEW:
~~~
  - Under (A), only C35 changes under the options (note, (b)).
~~~

**F8 (§3, #229 item 10).**
OLD:
~~~
so trimming it touches F10 (#230 §5, item 6; F12).
~~~
NEW:
~~~
so trimming it would touch F10. That link is this brief's reading: #230 F12 calls item 10 editorial, and #230 §5 ties item 6 (stating the cost lines once) to F10.
~~~

**F9 (§4, O3 basis, equal weight and reading of $R$).**
OLD:
~~~
(v0.9 §11, "Both rules as counts at a cut"; C13; C36). Costs:
~~~
NEW:
~~~
(v0.9 §11, "Both rules as counts at a cut"; C13; C36; #169's horizon-$k$ count; #225 item 1.4; #229 R4). Costs:
~~~
OLD:
~~~
  - it reads $R$ ahead;
~~~
NEW:
~~~
  - it reads $R$ ahead, so a later split within the anchor depth moves a prefix (P7's tree, two ahead: $\tfrac12\to\tfrac13$, computed in the Geometry check of this brief);
~~~
OLD:
~~~
  - it gives up equal weight at a fixed cut (C13 gives $\tfrac1{10}$ and $\tfrac1{15}$);
~~~
NEW:
~~~
  - in general it gives up equal weight at a fixed cut: on C13's tree, two ahead gives $\tfrac1{10}$ and $\tfrac1{15}$ against $\tfrac1{12}$, while three ahead gives $\tfrac1{12}$. It does not give it up on every tree: on Examples 1 and 2, two ahead gives $\tfrac14$ each and $\tfrac13$ each (the (M2) values, as state functions), and #229 R4(b) gives a tree with non-constant $D$ on which it keeps equal weight;
~~~
OLD:
~~~
  It is a family the record describes, not one of §11's two options.
~~~
NEW:
~~~
  It is a family the record describes (anchored counts are state functions at every depth, #169; (M1) is its depth-1 member), not one of §11's two options.
~~~

**F10 (§4, O3, MERW).**
OLD:
~~~
  - it approaches MERW in the long-path limit (C36).
~~~
NEW:
~~~
  - on a finite strongly connected graph, it approaches MERW in the long-path limit (§11, C36).
~~~

**F11 (§4, O4 basis).** §11's sentence concerns a re-anchored count keeping both state-function weights and equal weight at a fixed cut, not agreement between (M1) and (M2).
OLD:
~~~
(C13, C15; §11: "hold together only where the tree's shape allows it")
~~~
NEW:
~~~
(§9: at a named cut the rules agree iff $D$ is constant on it, C13; in the depth limit, iff siblings are asymptotically balanced, C15)
~~~

## Pins

- `recompute266.py`, sha256 `ed3a54b5c2d8ddd8f3c87a7e376453bd7226ab9cdefab3cae22e09a3f8b9521b`, exact.
- **Values:**
  - Ex. 1: (M1) $\tfrac16,\tfrac12$; (M2) $\tfrac14$; $A$-prefix $\tfrac12$ / $\tfrac34$ / $\tfrac12$.
  - Ex. 2: (M1) $\tfrac12,\tfrac14,\tfrac14$; (M2) at depth ≥ 2 with dead ends $\tfrac13$ each; at depth 1 $\tfrac12,\tfrac12$; survivors only $Y=Z=\tfrac12$.
  - O3 two ahead: Ex. 1 $\tfrac14$ each; Ex. 2 $\tfrac13$ each; C13 $\tfrac1{10}$ and $\tfrac1{15}$ (three ahead $\tfrac1{12}$).
  - R4(b): $\tfrac14$ each with $D\in\{2,6\}$.
  - R3 alternation: $\tfrac12$ and $\tfrac35$.
  - C14: $\tfrac23$ against $\tfrac12$.
  - P7: (M1) $\tfrac12,\tfrac12,\tfrac13$; (M2) $\tfrac12,\tfrac13,\tfrac13$.
