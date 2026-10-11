# Review: litmus note, David's FD1 "Purpose" ruling (#279), record and diff check

**Verdict: HOLD (narrow).** Heads read: #279 head `bf5dda4` (one commit), base main `43bf7a4`. `reviews/born-litmus-merw-substitution-pressure-test.md` (#264, merged as `7fab909`) was read for §3. Describe-only; this review makes no pick and has no lean.

The diff is clean, and David's L3 text is untouched. The HOLD is for one record point. The LT2 and LT3 marks ("cheating signal", "completeness gap") are the Lead's application of David's principle, not David's own sort, yet they are presented without the "Lead's draft, pending David" marker that the note uses for everything that is not David's words. Strings O1–O7 restore it. Separately, the PR body's FD marks overstate what the ruling's words settle for FD2, FD3 and FD5.

## 1. The quote and its heading

- **One block quote.** David's words appear exactly once, as a block quote of 86 words, in the "Working answer (L3)" section. It sits after "Pre-emptive use" and before `## Substitution test`. Each of its distinctive phrases occurs once as quoted ("tripping over our feet", "designed to detect cheating").
- **What I can and cannot verify.** I have no verbatim copy of David's words, so I cannot verify the quote word for word. I can verify that its content matches the relayed summary: the test is designed only to detect cheating; passing means no cheating was detected; whether the full Born rule is derived is a separate question the test does not answer. I also cannot verify the exact heading wording Physics Lead specified, or whether David set a hold level for this ruling. The heading files it as "part of the L3 answer", as the note's other relayed rulings are filed.
- **Attribution.** The heading records the date, the time "~10:03 AM ET", relay and "not recorded in the repository". It says "relayed to the Physics Lead in chat". The ruling was given directly in the Physics Lead's chat and relayed from there, which is how the note's other headings put it ("given directly to the Physics Lead in chat and relayed here; the exchange is not recorded in this repository").
  - **P1 (recommended)** aligns the heading with that standard and replaces "~" with "about".
  - "not signed" appears in the Outcome mapping status ("relayed, not signed; #264 FD1"). The note's earlier rulings don't carry it in their headings either, so it is consistent.
- **Paraphrase presented as a quote.** None in quotation marks.
  - The "*Purpose (David's ruling)*" bullet paraphrases the ruling and uses no quotation marks. Its question "was the Born rule put in by hand?" is David's own wording from "Scope and outcomes" (2026-10-10).
  - Its last clause, "it is possible to pass, being innocent of cheating, and still not have derived the full Born rule", follows the quote nearly word for word without quotation marks. **P2 (optional)** makes it plainly a reference to the quote.

## 2. David's existing L3 text

- **Byte-identical:** the text from `## The question` through the "Scope and outcomes" paragraph, the "Pre-emptive use" paragraph, and the whole `## Substitution test` section, including David's conjecture. Checked by substring match.
- "Genuine emergence needs YES on all four" occurs once before and after, unedited.
- **The new FOR DAVID item is in the PR body only.** It is not in the file or in #264's FD list, so once merged it is recorded nowhere in the repository. **N1 (optional)** records it, neutrally, in the Outcome mapping status.
- **The tension, stated neutrally.** The sentence can be read two ways:
  - As the bar for genuine emergence, the question the ruling separates out. On this reading it is consistent with the ruling: YES on all four is what full emergence would need, and the test's pass condition is only "no cheating detected". "Scope and outcomes" already said "Success means no circularity has been detected. It does not prove emergence."
  - As the test's pass condition. On this reading it conflicts with "This litmus test is designed to detect cheating and that's it": a NO from a source other than injection would fail a test that, per the ruling, asks only about cheating.
  - "The question" itself ("whether the Born rule genuinely emerges ... rather than being written in by hand") names both questions in one sentence, which is the conflation the ruling describes.
  - The record does not say which reading David intends. Neither reading is preferred here.

## 3. Outcome mapping: what the ruling settles

- **Purpose: settled by the quote.** Removing the pending marker is earned.
- **Sorting principle: earned in substance.** "designed to detect cheating and that's it" and "innocent of cheating ... and yet we still have not derived the full Born rule" together give: a NO is a failure of this test only if it signals cheating, and any other shortfall bears on the separate derivation question.
  - The terms "cheating signal" and "completeness gap" are the Lead's labels, not David's. They add no content, so no string.
- **Per-LT sort: not David's.** The ruling's words do not mention any LT, so every per-LT mark is the Lead's application. The PR marks LT2 and LT3 as "settled by the principle" in its body and leaves them unmarked in the file, while LT1 and LT4 stay pending. Neither the record nor the ruling distinguishes them.
  - **LT2.** The cheating-signal reading is not automatic. A NO on LT2 can mean inputs not yet fixed for independent reasons, for example because no law of R exists. That is an incompleteness, not an injection. The note's own LT2 bullet distinguishes a target weight fixed outside the claim from a quantity needing an LT1 object.
  - **LT3.** A NO from a cut or grain chosen to produce a target would be an injection. The draft routes that case to LT2, which is a reasonable reading but is the Lead's.
- **Answer to Ontology:** yes. On the record and on the standard that anything not David's own words is marked as a draft pending him, the LT2 and LT3 marks should stay "Lead's draft, pending David". O1–O7 do this. The purpose and the principle keep their settled status.

## 4. FD marks against #264 §3 (in the PR body, not the file)

| FD | #264 §3 asks | PR body mark | On the ruling's words |
|---|---|---|---|
| FD1 | adopt, amend or drop the block; which LT outcomes fail; one bar or two | partly settled | **Earned.** Two bars ("one binary litmus test" cannot "answer two binary questions"); the failure criterion is cheating only. Which LTs fail is not settled (all four sorts pending, §3 above). |
| FD2 | restate LT2 against §8.4's two branches; whether LT2 names what is counted and the bridge premise | narrowed | **Not earned by the words alone.** The "narrowing" rests on the Lead's LT2 sort, which is pending. On the words, FD2 is untouched. It is narrowed only if the LT2 sort is adopted. |
| FD3 | restate LT3, given its uneven (M1)/(M2) bearing; define "irrelevant" | narrowed | **Not earned by the words alone,** for the same reason: it rests on the LT3 sort. (The separate (M1) ruling at L3 bears on FD3's (M1)/(M2) clause, but that is not this ruling.) |
| FD4 | substitution failure condition, S3 | untouched | **Correct.** |
| FD5 | does "Scope and outcomes" govern the substitution test | narrowed | **Not earned.** The ruling speaks of "This litmus test". If "Scope and outcomes" governs the substitution test, its "pass" was already fixed on 2026-10-10 ("Success means no circularity has been detected. It does not prove emergence"), as the note's *The conjecture's "pass"* bullet already says. Untouched. |
| FD6, FD7 | F-M1 option (ii) wording; "main paper" | not listed | Untouched. The body should list them for completeness. |

## 5. LT3 sentence, Labels line and "Where it connects"

- **LT3 sentence.** "Under the per-LT sort above, a NO on LT3 is a completeness gap, so this uneven bearing concerns completeness, not a cheating verdict." This is accurate as an inference from the sort, and it adds to the bearing without contradicting it. Because the sort is the Lead's, **O7** marks it.
- **Labels line.** "David's purpose ruling of 2026-10-11 (#264 FD1; "Purpose" below) settles the test's purpose and the sorting principle; the parts it does not settle stay pending David." Accurate, given §3 above. #264 FD1 resolves (`reviews/born-litmus-merw-substitution-pressure-test.md` §3), and "Purpose" resolves to the new heading.
- **"Where it connects."** "(see "Outcome mapping")" resolves to the renamed heading, whose LT2 bullet carries the §8.4 analysis.

## 6. Guardrails and diff

- **Scope:** one file, with 6 lines removed and 18 added.
  - The changes are the Labels line, the Purpose heading and quote, and the Outcome mapping heading, status and new bullets.
  - Also changed: the end of the *Outcomes* bullet, one new sentence in the *LT3* bullet, and the "Where it connects" LT2 pointer.
  - The *LT2*, *Substitution condition* and *The conjecture's "pass"* bullets are unchanged. Nothing else in the file changed.
- **Words (`str.split`, whole file):** 2,076 → 2,659, +583. Confirmed.
- **New tokens:** not only "264" and "10:03". Also new are the date 2026-10-11 (twice), "263" (#263 B1), "0.9" (readiness v0.9 refresh) and "6" (gap 6), plus LT digits. All are labels, dates or times. No number is removed, and no physics number is added.
- **Forbidden words:** 0 hits for the guard list (egalit, cartoon, GRW, 4-geon, spin-foam, \chi).
- **No result claims:** "Born" occurs 15 → 22 times, and every new use is in "was the Born rule put in by hand" or "the full Born rule [derived]". There is no Born rule, $|a|^2$ or 1/N result. "law of R" still occurs 3 times, and no law of R is given.
- **Nothing recorded as signed:** "signed" occurs 0 → 2 times, both "relayed, not signed" in the Outcome mapping status, and the PR body's "relayed, not signed". No Everett-vs-Deutsch–Wallace framing is added ("Deutsch" stays at 2).
- **Relay standard:** consistent with "Scope and outcomes" and "Pre-emptive use", apart from P1's wording.

## 7. Exact strings

Each OLD occurs once at `bf5dda4`. All ten file strings were applied together by script (2,659 → 2,713 words).
- Required: O1–O7.
- Recommended: P1.
- Optional: P2, N1.
- PR body (recommended): B1, B2, and the FD marks in §4.

**O1** (required), `notes/born-litmus-test.md`, Outcome mapping heading:

OLD:
```
## Outcome mapping (purpose and sorting principle settled by David's "Purpose" ruling; per-LT detail Lead's draft)
```
NEW:
```
## Outcome mapping (purpose and sorting principle settled by David's "Purpose" ruling; per-LT sort Lead's draft, pending David)
```

**O2** (required), Outcome mapping status:

OLD:
```
Everything else here stays **Lead's draft, pending David**, including the sorts of LT1 and LT4.
```
NEW:
```
Everything else here stays **Lead's draft, pending David**, including the per-LT sort of all four LTs.
```

**O3** (required), Per-LT sort bullet:

OLD:
```
- *Per-LT sort.* Each mark rests on David's words and on the LT's own wording.
```
NEW:
```
- *Per-LT sort (Lead's draft, pending David).* Each mark applies David's principle to the LT's own wording; none is David's own sort.
```

**O4** (required), LT2 mark:

OLD:
```
  - **LT2 (Prior inputs): cheating signal.**
```
NEW:
```
  - **LT2 (Prior inputs): cheating signal (Lead's draft, pending David).**
```

**O5** (required), LT3 mark:

OLD:
```
  - **LT3 (Robustness): completeness gap.**
```
NEW:
```
  - **LT3 (Robustness): completeness gap (Lead's draft, pending David).**
```

**O6** (required), end of the *Outcomes* bullet:

OLD:
```
Which LT outcomes return a failure follows the per-LT sort above; the sorts of LT1 and LT4 are pending David.
```
NEW:
```
Which LT outcomes return a failure follows the per-LT sort above, which is the Lead's draft, pending David.
```

**O7** (required), new sentence in the *LT3* bullet:

OLD:
```
Under the per-LT sort above, a NO on LT3 is a completeness gap,
```
NEW:
```
Under the per-LT sort above (Lead's draft, pending David), a NO on LT3 is a completeness gap,
```

**P1** (recommended), Purpose heading:

OLD:
```
**Purpose (David, 2026-10-11, ~10:03 AM ET, relayed to the Physics Lead in chat; not recorded in the repository; part of the L3 answer)**
```
NEW:
```
**Purpose (David, 2026-10-11, about 10:03 AM ET, given directly to the Physics Lead in chat and relayed here; the exchange is not recorded in this repository; part of the L3 answer)**
```

**P2** (optional), *Purpose (David's ruling)* bullet:

OLD:
```
it is possible to pass, being innocent of cheating, and still not have derived the full Born rule.
```
NEW:
```
as the quote above puts it, a pass is compatible with not having derived the full Born rule.
```

**N1** (optional), Outcome mapping status, records the new FOR DAVID item:

OLD:
```
"Pre-emptive use", "Purpose" and "Substitution test") is unchanged.
```
NEW:
```
"Pre-emptive use", "Purpose" and "Substitution test") is unchanged. Open for David, not decided here: whether the working answer's "Genuine emergence needs YES on all four" states the emergence bar or the test's pass condition.
```

**B1** (recommended), PR #279 body, Per-LT sort table, LT2 row:

OLD:
```
| **cheating signal** (settled by the principle) |
```
NEW:
```
| **cheating signal** (Lead's draft, pending David) |
```

**B2** (recommended), PR #279 body, Per-LT sort table, LT3 row:

OLD:
```
| **completeness gap** (settled by the principle) |
```
NEW:
```
| **completeness gap** (Lead's draft, pending David) |
```

**PR body FD marks (recommended).**
- FD2 and FD3: "untouched by the ruling's words; narrowed only if the Lead's LT2/LT3 sort is adopted".
- FD5: "untouched (the ruling concerns "this litmus test"; "Scope and outcomes" already fixed "pass" on 2026-10-10)".
- Add FD6 and FD7 as untouched.
