# Review: litmus note, David's "Genuine emergence" clarification (#281), record and diff check

**Verdict: PASS with notes.** Heads read: #281 head `f4b0a9f` (one commit, branch `lead/litmus-genuine`), base main `b423130`. Describe-only; no pick and no lean.

**#279 history.** #279 merged as `b423130`, at head `54b0c40`. All ten of #280's file strings are present on main: O1–O7, P1, P2 and N1 (checked by script).

## Quote

- **Byte check.** The block quote matches the relayed text exactly once, with one normalisation: the curly quotes around "genuine" (U+201C, U+201D) are straight quotes in the file. No other character differs, and the quote has no other non-ASCII character.
- **Lowercase.** The lowercase "born" in "the born rule" is preserved verbatim, which is right. It is the file's only lowercase "born rule".
- **Placement.** The quote follows the "Purpose" quote and precedes `## Substitution test`.
- **Attribution.** The heading reads "Genuine emergence (David, 2026-10-11, about 10:09 AM ET, given directly to the Physics Lead in chat and relayed here; the exchange is not recorded in this repository; part of the L3 answer)". This is the note's standard form.
- **"Not signed."** Like the note's other headings, the heading does not say "not signed". The "Purpose" ruling gets "relayed, not signed" in the Outcome mapping status, but the new ruling does not. G1 adds it. Nothing records either ruling as signed.

## The resolved item

The new Status sentence reads: "settles how the working answer's "Genuine emergence needs YES on all four" reads: YES on all four is necessary but not sufficient for genuine emergence, which needs both a full derivation (emergence) and no circularity (genuine); this litmus test addresses only the second."

- **Faithful:** "necessary but not sufficient", and the two-part definition of genuine emergence.
- **"Addresses only the second."** David says the test "focuses on the word "genuine"". "Only" comes from the 10:03 "Purpose" ruling ("designed to detect cheating and that's it"), not from these words. That reading is consistent, but this sentence cites only the "Genuine emergence" ruling.
- **"Settles how ... reads" goes further than his words.** The open item asked whether the sentence states the emergence bar or the test's pass condition. His words settle that YES on all four is a necessary condition for genuine emergence. They do not say whether YES on all four is also the test's pass condition. The status sentence makes no explicit overreach, such as calling YES on all four the pass condition, or saying a pass shows there is no cheating anywhere. But "settles" closes the item fully.

**The subtle point, stated neutrally.** The words admit two readings:
- **(a)** The four LTs together are the "genuine" test. YES on all four is its pass condition, and full derivation is the further requirement that makes the pair sufficient. On this reading, a NO on any LT is a failure, which is in tension with the sorting principle's "completeness gap" category.
- **(b)** The LTs span both questions. Some, for example LT3, bear on emergence rather than genuineness, and only some NOs are cheating signals.

The file states neither reading. It leaves the question to the per-LT sort, which correctly stays "Lead's draft, pending David", including all four LT marks. **G1 (recommended)** scopes the sentence to what the words settle and records the remaining question as open.

## Consistency, diff and guardrails

- **Consistency.** The new quote is consistent with "Scope and outcomes" ("Success ... does not prove emergence") and with "Purpose": both say a pass does not mean a full derivation.
- **David's L3 text.** Every line of the note above "Outcome mapping" on main is present unchanged. David's existing L3 text is not edited.
- **Diff.** It touches only the new heading, the quote and the Status paragraph's last sentence. The open-item sentence is replaced; it is the Lead's text, not David's.
- **Words (`str.split`, whole file):** 2,713 → 2,825, +112.
- **New tokens:** 2026-10-11, 10:09, the "4" in "all 4" twice, and the 3 of "L3". No number is removed.
- **Guardrails:**
  - Forbidden words (egalit, cartoon, GRW, 4-geon, spin-foam, \chi): 0.
  - No Born, $|a|^2$ or 1/N result claim; "|a|" stays at 1.
  - "signed" is unchanged (2, both "not signed").

## String (OLD occurs once at `f4b0a9f`)

**G1** (recommended), `notes/born-litmus-test.md`, Outcome mapping status:

OLD:
```
David's "Genuine emergence" ruling above settles how the working answer's "Genuine emergence needs YES on all four" reads: YES on all four is necessary but not sufficient for genuine emergence, which needs both a full derivation (emergence) and no circularity (genuine); this litmus test addresses only the second.
```
NEW:
```
David's "Genuine emergence" ruling above (relayed, not signed) settles part of how the working answer's "Genuine emergence needs YES on all four" reads: YES on all four is necessary but not sufficient for genuine emergence, which needs both a full derivation (emergence) and no cheating via circularity (genuine); this litmus test focuses on the second, and with the "Purpose" ruling it is designed to detect cheating only. Open for David, not decided here: whether YES on all four is also this test's pass condition, so that a NO on any LT is a failure, or whether some LTs (for example LT3) bear on emergence rather than on genuineness; this is the per-LT sort below.
```
