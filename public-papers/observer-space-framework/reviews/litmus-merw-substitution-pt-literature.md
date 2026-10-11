# Diff check of #264, and record strings for its 16 placeholders — Literature

**Part 1 verdict: HOLD (narrow).** One required string (R1, the R3 mechanism). Everything else checks.
**Heads read:**
- #264 head `fba589d`: commits `2abfbe0` (record) and `fba589d` (apply).
- Base and main `c483425`, with #263 at `c483425`.
- v0.9 and readiness read at `c483425`.
- Re-checked before filing.

**Scope:** `reviews/born-litmus-merw-substitution-pressure-test.md` and the three notes. These are the only files that change. Paper 1 and `versions/` are untouched.

## Part 1: diff check

1. **Counts.** I recounted the §2 table myself:
   - B1–B9: 6 QUALIFY (B1–B5, B7) and 3 CONFIRM.
   - M1–M27: 3 QUALIFY (M3, M17, M18) and 24 CONFIRM.
   - X1–X30: 12 QUALIFY (X1, X6, X7, X8, X11, X12, X14, X16, X17, X22, X28, X30) and 18 CONFIRM.
   - Total: **45 CONFIRM, 21 QUALIFY, 0 REJECT** over 66 items. The extra REJECT (#263's R3 statement) and the 7 FD items are separate. ✓
2. **Rebuild.**
   - All pins match: `apply263.py` (`a9f782f0…`), `parse263.py` (`1ab728a2…`), `merw263.py` and `r3settle.py`.
   - I re-parsed #263 and got byte-identical `claude_strings.json` (70 strings).
   - Re-running `apply263.py` on copies of the base notes applied all 71 strings, each OLD occurring once. All three rebuilt notes are byte-identical to `fba589d`. ✓
   - Every QUALIFY amendment in the script matches the record's stated amendment.
   - **Housekeeping.** `parse263.py` writes to a hard-coded `/workspace/g263/claude_strings.json`. My re-run rewrote that file with identical bytes; only its mtime changed.
3. **L3 answer.**
   - From "## The question" through the conjecture paragraph, the text is byte-identical to base and occurs once.
   - It is 3,942 bytes with its final newline; the record says 3,941, presumably without it.
   - "Outcome mapping (Lead's draft, pending David)" comes after it. Its Status line says "not David's wording" and "pending David". ✓
4. **FD items: none quietly applied** (the #260 pattern).
   - FD1, FD3, FD4 and FD5 appear only inside the pending block, and that block decides no call.
   - FD2: the expanded "Where it connects" list ends "Whether LT2 covers them is open".
   - FD6: F-M1's option (ii) wording ("could pass") is unchanged. M8 adds only that rewording "is the Lead's or David's call".
   - FD7: "main paper" is unchanged in the substitution note. ✓
5. **Neutrality.**
   - No picks, and no Born, $|a|^2$ or 1/N result.
   - The substitution note describes DW and cites the critics and the defence on both sides. It quotes the v0.9 §2 firewall and does not argue against DW.
   - There is no Everett-vs-DW framing, and Bell is not called refuted.
   - None of the banned words occurs in the four files.
6. **Our earlier strings** (#249, #251, #253, #255, #257). Each NEW string was checked against the head. All survive except five, each revisited with its content kept or corrected:
   - **#253 M2 (LT1 row):** revisited by M9, as the record flags. The row still begins "A claim would have to exhibit an object that superposes, evolves linearly and interferes". M9 only says which of the three the nonnegative operators lack (interference). **LT1's wording is not weakened** (the L3 text is byte-identical).
   - **#253's R3 sentence:** "The computed shares are robust to the classifier, so such a claim would be too on this point." M5c replaces it with "do not depend on the classifier. This checks the computation; it is not a test of a claim's robustness under LT3". The record does not flag that this revisits our string. The new wording is accurate, and we accept it.
   - **#249's "Open calls" line:** expanded by B4. Every item it listed is still listed.
   - **#251's Waits-on cell:** "(Z-0)–(Z-v)" becomes "(Z-0)–(Z-ix)", which tracks #259 and #261.
   - **#257's L1, the branch-counting cell and the "Contested" list:** survive verbatim, with placeholders inserted.
7. **R3.**
   - `r3settle.py` re-run with my venv (26 s) reproduces `r3settle.out` byte for byte:
     - `kr.classify` gives 87,357 states, 14,477 stuck and one dead end.
     - `c33r.py` gives 87,356 states and 14,478 stuck.
     - The one extra edge runs from the apastron 16.900001215 to the target 17.147960961.
   - **This resolves the open "which state, and why" item** from our #247 and #251.
   - One addition (R1): I took the same double-precision $(E,L)$ for the target, $E=0.9725255054951221$ and $L=4.558956433827909$, and found the roots of $\dot r^2$ in 40-digit arithmetic. They are 2.6084599, **17.14793743** and **17.14796089**, so the orbit is bound.
     - The computed target, 17.147960961, lies $6.7\times10^{-8}$ *beyond* the outer root, inside the forbidden region. That offset is double-precision rounding.
     - `kr.classify` takes the outer root (it is below $r_p(1-10^{-9})$) as the "lower" turning point. It finds $\dot r^2<0$ at the midpoint, so it returns a plunge.
     - `c33r.py`'s bound label is the exact orbit's, and C33's 14,478 is the count under it.
     - The note's 87,357/14,477 is still right as `kr.classify`'s output, so the Lead's "settled" stands. The note should say which label the exact orbit has.
8. **Words** (`str.split`):
   - Litmus 843 → 1,985; MERW 1,417 → 2,810; substitution 1,451 → 2,979, as claimed.
   - The record has 2,246.
   - With the Part 2 strings and R1 applied: litmus 2,076, MERW 2,929, substitution 3,824.

### Part 1 findings

- **R1 (required, accuracy).** The R3 bullet gives both classifier labels as code outputs. It does not say that the plunge label is a rounding artefact or that the exact orbit is bound. String R1 adds this.
- **N1.** M5c revisits our #253 R3 sentence without flagging it. We accept the new wording.
- **N2.** `parse263.py` writes to a fixed path in `/workspace/g263`. My re-run rewrote it with identical bytes.
- **N3.** The L3 byte count is 3,942 with the final newline (record: 3,941).

### Part 1 string

Its OLD occurs once at `fba589d`.

**R1** — `notes/merw-litmus-scoping.md`

OLD:
```text
which (a) rejects. That one extra admissible edge is the whole difference:
```
NEW:
```text
which (a) rejects. In 40-digit arithmetic on the same $(E,L)$ the target's orbit is bound, with turning points $17.14793743$ and $17.14796089$; the computed target lies $6.7\times10^{-8}$ beyond the outer one (double-precision rounding), and `kr.classify` then takes that outer root as the lower turning point and returns a plunge. The bound label is the one the exact orbit has, so C33's 14,478 is the count under it. That one extra admissible edge is the whole difference:
```

## Part 2: record strings for the 16 placeholders

There are 16 placeholders: 2 in the litmus note, 2 in the MERW note and 12 in the substitution note. Each OLD below is the full placeholder and occurs exactly once at `fba589d`.
- Three OLDs extend the placeholder by a few adjacent characters, so that the sentence still reads after replacement:
  - P8: ". If it is, a run on DW";
  - P9: ". If recorded, counting";
  - P10: the leading space.
- Applying all 16 strings and R1 to the head leaves no placeholder in any note.

**How sources were checked.**
- Crossref queries were run serially, 1.2 s apart.
- Full texts read: arXiv for Wallace 2010 (0906.2718), Kent 2010 (0905.0624), Wallace 2003 (quant-ph/0303050) and Aaronson 2004 (quant-ph/0401062); the AMS PDF for Parry 1964.
- Abstracts from publisher pages for Dizadji-Bahmani 2015, Galley and Masanes 2017 and 2018, and Saunders 2021.
- Baker 2007's abstract as listed on PhilSci-Archive/PhilPapers, because PhilSci-Archive refused direct fetches.
- Read 2018: Crossref only.

**Not verified, and said so in the strings:**
- the content of Read 2018;
- Albert 2010's own text (the fatness rule is quoted from Wallace's description);
- the Wallace 2012 section numbers §3.11 and §5.8.1 (taken from a retailer's table of contents);
- whether the 2010 chapter and the 2012 book match the preprint's wording;
- the full texts of Baker 2007 and Dizadji-Bahmani 2015 (abstracts and section titles only).

**Not used:**
- Maudlin 2014 as a disputant: paywalled, so content was not checked. It stays cited as before.
- Jansson 2016: not checked.
- Albert 2010 and Price 2010 as disputants of branching indifference: Wallace §9 places their rules' breaks at diachronic consistency and at continuity respectively. Albert is used in P13.

**Corrections to the proposed citations:**
- The Galley and Masanes 2017 title is "Classification of all alternatives to the Born rule in terms of informational properties".
- Aaronson's $p$-norm result is that for $p\ne2$ the only norm-preserving linear maps are generalized permutation matrices. For $p=1$ on nonnegative vectors, stochastic matrices also preserve the norm, as P15 says.
- Parry's pages are 55–66; Crossref lists only "55".

**P1** — `notes/born-litmus-test.md`. Sources: Dizadji-Bahmani 2015 (Crossref; abstract on the publisher page); Kent 2010 (Crossref; arXiv:0905.0624 full text, abstract and the R5 line); Wallace 2010 §9 (arXiv:0906.2718 full text).

OLD:
```text
[RECORD STRING PENDING — Literature: who disputes the fine-graining and branching-indifference premise, and on what grounds (#263 §2.3 and X16; readiness §1.1 cites Dizadji-Bahmani 2015)]
```
NEW:
```text
(Dizadji-Bahmani 2015, *Brit. J. Phil. Sci.* 66(2), 257–283, doi:10.1093/bjps/axt035, argues "that Wallace is not successful in showing that BI [branching indifference] is rational" and that branch counting, which violates it, is a rational alternative; Kent 2010, in *Many Worlds?*, pp. 307–354, arXiv:0905.0624, argues that Wallace's axioms "are not constitutive of rationality" and that "Branching indifference, R5, is violated by Gell-Mann–Hartle aesthete strategies, among others"; Wallace 2010, §9, replies that branch counting "violates the combination of branching indifference and diachronic consistency")
```

**P2** — `notes/born-litmus-test.md`. Sources: Baker 2007 (Crossref; abstract as listed on PhilSci-Archive item 2717 and PhilPapers, because PhilSci-Archive refused direct fetches; full text not read).

OLD:
```text
[RECORD STRING PENDING — Literature: a citation for this location of circularity (#263 B4 proposes Baker 2007)]
```
NEW:
```text
(Baker 2007, *Stud. Hist. Phil. Mod. Phys.* 38(1), 153–169, doi:10.1016/j.shpsb.2006.05.003, whose abstract says the decision-theoretic account "is shown to be circular": probability talk needs a basis that identifies measurement outcomes, and that basis "can only be established by the process of decoherence, which is itself probabilistic"; abstract only, full text not read here)
```

**P3** — `notes/merw-litmus-scoping.md`. Sources: Parry 1964 (AMS full text: §3 Lemma 4, Theorem 5; §4 Theorem 10).

OLD:
```text
[RECORD STRING PENDING — Literature: the directed-case source and theorem, which v0.9 does not cite (#263 M3 proposes Parry 1964)]
```
NEW:
```text
Parry 1964, §3 Lemma 4 and Theorem 5, §4 Theorem 10: for a finite transitive 0/1 structure matrix $\Sigma$, not assumed symmetric, with simple Perron eigenvalue $\beta$ and positive right and left eigenvectors $l$ and $h$, the chain with transitions $\sigma(i,j)\,l(j)/(\beta\,l(i))$ has stationary probabilities $h(i)\,l(i)$ (normalised so that they sum to 1), and it is the only stationary process compatible with $\Sigma$ whose entropy equals the maximal value $\log\beta$
```

**P4** — `notes/merw-litmus-scoping.md`. Sources: Parry 1964 (Crossref DOI; the AMS page gives pp. 55–66, where Crossref has only "55").

OLD:
```text
[RECORD STRING PENDING — Literature: check and cite it (#263 M18: Parry 1964)]
```
NEW:
```text
(Parry, W., "Intrinsic Markov chains", *Trans. Amer. Math. Soc.* 112(1), 55–66 (1964), doi:10.1090/S0002-9947-1964-0161372-1; checked by Literature against the AMS text)
```

**P5** — `notes/substitution-test-scoping.md`. Sources: Crossref for all nine works; Saunders 2021 abstract (arXiv:2201.06087 / Royal Society page).

OLD:
```text
[RECORD STRING PENDING — Literature: the panel's cases and citations (#263 X14 proposes Zurek, Saunders 2021, Sebens and Carroll 2018, Bohmian equivariance, Gleason 1957, frequency-operator arguments and MERW)]
```
NEW:
```text
(candidate cases, options only: envariance, Zurek 2005; a state-dependent branch-counting rule, Saunders 2021; self-locating uncertainty, Sebens and Carroll 2018; Bohmian quantum equilibrium, Dürr, Goldstein and Zanghì 1992, with Goldstein and Struyve 2007 on its uniqueness; Gleason 1957; frequency-operator arguments, Hartle 1968 and Farhi, Goldstone and Gutmann 1989, with the critique by Caves and Schack 2005; and MERW. Bibliographic details are verified (References); content beyond titles and abstracts is not checked here)
```

**P6** — `notes/substitution-test-scoping.md`. Sources: Wallace 2003 (Crossref; arXiv abstract; full text §7, "Measurement Neutrality"); Greaves 2004 (Crossref; arXiv abstract).

OLD:
```text
[RECORD STRING PENDING — Literature: the reply to that charge and its reception (#263 X7: Wallace 2003; Greaves 2004)]
```
NEW:
```text
Wallace (2003) argues "that the flaw which they point out in the proof does not apply if the Everett interpretation is assumed", and (§7) names a premise "hidden by Deutsch's (and my) notation", measurement neutrality; Greaves (2004) reads the decision-theoretic probabilities as the degrees to which an agent cares about each future branch, and says this "reduces the intuitive plausibility of one of the Deutsch-Wallace axioms (Measurement Neutrality)"
```

**P7** — `notes/substitution-test-scoping.md`. Sources: Wallace 2010 preprint p. 1 (arXiv:0906.2718); Crossref for the chapter (pp. 227–263) and for the book's ch. 5 (pp. 157–198).

OLD:
```text
[RECORD STRING PENDING — Literature: the preprint, chapter and book labels, and what is unchecked against the book (#263 X17)]
```
NEW:
```text
(the preprint, "A formal proof of the Born rule from decision-theoretic assumptions", calls itself a preliminary version of the chapter "How to prove the Born rule", *Many Worlds?*, pp. 227–263, doi:10.1093/acprof:oso/9780199560561.003.0010; the book is Wallace 2012, *The Emergent Multiverse*, whose ch. 5 is pp. 157–198, doi:10.1093/acprof:oso/9780199546961.003.0007. Section numbers and quotations given as Wallace 2010 are the preprint's; the chapter's and the book's wording, numbering and axiom names are not checked here)
```

**P8** — `notes/substitution-test-scoping.md`. Sources: Wallace 2010 §9 (arXiv:0906.2718 full text); Kent 2010; Dizadji-Bahmani 2015.

OLD:
```text
[RECORD STRING PENDING — Literature: whether part of S1 for DW is already published, with the passage (#263 X12: Wallace 2010 §9 on rival rules), and whether the critics mainly dispute S3]. If it is, a run on DW
```
NEW:
```text
Part of S1 for DW is already published. Wallace (2010, §9, "Other proposed strategies for action") says the proposed rival rules "all contradict the Born rule, and so all violate the decision-theoretic axioms of this paper", and names for each the premise it breaks: branch counting, "the combination of branching indifference and diachronic consistency"; the fatness rule, diachronic consistency; the fake-state rule, state supervenience; Price's distributive-justice rule, continuity, or it is not a counterexample. Critics (Kent 2010; Dizadji-Bahmani 2015) dispute whether such premises are requirements of rationality, which is S3's question; whether that is their main dispute is not assessed here. A run on DW
```

**P9** — `notes/substitution-test-scoping.md`. Sources: Wallace 2010 §5 and §9 (full text); Kent 2010 App. A (full text); Dizadji-Bahmani 2015 section titles (publisher TOC); Saunders 2021 abstract. The Wallace 2012 section titles come from a retailer's table of contents only (marked in the string).

OLD:
```text
[RECORD STRING PENDING — Literature: Wallace's argument that branch number is not well defined once branching is the approximate product of decoherence, and the replies to it (#263 X6: Wallace 2010 §9; Wallace 2012 §§3.11, 5.8.1; Kent 2010)]. If recorded, counting
```
NEW:
```text
on Wallace's account, "There is no such thing as 'branch count'": "the branching structure emergent from unitary quantum mechanics does not provide us with a well-defined notion of how many branches there are" (Wallace 2010, §9; also §5); the book treats this in §3.11, "How many worlds?", and §5.8.1, "Branch counting" (section titles from a published table of contents, not checked against the book). Replies: Kent (2010, App. A, "Further comments on counting descendants") re-examines the argument; Dizadji-Bahmani (2015, §4.2, "No such thing as the number of branches") argues that "Wallace's arguments against BC are unpersuasive"; Saunders (2021) defends "a version of the branch-counting rule" that "both depends on the state and is continuous in the norm topology", whose ratios of branch numbers "agree with the Born rule". On that account counting
```

**P10** — `notes/substitution-test-scoping.md`. Sources: Dizadji-Bahmani 2015 abstract (publisher page).

OLD:
```text
 [RECORD STRING PENDING — Literature: Dizadji-Bahmani's own target and argument, which #263 X16 says this gloss overstates]
```
NEW:
```text
; Dizadji-Bahmani's own target is branching indifference: he argues "that Wallace is not successful in showing that BI is rational", that branch counting is a rational strategy "which violates BI", and "that Wallace's arguments against BC are unpersuasive" (abstract)
```

**P11** — `notes/substitution-test-scoping.md`. Sources: Read 2018: Crossref only. Content not verified (marked in the string).

OLD:
```text
[RECORD STRING PENDING — Literature: a defence of the programme in general, for balance (#263 X30: Read 2018)]
```
NEW:
```text
for the programme, besides Wallace, Read 2018, "In defence of Everettian decision theory" (bibliographic details verified; its content and target are not verified here)
```

**P12** — `notes/substitution-test-scoping.md`. Sources: Aaronson 2004 (arXiv full text §2); Galley and Masanes 2017, 2018 (Crossref; abstracts on Quantum's pages).

OLD:
```text
[RECORD STRING PENDING — Literature: physics-side results on what breaks when the norm or the Born rule is changed inside quantum theory, as a further comparison point (#263 X11: Aaronson 2004; Galley and Masanes 2018)]
```
NEW:
```text
for comparison on the physics side, Aaronson (2004, §2) shows that for $p\ne2$ "the only $p$-norm-preserving linear transformations are permutations of diagonal matrices"; Galley and Masanes (2017) classify all alternatives to the measurement postulates that keep the pure-state structure and dynamics, and (2018) prove that in all of them "the purification principle is violated" and state tomography with local measurements is impossible
```

**P13** — `notes/substitution-test-scoping.md`. Sources: Wallace 2010 §9 (full text); Albert 2010 (Crossref). Albert's own text not read (marked in the string).

OLD:
```text
[RECORD STRING PENDING — Literature: whether a published rule of this kind exists, and where Wallace locates its break (#263 X11: Albert 2010, the fatness rule; Wallace 2010 §9)]
```
NEW:
```text
One published rule of this kind is Albert's fatness rule (Albert 2010; as Wallace 2010, §9, describes it, "each branch is given a probability proportional to its quantum-mechanical weight multiplied by the mass of the agent", and it "is purely presented as a counter-example"): it weights equal-amplitude branches unequally where the agent's mass differs between them. Wallace (§9) locates its break at diachronic consistency ("It violates diachronic consistency"). Albert's own text is not checked here.
```

**P14** — `notes/substitution-test-scoping.md`. Sources: as P2.

OLD:
```text
[RECORD STRING PENDING — Literature: a citation for this location of circularity (#263 X8: Baker 2007)]
```
NEW:
```text
(Baker 2007, whose abstract says the decision-theoretic account "is shown to be circular" because the basis that identifies outcomes "can only be established by the process of decoherence, which is itself probabilistic")
```

**P15** — `notes/substitution-test-scoping.md`. Sources: Aaronson 2004 §2 (arXiv full text, including the $p=1$ stochastic case).

OLD:
```text
[RECORD STRING PENDING — Literature: the result that for $p\ne2$ no nontrivial linear map preserves the $p$-norm (#263 X28: Aaronson 2004)]
```
NEW:
```text
(Aaronson 2004, §2: "when $p\ne2$, the only $p$-norm-preserving linear transformations are permutations of diagonal matrices"; for $p=1$ on nonnegative vectors the stochastic matrices also preserve it, the classical case Aaronson notes)
```

**P16** — `notes/substitution-test-scoping.md`. Sources: every entry checked against Crossref, arXiv or the publisher page (serial Crossref queries 1.2 s apart).

OLD:
```text
[RECORD STRING PENDING — Literature: a reference list for the works this note cites outside v0.9 and readiness (#263 X22 drafts one)]
```
NEW:
```text
- Aaronson, S. (2004). Is quantum mechanics an island in theoryspace? arXiv:quant-ph/0401062.
- Albert, D. Z. (2010). Probability in the Everett picture. In *Many Worlds?*, 355–368. doi:10.1093/acprof:oso/9780199560561.003.0013.
- Baker, D. J. (2007). Measurement outcomes and probability in Everettian quantum mechanics. *Stud. Hist. Phil. Mod. Phys.* 38(1), 153–169. doi:10.1016/j.shpsb.2006.05.003.
- Caves, C. M., and Schack, R. (2005). Properties of the frequency operator do not imply the quantum probability postulate. *Ann. Phys.* 315(1), 123–146. doi:10.1016/j.aop.2004.09.009. Corrigendum: *Ann. Phys.* 321(2), 504–505 (2006), doi:10.1016/j.aop.2005.09.012.
- Farhi, E., Goldstone, J., and Gutmann, S. (1989). How probability arises in quantum mechanics. *Ann. Phys.* 192(2), 368–382. doi:10.1016/0003-4916(89)90141-3.
- Galley, T. D., and Masanes, Ll. (2017). Classification of all alternatives to the Born rule in terms of informational properties. *Quantum* 1, 15. doi:10.22331/q-2017-07-14-15.
- Galley, T. D., and Masanes, Ll. (2018). Any modification of the Born rule leads to a violation of the purification and local tomography principles. *Quantum* 2, 104. doi:10.22331/q-2018-11-06-104.
- Gleason, A. M. (1957). Measures on the closed subspaces of a Hilbert space. *J. Math. Mech.* (now *Indiana Univ. Math. J.*) 6(4), 885–893. doi:10.1512/iumj.1957.6.56050.
- Goldstein, S., and Struyve, W. (2007). On the uniqueness of quantum equilibrium in Bohmian mechanics. *J. Stat. Phys.* 128(5), 1197–1209. doi:10.1007/s10955-007-9354-5.
- Greaves, H. (2004). Understanding Deutsch's probability in a deterministic multiverse. *Stud. Hist. Phil. Mod. Phys.* 35(3), 423–456. doi:10.1016/j.shpsb.2004.04.006. arXiv:quant-ph/0312136.
- Hartle, J. B. (1968). Quantum mechanics of individual systems. *Am. J. Phys.* 36(8), 704–712. doi:10.1119/1.1975096.
- Kent, A. (2010). One world versus many: the inadequacy of Everettian accounts of evolution, probability, and scientific confirmation. In *Many Worlds?*, 307–354. doi:10.1093/acprof:oso/9780199560561.003.0012. arXiv:0905.0624.
- Maudlin, T. (2014). Critical study: David Wallace, *The Emergent Multiverse: Quantum Theory According to the Everett Interpretation*. *Noûs* 48(4), 794–808. doi:10.1111/nous.12072.
- Price, H. (2010). Decisions, decisions, decisions: can Savage salvage Everettian probability? In *Many Worlds?*, 369–390. doi:10.1093/acprof:oso/9780199560561.003.0014.
- Read, J. (2018). In defence of Everettian decision theory. *Stud. Hist. Phil. Mod. Phys.* 63, 136–140. doi:10.1016/j.shpsb.2018.01.005.
- Saunders, S., Barrett, J., Kent, A., and Wallace, D. (eds) (2010). *Many Worlds? Everett, Quantum Theory, and Reality*. Oxford University Press. doi:10.1093/acprof:oso/9780199560561.001.0001.
- Wallace, D. (2003). Everettian rationality: defending Deutsch's approach to probability in the Everett interpretation. *Stud. Hist. Phil. Mod. Phys.* 34(3), 415–439. doi:10.1016/S1355-2198(03)00036-4. arXiv:quant-ph/0303050.
- Wallace, D. (2010). How to prove the Born rule. In *Many Worlds?*, 227–263. doi:10.1093/acprof:oso/9780199560561.003.0010. Preprint: A formal proof of the Born rule from decision-theoretic assumptions, arXiv:0906.2718.

Cited here and already listed in v0.9 or readiness: Barnum et al. (2000); Burda et al. (2009); Deutsch (1999); Dizadji-Bahmani (2015); Dürr, Goldstein and Zanghì (1992); Saunders (2021); Sebens and Carroll (2018); Wallace (2012); Zurek (2005). Each entry above was checked against Crossref, arXiv or the publisher's page.
```
