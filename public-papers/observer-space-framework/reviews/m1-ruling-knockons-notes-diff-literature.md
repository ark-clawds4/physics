# Review: (M1)-ruling knock-ons in the notes (#274), diff and record check

**Verdict: HOLD (narrow).** Heads read: #274 head `7f5df34` (commits `178a14c` and `7f5df34`), base main `2d2e4be`. Geometry #270 (merged, `9db31b0`) and #275 (open, head `18bb88e`) were read for cross-checking. Describe-only; this review makes no pick and has no lean.

The strings apply verbatim, and nothing else changed. The ruling is recorded correctly, and commit 2's scope is faithful to the record. One fix is required: the Zeno note's (c) cells for (Z-iii) and (Z-vii) (strings 9 and 12) say the two readings leave depth-1 "where a Zeno history passes through the state". By #270, they depart only where the Zeno mass $z$ at the state is positive. I dispute Geometry's claim that no other #274 string overstates for that reason.

## 1. Diff checks

- **Files:** three changed: `notes/zeno-mass-scoping.md`, `reviews/born-rule-readiness.md` and `notes/merw-litmus-scoping.md`.
- **Byte-identical:** `notes/substitution-test-scoping.md` and `notes/born-litmus-test.md` are byte-identical to main. Nothing under `papers/` changed, so Paper 1 is untouched.
- **Commit 1:** all 23 strings (16 Zeno, 5 readiness, 2 MERW) match main exactly once. Applying them by script to main reproduces `178a14c` exactly for all three files, so nothing else changed.
- **Commit 2:** it changes one line, gap 4's Open cell in the readiness refresh. Its OLD, as given in the PR body, occurs once at `178a14c`, and applying the body's NEW gives `7f5df34` exactly. Item 19 in the PR body shows the cumulative NEW.
- **Readiness above `## v0.9 refresh`:** byte-identical to main at both heads.
- **Word deltas (`str.split`, whole file):** all match the PR body.
  - Zeno note: 3,665 → 3,931 (+266).
  - Readiness: 4,945 → 5,061 (+116) after commit 1 and 5,106 (+161) after commit 2, so commit 2 adds +45.
  - MERW note: 2,929 → 2,943 (+14).
- **FD and LT:** every line containing FD$n$, LT$n$ or F-M1 is unchanged, except the two MERW "Waits on" cells (strings 22 and 23). Their LT columns are unchanged. FD2 occurs once, in the readiness file, and that line is byte-identical at both heads; so are the readiness file's LT lines.
- **Guardrails:**
  - "Born", "|a|", "Everett", "Deutsch" and "Wallace" are unchanged in count in all three files.
  - No Born, $|a|^2$ or 1/N result, and no Everett-vs-Deutsch–Wallace framing.
  - The new numeric tokens are labels (#269, #270, #272, 0.9.1, `2d2e4be`, 2026-10-11) and the departure values $1$, $1/2$, $2/3$. Those values are already in the Zeno note's table and in #270 §2, so no physics number is new.

## 2. Ruling record

- Every new mention reads L3, relayed and not signed: the Zeno status line, readiness string 17 (Read-at), strings 18 and 19, and MERW strings 22 and 23.
- Nothing is above L3. "signed" occurs only as "not signed".
- The pointers are right. #269 merged into its stacked base branch (`803b5f9`), and #272 landed the same file on main (`2d2e4be`). "#269/#272" and "v0.9.1 §11" resolve on main, where the §11 row quotes David's L3 sentence.

## 3. Zeno note

- **No new pick.** All ten reading rows, (Z-0)–(Z-ix), are present. The only pick-type wording added is "no reading is picked". The remaining set named in the status line matches #270 §2's "remain" list.
- **Counting (Z-iv) "dropped".** This is right in substance: #270 §2 confirms that counting (Z-iv) is a count-only reading and that (M1) is not a count at a distant cut. The count-only parts are the ones #270 names: (Z-v)'s depth-cut clause, (Z-viii)'s "on C35 also counting (Z-iv)" and (Z-ix)'s (M2) cell. Strings 15 and 16 (the (d) costs) and string 8 (N-b) mark the same parts.
  - **L3 hold:** "dropped" reads as final, while the ruling is held at L3 and is open to reversal. **Z6 (recommended)** defines the word once in the status line as "set aside while the L3 ruling holds and open to reversal with it". That avoids eleven separate edits.
- **(Z-iii)/(Z-vii) "narrowed."** The values match #270 §2 exactly:
  - C35: $X$ gets $1$ under both, against $1/2$.
  - V2: (Z-iii) gives $X$ $2/3$, and (Z-vii) gives $Y_1$ $1$, against $1/2$.
- **Two problems with the (Z-iii)/(Z-vii) wording:**
  - **Strings 9 and 12 overstate (required, Z3 and Z4).** "no longer depth-1, where a Zeno history passes through the state" is false where a Zeno history passes with $z=0$. #270 §2 says "Both equal the depth-1 share wherever $z=0$ at the state (V0: $\tfrac12$ under each)". On V0 a Zeno history passes (the note's (d): "A single measure-zero Zeno history is enough to make the weights undefined (V0)"), yet (Z-iii) and (Z-vii) give the depth-1 value. The right scope is $z>0$, using the note's own $z$ ("the per-vertex product mass of the Zeno histories through it").
  - **Strings 2 and 3 are true but loose (recommended, Z1 and Z2).** They say "equal to (M1) wherever no Zeno history passes ..., departing only where one does". This is true, but it leaves out the $z=0$ case, so Z1 and Z2 state it as $z=0$ / $z>0$. The PR body's claim that these statements "are already scoped to states with no Zeno history passing" holds for the "equal" half only.
- **"Narrowed" as a label.** #270 left open whether the ruling excludes (Z-iii)/(Z-vii) where they depart, or leaves that to the Zeno call ("not math, and the record is silent"). The status line's "narrowed" does not record that question. **Z5 (recommended)** adds it.

## 4. Readiness, refresh section

- **Gap 4 Open (string 18, as revised by commit 2): faithful to the record.**
  - §9 supplies the agreement: "finite-cut marginals are consistent by construction" (Ionescu-Tulcea), with finite stars and dead ends kept in the cut (§9 *Dead ends*, unconditioned).
  - C35's row gives $X$ "undefined (state-level gate ...), $1/2$ (history-level excision, mass kept ...), or $1$ (Zeno mass conditioned away)". The Zeno note gives the cut's $1/2$ past the accumulation under §9's dead-end convention.
  - "No Zeno history passes" is the correct scope for this claim, because under (Z-i) even a measure-zero Zeno history leaves weights undefined.
  - It leaves out (Z-0), (Z-vi), (Z-vii) and (Z-ix), but "turns on the convention" covers them. No string.
- **Gap 4 Waits on (string 19).** It matches #270 §2's re-mark: the ruling selects T2's per-step side. #270 lists two open questions, the closure of T2 and #139 (b), but the string names only T2's. **R2 (recommended).**
- **Gap 4 Cost (strings 20 and 21).** Accurate. "(Z-0)–(Z-viii)" remains, though the note runs to (Z-ix). That staleness predates this PR (brief §5 item 3) and is not this PR's to fix.
- **FD2:** unchanged.

## 5. Same scope in #273

#273's §11 sentence "so the two give the same weights" has the same overstatement as commit 1's string 18. #275 F1 and F3 give it the same scope as commit 2, "wherever no Zeno history passes (finite stars; dead ends kept in the cut, §9)", with the same three-way C35 split, so the two files will agree once F1 is applied. My #273 review (`reviews/v0.9.1-m1-knockons-diff-literature.md`) endorses F1 and F3. It amends #275 F2, which repeats the departure overstatement for (Z-iii) ("wherever a Zeno history passes"), to the positive-mass scope.

Two claims, two scopes:
- **Agreement of the cut and completed-history weights** needs "no Zeno history passes", because of (Z-i).
- **Departure of (Z-iii)/(Z-vii) from depth-1** needs "$z>0$".

## 6. Exact strings

Each OLD occurs once at `7f5df34`. All seven were applied together by script (Zeno note 3,931 → 4,000 words).

Required: Z3, Z4. Recommended: Z1, Z2, Z5, Z6, R2.

**Z3** (required), `notes/zeno-mass-scoping.md`, (c) row (Z-iii):
- OLD: `so they are no longer depth-1, where a Zeno history passes through the state; elsewhere they equal (M1)`
- NEW: `so they are no longer depth-1, where the Zeno mass $z$ at the state is positive; where it is zero they equal (M1)`

**Z4** (required), `notes/zeno-mass-scoping.md`, (c) row (Z-vii):
- OLD: `(§8.2 items 6–7), where a Zeno history passes through the state; elsewhere they equal (M1)`
- NEW: `(§8.2 items 6–7), where the Zeno mass $z$ at the state is positive; where it is zero they equal (M1)`

**Z1** (recommended), `notes/zeno-mass-scoping.md`, (a) row (Z-iii):
- OLD: `| $z<1$. Narrowed under the (M1) ruling: equal to (M1) wherever no Zeno history passes through the state, departing only where one does`
- NEW: `| $z<1$. Narrowed under the (M1) ruling: equal to (M1) wherever the Zeno mass $z$ at the state is zero, departing only where it is positive`

**Z2** (recommended), `notes/zeno-mass-scoping.md`, (a) row (Z-vii):
- OLD: `| wherever some arm stays. Narrowed under the (M1) ruling: equal to (M1) wherever no Zeno history passes through the state, departing only where one does`
- NEW: `| wherever some arm stays. Narrowed under the (M1) ruling: equal to (M1) wherever the Zeno mass $z$ at the state is zero, departing only where it is positive`

**Z5** (recommended), `notes/zeno-mass-scoping.md`, status line:
- OLD: `and (Z-iii)/(Z-vii) are narrowed;`
- NEW: `and (Z-iii)/(Z-vii) are narrowed (they equal (M1) where the Zeno mass $z$ at the state is zero; whether the ruling excludes them where it is positive, or leaves that to the Zeno call, is open, #270 §2);`

**Z6** (recommended), `notes/zeno-mass-scoping.md`, status line:
- OLD: `counting (Z-iv) is dropped (kept below as a record row)`
- NEW: `counting (Z-iv) is dropped, that is, set aside while the L3 ruling holds and open to reversal with it (kept below as a record row; "dropped" has this sense throughout)`

**R2** (recommended), `reviews/born-rule-readiness.md`, gap 4 Waits on:
- OLD: `and whether T2 is closed stays open;`
- NEW: `and whether T2 and #139 (b) are closed stays open;`
