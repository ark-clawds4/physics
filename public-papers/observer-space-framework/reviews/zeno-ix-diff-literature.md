# Diff and claim check of #261 ((Z-ix) added to the Zeno-mass note) — Literature

**Verdict: HOLD (narrow).** Two required strings: A1 (attribution) and L1 (the row label). Everything else checks.
**Heads read:** #261 head `d6207ee` (one commit). Base and main `af55f77` (#259 merged, with #260 at `ecdb9fb` below it). v0.9 read at `af55f77`. Re-checked before filing.
**Scope:** `notes/zeno-mass-scoping.md` only. Paper 1 and `versions/` are untouched.

## Checks

1. **Diff.**
   - #260's strings P1, P2 and O1 all landed at `af55f77`, each found once: P1 in the pressure test, P2 in `born-rule-readiness.md`, O1 in the note.
   - #261 changes one file, with 38 insertions and 3 changed lines.
   - The changed lines:
     - l.3: a "Revised again" line;
     - l.9: (Z-ix) added to the "other conventions" list, a stated cross-reference;
     - the pins line: `zeno9.py` added.
   - The insertions:
     - the (Z-ix) definition row (l.26);
     - the (N-a)/(N-b)/toys/comparison section (ll.30–57);
     - the (c)-table row (l.78);
     - the T1/FD1 paragraph (ll.82–83);
     - the (d) cost bullet (l.97);
     - critic questions 6–7.
   - Removing those lines and the three changed lines leaves the rest byte-identical to the base. Rows (Z-0)–(Z-viii) and all their cost cells are unchanged. ✓
2. **Numbers.**
   - The `zeno9.py` SHA-256 matches its pin (`374027d8…`). Rerunning it reproduces every value in the row and section.
   - The partner values on C35, V0, V1 and V2 agree with the note's existing table and with my #260 recompute (V2: undefined / $1/2$ / $2/3$).
   - With a limit state added, $X$ gets $1/2$ on all four if clause (2) is met, and is undefined if not.
   - The accumulating mass is $z$ itself: C35 $1/2$, V0 $0$, V1 $1$, V2 $1/4$. This is my #260 recompute.
   - No toy has a limit state as stated. C35 (v0.9 table) has vertices only at $\tau=1-2^{-k}$, and nothing at the accumulation value. ✓
   - New values: $1/2$, $1/4$, $2/3$, as claimed.
3. **Factual claims.**
   - **"Not nested in (Z-ii)"** is correct. The per-vertex values coincide, but (Z-ii) ends the histories and (Z-ix) continues them. The note states this as structure, not as a verdict.
   - **"Fails (Z-viii) as written wherever $z>0$"** is correct. Continuation leaves the accumulating mass $z$ in place, and V0 ($z=0$) meets it. The alternative reading of (Z-viii) under which (Z-ix) meets it is also given. Stated as fact. ✓
   - **The (Z-v) retiming** cannot be extended: $k\to\infty$ leaves no real time for a vertex after the accumulation. ✓
4. **Mappings.**
   - T1 is the *Mathematical Foundations* tension in v0.9 §11 ("T1–T3 are the tensions named in *Mathematical Foundations* v0.3"), and its "Drop (A)" side cites C5.
   - The FD1 paragraph matches #259's FD1. Option (i) leaves item 8 literal, so C5's chains are Zeno histories and (Z-ix) applies. Option (ii) (strict alternation alone) removes the T1 link.
   - "T3 only through a partner" is correct: (Z-ix) changes no weight above an existing limit.
   - The (M1)/(M2) cell states needs on both sides, and picks nothing.
   - FD1 and FD2 remain pending. ✓
   - Note: `c5chain.py` (pin `f6e912eb…`) rerun gives a toward-10 chain of 3000 jumps with periastra in $[9.8926, 10.1074]$. So whether a C5 chain has a limit in the observer data is genuinely open, as the note says ("not yet posed").
5. **Neutrality.**
   - (Z-ix) has a full cost bullet: topology, existence proof, the N-a choices, $R$/$A$ at $T$, conditional item 8, clause (2), and its partner's cost. That matches the depth of the others.
   - "No new rule is needed at $T$" (definition) is answered in the cost line ("but $R$ and $A(O^u,a)$ must be defined there").
   - (N-a) lists choices. (N-b) lists the compositions with every row, with no pick.
   - The added text has no "natural", "preferred" or "best".
   - Critic questions 6 and 7 are well-posed open questions. Q6's "or does (Z-ix) move the open question … to the topology?" names a cost the (d) line already states, and is not loaded.
   - Exception: the row label. See F2.
6. **Guardrails.**
   - No Born, $|a|^2$ or 1/N result; no law of $R$; no pick of a Z-reading, (M1)/(M2), T1–T3 or #139.
   - No Everett-vs-DW framing; nothing on Bell.
   - None of the banned words or the acronym.
   - Paper 1 and `versions/` untouched.

## Findings

- **F1 (required, attribution).**
  - The row names the route (Physics Lead's chat), the time (about 6:50–6:53 PM ET, 2026-10-10) and the absence of a record ("not otherwise recorded in the repository"). That meets the #249/#253/#255 standard.
  - The verbatim sentence cannot be checked against any source in this repository: there is no chat log here. It is quoted once, and the header's "proposed by David and relayed by the Physics Lead" agrees with it.
  - The gap: the quoted sentence speaks only about a $T$ that does *not* exist. The continuation rule ("the observer continues from it under the same rule … no new rule is needed at $T$") and the label's "continue through existing limits" are not in the quote. They are unmarked paraphrase that the cell attributes to David. String A1 marks them as paraphrase of the relay.
- **F2 (required, neutrality).** The other rows are named by mechanism ("null-set gate", "arm pruning", "cut limit"). "(Z-ix) David's reading" is the only row named by person, which is the implicit ranking the brief rules out. String L1 makes the label mechanical; the attribution stays in full in the definition cell. Lines 3, 30 and 38 are unchanged: they attribute, they don't label.
- **N1 (note).** The (c)-table cell's "(Z6)" is #258's item. The note already cites it that way at critic question 2. No string needed.

## Strings

Each OLD occurs exactly once in `public-papers/observer-space-framework/notes/zeno-mass-scoping.md` at `d6207ee`.

**A1**

OLD:
```text
If the limit state $T$ of a Zeno history (David's T, not the cut $T$ of (Z-iv)) does exist
```
NEW:
```text
The rest of the proposal, as relayed in paraphrase rather than quoted: if the limit state $T$ of a Zeno history (David's T, not the cut $T$ of (Z-iv)) does exist
```

**L1**

OLD:
```text
| (Z-ix) David's reading: continue through existing limits |
```
NEW:
```text
| (Z-ix) limit continuation |
```

## Word counts (`str.split`)

The note goes from 2,240 to 3,631 words (+1,391), as claimed. The base's 2,240 is 2,238 plus #260's O1 (+2). With A1 and L1 applied it would be 3,639.
