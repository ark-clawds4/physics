# Pressure test: Claude's critique of the litmus, MERW and substitution notes (#263)

**Read at:** `main` `c483425`. **Target record:** `reviews/born-litmus-merw-substitution-claude-opus.md` (#263; read at `05b74bc`, and the three notes are unchanged between that commit and `c483425`). **Reference:** `versions/v0.9-prose.md`, `papers/observer-space-ontology.md` (Paper 1), `reviews/born-rule-readiness.md` at `c483425`.
**Verdicts:** CONFIRM (applied as written), QUALIFY (applied with the amendment stated), REJECT, FOR DAVID (neutral; nothing applied).
**Rules kept.** David's L3 answer in `notes/born-litmus-test.md` (from "The question" through the conjecture paragraph) is byte-identical after commit 2. Anything that would restate it is under FOR DAVID. #263's outcome-mapping block goes in as **"Outcome mapping (Lead's draft, pending David)"**, after the L3 answer. Record-side content (literature citations, quotations and characterisations not already in v0.9, Paper 1 or readiness) is left as a marked placeholder `[RECORD STRING PENDING — Literature: …]` (§4). Quotations of v0.9, Paper 1 and readiness were checked against the files. This record makes no pick, Born derivation, $|a|^2$ or $1/N$, law of $R$ or (M1)/(M2) choice, edits neither v0.9 nor the essays, and argues neither for nor against Deutsch–Wallace.

## 1. Recomputed (`merw263.py`, `r3settle.py`; graph as `merw_rule.py`)

| Quantity | #263 | Here |
|---|---|---|
| States, SCCs ($c=0.01$, `c33r.py`) | 87,356; 58,237 (29,119 2-cycles + 29,118 singletons) | the same |
| Shares, $L$ arcs after the first step | 0.400, 0.381974, 0.381966, 0.308087, 0.137830, 0.011828, 0.005865 | the same (these are the note's pinned values) |
| Shares, $L$ arcs in all | $1/3$, $55/144$, 0.381966, 0.314054, 0.139361, 0.011839, 0.005868 | the same; $1/3$ and $55/144$ exact |
| Fibonacci range | $N_L=F_{L+2}$ for $L\le28$; $N_{29}=F_{31}-7$; 7 segment states with no jump at 28 arcs | the same (exact integers) |
| $L\times$share (in all) | 11.84, 11.74 | 11.8390, 11.7353 |
| Growth | 14.185436 | 14.185436; then 14.092175 ($N_{4000}/N_{2000}$), 14.045952 ($N_{8000}/N_{4000}$), toward 14 |
| $c=0.1$ | $N_L=L+1$; share $1/(L+1)$ in all | the same ($L\le40$ exact; share $1/2001$ at 2000) |
| Converses of admissible edges passing (a) | 0 of 29,118; 0 of 2 | the same |
| Eigenvalue 1, geometric multiplicity | 14,478 (rank of $A-I$ 72,878) | rank 72,878 over GF($2^{31}-1$), so 14,478; index 15 not recomputed (consistent with the growth exponent tending to 14) |
| Nonnegative right eigenvector | unique, on the root orbit | confirmed by hand: for any non-root orbit, $v_{\rm lo}=v_{\rm hi}+\sum$(its jump children) and $v_{\rm hi}=v_{\rm lo}+\sum$(…) force the children's sum to 0, and its own jump-arrival state equals its segment value, so nonnegativity puts every non-root value at 0 |
| Toys (M15, M23) | 0.933865 / 0.935064 / 0.967549; $K_4$ 0.957631; off $K_4$ near 0.0425 | the same (off $K_4$: 0.042369, 0.042452, 0.042466, 0.042468) |
| B3 grain toy; X11 odds | $1/3$ each against $1/2,1/4,1/4$; $p=0..3$: 0.5→0.667, 0.396→0.481, 0.3→0.3, 0.219→0.166 | the same |
| Quotations | v0.9 and Paper 1 passages used by B2, M8, X4, X13, X24, X29 | each found in the file (`c483425`) |

**R3 settlement.** `merw_rule.py` (`8ba694f7…`) re-run at $c=0.01$ reproduces the note's pinned outputs byte for byte (`/workspace/g249/r001_kr.txt`, `r001_robust.txt`). The exact counts (`r3settle.py`) are below.

| Classifier | States | Segment / jump-arrival / dead-end | Decision states | Orbits | Stuck (no admissible edge) |
|---|---|---|---|---|---|
| `kr.classify` (`g154/kr.py`) | **87,357** | 58,238 / 29,118 / 1 | 29,119 | 29,119 | **14,477** |
| `classify_robust` (`g168/c33r.py`) | **87,356** | 58,238 / 29,118 / 0 | 29,118 | 29,119 | **14,478** |

The note's figure is **right**: it is not a typo. The one difference is a single extra admissible edge. From the apastron $r=16.900001215$ of $[16.158567,16.900001]$, the target $r=17.147960961$ is labelled a plunge by `kr.classify`, with range $[0,17.147961]$. That range contains the source, so (a) passes and the jump goes to a dead end. `c33r.py` labels the same target a bound orbit $[17.147937,17.147961]$ (relative width $1.4\times10^{-6}$), which (a) rejects.

The edge adds the dead-end state and makes its source a decision state. It also takes one orbit off the list of orbits with no admissible edge, which gives 14,477 under `kr.classify`. Counted as orbits with no *bound* admissible edge, both classifiers give 14,478. The orbit sets agree to $10^{-9}$, and the shares agree to 6 decimals. The jump-count laws agree only to within one unit in the fourth significant figure, so the note's "to 4 figures" is corrected.

#263 §1 and §6 say that the classifiers agree on every candidate and that this candidate is "inadmissible under either label". That holds for #263's own rebuilds, not for `kr.py`'s plunge convention, under which this target is admissible. This matches #258's census (`g258/census.py`), which found the same single disagreement.

## 2. Verdicts

| Item | Verdict | Reason / amendment |
|---|---|---|
| B1 outcome mapping | QUALIFY | Applied as **"Outcome mapping (Lead's draft, pending David)"**. It is placed after the whole L3 answer, not after "Pre-emptive use", because "Substitution test" is also part of the L3 answer, so the answer stays contiguous. The Dizadji-Bahmani characterisation becomes a placeholder (§4). FD1 |
| B2 LT2 vs §8.4 | QUALIFY | In the pending block, through B1's string. Quotes checked (§8.4: "within an independently named class of uniform rules", "or else states an empirical target"; "work on circularity"; §10 "drawn by hand"). FD2 |
| B3 LT3 tilt | QUALIFY | In the pending block. Grain toy recomputed. FD3 |
| B4 open calls | QUALIFY | Applied. The pointer goes to the pending block, and the Baker citation becomes a placeholder. Readiness "Waits on" entries checked. Whether LT2 names these: FD2 |
| B5 substitution condition | QUALIFY | Inserting text inside David's paragraph would change the L3 text, so the content goes into the pending block as a bullet. FD4 |
| B6 pointer to the substitution note | CONFIRM | |
| B7 the conjecture's "pass" | QUALIFY | Moved from David's conjecture paragraph into the pending block. FD5 |
| B8 Labels line | CONFIRM | The Labels line is the Lead's, not the L3 answer |
| B9 gloss | CONFIRM | Through B6, on the Lead's "Where it connects" line |
| M1 two conventions | CONFIRM | Recomputed (§1) |
| M2 (a–d) converse pairs | CONFIRM | 0 of 29,118 and 0 of 2 recomputed. §5's definition of backward pairs checked |
| M3 (a, b) $\psi^{\rm L}\psi^{\rm R}$ | QUALIFY | The mathematics is applied. The source for the directed case is a placeholder (§4) |
| M4 R1's reasons | CONFIRM | SCCs, geometric multiplicity and the right eigenvector recomputed. Index 15 is kept as #263 states it (§1) |
| M5 (a–c) LT3 row, R3 | CONFIRM | |
| M6 (a, b) graph vs completed histories | CONFIRM | |
| M7 LT2 row | CONFIRM | Escaped pipes keep 4 cells (cell counts checked) |
| M8 F-M1 costs and places | CONFIRM | §11's two "MERW hazard" mentions verified. Whether to reword option (ii): FD6 |
| M9 superposes vs cancels | CONFIRM | It revisits #253's string M2, so Literature should be told (no message sent from here) |
| M10–M16 | CONFIRM | M11, M15 and M16 (through M2d) recomputed. M12's O6 adds an option without picking one |
| M17 R3's differing state | QUALIFY | Settled (§1). The string names the state and corrects "to 4 figures" |
| M18 Scope exception | QUALIFY | The exception is applied, and the source is a placeholder |
| M19–M27 | CONFIRM | Commits `001dde2`, `974aeec` and `f8917fb` verified. Figures recomputed |
| X1 S1 traced to premises | QUALIFY | Applied. The Wallace quotation is replaced by a pointer to the table's existing wording |
| X2, X3 S3 cells, "in part" | CONFIRM | C26 checked |
| X4, X5 cost lines | CONFIRM | Paper 1 §8 "proportional to $|a_n|^2$" checked |
| X6 branch number not well defined | QUALIFY | The slot and its neutral S3 sentence are applied. The argument and its replies are a placeholder |
| X7 Barnum et al. and the reply | QUALIFY | Placeholder |
| X8 table (ii) | QUALIFY | The MERW-row fix and the exhaustion row are applied. The outcome-labelling row is applied with its citation as a placeholder |
| X9 §8.4 vs LT2 | CONFIRM | Same reading as B2. FD2 |
| X10 minimal edits | CONFIRM | |
| X11 (a, b) the substitute family | QUALIFY | The 2-norm point, $p=0$ and the missing equal-amplitude probe are applied, with odds recomputed. The physics-side results and the fatness rule are placeholders |
| X12 S1 for DW already published | QUALIFY | Placeholder, with the conditional consequence kept |
| X13 Paper 1 §9 | CONFIRM | The quotation is in Paper 1 |
| X14 panel option | QUALIFY | The option and its costs are applied. The case list and citations are a placeholder |
| X15 empty break column | CONFIRM | |
| X16 Dizadji-Bahmani | QUALIFY | Placeholder |
| X17 Wallace 2010 label | QUALIFY | Placeholder |
| X18–X21 | CONFIRM | C35 and V2 values from `notes/zeno-mass-scoping.md` |
| X22 references | QUALIFY | A References heading with a placeholder |
| X23–X27, X29 | CONFIRM | C13's 3/5 against 1/2 checked |
| X28 (R-c)'s reason | QUALIFY | The unitarity clause is applied. The $p$-norm result is a placeholder |
| X30 balance | QUALIFY | Placeholder |
| #263 §1/§6, R3 "not reproduced" / "inadmissible under either label" | REJECT | It reproduces exactly under `kr.py` (§1) |
| #263 §3, §4.3, §5 answers | CONFIRM | Used through the strings; no critic question is rewritten |
| #263 §5.4, outside the targets (readiness §1.1 items; readiness gap 4's "(Z-0)–(Z-viii)") | CONFIRM | Not applied: readiness is outside this PR. Left for a readiness pass |

**Tally:** 66 numbered items (B1–B9, M1–M27, X1–X30): 45 CONFIRM, 21 QUALIFY, 0 REJECT, 0 FOR DAVID as item verdicts. In addition: 1 REJECT (#263's R3 statement), and the FOR DAVID list below.

## 3. FOR DAVID (neutral; nothing applied to the L3 answer)

- **FD1 (B1).** Adopt, amend or drop "Outcome mapping (Lead's draft, pending David)". In particular, decide which LT outcomes return a failure and which only withhold a pass, and whether "YES on all four" and "no circularity detected" are one bar or two.
- **FD2 (B2, B4, X9).** Decide whether LT2 is restated against §8.4's two branches (named class; empirical target), and whether LT2 names what is counted (individuation of arms, outcome labelling) and the bridge premise from symmetric cases to equal weight.
- **FD3 (B3).** Decide whether LT3 is restated, given its uneven bearing on (M1) and (M2), and how "irrelevant" is defined.
- **FD4 (B5).** Decide whether the substitution paragraph's failure condition is restated. Read literally, every valid derivation meets it, so the verdict turns on S3.
- **FD5 (B7).** Decide whether "Scope and outcomes" governs the substitution test, which sets what the conjecture's "pass" would mean.
- **FD6 (M8).** Option (ii) of F-M1 says "could pass", against "Pre-emptive use". It could be reworded to "what a claim through it would have to show under LT1–LT4". F-M1 itself stays David's call.
- **FD7 (#263 §5.4).** Which paper the substitution note's "main paper" means: v0.9 or a later version.

## 4. Placeholders for Literature (16)

Litmus note:
1. The "Outcome mapping" LT3 bullet: who disputes the fine-graining and branching-indifference premise, and on what grounds (#263 §2.3, X16).
2. "Where it connects" (B4): a citation for circularity at the outcome labelling (Baker 2007 proposed).

MERW note:
3. Section (a) (M3a): the directed-case source and theorem (Parry 1964 proposed).
4. The Scope line (M18): the same source, as the exception to v0.9's literature.

Substitution note:
5. X6: Wallace's argument that branch number is not well defined, and the replies to it.
6. X7: Wallace 2003's reply to Barnum et al., and Greaves 2004.
7. X8: the outcome-labelling row's citation (Baker 2007).
8. X11a: physics-side results (Aaronson 2004; Galley and Masanes 2018).
9. X11b: a published rule weighting equal-amplitude branches unequally (Albert 2010), and where Wallace §9 locates its break.
10. X12: S1 for DW already published (Wallace 2010 §9).
11. X14: the panel's cases and citations.
12. X16: Dizadji-Bahmani's own target and argument.
13. X17: the preprint, chapter and book labels, and what is unchecked against the book.
14. X22: the reference list.
15. X28: the $p$-norm result (Aaronson 2004).
16. X30: a general defence of the programme, for balance (Read 2018).

## 5. Applied in commit 2

- **Litmus note:** a one-line change to the Labels line (B8 plus a "Revised" sentence); the pending-David block (B1–B3, B5, B7); B4; B6 (with B9). The L3 answer is byte-identical (3,941 bytes).
- **MERW note:** M1–M15 and M17–M27 (M16 through M2d), a "Revised" line, and two pin lines.
- **Substitution note:** X1–X30 as in §2, and a "Revised" line.
- **Checks (`verify263.py`):** no value-number removed from any file; every added number is in `merw263.out` or `r3settle.out`, or is a listed pointer (C13, C35/V2, interval endpoints, PR numbers); table cell counts unchanged.

**Words:** litmus 843 → 1,985; MERW 1,417 → 2,810; substitution 1,451 → 2,979.

## Pins

These scripts are on the shared machine, outside the repository (SHA-256):
- `g249/merw_rule.py` `8ba694f70b4cba5b2e930e1e4e7fcf60a9b23f77d3e0c7c6f2238e61bb82d871`
- `g263/r3settle.py` `f3f317d277507231a9ed12f13743a30a1da76b841ccd52b972efbee017c38042`
- `g263/merw263.py` `a8137c35d0602137f103f49b7f79aed889ee9b283429eff7b8353512c4ec160f`
- `g263/parse263.py` `1ab728a2f94a081d0a803bb09657acbc6aefaad448c4002cd611aa406e00a2e1`
- `g263/apply263.py` `a9f782f066e778e22e2df69dc5e73dc3e1822b8a4cabfc08c881c5badd4e729c`
- `g263/verify263.py` `da92f166081ef9df4b67c3cec4a0c88f7d21ee400874137f2de5de4623167480`

They import `g154/kr.py` `0432cc20f56afbc3ad862b16de8f825bf9e1d4a490cde07ad8e5740f9d872dee` and `g168/c33r.py` `f9e9c31b61e9c3889245af8b70cec65bb4a105c50ccbd96c75fd488e431dcd45`. Python 3.13 runs in `/workspace/g128/venv`.
