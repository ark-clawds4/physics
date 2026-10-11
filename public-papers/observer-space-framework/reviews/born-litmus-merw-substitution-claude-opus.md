# External critique: Born litmus test, MERW scoping and substitution-test scoping
Reviewer: Claude Opus 5.5 (independent external critic)
Date: 2026-10-11
Verdict (`notes/born-litmus-test.md`): **HOLD**
Verdict (`notes/merw-litmus-scoping.md`): **HOLD**
Verdict (`notes/substitution-test-scoping.md`): **HOLD**

**File:** `reviews/born-litmus-merw-substitution-claude-opus.md`. **Read at:** `main` `05b74bc`. The three notes and `versions/v0.9-prose.md` are byte-identical at `3861dfc` and `05b74bc` (`git diff` is empty). **Reference:** `versions/v0.9-prose.md` (unchanged since `e493913`). **Targets:**
- `notes/born-litmus-test.md` (#248, revised in #252 and #254), the **litmus note**;
- `notes/merw-litmus-scoping.md` (#250, revised in #252 and #254; check #251), the **MERW note**;
- `notes/substitution-test-scoping.md` (#256; check #257), the **substitution note**.

**Records read:**
- the Literature checks #249, #251, #253, #255 and #257;
- `reviews/born-rule-readiness.md`, including the v0.9 refresh as revised in #259;
- `notes/zeno-mass-scoping.md` at `05b74bc` (options (Z-0)–(Z-ix));
- `reviews/law-of-R-scoping.md` (F rows only);
- #230's FOR DAVID list (`reviews/v0.8.1-prose-full-claude-pressure-test.md` §4), for F5 and F11;
- Paper 1 (`papers/observer-space-ontology.md`) §§8–9.

**Rules kept.**
- There is no Born derivation, no $|a|^2$ or $1/N$ weight put in by hand, and no law of $R$.
- I pick neither (M1) nor (M2), no Zeno reading, and no option of any note.
- I rule on none of the author's open calls: not F-M1 or its "hazard, not a route" wording, not T1–T3, not #230's F1–F12 (F5 and F11 included).
- I do not decide David's conjecture, and I do not decide which LT outcomes count as failures. Where a finding bears on one half of the conjecture, I say which half and in which direction, and leave it there.
- No string changes David's wording. Where his text is affected, the string adds separate text marked as the Lead's.
- No existing file is edited. This PR adds this file only.

**Labels.**
- **Required:** one of the following:
  - a false or unsupported statement that the note's argument uses;
  - a wrong mapping of a test, option or open call;
  - a missing option or entry point whose absence changes what the note concludes;
  - cost lines or wording that tilt toward one option, a pick, or one half of the conjecture.
- **Suggested:** materially improves precision, completeness, balance or symmetry without changing a conclusion, or corrects a pointer the argument does not rest on.
- **Nit:** cosmetic or pointer-level.

**String conventions.** Each string names its file: **(lit)** is the litmus note, **(merw)** the MERW note, **(sub)** the substitution note. A script checked every OLD below against its file at `05b74bc`:
- each OLD occurs exactly once;
- no two OLDs overlap;
- all NEWs apply together, in any order, without conflict;
- after application, every table row keeps its cell count.

Where two findings share a string, the string is listed under the first and named in the second. NEW text follows each file's own notation: plain text in the litmus note, LaTeX in the other two.

**How this was checked.**
1. I read the three notes against v0.9 and the records, and drafted findings.
2. A first workflow ran nine agents in parallel:
   - two independent rebuilds of the C33 state graph from the rule as stated, one in float64 and one in mpmath at 40 digits, with exact integer walk counts and exact ranks over GF(p);
   - one agent on the toys and the linear algebra;
   - three literature agents;
   - three blind critics, one per note.
3. I rebuilt the graph a third time myself and merged the results.
4. A second workflow ran seven agents:
   - two adversarial skeptics per note, one checking correctness and evidence, one checking the rules and neutrality, both against every draft finding, string and answer;
   - a completeness critic.

   Two skeptics recomputed toys independently. Of about 220 items checked, most were amended. The text below carries the amendments, and §5.4 records what changed in substance.
5. A script checked the strings mechanically.

**Literature access.** No full text was reachable from this environment: arxiv.org, api.crossref.org, philsci-archive and the publisher sites were refused by the network policy. Only web-search extracts were available.
- **[search]** marks a literature statement that rests on such extracts.
- **[#257]** or **[#251]** marks one that rests on the repository's earlier full-text checks.
- §6 lists what remains unchecked.

---

## 0. Summary

**Litmus note: HOLD.** The note is careful about attribution and claims nothing. It has no "Questions for an outside critic" section; §2 answers the questions the review was asked. HOLD is for three Required findings, all fixed by one block in the Lead's voice placed after "Pre-emptive use", so that David's L3 answer stays contiguous.
1. **The outcome mapping is missing (B1).**
   - "Genuine emergence needs YES on all four" and "Success means no circularity has been detected" are different bars, unless every NO counts as a failure. The note never says which NO is a failure.
   - As worded, LT2 is the test that asks about injection directly. Paper 1's trivial scheme would, on its face, meet LT1, LT3 and the first half of LT4, and fail only LT2.
2. **LT2 and the §8.4 clause it is mapped to differ in both directions (B2).**
   - §8.4 also admits a motivation that "states an empirical target", which LT2 excludes when the target is Born.
   - LT2 asks for a named class only "ideally", where §8.4's first branch requires one.
   - v0.9 itself leaves circularity to a later bar.
3. **LT3 bears unequally on (M1) and (M2) (B3).**
   - Its cut clause, and its splitting clause read as later splitting, hold for (M1) by construction and fail for (M2) in general.
   - A same-vertex split moves both.
   - Its grain clause can favour the count.
   - "Irrelevant" is undefined.
   - The splitting clause parallels the Deutsch–Wallace premise that critics dispute.

**MERW note: HOLD.**
- **Reproduction.** These instance figures reproduce in three independent rebuilds: C33's counts, 87,356 states, 29,119 orbits, 14.185, all seven R2 shares (under the convention M1 names) and the concentrations. The eigenstructure was computed in two of them. The R4 toys reproduce in three separate recomputations, for the configurations M15 and M23 name. R3's 87,357 / 14,477 variant did not reproduce.
- **Conclusions stand.** MERW is undefined on the instance, and a count-based claim is not stable in $L$.
- **Options.**
  - The operator table is reasonable but lacks a proper-time operator (M12). O3 is ambiguous (M13), and the Costs line is asymmetric (M16).
  - F-M1's options are neutrally worded, but option (i) has no cost line, and the list of places omits §11's two hazard mentions (M8).

HOLD is for eight Required findings:
1. **R2 mixes two walk-length conventions (M1).** The seven shares count $L$ arcs *after* the first step. The setup line, C36, the concentrations and 14.185 all count $L$ arcs in all.
2. **"Backward pairs" is the wrong category (M2).** Symmetrising adds the converse of every jump edge. The converse of a type-(ii) edge is an ordinary type-(ii) pair. All 29,118 converses fail (a) on the instance.
3. **On a directed graph MERW's density is $\psi^{\rm L}\psi^{\rm R}$ (M3).** It is the square of a Perron vector only where the two vectors coincide.
   - O2's flagged graph is never symmetric, so on O2 any coincidence has to come from $R$ itself.
   - Symmetry is sufficient for the coincidence, not necessary.
4. **R1's stated reasons are imprecise (M4).**
   - The SCCs include 29,118 singletons.
   - 29,119 is the algebraic multiplicity; the geometric multiplicity is 14,478.
   - The nonnegative right eigenvector *is* unique, but it lives on the root orbit alone.
   - The forward condition the note sets ("a unique leading eigenvector") is not sufficient.
5. **The LT3 row drops "refining the grain" (M5)** and puts the classifier in its place. R3's closing sentence repeats the mapping.
6. **"The graph is a continuum" should read "the completed histories" (M6).**
7. **The LT2 row has the §8.4 gap of B2 (M7).**
8. **F-M1's options are asymmetric and its list of places is incomplete (M8).** Option (i) has no cost line, and §11's two hazard mentions are missing. Nothing here picks an option.

**Substitution note: HOLD.**
- **What holds.** The DW axiom record matches #257, the framing caution is sound, and the note gives no verdict.
- **Options.**
  - T-a/T-b and (R-a)–(R-c) carry asymmetric cost lines.
  - The substitute family is one family: counting is $p=0$. It never reaches the step critic question 2 asks about.
  - A fourth relation option is worth recording (X20).

HOLD is for nine Required findings:
1. **The record format can tilt the conjecture's first half (X1–X3).**
   - S1 does not trace breaks back to premises, and Wallace states the break for branch counting as a *combination* of two axioms.
   - S3 has two cells where four exist.
   - "In part" names DW's contested step as its own example.
2. **The cost lines are asymmetric (X4, X5).**
   - T-b has no cost line.
   - (R-a) and (R-c) have none.
3. **The DW record is one-sided twice (X6, X7).**
   - The branch-counting row leaves out Wallace's argument that branch number is not well defined.
   - Barnum et al. appear without Wallace's 2003 reply.
4. **Table (ii) has two defects (X8).**
   - The MERW row repeats "backward pairs" and attributes $p=2$ to the uniform-path definition alone, without saying that the density is a square only where the left and right Perron vectors coincide.
   - The table has no row for the outcome labelling, one step at which the literature places circularity.
5. **"The §8.4 motivation clause is LT2's check" repeats the gap that B2 and M7 fix (X9).**

**The Wallace caveat** (§4.2): checking the axioms against arXiv:0906.2718 rather than the book matters little for what the note now says. It matters for any lemma-level S1 run, for the branch-counting row, and possibly for the richness-axiom names.

---

## 1. Recomputed

**What was run.**
- **Three independent rebuilds** of C33's (a)-restricted Kretschmann graph from the rule as stated (v0.9 §7, §8.2; C16's H2; C30, C31, C33):
  - **A:** float64, with two classifiers;
  - **B:** mpmath at 40 digits, with two classifiers;
  - **mine:** float64.

  All three agree on the counts, the converse test, the shares and the concentrations.
- **The eigenstructure rows** come from A and B, with exact ranks over GF($2^{31}-1$), GF($2^{61}-1$) and GF($10^9+7$).
  - The underlying undirected state graph is a tree (87,356 vertices, 87,355 edges, connected), hence 2-colourable. So $D\mathcal AD=-\mathcal A$, and the eigenvalue $-1$ row follows from the eigenvalue 1 row.
- **The R4 toys** were recomputed by three agents independently, then rerun by one skeptic. Both MERW skeptics also rebuilt the two-orbit flagged toys of §3 Q1.
- **Walk counts** use exact integers.

**C33 and R1** ($c=0.01$ unless stated).

| Quantity | Note or C33 | Recomputed |
|---|---|---|
| Reachable orbits; states | 29,119; 87,356 | 29,119; 87,356 = 58,238 segment states + 29,118 jump-arrival states |
| Orbit structure | "no cycle" | a tree: every non-root orbit has exactly one jump arrival; complete binary to depth 12, then 8,181 and 12,747 orbits at depths 13 and 14 |
| $m\le1$; longest chain; stuck orbits | yes; 14; 14,478 | yes; 14; 14,478 (5 at depth 12, 1,726 at 13, 12,747 at 14) |
| EPP1 jump law; expected decisions | $26/3^{12}$, $9338/3^{10}$, $447373/3^{12}$; 27.68 | exactly these; $14712160/531441=27.683525$ |
| Maximum apastron | 25.37 ($c=0.01$), 23.24 ($c=0.1$) | 25.366919, 23.236756 |
| Admissible edge types | — | 14,477 inward from a periastron (landing on a periastron); 14,641 outward from an apastron (landing on an apastron); no other type |
| Converse of an admissible edge passes (a) | — | **0 of 29,118** ($c=0.01$); 0 of 2 ($c=0.1$). On the instance every admissible target lies outside its source orbit's radial range; a general form of this is #230's F11, which is David's call |
| Classifier sensitivity (R3) | 87,357 against 87,356 | The two classifiers agree on all 116,476 candidate targets. The most nearly circular candidate (relative width $1.4\times10^{-6}$) is inadmissible under either label, and the smallest (a)-margin is $4.2\times10^{-6}$ relative, far above rounding. The 87,357 / 14,477 variant was not reproduced |
| Strongly connected components | "exactly the 29,119 orbit 2-cycles" | 58,237: the 29,119 orbit 2-cycles plus 29,118 singleton jump-arrival states |
| Eigenvalue 1 | "multiplicity 29,119" | algebraic 29,119; **geometric 14,478** (rank of $A-I$ is 72,878 over two primes; 14,478 disjoint eigenvectors give the lower bound over $\mathbb Q$); **index 15** |
| Eigenvalue $-1$ | — | the same, by 2-colourability |
| Nonnegative eigenvectors for eigenvalue 1 | "no unique Perron vector" | right: **unique up to scale**, supported on the root orbit's two segment states only. Left: a cone with 14,478 extreme rays, one per stuck orbit. Every left–right product vanishes |
| Entropy rate | — | 0 (spectral radius 1; polynomial growth) |
| $\log_2(N_{2000}/N_{1000})$ | 14.185; 0.999 | 14.185436 at $L$ arcs in all (14.174938 at $L+1$); $c=0.1$: $N_L=L+1$ exactly, 0.999279 |

**R2** (jump-arm share at the root).

| $L$ | Note | $L$ arcs in all (C36's convention) | $L$ arcs after the first step |
|---|---|---|---|
| 2 | 0.400 | $1/3$ | **$2/5$** |
| 10 | 0.381974 | $55/144=0.381944$ | **$89/233=0.381974$** |
| 20 | 0.381966 | 0.381966 | **0.381966** |
| 50 | 0.308087 | 0.314054 | **0.308087** |
| 100 | 0.137830 | 0.139361 | **0.137830** |
| 1000 | 0.011828 | 0.011839 | **0.011828** |
| 2000 | 0.005865 | 0.005868 | **0.005865** |
| Concentration on 14 jumps, $L=200$ | 0.8931 | **0.893056** | 0.893774 |
| Concentration on 14 jumps, $L=2000$ | 0.9909 | **0.990864** | 0.990869 |
| $c=0.1$ share at $L=2000$; on 1 jump | 0.000500; 0.9995 | $1/2001$; $2000/2001$ | $1/2002$; $2001/2002$ |

- **The two conventions.** All seven shares match "after the first step". The concentrations and 14.185 match "in all", which is C36's convention and the one the setup line names.
- **The Fibonacci regime.** At $L$ arcs in all, the walk counts are exactly Fibonacci ($N_L=F_{L+2}$) for $L\le28$, so the share is exactly $F_L/F_{L+2}$, which tends to $1/\varphi^2$.
- **Where it ends.** Seven segment states with no admissible jump lie 28 arcs from the root: six apastron states of depth-13 orbits and one periastron state of a depth-14 orbit. Exactly 7 walks of 28 arcs end there, so the count first falls short at 29 arcs ($N_{29}=F_{31}-7$).
- **Large $L$.**
  - $L\times$share is 11.84 at $L=1000$ and 11.74 at $L=2000$.
  - A fit gives the limit 11.633, which matches the structural value $2\cdot14\cdot5296/12747=11.633169$; 5,296 of the 12,747 depth-14 orbits lie below the root's jump arm.
  - At $c=0.1$ the share is exactly $1/(L+1)$ (in all), or $1/(L+2)$ (after the first step).

**R4 and the toys.** Every figure reproduces, with three specifics:
- The overlap 0.933865 is for two $P_4$ joined **end to end** ($P_8$). An end-to-inner join gives 0.935064, and an inner-to-inner join 0.967549.
- The $P_4$–$K_4$ masses 0.0423692, 0.00567555, 0.00076036 and 0.000101869 hold for $P_4$ attached by an end vertex, with the bridge vertices **not** counted.
- $\mathrm{tr}\,H^4=24+8\cos\theta$.

**MERW structure** (brute force on small graphs).
- **Directed graph.** On a strongly connected aperiodic directed graph, the marginal at the walk's middle site under the uniform measure on long walks converges to $\psi^{\rm L}_i\psi^{\rm R}_i/(\psi^{\rm L}\cdot\psi^{\rm R})$ (error $9\times10^{-7}$ at $L=200$). $(\psi^{\rm R})^2$ and $(\psi^{\rm L})^2$ miss by 0.05–0.07.
- **Symmetric, non-regular, non-bipartite graph** (a triangle with a pendant 2-path).
  - At the walk's middle site the exponent is 2 (error $4\times10^{-7}$ at $L=80$; $p=1$ and $p=3$ miss by 0.07). At the walk's first site it is 1.
  - On a bipartite graph the middle-site marginal alternates with parity, and only its average is $\psi^2$ ($K_{1,3}$).
- **$\psi^{\rm L}=\psi^{\rm R}$ without symmetry.** Two non-symmetric examples have equal left and right Perron vectors exactly:
  - a primitive circulant digraph ($I+P+P^2$), with both vectors constant;
  - a flagged two-orbit graph with jumps from $X$'s periastron to $Y$'s and from $Y$'s apastron to $X$'s, under strict alternation and the arrival flag: irreducible, $\lambda=\sqrt2$, $\psi^{\rm L}=\psi^{\rm R}\propto(\sqrt2,1,1,\sqrt2,1,1)$, checked exactly in sympy.
- **Golden-mean shift** $\begin{pmatrix}1&1\\1&0\end{pmatrix}$: MERW's probability of the jump arm is exactly $1/\varphi^2=(3-\sqrt5)/2$.

---

## 2. Is LT1–LT4 the right test?

### 2.1 What each test catches under David's scope ruling

The ruling makes the test answer one question: "was the Born rule put in by hand?" Failure means injection in whole or in part. Success means "no circularity has been detected" and "does not prove emergence". The working answer is a different bar: "Genuine emergence needs YES on all four".

Paper 1's trivial scheme is the in-house example of injection: copies "proportional to $|a_n|^2$" (Paper 1 §8; v0.9 §10). LT2's own parenthetical names the contrast with it. Applied to the decoherent, orthogonal branches of a quantum state, the scheme would, on its face:
- **meet LT1:** the squared quantity is the state's own amplitude, which superposes and interferes;
- **meet LT3:** squared moduli add under orthogonal refinement, so refining, re-cutting and further splitting leave each outcome's total unchanged;
- **meet LT4's first disjunct:** it returns Born weights in every setup, by construction;
- **fail only LT2:** its multiplicities are defined by the target.

Conversely, a NO on LT1, LT3 or LT4 can have a source other than an input tuned to a target:
- MERW's square is, in LT1's words, "a coincidence of form" unless the same $\psi$ does amplitude work elsewhere;
- the MERW note's R2 count is not stable in $L$ because of the instance's tree shape, not because of any target weight;
- no second setup exists.

| Test | What a NO shows | Is that, by itself, an injection? | Pre-emptively, on v0.9 |
|---|---|---|---|
| LT1 | The square does no amplitude work: a coincidence of form | Not by itself. It is one if the square was inserted at the counting step to hit a target, which is LT2's question; whether a hand-supplied amplitude structure (the MERW note's O5 phases) counts as an LT1 failure is the MERW note's question 3 | Nothing to check: no amplitude-like object (readiness v0.9 refresh, gap 6) |
| LT2 | An input was tuned to the target | Yes, in whole or in part | As worded, the test whose NO is itself an injection finding. Whether a NO on another LT can also be a failure is David's call (B1) |
| LT3 | The result is fragile | Not by itself. A cut or grain *chosen* to hit a target is an LT2 failure | MERW's R2 is fragile in $L$. That shows fragility, not injection |
| LT4 | No second setup, wrong weights in a second setup, or no new interference | Not by itself, though wrong weights in a second setup can be evidence that the first was tuned. Its home is confirmation theory: use-novelty (Worrall 1985 [search]), a requirement Mayo 1991 discusses critically [search]. LT2's "not tuned" applies the same idea to inputs | Nothing to check (readiness gap 5) |

**Reading.** As worded, the ruling's single question is asked directly by LT2. LT1, LT3 and LT4 are reasonable conditions for *emergence*, and the record does not say whether a NO on any of them can also be a failure. Reading "YES on all four" as necessary for emergence is consistent with success under the ruling being the weaker "no circularity detected".

If some NO is not a failure, there are three outcomes:
- failure (injection detected);
- no failure, but not YES on all four;
- YES on all four.

The record names failure and success, and states "YES on all four" as a condition for emergence. It does not say whether success and "YES on all four" coincide. If every NO were a failure, the middle outcome would be empty. Which NOs count as failures is David's call. B1 asks only that the gap be recorded.

### 2.2 Redundant, missing, mis-stated

**Overlaps.**
- LT1's "interferes" and LT4's "interference that was not put in" overlap. So do LT1's "superposes" and "evolves linearly" in quantum mechanics, though not on a nonnegative cone (M9).
- LT2 and LT4 overlap: both are use-novelty (no double-counting) conditions, LT2 on inputs and LT4 on outputs [search].
- LT3's "refining the grain" and "changing the cut" overlap, because (M2)'s named cut *is* a grain (v0.9 §3, Terms).
- The substitution test overlaps LT2 (§4.3, question 1).

**Mis-stated or uneven.**
- **LT2 against §8.4 (B2).**
  - §8.4 admits a motivation only if it selects the rule "within an independently named class of uniform rules", "or else states an empirical target". With Born as the target, the second branch admits what LT2 excludes.
  - In the other direction, LT2's "fixed for independent reasons", with a named class only "ideally", admits reasons §8.4 does not.
  - v0.9 itself does not treat the clause as a circularity check. §8.4 leaves "weights forced, not assumed" to a later bar needing "work on circularity", and §10 keeps the circularity wall.
- **LT2 and LT1 are coupled.**
  - Read as a quantity inside the theory, LT2's "$|\psi|^2$" needs an object that meets LT1, and v0.9 has none (readiness v0.9 refresh, gap 6).
  - Read as a target weight fixed outside the claim, as with v0.9 §10's tree "drawn by hand ... to match $|a|^2$", it needs no such object, and LT2 can fail on v0.9 now.
  - When a claim builds its $\psi$ from the same inputs, as MERW's Perron vector is built from the operator chosen, LT1 and LT2 are not independent.
- **LT3 is not neutral between (M1) and (M2) (B3).**
  - **The cut clause and later splitting favour (M1).** In v0.9 a prefix's per-vertex weight does not change with the cut, while the count's does (§9; C13, C14). A later split of a descendant leaves (M1) unchanged and changes (M2) (readiness §1.2, P7). So "changing the cut", and "irrelevant further splitting" read as later splitting, hold for (M1) by construction. They fail for (M2), except for the cut clause where $D$ is constant on the cuts compared (C13) or in the depth limit under asymptotic sibling balance (C15).
  - **The tilt is not one-way.**
    - A same-vertex split into arms with the same outcome moves both measures (readiness §1.2, given an outcome labelling).
    - "Refining the grain" can favour the count. Re-describing a three-way decision $r\to\{A,B,C\}$ as two binary ones, $r\to\{A,N\}$ and $N\to\{B,C\}$, moves the per-vertex weights from $1/3$ each to $1/2,1/4,1/4$. The count at the depth-2 cut, dead ends included (§9), stays at $1/3$ each.
  - **"Irrelevant" is undefined.** It needs an outcome labelling (readiness gap 5). Defined instead as "leaves the weights unchanged", it would presuppose a measure.
  - **The phrase has a history.** It is the branch-counting objection recorded in readiness §1.1 item 4 (counts "change under irrelevant further splitting"). The clause parallels the Deutsch–Wallace fine-graining premise, which the literature disputes (§2.3).
  - This is a fact about the test, not a pick. The note's "None is decided here" needs it recorded, so that LT3 is not read as deciding (M1)/(M2).

**Missing.** Measured against the literature (§2.3), LT2's input list ("the law of R, the slice and the measure") omits two items:
- **What is counted.** This means the individuation of arms (the isotropy quotient, C9; first-edge equivalence, C11) and the outcome labelling (readiness gap 5). It is one place where the literature locates circularity in decoherence-based derivations (Baker 2007; Dawid and Thébault 2015 [search]).
- **The bridge premise.** This is the premise taking symmetric or equal-weight cases to equal probability: state supervenience, non-contextuality or envariance in the literature. Its nearest in-house counterpart is EPP1's equal shares. Those apply to all arms, symmetric or not, so the symmetric premise itself is idle (readiness §1.2, DW (a) row).

The ruling's "in part" covers both, but no LT names them. B4 records them as open, without deciding whether LT2 covers them.

### 2.3 How the literature judges the four programmes, and where LT1–LT4 sit

Bibliographic data and one-line content: **[search]** unless marked. The DW axioms and Wallace 2010 §9 are **[#257]**.

| Criterion | Where it arises or is applied in the literature | In LT1–LT4 |
|---|---|---|
| Independent motivation of premises | DW: Barnum, Caves, Finkelstein, Fuchs and Schack 2000 ("hidden probabilistic assumptions"), answered by Wallace 2003 (the flaw does not apply once Everett is assumed); Dizadji-Bahmani 2015 (branching indifference not shown rational); Kent 2010 (coherent strategies violate some axioms); Price 2010; Albert 2010; Jansson 2016 (state supervenience); Mandolesi 2019. Zurek: Schlosshauer and Fine 2005; Barnum 2003 (continuity); Caves's unpublished notes (a "foundational noncontextuality assumption"). Sebens–Carroll: Dawid and Friederich 2022 (ESP-QM motivated only by quantum mechanics' success, Born included). Saunders 2021 §8 raises the question-begging objection against himself and replies to it | **LT2**, which carries almost all of it |
| The bridge from symmetric or equal-amplitude cases to equal probability | Deutsch's symmetry step; Wallace's equivalence lemma (needs $\lvert\alpha\rvert=\lvert\beta\rvert$ [#257]); Zurek's envariance; Saunders's equal-norm units; McQueen and Vaidman 2019 (a defence) | Only the ruling's "in part"; no LT names it |
| Outcome or branch individuation presupposing the weights | Baker 2007 (decoherence-based branches presuppose probability); Dawid and Thébault 2015 (against DW); Zurek's own remark that decoherence employs reduced density matrices and hence Born's rule (arXiv:0707.2832, authorship unchecked); Herbut 2007, a refinement of Zurek rather than a critique, in whose version the trace is not avoided | **Missing** from LT2's list (B4) |
| Fine-graining invariance and rival rules | Wallace 2010 §9 and 2012 §5.8 (each rival breaks an axiom or is no counterexample); Wallace 2012 §3.11 (branch number not well defined); Dizadji-Bahmani 2015; Saunders 2021 (counts at a grain of equal-norm units) | **LT3**'s splitting clause parallels the disputed premise (B3) |
| The norm or typicality step in limit arguments | Hartle 1968 and Farhi, Goldstone and Gutmann 1989, where the step arises; Caves and Schack 2005 (the frequency operator does not imply the probability postulate) | Not named. Its nearest relative is §8.4's "typicality rule" |
| Identity of the squared object with an amplitude | Not an issue for these four programmes, which start from Hilbert-space amplitudes. It arises for programmes that rebuild the amplitude: stochastic mechanics (Wallstrom 1994: a quantisation condition added by hand), MERW readings (Duda; Faber 2024, "quantum mechanics cannot be simply a result of MERW") | **LT1**: not redundant here, though it discriminates nothing among the four |
| Novel prediction | Not found as a criterion for Born derivations in the extracts reached, which does not show that it is absent | **LT4**: an anti-ad-hoc, use-novelty criterion |

**By programme.**
- **Deutsch–Wallace:** judged mainly on premise independence (LT2), on the bridge premise, and on fine-graining invariance (LT3's parallel).
- **Zurek:** judged on the envariance bridge and on additivity and continuity (Schlosshauer and Fine 2005; Barnum 2003). That is the bridge premise, which no LT names.
- **Saunders 2021:** the charge found is the question-begging objection he raises himself and answers (§8). No published external critique was found in the extracts (unchecked). His count at a grain of equal-norm units is the case nearest (M2), and it bears on LT2 and LT3.
- **Sebens–Carroll:** judged on the motivation of ESP-QM (Dawid and Friederich 2022; LT2). Kent 2015 (in readiness's references) disputes whether self-locating uncertainty makes sense in the universal wave function, which is not a circularity charge.

**Verdict on the question asked.**
- LT1–LT4 is a reasonable set of conditions for *emergence* for a programme with no native amplitude.
- Of the four, LT2 is the one whose wording asks the ruling's single question directly. Two things would sharpen it:
  - naming what is counted and the bridge premise (whether LT2 already covers them is open; B4);
  - stating its relation to §8.4's two branches.
- LT1 is not redundant for this framework, and MERW shows why. For a symmetric operator its square is fixed by the uniform-path construction (§4.3, question 4), yet it does no amplitude work. Whether choosing a symmetric operator is a prior input or tuning is the MERW note's own question 4.
- LT3, as worded, parallels the premise the DW literature disputes, and it bears unevenly on (M1) and (M2). Recording that (B3) keeps it from being read as a neutral criterion. Whether to restate it is David's call.
- As worded, LT4 bears on accommodation rather than injection, unless wrong weights in a second setup are read as evidence that the first was tuned.

None of this decides which LTs return a failure. That call is David's.

### 2.4 The substitution test and the conjecture (no verdict)

- **Every valid derivation breaks something.** If premises $P$ entail $W$ and $W'$ contradicts $W$ on the cases $P$ covers, then $P$ is inconsistent with $W'$. So "something upstream breaks" holds for every valid derivation, Paper 1's trivial scheme included: its multiplicity assignment must be re-chosen. The test discriminates only through S3-type judgements of what breaks, in the substitution note's terms: whether it is independently motivated, and whether it restates the rule.
- **Part of the test has already been run on DW.** Wallace 2010 §9 (and 2012 §5.8) takes each rival rule and names the axiom, or combination of axioms, it violates, or argues it is no real counterexample [#257]. That is close to an S1 for DW. The critics (Kent, Price, Albert, Dizadji-Bahmani, Jansson, Mandolesi) mainly dispute whether the violated axioms are independently motivated. Kent also disputes whether a precise decision theory over fuzzy branches is coherent at all [search].
- **Physics-side precedents exist.** They ask what breaks when the norm or the Born rule is changed inside quantum theory, and bear on the substitution note's $|a|^p$ row and on (R-c):
  - Aaronson 2004 [search]: for $p\ne2$ no nontrivial linear map preserves the $p$-norm on all vectors ($p=1$ has stochastic maps on the nonnegative cone, the classical case);
  - Galley and Masanes 2018 [search]: any modification of the Born rule violates purification and local tomography.
- **What would decide the conjecture.** Its first half turns on an S3-type judgement of DW's axioms, a live dispute (§4.3, question 2). Its second half cannot be run until a Born-type claim exists ("Pre-emptive use": "It cannot pass a claim that has not been made"). I decide neither half.

---

## 3. MERW note: answers to its critic questions

**Q1. Is any irreducible $R$ compatible with strict alternation and the arrival flag, or does R1's block structure hold in general?**
- **Compatible, in principle.** Items 2 and 7 do not force reducibility.
  - On a flagged graph whose orbits are bound, as on the instance, each orbit's two segment states form a cycle, and each jump-arrival state has one out-arc into its own orbit. Such a finite flagged graph is irreducible exactly when the orbit-level jump digraph on the reachable orbits is strongly connected.
  - Two abstract orbits that jump to each other already give a strongly connected flagged graph. All 16 two-orbit toys of this kind are strongly connected, with spectral radius $\sqrt2$, 1.324718 or 1.362599.
  - This is a digraph fact, not a public example.
- **What produces R1's block structure on the instance is the rule under (a), not items 2 and 7.**
  - No admissible edge's converse passes (a): 0 of 29,118 (§1).
  - The jump digraph is a tree.
  - On the instance the target's radial width shrinks along every edge (ratios 0.157–0.967), which acts as a decreasing quantity along jumps. That is computed, not proved.
  - Whether (a) forbids jump cycles for every $R$ is not settled here. A general version of the first point is close to #230's F11 (the #203 lemma), which is David's call.
- **Exact returns.** Irreducibility needs exact returns to earlier orbits. For a rule whose targets vary continuously with the source, such returns from a given root are non-generic unless the rule is built to produce them. That is a law-of-$R$ question.
- **What items 2 and 7 do settle: the flagged graph is never symmetric when $R$ has a type-(ii) edge.**
  - The converse of a jump arc would have to be the arrival state's one out-arc, a segment from the target back to the source. The edge would then be backward or type (i), not type (ii) (§5).
  - So symmetry never makes $\psi^{\rm L}$ and $\psi^{\rm R}$ coincide on O2. They can still coincide without it: the $\sqrt2$ toy has $\psi^{\rm L}=\psi^{\rm R}$ exactly (§1).
  - Whether an irreducible O2 yields a square therefore depends on $R$ (M3).

**Q2. Is the $1/\varphi^2$ plateau a property of the rule, or a C36-type Fibonacci effect of the root orbit?**
- **It is the golden-mean shift.** While every segment state within reach has exactly one admissible jump, strict alternation makes the local walk structure the golden-mean shift. Its walk counts are Fibonacci, and its MERW probability of the jump arm is $1/\varphi^2$ exactly (§1).
- **It depends on two things only:** alternation (§8.2 item 2) and $m=1$ near the root (C33's $m\le1$).
  - It does not depend on the root orbit's geometry. Any segment state whose subtree has $m=1$ for about $L/2$ levels gives it.
  - It is "C36-type" in its arithmetic. C36's $P_4$ count from an inner vertex has the same $N_L=F_{L+2}$ and the same $\lambda=\varphi$.
- **The general formula.** With $m$ jump arms per segment state the alternation graph has $\lambda^2=\lambda+m$, and the maximal-entropy jump share is $m/\lambda^2$:
  - $1/\varphi^2$ at $m=1$;
  - $1/2$ at $m=2$, against EPP1's $2/3$.
- **Where it ends.** The nearest segment states with no admissible jump lie 28 arcs from the root, so the counts first depart from Fibonacci at $L=29$. The share then falls as about $11.6/L$.
- So the plateau is a property of the alternation grammar with one arm per decision, transient on this instance. It is not a feature of the Kretschmann geometry or of the root.

**Q3. Once a claim through a Perron vector is made, does its positivity bear on LT1, given that failure means injection? Would only O5's hand-supplied phases count as an LT1 failure?**
- **Positivity bears on LT1 as a missing YES.**
  - A positive $\psi$ cannot cancel. So unless the same $\psi$ did amplitude work elsewhere, its square would be, in LT1's words, "a coincidence of form".
  - Positivity itself is not put in by hand: Perron–Frobenius gives it for any nonnegative irreducible operator. Whether the operator is chosen independently is LT2's question (Q4).
  - Whether a NO of this kind counts as a failure under the ruling is B1's outcome-mapping gap, which is David's call.
- **O5's phases** would be a prior input supplied to get interference, so they bear first on LT2 and on the substitution test.
  - The sharper point is the step from a complex $\psi$ to a probability on O5.
  - The uniform-path argument that fixes the exponent for a nonnegative operator does not survive complex weights, since path sums are no longer counts.
  - So on O5 the map from $\psi$ to a density would have to be supplied. That is where an injection check would bite.
- **Through O2 the density is $\psi^{\rm L}\psi^{\rm R}$.** It is the square of a Perron vector only where the two coincide, which symmetry never secures on O2 (Q1; M3).

**Q4. Does O3's symmetrisation count as a prior input in LT2's sense, or as tuning?**
- **It is the step that makes $\psi^{\rm L}$ and $\psi^{\rm R}$ coincide by symmetry, turning $\psi^{\rm L}\psi^{\rm R}$ into $\psi^2$.** So it is an input on which the exponent's being a square can rest, which is what a substitution run would probe. (A non-symmetric $R$ could also make them coincide, but nothing in the record supplies one.)
- **On the instance it changes three prior inputs:**
  - $R$ gains converse pairs;
  - (a) gives way to (b), since every converse fails (a);
  - items 2 and 7 change, or the flag is dropped. With converse pairs in $R$ and no arrival rule, a history can jump back and forth at one accumulated $\tau$, so clause (2) of the hard gate fails per history (§8.2; C5).
- **Which it is depends on the reason.**
  - On LT2's wording, it reads as an input fixed for independent reasons only if a reason for $R$'s symmetry is stated in advance, independently of the density's form.
  - If it is adopted because $\psi^2$ needs a symmetric matrix, it reads as LT2's "tuned until |psi|^2 appears". Whether a square that does no amplitude work counts as that target is part of the outcome mapping left to David (B1).
- **The record states no independent reason,** and v0.9's structure is time-directed throughout: future-directed realisation, the arrival flag, strict alternation.
- Which reading holds is not decided here.

**Q5. Is "robust to the classifier" (R3) LT3's grain, or is the grain $L$?**
- **R3 is not LT3's grain.** By v0.9 §3 a grain is "a physically relevant level of description", and (M2)'s named cut is one. R3 checks the computation. Both rebuilds here find no classification sensitivity at all.
- **$L$ is LT3's "cut"**, a depth cut on the walk tree. By v0.9 §3 a named cut is also a grain, so a claim at fixed $L$ is a claim at a grain. But R2 varies the cut's depth, not the level of description, so it probes LT3's "changing the cut", not "refining the grain". R2 shows a count-based claim is not robust to that change.
- **What is not probed:**
  - a refined grain proper, such as a finer slice or a re-described decision (§2.2);
  - "irrelevant further splitting";
  - a proper-time cut, which the note's Limits line names.
- Which grain is physical is open (v0.9 §2: "No grain of Obs or V is locked").

---

## 4. Substitution note: Deutsch–Wallace, the Wallace caveat, and its critic questions

### 4.1 Is Deutsch–Wallace described accurately and fairly?

**Accurate, as far as it goes.** The note's summary of Deutsch 1999 matches the source [#257]. Two small points [search]:
- it leaves out the substitutability premise;
- it skips the passage from rational to irrational ratios, which I could not confirm in the source.

The axiom list, the "Born rule theorem" and readiness §1.1's conditions (a) and (b) match #257.

**Fair as a comparison point, with three gaps, all leaning the same way:** toward "fails" in the conjecture's first half.
1. **Barnum et al. appear without Wallace 2003's direct reply (X7).** The reply argues that the flaw does not apply once Everett is assumed. It also makes explicit a tacit premise of Deutsch's proof, measurement neutrality [search].
2. **The branch-counting row records only the axiom-level break, plus a critic's gloss (X6).**
   - It omits Wallace's line that branch number is not well defined once branching is the approximate product of decoherence ("There is no such thing as 'branch count'", Wallace 2010 §9 [#257]; Wallace 2012 §3.11 "How many worlds?" [search]).
   - On Wallace's account counting is then undefined, not only excluded by an axiom. In the note's format that is S1's "not defined" slot (X1).
   - The argument is itself disputed. Kent 2010 argues that the same fuzziness makes a precise decision theory over branches incoherent. Dizadji-Bahmani 2015 finds Wallace's arguments against counting unpersuasive [search].
   - Whether it is the kind of upstream break David's test asks for is an S3 judgement, which I do not make. The row should record it either way.
3. **The Dizadji-Bahmani attribution is readiness's gloss, not his wording (X16).**
   - His stated target is branching indifference. He argues Wallace has not shown it rational and that branch counting, which violates it, is a rational alternative. He engages Wallace's arguments against counting and rejects them [search].
   - So readiness's "The rival is ruled out by an axiom, not an argument", which the note's "excludes branch counting by assumption" leans on, overstates him.

**Not a rival set up to be knocked down.** The framing caution, the "[PJ]" flags and the absence of any verdict all hold. Table (ii) is candid that EPP1, (M2)'s cut and the Zeno convention are declared items, not derived ones.
- **But the record format (X1–X3) would, if applied as written, tilt the first half toward "fails".**
  - An S1 that does not trace breaks back to premises can read empty for branch counting over primitive premises.
  - "In part" names DW's contested step as its own example.
- **Separately, a gap rather than a tilt.** Neither substitute probes the equal-amplitude step (X11). That leaves the first half untested where the literature disputes it, without pushing it either way.

### 4.2 Does it matter that the Wallace 2012 ch. 5 axioms were checked against arXiv:0906.2718?

**Little, for what the note now says.**
- The note says openly that its axiom statements "follow the preprint".
- The book's ch. 5 headings mirror the preprint's [search, from third-party copies of the table of contents]:
  - 5.3 "The quantum decision problem";
  - 5.4 "The dictates of rationality";
  - 5.5 "A quantum representation theorem";
  - formal statements of the axioms and of the theorem;
  - 5.8 "Other proposed strategies for action", with 5.8.1 "Branch counting" and 5.8.2 "The fatness rule".
- Lewis's NDPR review describes the same grouping: standard rationality axioms, richness axioms, and Everett-specific axioms [search].
- The book's axiom names and wording were not read.

**It matters in four places:**
1. **Lemma-level S1.**
   - The book adds appendices with formal proofs of supporting results: App. C "Formal proofs of decision-theoretic results" and App. D "Proof of the Utility Equivalence Lemma" [search].
   - The $|a|^p$ row's "equivalence lemma" has to be matched to the book's "Utility Equivalence Lemma" before any run that says which lemma uses which premise.
2. **The axioms and the proof themselves.**
   - Mandolesi (2018), restating the axioms "as stated in [Wal12]", also lists Restriction, Composition and Indolence under richness. Those names are absent from the preprint's list, and whether they are Wallace's is unchecked [search].
   - Mandolesi reports the formal proof mostly correct but in need of fixes, including an axiom missing the hypothesis "that the norms of the two states are equal". That bears directly on the $|a|^p$ row's "norm's role".
   - He argues that the justification of most axioms is problematic, and that the axioms are not reasonable enough to be mandates of rationality (2019) [search].
   - Which version of Wallace he analysed is unchecked.
3. **The branch-number argument is stated most fully in ch. 3** (§3.11, pp. 99–102 [search]). The ch. 5 survey (§5.8.1, if it mirrors preprint §9 [#257]) states it only briefly (X6).
4. **One label, two texts.** "Wallace 2010" names both the preprint ("A formal proof of the Born rule from decision-theoretic assumptions") and the published chapter ("How to prove the Born rule", *Many Worlds?*, pp. 227–263). Whether their texts are identical is unchecked (X17).

**Recommendation (Suggested, X17).** Cite the chapter for the formal argument, but attribute quoted wording, section numbers and lemma names to the preprint (arXiv:0906.2718) until the chapter and the book are read. Read ch. 5, App. C–D and §3.11 of the book before any S1 run.

### 4.3 Answers to the note's critic questions

**1. Does the test have content beyond S3, and is S3 just LT2 under another name?**
- **It has content, once S1 traces breaks back to sets of premises (X1).** S1 then locates where a derivation carries the weight. That localisation is informative, as Wallace 2010 §9 shows.
  - For counting, Wallace names a combination of two axioms.
  - Wallace treats no $|a|^p$ rule [#257]. Counting is the $p=0$ member (X11), and one payoff-neutral split moves every $p\ne2$, so the same combination plausibly applies. That is my inference; the note's row names other candidates.
- **S2 adds more** (X10): which relaxations exist, and how many.
- **The choice of substitutes adds the most.** A step assumed only on a sub-case is caught only by a $W'$ that disagrees with $W$ there.
  - Both of the note's substitutes agree with Born on equal amplitudes, so neither reaches the step critic question 2 asks about (X11).
  - Counting does reach branching indifference, which is contested in its own right.
- **S3 is not identical to LT2.** LT2 covers three named inputs and tuning. S3 covers any premise and adds a "restates $W$ on a sub-case" axis that LT2 lacks.
- **Calibration is the open risk.** A test that fails every case discriminates nothing. A known-failure control (Paper 1's trivial scheme, X14) checks only one side. Calibration also needs a case whose pass the parties agree on, and finding one is itself open.
- Which relation option to take, (R-a) to (R-d), is the author's call.

**2. In DW, is the equal-amplitude symmetry an independent input, or the Born rule on a sub-case? Is this settled?**
- **Not settled. It is the central live dispute.** All [search]:
  - *On this step:* Barnum et al. 2000 (charge); Wallace 2003 (reply); Greaves 2004 (finds measurement neutrality less plausible on her reading); Jansson 2016 (state supervenience); Mandolesi 2019 (a missing equal-norm hypothesis).
  - *On other premises:* Hemmo and Pitowsky 2007; Baker 2007 (individuation); Rae 2009; Kent, Price and Albert 2010; Dizadji-Bahmani 2015 (branching indifference).
  - *Defences:* Wallace 2010 and 2012; Read 2018.
- **Vaidman's survey.** His 2020 survey concludes that the Born rule "cannot be derived from the other postulates of quantum theory without some additional assumptions". Its yardstick, at abstract level, is an audit of extra assumptions, not a verdict of circularity [search].
- **In Wallace 2010 the step is not a primitive axiom** [#257]. It is the equivalence lemma, derived from erasure and state supervenience with the other axioms. The same holds for 2012 if App. D's "Utility Equivalence Lemma" is that lemma [search]. So the question becomes whether those axioms are independently motivated.
- **The note must not answer it by definition (X3).**
- I give no answer.

**3. Is a declared postulate such as EPP1 "put in by hand" in the test's sense, or outside its scope because it claims nothing about Born?** There are two readings, and I rule on neither.
- **Scope-limited.** The test asks whether *the Born rule* was put in. EPP1 carries no amplitude ($1/|A|$; readiness gap 6).
  - It becomes relevant only if a Born-type claim routes through it, for example with arm multiplicities set so that EPP1 reproduces $|a|^2$. v0.9 §2 already excludes that, and it is Paper 1's trivial scheme.
  - At that point EPP1 is an S3 item, to be placed in one of X2's four cells. I do not place it.
- **General.** Any weight rule offered as "the" measure is tested. Then "any other per-arm weight" breaks nothing upstream, which is the slide-in signature.
- **Two separate notes.**
  - "Declared" is not "independently motivated". The test asks about motivation, not declaration.
  - EPP1's cost as a named postulate is already on v0.9's (M1) cost line (§11, Problem note 9), whatever the test says.
- X15 records that, by the T-a definitions as stated, table (ii)'s empty break column is not by itself a "slides in" verdict. It leaves open whether a declared postulate is tested in its own right.

**4. Does the $p=2$ in MERW's density count as breaking something upstream, or as the definition restating the target?**
- **The facts (§1).**
  - Under the uniform measure on long paths, a site in the interior of a path has density $\psi^{\rm L}_i\psi^{\rm R}_i$: one factor from the paths arriving (the past half), one from the paths leaving (the future half). At a free end there is a single factor.
  - The two factors coincide for a symmetric operator, and in some other cases, such as a regular digraph, where both are constant. In general they differ. Burda et al. treat only the symmetric case [#251].
  - Duda reads the product as past and future half-path ensembles [search]. Parry's maximal-entropy measure gives it for directed graphs [search].
- **So swapping $\psi^2$ for $\psi^p$ would break an upstream construction:** the uniform weight on paths, which no $p\ne2$ realises at an interior site of a non-regular graph. (On a regular graph $\psi$ is constant and every $p$ agrees.) That premise is stated without any $\psi$, so on its face it is not the target restated.
- **The "2" is combinatorial, not an amplitude square.** LT1 is where MERW stops (§3, Q3). MERW is therefore the clean case that separates the substitution test from LT1: an exponent the construction fixes, on an object that does no amplitude work.
- Whether "the two halves of a path" counts as an independent structure is the S3 call, and I do not make it.
- This bears on neither half of the conjecture: v0.9 makes no MERW claim, and F-M1 is David's.

**5. Can a companion paper run the test on DW without staging the framing v0.9 §2 excludes?**
- **Who is bound.** v0.9 §2 binds v0.9. Paper 1 §9 states Paper 1's own stance: "It does not argue against Deutsch and Wallace in order to occupy their problem." Whether that stance extends to a companion paper is the author's call.
- **The risk.** A DW-only run published beside a conjecture that DW fails and this framework passes stages a two-party comparison, whatever the wording.
- **Options, each with its cost (no pick):**
  - (a) A panel in one record format, with Paper 1's trivial scheme as a known-failure control (X14). Cost: more Literature work, an S3 judgement for every case, and a control whose own failure needs S3 (X4).
  - (b) Report S1 and S2 for DW only, engaging Wallace 2010 §9 (X12), and leave S3 to the literature with both sides cited. Cost: it cannot bear on the conjecture's first half, which turns on S3 (§2.4). What it adds is S2.
  - (c) A pre-emptive audit of this framework only, with DW as David's illustration and no S3 verdict on DW. Cost: it leaves the conjecture's first half untested.
  - (d) Pre-register the substitute family and the S3 criteria before any run. Cost: one more fixed choice to defend.

---

## 5. Findings

### 5.1 Litmus note (`notes/born-litmus-test.md`)

#### Required

**B1. The outcome mapping is missing** (§2.1).
- **The finding.** The two bars ("YES on all four"; "no circularity has been detected") coincide only if every NO is a failure, and the note does not say which NOs are failures.
- **The fix.** The string records the gap in the Lead's voice and decides nothing.
  - It is placed as one block after "Pre-emptive use", so David's L3 answer stays contiguous.
  - It also carries B2 and B3.

String B1 (lit; carries B1, B2 and B3) — OLD:
```text
For each LT, it records whether there is yet anything to check and what a later claim would have to show.
```
NEW:
```text
For each LT, it records whether there is yet anything to check and what a later claim would have to show.

**Reading the L3 answer against the rulings and v0.9 (the Lead's note, not David's wording; nothing here decides a call).**
- *Outcomes.* The record does not say how a NO on each LT maps onto failure and success. As worded, LT2 is the test that asks about injection directly; its own parenthetical names the contrast with Paper 1's trivial scheme. That scheme (copies "proportional to |a_n|^2", Paper 1 §8; v0.9 §10), applied to the decoherent branches of a quantum state, would on its face meet LT1 (the squared quantity is the state's own amplitude), LT3 (squared moduli add under orthogonal refinement) and the first disjunct of LT4 (it returns the Born weights in every setup), and would fail only LT2. Conversely, a NO on LT1, LT3 or LT4 can have a source other than an input tuned to a target: for example, the count in `notes/merw-litmus-scoping.md` R2 is not stable in L because of the instance's tree shape, not because of any target weight. So, unless such a NO is itself to count as a failure, "YES on all four" and "no circularity has been detected" are different bars. Which LT outcomes can return a failure, and which only withhold a pass, is open.
- *LT2.* v0.9 §8.4 admits a motivation only if it selects the rule "within an independently named class of uniform rules", "or else states an empirical target". With the Born rule as that target, the second branch would admit what LT2 excludes ("not tuned until |psi|^2 appears"); in the other direction, LT2's "fixed for independent reasons", with a named class only "ideally", admits reasons §8.4 does not. v0.9 itself does not treat the clause as a circularity check: §8.4 leaves "weights forced, not assumed" as a later bar that would need "work on circularity". Read as a quantity inside the theory, LT2's "|psi|^2" needs an object that meets LT1, and v0.9 has none (readiness v0.9 refresh, gap 6); read as a target weight fixed outside the claim, as with v0.9 §10's tree "drawn by hand ... to match |a|^2", it needs no such object, and that is the form a pre-emptive run can check now.
- *LT3.* In v0.9 a prefix's per-vertex weight does not change with the cut, while the count's does (§9; C13, C14), and a later split of a descendant leaves per-vertex weights unchanged and changes counts (readiness §1.2, P7). So "changing the cut", and "irrelevant further splitting" read as later splitting, hold for (M1) by construction and fail for (M2), except for the cut clause where D is constant on the cuts compared (C13) or in the depth limit under asymptotic sibling balance (C15). The tilt is not one-way: a same-vertex split into arms with the same outcome moves both (readiness §1.2), and "refining the grain" can favour the count (re-describing a three-way decision as two binary ones moves the per-vertex weights from 1/3 each to 1/2, 1/4 and 1/4, while the count at the depth-2 cut, dead ends included (§9), stays at 1/3 each). "Irrelevant" is not defined: it needs an outcome labelling (readiness gap 5), and defined as "leaves the weights unchanged" it would presuppose a measure. The phrase is the branch-counting objection recorded in readiness §1.1, item 4; the clause parallels the Deutsch–Wallace fine-graining premise, which critics argue has not been shown to be rational (readiness §1.1; Dizadji-Bahmani 2015, on branching indifference). This is recorded so that LT3 is not read as deciding (M1)/(M2).
```

**B2. LT2 and the §8.4 clause it is mapped to differ in both directions, and LT2 is coupled to LT1** (§2.2). Carried by String B1. Required because the Lead's text ("the §8.4 motivation clause (LT2)") maps them as one.

**B3. LT3 bears unequally on (M1) and (M2), and "irrelevant" is undefined** (§2.2). Carried by String B1.
- Its cut clause and later-split reading hold for (M1) by construction and fail for (M2) in general.
- A same-vertex split moves both.
- Its grain clause can favour (M2).

Required because the test, unrecorded, would bear on an open call the note says it does not decide.

#### Suggested

**B4. The list of open calls the tests touch is incomplete.**
- LT1 and LT4 have no entry.
- Of readiness's "Waits on" calls, the list omits:
  - T3 and #139 (a), on which gaps 1 and 2 wait;
  - #139 (b) and #230's F5, F6, F9 and F10, on which gap 4 waits;
  - #230's F7 and F11, on which gap 3 waits.
- The Zeno-mass convention, which moves weights (C35), is missing.
- Several choices that move weights or the tree are on no LT's list:
  - arrival semantics and T1;
  - realisation (a)/(b);
  - arm individuation;
  - the outcome labelling;
  - the bridge from symmetric cases to equal weight;
  - a typicality rule.

Listing calls rules on none of them.

String B4 (lit) — OLD:
```text
- Open calls that the tests touch: the law of R and the §8.4 motivation clause (LT2); (M1)/(M2), completed versus cut, and the grain (LT3). None is decided here.
```
NEW:
```text
- Open calls and open items that the tests touch (v0.9 §11; readiness v0.9 refresh, "Waits on"). None is decided here.
  - LT1: amplitude-like structure (readiness gap 6, which waits on #139 (e) and #230's F5).
  - LT2: the law of R, the slice and the §8.4 motivation clause (see the Lead's reading after "Pre-emptive use"); T3 and #139 (a), on which readiness gaps 1 and 2 wait.
  - LT2 and LT3: the measure, (M1)/(M2) and T2 (readiness gap 4, which also waits on #139 (b) and #230's F5, F6, F9 and F10); completed versus cut, and the grain; the Zeno-mass convention (§8.3, C35; options (Z-0)–(Z-ix) in `notes/zeno-mass-scoping.md`).
  - LT4: a measurement model ("same outcome"; readiness gap 5, no listed call), coupled to the mapping choice in §11's "Which Bell premise" call and to realisation (a) versus (b).
  - All four: the "hazard, not a route" wording (F-M1 in `notes/merw-litmus-scoping.md`, whose options (ii) and (iii) refer to LT1–LT4).
  - Not on LT2's list ("the law of R, the slice and the measure") but able to move weights or the tree: arrival semantics and T1 (§8.2 item 7; C5, C6); realisation (a)/(b) (C16, C33; readiness gap 3, which also waits on #230's F7 and F11); how arms are individuated (the isotropy quotient, C9; first-edge equivalence, C11); an outcome labelling (readiness gap 5), a step at which part of the literature locates circularity in decoherence-based derivations (for example Baker 2007); the step from symmetric or equal-share cases to equal weight (in the literature, state supervenience, non-contextuality or envariance; in-house, EPP1's equal shares); and a typicality rule (§8.4). Whether LT2 covers them is open.
```

**B5. Read literally, the substitution paragraph's failure condition is not triggered by Paper 1's trivial scheme** (§2.4).
- David's sentences state a sound one-way condition.
- But the trivial scheme's multiplicity input must change under a swap, so "nothing else changing" is not met.
- The verdict therefore turns on S3.

String B5 (lit) — OLD:
```text
swapping the rule should break something upstream: an input, a lemma or a symmetry.
```
NEW:
```text
swapping the rule should break something upstream: an input, a lemma or a symmetry. *(The Lead's note, not David's wording: read literally, this condition is met by every valid derivation. Its premises are inconsistent with any rival rule on the cases they cover, so something upstream always has to change. In Paper 1's trivial scheme (Paper 1 §8), what changes is the multiplicity assignment, which restates the rule. The verdict therefore turns on two judgements of each changed item: whether it is independently motivated, and whether it restates the rule on all or part of its domain (S3 in `notes/substitution-test-scoping.md`).)*
```

**B6. No pointer to the substitution note or to David's ruling of about 11:48 ET.** The substitution note (#256) was merged after the litmus note's last edit (#254). The string also carries B9.

String B6 (lit; carries B9) — OLD:
```text
which scopes what a Born-type claim through the MERW squared-eigenvector density would have to show under LT1–LT4.
```
NEW:
```text
which scopes what a Born-type claim through the MERW squared-eigenvector density (the square of the leading eigenvector when the adjacency matrix is symmetric; on a strongly connected directed graph, the product of the left and right leading eigenvectors) would have to show under LT1–LT4.
- `notes/substitution-test-scoping.md` (#256), the scoping and outline for a separate companion paper on the substitution test (David's ruling of about 11:48 ET on 2026-10-10, relayed by the Physics Lead; the exchange is not recorded in this repository).
```

**B7. What a "pass" in the conjecture would mean under David's own rulings.**
- #255 F5 noted the "Pre-emptive use" point without a string.
- The NEW is conditional, because the relation between the two tests is open.
- It bears only on the conjecture's second half, by limiting what a pass would show, and decides neither half.

String B7 (lit) — OLD:
```text
(for example, whether it sharpens LT2) is open.
```
NEW:
```text
(for example, whether it sharpens LT2) is open (options (R-a) onward in `notes/substitution-test-scoping.md`, none picked). If "Scope and outcomes" also governs this test, the conjecture's "pass" would mean only that no circularity was detected, not that the Born rule emerges; and since "Pre-emptive use" says the test "cannot pass a claim that has not been made", the conjecture's second half can concern only a future claim, as v0.9 makes none (§2).
```

#### Nit

**B8. The Labels line overstates.** The Status line says the wording is "David's as relayed", and Chief of Staff drafted a first version.

String B8 (lit) — OLD:
```text
The wording is David's, unchanged.
```
NEW:
```text
The wording of LT1–LT4 is David's as relayed, unchanged.
```

**B9. "The squared eigenvector of maximal-entropy random walks" needs a gloss.**
- The square holds only for a symmetric adjacency matrix (#251 string 1).
- On a strongly connected directed graph, the density is a left-times-right product (M3).
- David's "Pre-emptive use" paragraph is left untouched. The gloss goes on the Lead's own "Where it connects" line, carried by String B6.

### 5.2 MERW note (`notes/merw-litmus-scoping.md`)

#### Required

**M1. R2 mixes two walk-length conventions** (§1).
- **What the note says.** The setup line says "uniform weight on length-$L$ walks from the root (C36's root count)". The concentrations and 14.185 follow that convention.
- **What the shares are.** The seven shares count $L$ arcs *after* the first step, which is C36's count at $L+1$. That is why 0.400 appears at $L=2$: with one jump arm per segment state, C36's count gives $1/3$ there.
- **The fix.** No conclusion changes. The NEW keeps the pinned figures and labels them.

String M1 (merw) — OLD:
```text
the root's jump-arm share is 0.400, 0.381974, 0.381966, 0.308087, 0.137830, 0.011828, 0.005865 at $L=2$, 10, 20, 50, 100, 1000, 2000: near $1/\varphi^2=0.381966$ for $L\le20$, then toward 0.
```
NEW:
```text
the root's jump-arm share is 0.400, 0.381974, 0.381966, 0.308087, 0.137830, 0.011828, 0.005865 at $L=2$, 10, 20, 50, 100, 1000, 2000, counting $L$ arcs after the first step (C36's root count at length $L+1$; at length $L$, the convention of the setup line of (c) and of the concentration and growth figures, the shares are $1/3$, $55/144=0.381944$, 0.381966, 0.314054, 0.139361, 0.011839, 0.005868). At length $L$ they are exactly the Fibonacci ratios $F_L/F_{L+2}$ for $L\le28$, which tend to $1/\varphi^2=0.381966$. Seven segment states with no admissible jump lie 28 arcs from the root, so from $L=29$ the shares depart from these ratios, and they then fall toward 0.
```

**M2. "Backward pairs" is the wrong category** (O3, O5, Limits, Costs).
- **What v0.9 means by the term.** §5 defines backward pairs as pairs reachable along the source's own curvelet only at $\tau<0$. §11's "Backward-only pairs in $R$" is the same category.
- **What symmetrising adds instead.**
  - At the level of $R$ it adds the converse $(w,v)$ of every jump edge $(v,w)$.
  - The converse of a type-(ii) edge is again type (ii): "Every other pair is type (ii)" (§5). Under (a), $v$'s lump does lie on $w$'s curvelet in $w$'s past, but with a different orientation (C3).
  - No backward pairs are needed. Bound orbits recur, so each orbit's segment 2-cycle is already symmetric.
- **On the instance every converse fails (a):** 0 of 29,118 at $c=0.01$, 0 of 2 at $c=0.1$ (§1).
- **On the flagged state graph**, $\mathcal A+\mathcal A^{\top}$ would also make arcs leave jump-arrival states by a jump and enter them along a segment. §8.2 items 2 and 7 exclude both. Dropping the flag instead lets a history jump back and forth at one accumulated $\tau$, so clause (2) of the hard gate fails per history (§8.2; C5).
- The substitution note inherits the label (X8).

String M2a (merw) — OLD:
```text
| Backward pairs in $R$ (open, §11) | Only if a law of $R$ supplies backward pairs |
```
NEW:
```text
| The converse of every jump edge. The converse of a type-(ii) edge is again an ordinary type-(ii) pair (§5), not a backward pair (§5's backward pairs are reachable along the source's own curvelet only at $\tau<0$; §11). On the instance under (a) every converse fails (a) (0 of 29,118 converses admissible at $c=0.01$, 0 of 2 at $c=0.1$). On the flagged state graph, symmetrising would also make arcs leave jump-arrival states by a jump and enter them along a segment, which §8.2 items 2 and 7 exclude | Only if a law of $R$ supplies converse pairs: on the instance that needs (b), and on the flagged graph a change to items 2 and 7, or dropping the flag, as O1 does (with converse pairs and no arrival rule a history can jump back and forth at one accumulated $\tau$, so clause (2) of the hard gate fails per history, C5) |
```

String M2b (merw) — OLD:
```text
Hermiticity (backward pairs)
```
NEW:
```text
Hermiticity (converse pairs, as for O3)
```

String M2c (merw) — OLD:
```text
**Not run:** an O3 (symmetrised) census, minutes of compute, which needs backward pairs no rule supplies.
```
NEW:
```text
**Not run:** an O3 (symmetrised) census, minutes of compute. Its added arcs are the converses of jump edges, type-(ii) pairs that no rule supplies and that fail (a) on the instance, plus arcs that break the arrival flag (O3 row).
```

String M2d (merw; also carries M16) — OLD:
```text
**Costs.** O2: none to state, but a claim through it would first need a unique $\psi$, which (a) does not give (R1). O3: backward pairs (§11) and an irreducibility proof per $R$.
```
NEW:
```text
**Costs.** O2: a claim through it would first need an irreducible state graph, which the (a)-restriction does not give on the instance (R1), and its density would then be $\psi^{\rm L}\psi^{\rm R}$, in general not a square (section (a) above). O3: converse type-(ii) pairs for every jump edge (§5), which fail (a) on the instance, and on the flagged graph a change to §8.2 items 2 and 7 (dropping the flag instead lets a history jump back and forth at one accumulated $\tau$, so clause (2) of the hard gate fails per history, C5); and a connectedness check per $R$. O6, if added: as O2.
```

**M3. On a directed graph MERW's density is $\psi^{\rm L}\psi^{\rm R}$, not $\psi^2$, in general.**
- **What the note gets right.** Its section (a) restricts $\psi^2$ to the symmetric case.
- **The directed case.** On a directed irreducible graph the same construction has stationary density $\psi^{\rm L}_i\psi^{\rm R}_i$: Parry's maximal-entropy measure [search]. That is the square of a Perron vector only where $\psi^{\rm L}\propto\psi^{\rm R}$.
  - Symmetry is sufficient for this, not necessary. A circulant digraph and a flagged two-orbit toy both have $\psi^{\rm L}=\psi^{\rm R}$ (§1).
  - O2's flagged graph is never symmetric when $R$ has a type-(ii) edge (§3, Q1). So on O2 a coincidence would have to come from $R$ itself, and a square by symmetry needs O3.
- **"Unique" needs a finite matrix.** On an infinite state space neither existence nor uniqueness of a positive eigenvector is automatic. That bears on O1, and on O2 without (a) (M6) (Vere-Jones 1967; Gurevich's criterion via Ruette 2003 [search]).
- **What the note implies.** The O2 row lists only irreducibility as "To be added", which implies that $\psi^2$ would then follow.

String M3a (merw) — OLD:
```text
Perron–Frobenius makes $\psi$ real, positive and unique for a nonnegative irreducible operator, with $\psi^2$ MERW's stationary density when the operator is the symmetric adjacency matrix of a finite connected graph, the only case Burda et al. (2009) treat (§9).
```
NEW:
```text
Perron–Frobenius makes $\psi$ real, positive and unique up to scale for a nonnegative irreducible finite matrix (on an infinite state space neither existence nor uniqueness is automatic, which bears on O1 and on O2 without (a)), with $\psi^2$ MERW's stationary density when the operator is the symmetric adjacency matrix of a finite connected graph, the only case Burda et al. (2009) treat (§9). On a directed irreducible graph the same construction, $P_{ij}=\mathcal A_{ij}\psi^{\rm R}_j/(\lambda\psi^{\rm R}_i)$, has stationary density proportional to $\psi^{\rm L}_i\psi^{\rm R}_i$, the product of the left and right Perron vectors (Parry's measure of maximal entropy; Parry 1964). That is the square of a Perron vector only where the two coincide: always for a symmetric operator, and sometimes otherwise (a regular digraph, for example). O2's flagged state graph is never symmetric when $R$ has a type-(ii) edge: the converse of a jump arc would have to be the arrival state's one out-arc, a segment from target to source, and the edge would then be backward or type (i) (§5). So on O2 the two vectors coincide only if $R$ makes them; a square by symmetry needs O3.
```

String M3b (merw) — OLD:
```text
Irreducibility. The graph is reducible (computed below), so no unique $\psi$ exists
```
NEW:
```text
Irreducibility; even then the density is $\psi^{\rm L}\psi^{\rm R}$, in general not a square (section (a) above). On the instance the graph is reducible (computed below), so no positive Perron vector exists
```

**M4. R1's stated reasons are imprecise, though its conclusion stands** (§1).
- **The SCC count.** The SCCs include 29,118 singletons. #251 F3 itself reports 58,237.
- **"Multiplicity 29,119" is the algebraic multiplicity.**
  - The geometric multiplicity is 14,478, one per stuck orbit, and the index is 15.
  - Eigenvalue $-1$ has the same multiplicities.
- **"No unique Perron vector" is false on one side.** The nonnegative right eigenvector is unique up to scale, but it lives on the root orbit alone.
- **What actually makes MERW undefined.** No eigenvector is positive, and every left–right product vanishes.
- **The note's forward condition is insufficient.** "An $R$ with a unique leading eigenvector" is not enough. A reducible matrix can have a unique leading eigenvector that is not positive: $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ has only $(1,0)$.

String M4 (merw) — OLD:
```text
the strongly connected components are exactly the 29,119 orbit 2-cycles; jumps are acyclic (C33). Spectral radius 1, multiplicity 29,119: no unique Perron vector, so **MERW's $\psi^2$ is undefined here**. There is as yet no $\psi$ here to check for injection; a future claim through O2 would first have to supply an $R$ with a unique leading eigenvector.
```
NEW:
```text
the strongly connected components are the 29,119 orbit 2-cycles and the 29,118 jump-arrival states, which are singletons (58,237 in all); jumps are acyclic (C33). The spectral radius is 1, so the entropy rate is 0. Eigenvalue 1 has algebraic multiplicity 29,119, one per 2-cycle ($-1$ likewise, from period 2), geometric multiplicity 14,478, one per stuck orbit, and index 15, the longest chain of 2-cycles (the root and 14 jumps). The nonnegative right eigenvector is unique up to scale but supported on the root orbit's two segment states alone; the nonnegative left eigenvectors form a cone whose extreme rays, one per stuck orbit, are supported on those orbits. Every left–right product vanishes, so **MERW's density ($\psi^2$ for a symmetric operator, $\psi^{\rm L}\psi^{\rm R}$ for a directed one) is undefined here**. There is as yet no $\psi$ here to check for injection; a future claim through O2 would first have to supply an $R$ whose state graph has positive left and right Perron vectors (an irreducible one has them).
```

**M5. The LT3 row misstates David's LT3, and R3's conclusion repeats the mapping.**
- **The row.** David's LT3 reads "survives refining the grain, changing the cut, and irrelevant further splitting". The row replaces "refining the grain" with "classifier". By v0.9 §3 a classifier is not a grain (§3, Q5).
- **R3.** Its heading and its bold closing sentence read classifier agreement as LT3 robustness. Its closing sentence says "such a claim would be too on this point".
- **A missing case.** The row also covers only later splitting. Given an outcome labelling, a same-vertex split moves both measures (readiness §1.2, P7).

String M5a (merw) — OLD:
```text
A claim would have to be robust to cut depth, classifier and later splitting; the first two are probed in (c); counts are not invariant under later splitting (readiness P7)
```
NEW:
```text
A claim would have to survive LT3's three changes: refining the grain, changing the cut, and irrelevant further splitting. (c) probes the cut (R2 varies the walk length $L$, a depth cut) and checks the computation against a second classifier (R3, not a grain in v0.9 §3's sense); it probes neither a refined grain (for example a finer slice) nor a proper-time cut. Counts are not invariant under later splitting, and given an outcome labelling neither rule is invariant under a same-vertex split (readiness §1.2, P7)
```

String M5b (merw) — OLD:
```text
**R3, the classifier (LT3).**
```
NEW:
```text
**R3, the classifier (a check on the computation, not LT3's grain; see the LT3 row).**
```

String M5c (merw) — OLD:
```text
**The computed shares are robust to the classifier, so such a claim would be too on this point.**
```
NEW:
```text
**The computed shares do not depend on the classifier. This checks the computation; it is not a test of a claim's robustness under LT3.**
```

**M6. "Graph" is used where "completed histories" is meant.**
- **Without (a).** The reachable state graph has at most 3 arms per state (C29), and every state is reached by a finite walk. So it is countably infinite (C5's chains), not a continuum. The continuum is the set of completed histories (C16).
- **Under (a), on the instance.** The reachable graph is finite (87,356 states) and the completed histories are countable (C33).

String M6a (merw) — OLD:
```text
(countable graph under (a), C33; continuum without, C16)
```
NEW:
```text
(under (a), a finite reachable graph on the instance and countable completed histories, C33; without (a), a countably infinite reachable graph, C5, C29, and a continuum of completed histories, C16)
```

String M6b (merw) — OLD:
```text
without (a) (C16) the graph is a continuum.
```
NEW:
```text
without (a) the reachable graph is countably infinite (C5, C29) and its completed histories form a continuum (C16).
```

**M7. The LT2 row reduces LT2 to §8.4's clause**, which differs from LT2 in both directions (B2). The pipes in David's quoted "|psi|^2" are escaped, so that the table row keeps four cells.

String M7 (merw) — OLD:
```text
A claim would have to meet the §8.4 motivation clause; no rule meets it now (C26)
```
NEW:
```text
A claim would have to fix the law of $R$, the slice and the measure for independent reasons (LT2); the §8.4 motivation clause is the existing check on $R$ and no rule meets it now (C26), but its second branch ("states an empirical target") would admit a rule motivated by the Born weights themselves, which LT2 excludes ("not tuned until \|psi\|^2 appears")
```

**M8. F-M1's option costs are asymmetric and its list of places is incomplete.** None of what follows picks an option. Required under the Labels because the uncosted option is favoured.
- **Asymmetric costs.** Option (i) has no cost line.
- **Missing places.** §11 names the MERW hazard as an (M2) cost twice: "the MERW hazard of §9" in the (M2) bullet, and "MERW hazard" in the (M1)/(M2) call row. Option (iii) would leave those pointing at §9 text that no longer says "hazard".
- **A wording mismatch.** Option (ii)'s "could pass" reads against "Pre-emptive use" ("It cannot pass a claim that has not been made"), as #255 F9 noted. #253 F8 had noted a mismatch of (ii) and (iii) with the earlier qualifier.
- **An overlapping open item.** #230's F5 (the Duda wording) is open on the same §9 passage and §12's row.

String M8 (merw) — OLD:
```text
(ii) and (iii) change firewall text and a hold-level reading.
```
NEW:
```text
(i) changes no text, and v0.9 then carries no pointer to this note. (ii) and (iii) change firewall text and a hold-level reading. §11 also names the MERW hazard as an (M2) cost twice ("the MERW hazard of §9" in the (M2) bullet; "MERW hazard" in the (M1)/(M2) call row), which (iii) would leave pointing at §9 text that no longer says "hazard". (ii)'s "could pass" reads against "Pre-emptive use" ("It cannot pass a claim that has not been made"; #255 F9). An option worded as "what a claim through it would have to show under LT1–LT4" would avoid that; whether to reword is the Lead's or David's call. #230's F5 (the Duda wording, which sets how strongly the (M2) hazard reads) is open on the same §9 passage and §12's row.
```

#### Suggested

**M9. "O1–O4 supply no object that superposes" holds only for signed combinations.**
- Walk-count vectors $\mathcal A^Lx$ and EPP1 probability vectors superpose with nonnegative coefficients and evolve linearly, as classical mixtures do.
- What none of them can do is cancel. A Perron vector is a fixed point of the evolution, not an evolving state.
- Readiness §1.2 says only "No amplitudes, phases or interference exist, so histories never cancel".
- This revisits the first clause of #253's string M2, which restored "superposes or cancels"; Literature should be told. The NEW keeps #253's point, that nothing here cancels.

String M9 (merw) — OLD:
```text
O1–O4 supply no object that superposes or cancels (readiness §1.2)
```
NEW:
```text
the nonnegative operators (O1–O4, and O6 if added) supply no object that interferes: walk-count vectors $\mathcal A^Lx$ and EPP1 probability vectors superpose with nonnegative coefficients and evolve linearly, but cannot cancel, and a Perron vector is a fixed point of that evolution, not an evolving state (readiness §1.2: "No amplitudes, phases or interference exist, so histories never cancel")
```

**M10. The LT1 waits-on pointer is wrong.** Readiness gap 6 waits on "#139 (e); F5". "No listed call" is gap 5's entry.

String M10 (merw) — OLD:
```text
(readiness gap 6; no listed call)
```
NEW:
```text
(readiness gap 6, which waits on #139 (e) and #230's F5)
```

**M11. "Its limit is set by the longest chain" is ambiguous.**
- It is true of the limiting jump-count law, and false of the share.
- The share tends to 0 at both values of $c$ (§1).

String M11 (merw) — OLD:
```text
the count is not stable in $L$, and its limit is set by the longest chain, which depends on $c$.
```
NEW:
```text
the share is not stable in $L$ and tends to 0 at both values of $c$ (about $11.6/L$ at $c=0.01$; at $c=0.1$ exactly $1/(L+1)$ at length $L$); the longest chain, which depends on $c$, sets the growth of the walk count ($L^{14}$ against $L$) and the jump count on which walks concentrate.
```

**M12. A missing option: the proper-time transfer operator.**
- The note's Limits already say "a walk-length cut, not proper time", and v0.9 uses proper-time cuts (§9; C14, C29).
- Adding the operator picks nothing.
- Its absence changes no conclusion, so the finding is Suggested.

String M12 (merw) — OLD:
```text
the path-integral route is out of scope (readiness §1.2) |
```
NEW:
```text
the path-integral route is out of scope (readiness §1.2) |
| O6 Proper-time transfer operator $\mathcal A_{ij}e^{-s\tau_{ij}}$ on O2's state graph ($\tau_{ij}$ the segment's proper time, 0 on a jump; $s$ set so that the spectral radius is 1) | Nonnegative; under strict alternation every cycle carries positive $\tau$. Given irreducibility (and cycle proper times not all multiples of one period), its Perron data give the count at a long proper-time cut, where O2 gives the walk-length count (§9's proper-time cuts; C14, C29). On the instance the entropy is 0, so $s=0$ and its spectrum is O2's | As O2: irreducibility, and a $\psi^{\rm L}\psi^{\rm R}$ density | A law of $R$ |
```

**M13. O3 is ambiguous between two symmetrisations.**
- $\mathcal A+\mathcal A^{\top}$ has entry 2 on every two-way pair, including each orbit's segment 2-cycle.
- Burda et al.'s setting, which the row's parenthesis cites, is the 0/1 adjacency of the underlying undirected graph.

String M13 (merw) — OLD:
```text
O3 Symmetrised adjacency $\mathcal A+\mathcal A^{\!\top}$
```
NEW:
```text
O3 Symmetrised adjacency, either $\mathcal A+\mathcal A^{\!\top}$ (entry 2 on each two-way pair, such as an orbit's segment 2-cycle) or the 0/1 adjacency of the underlying undirected graph, which in general give different $\psi$
```

**M14. R4's closing sentence tests the wrong property.** The disjoint toy does superpose: its leading eigenspace is 2-dimensional. With disjoint supports, though, it cannot cancel.

String M14 (merw) — OLD:
```text
A future LT1 claim through O3 would have to show superposition that these toys do not.
```
NEW:
```text
A future LT1 claim through O3 would have to show interference that these toys do not; the degenerate disjoint toy does superpose (every $a\psi_1+b\psi_2$ is a leading eigenvector) but, with disjoint supports, cannot cancel.
```

**M15. R4's bridge sequence measures decay along the bridge.**
- The figures reproduce only for $P_4$ attached by an end vertex, with the bridge vertices not counted.
- $K_4$ already holds 0.957631 at no bridge.
- The mass off $K_4$ stays near 0.0425 as the bridge grows.

String M15 (merw) — OLD:
```text
with 1–3 bridge vertices, winner-take-all rather than superposition.
```
NEW:
```text
with 1–3 bridge vertices ($P_4$ attached by an end vertex; bridge vertices not counted). $K_4$ already holds 0.957631 with no bridge, and the mass off $K_4$ stays near 0.0425 as the bridge grows, so the falling sequence is decay along the bridge; the localisation itself is winner-take-all rather than superposition.
```

**M16. The Costs line is asymmetric.** O2 is listed as having "none to state", but it carries the same irreducibility hurdle as O3, plus a density that is in general not a square. This is carried by String M2d. It is Suggested, because the operators are candidate routes for a hypothetical claim, not options of an open call.

**M17. R3 should name the state that differs.** Two independent rebuilds find no target near a classification boundary, so the 87,357 / 14,477 variant could not be reproduced (§1).

String M17 (merw) — OLD:
```text
one state differs (87,357 against 87,356);
```
NEW:
```text
one state differs (87,357 against 87,356; which state, and why, is not recorded);
```

**M18. Once M3a cites Parry (1964), the Scope line's literature rule needs an exception.**

String M18 (merw) — OLD:
```text
Literature only as v0.9 cites it (Burda et al. 2009; Duda 2011; Faber 2024).
```
NEW:
```text
Literature only as v0.9 cites it (Burda et al. 2009; Duda 2011; Faber 2024), except Parry (1964, *Trans. Amer. Math. Soc.* 112, 55–66) for the directed case in section (a), which v0.9 does not cite and Literature has not checked.
```

#### Nit

**M19. The Read-at line predates the paragraphs the Scope line cites.**

String M19 (merw) — OLD:
```text
`notes/born-litmus-test.md` (L3) as merged in #248 (`001dde2`)
```
NEW:
```text
`notes/born-litmus-test.md` (L3) as merged in #248 (`001dde2`), with "Scope and outcomes" and "Pre-emptive use" as added in #252 (`974aeec`) and revised in #254 (`f8917fb`)
```

**M20. The Zeno range is stale.** #259 and #261 added (Z-vi)–(Z-ix).

String M20 (merw) — OLD:
```text
(Z-0)–(Z-v) where a cut meets accumulation
```
NEW:
```text
(Z-0)–(Z-ix) of `notes/zeno-mass-scoping.md` where a cut meets accumulation
```

**M21. The LT1 row's pointer.** "§8.2 item 1" constrains $R$'s sources, which is LT2's pointer.

String M21 (merw) — OLD:
```text
| §8.2 item 1; C36 |
```
NEW:
```text
| §9 (MERW paragraph); §10 (circularity wall); C36 |
```

**M22. "Finite under the (a)-restriction" holds on one instance.**

String M22 (merw) — OLD:
```text
Nonnegative, finite under the (a)-restriction (C33)
```
NEW:
```text
Nonnegative; finite on the instance under the (a)-restriction (C33)
```

**M23. Name the join.** 0.933865 holds only for the end-to-end join.

String M23 (merw) — OLD:
```text
Two $P_4$ joined by an edge:
```
NEW:
```text
Two $P_4$ joined end to end by an edge (that is, $P_8$; an end-to-inner join gives 0.935064, and an inner-to-inner join 0.967549):
```

**M24. The positivity lead-in overstates what the inequality shows.** The inequality is stated for $a,b\ge0$, but "Positivity excludes cancellation" is unqualified, and signed combinations of positive vectors can cancel.

String M24 (merw) — OLD:
```text
Positivity excludes cancellation:
```
NEW:
```text
Positivity excludes cancellation among nonnegative combinations, the only ones a nonnegative operator produces from nonnegative data:
```

**M25. The growth figures.** The exponent tends to 14, and at $c=0.1$, $N_L=L+1$ exactly.

String M25 (merw) — OLD:
```text
$\log_2(N_{2000}/N_{1000})=14.185$ (longest chain 14); $0.999$ at $c=0.1$ (3 orbits, chain 1).
```
NEW:
```text
$\log_2(N_{2000}/N_{1000})=14.185$, tending to 14 (longest chain 14 jumps; index 15); $0.999$ at $c=0.1$, where $N_L=L+1$ exactly (3 orbits, chain 1).
```

**M26. "Dead ends drop out" is vacuous on the instance.** Every state has an out-arc, and v0.9 §9's convention keeps dead ends in a cut.

String M26 (merw) — OLD:
```text
dead ends drop out;
```
NEW:
```text
dead ends would drop out, where v0.9 §9's convention keeps them in a cut (none occur on the instance: every state has an out-arc);
```

**M27. R2's bold line says "grain" where the probe varies a cut** (§3, Q5).

String M27 (merw) — OLD:
```text
claim at this grain would not be robust (LT3):
```
NEW:
```text
claim at this cut would not be robust (LT3):
```

### 5.3 Substitution note (`notes/substitution-test-scoping.md`)

#### Required

**X1. S1 does not trace breaks back to premises.**
- **Two literal readings.**
  - S1 lists "premises, lemmas or symmetries ... inconsistent with $W'$". Read item-wise over primitive premises, S1 for branch counting can be empty: Wallace states the break as the combination of branching indifference and diachronic consistency [#257]. The definition then says "slides in", a failure.
  - Read item-wise with lemmas, S1 holds derived items, such as the fine-graining condition readiness §1.1 says excludes counting. Their S3 status turns on the premises they come from, and the format does not trace them.
- **The tilt.** On the first reading the format alone would tilt the first half of the conjecture toward "fails". How far depends on which premises are listed, since the row also lists fine-graining invariance, a single item.
- **The cost claim.** The note's "every valid derivation has a non-empty S1 by logic" holds for set-valued S1, and for item-wise S1 only if lemmas count.
- **A missing slot.** S1 also needs a place for a $W'$ that is undefined on $D$'s objects (X6).

String X1 (sub) — OLD:
```text
- **(S1)** the break list: the premises, lemmas or symmetries of $D$ that are inconsistent with $W'$;
```
NEW:
```text
- **(S1)** the break list: the premises, lemmas or symmetries of $D$ that are inconsistent with $W'$, each traced back to the minimal sets of premises of $D$ that are jointly inconsistent with $W'$ (a set may have two or more members: Wallace says branch counting "violates the combination of branching indifference and diachronic consistency"), and any object of $D$ on which $W'$ is not defined;
```

**X2. S3's dichotomy is not exhaustive.** It runs two judgements together: independent motivation, and restating $W$. Four cells result.
- **"Both":** independently motivated, yet restating $W$ on a sub-case, as the equal-amplitude step is charged with doing. This is the step critic question 2 contests.
- **"Neither":** not independently motivated, and not a restatement of $W$.

String X2 (sub) — OLD:
```text
- **(S3)** whether each broken item is independently motivated, or is $W$ (or a special case of $W$) restated.
```
NEW:
```text
- **(S3)** for each broken item or set, two separate judgements: whether it is independently motivated, and whether it restates $W$ (or a special case of $W$). Four cells result, including "both" (independently motivated, yet restating $W$ on a sub-case, as the equal-amplitude step is charged with doing: the step critic question 2 asks about) and "neither" (not independently motivated, and not a restatement of $W$; the Kretschmann rule, stated and uniform but unmotivated (C26), is an example outside any derivation).
```

**X3. "In part" settles critic question 2 by definition.**
- **The example.** The definition's example, "such as equal weights", presents DW's contested step as a case of restatement.
- **Read as "entails", it is degenerate.** The premises of every valid derivation jointly entail $W$ on every sub-case. So every derivation would fail "in part": DW, every symmetry-based route, and, if amplitudes were ever introduced, any equal-weight item in this framework, EPP1 included.
- **The neutral fix.** Neither including nor excluding the "both" cell by definition is neutral. The NEW leaves the cell open, and gives "slides in" the same care.

String X3 (sub) — OLD:
```text
"Slides in" means that S1 is empty, or holds only items judged under S3 to be restatements. "In part" means that some item restates $W$ on a sub-case, such as equal weights, or is a parameter tuned to $W$.
```
NEW:
```text
"Slides in" means that S1 is empty, or holds only items judged under S3 to restate $W$. "In part" means that some item restates $W$ on a sub-case (for example, equal weights for equal amplitudes, if S3 judges that a restatement), or is a parameter tuned to $W$. "Restates" is narrower than "entails": the premises of any valid derivation jointly entail $W$ on every sub-case, so entailment alone would make every derivation fail "in part". Whether an item in S3's "both" cell (independently motivated, yet restating $W$ on a sub-case) triggers either definition is left open **[PJ]**: it is critic question 2, and the same judgement would reach any equal-weight item in this framework, EPP1 included, if amplitudes were ever introduced.
```

**X4. The T-a and T-b cost lines are asymmetric.**
- **Where the one cost sits.** It is under T-b but is a cost of T-a. T-b has none of its own, which favours it.
- **Two literal readings for the trivial scheme.** If the copy-number rule counts as "something else", it changes under a swap, so the scheme does not slide in, and a failure needs S3 left implicit. If the rule counts as $W$ itself, the scheme slides in.

String X4 (sub) — OLD:
```text
**Option T-b** keeps David's informal wording ("slides in / does not"). **Cost:** under T-a every valid derivation has a non-empty S1 by logic, so the content lies in S3, an LT2-type judgement.
```
NEW:
```text
**Cost of T-a:** where $W'$ conflicts with $W$ on the domain $D$ covers, every valid derivation has a non-empty S1 by logic, so the content lies in where S1 falls, in S2 and in S3, an LT2-type judgement. **Option T-b** keeps David's informal wording ("slides in / does not"). **Cost of T-b:** "nothing else changing" is not defined. Paper 1's trivial scheme (Paper 1 §8: copies "proportional to $|a_n|^2$") shows the gap. If the copy-number rule counts as something else, swapping $|a|^2$ for $|a|^p$ changes it, so the scheme does not slide in, and ruling it a failure needs the judgement that the changed item restates $W$, which is S3 left implicit (David's "cannot be passed on a technicality" may be read as supplying it). If it counts as $W$ itself, the scheme slides in.
```

**X5. The relation options' cost lines are asymmetric.** Only (R-b) has a cost, which tilts the choice toward the uncosted options. The NEW also carries (R-d)'s cost, if X20 is applied.

String X5 (sub) — OLD:
```text
**Adds** under any option: a concrete counterfactual, named substitutes $W'$ and a record format (S1–S3). **Cost:** (R-b) needs an S3 criterion distinct from LT2, or it reduces to (R-a).
```
NEW:
```text
**Adds** under any option: a concrete counterfactual, named substitutes $W'$ and a record format (S1–S3). **Costs:** (R-a): LT2 as worded names the law of $R$, the slice and the measure, so applying S3 to other items (symmetries, rationality axioms, the outcome labelling) widens LT2, and S1–S2, which record what must change rather than where inputs come from, have no slot in it. (R-b): it needs an S3 criterion distinct from LT2, or it reduces to (R-a). (R-c): it can run only where LT1, LT3 and LT4 can be stated, which for this framework waits on readiness gaps 6 (LT1), 4 (LT3) and 5 (LT3's "irrelevant", and LT4), and on a law of $R$ (gap 1). (R-d), if recorded: two criteria then bear on one test, and which governs when they disagree must be said.
```

**X6. The branch-counting row leaves out Wallace's argument that branch number is not well defined** (§4.1).
- The NEW records it in the note's neutral voice: "on Wallace's account".
- It also notes that whether the argument succeeds is part of what the S3 column records as contested.

String X6 (sub) — OLD:
```text
| Uniform branch counting | Branching indifference with diachronic consistency (the combination Wallace says branch counting violates) / fine-graining invariance;
```
NEW:
```text
| Uniform branch counting | Upstream of the axioms, on Wallace's account: branch number is not well defined once branching is the approximate, emergent product of decoherence (Wallace 2010, §9: "There is no such thing as 'branch count'"; Wallace 2012, §3.11, "How many worlds?", and §5.8.1, "Branch counting" **[L]**), so counting would be undefined on $D$'s objects rather than excluded by an axiom; whether that argument succeeds is part of what the S3 column records as contested (Kent 2010 argues that the same fuzziness makes a precise decision theory over branches incoherent). At the axiom level: branching indifference with diachronic consistency (the combination Wallace says branch counting violates) / fine-graining invariance;
```

**X7. Barnum et al. are cited without Wallace's direct reply.** The section is headed "described only" and treats DW "not as a rival", yet it records the charge without the defence. Wallace 2003's abstract is [search]. Its measurement-neutrality passage and Greaves 2004 are [search].

String X7 (sub) — OLD:
```text
Barnum et al. (2000; readiness refs) charge a hidden probabilistic assumption.
```
NEW:
```text
Barnum et al. (2000; readiness refs) charge a hidden probabilistic assumption; Wallace (2003) replies that the flaw they identify does not apply once the Everett interpretation is assumed, and makes explicit a tacit premise of Deutsch's proof, measurement neutrality; Greaves (2004) finds measurement neutrality less plausible on her reading **[L]**.
```

**X8. Table (ii) has two defects.**
- **The MERW row.**
  - It repeats "backward pairs" (M2).
  - Its "$p=2$ comes from the uniform-path definition" needs more: at an interior site the density is $\psi^{\rm L}\psi^{\rm R}$, which is the square of the Perron vector only where the two coincide (§4.3, question 4).
  - The truncation it lists is O1's.
- **Missing rows.**
  - There is no row for the outcome labelling (the measurement model, readiness gap 5). That is one step at which the literature locates circularity in decoherence-based derivations (Baker 2007 [search]).
  - The exhaustion (§8.3; §9 *Exhaustion*; §11) is another entry point.

The two new rows are appended in the same string, because they follow the MERW row.

String X8 (sub) — OLD:
```text
so $p=2$ comes from the uniform-path definition. **[PJ]**: whether that counts as an upstream break is the S3 question | Symmetrisation (O3, backward pairs) or phases (O5) supplied by hand; a truncation chosen for its density |
```
NEW:
```text
so $p=2$ comes from the uniform-path definition together with that symmetry: at an interior time the uniform-path density is $\psi^{\rm L}_i\psi^{\rm R}_i$, one factor from each half of the path (a single factor at a free end), and it is the square of the Perron vector only where the left and right vectors coincide, as they do for a symmetric operator. On O2 at $c=0.01$ there is no positive Perron pair to swap (MERW note R1). **[PJ]**: whether that counts as an upstream break is the S3 question | Symmetrisation (O3: converse type-(ii) pairs, not §5's backward pairs; they fail (a) on the instance) or phases (O5) supplied by hand; a truncation (O1) chosen for its density |
| Outcome labelling, the measurement model (§4 "Measurement, informally"; readiness gap 5) | Another grouping of arms into "the same outcome" | Nothing yet: no labelling exists to swap | Grouping arms into outcomes so that their weights hit a target, one step at which the literature locates circularity in decoherence-based derivations (Baker 2007 **[L]**) |
| Exhaustion, if countable stars are kept (§8.3; §9 *Exhaustion*; §11) | Another exhaustion | Nothing yet: the default is finite stars | An exhaustion chosen so that a limit of ratios hits a target |
```

**X9. "The §8.4 motivation clause is LT2's check" repeats the gap that B2 and M7 fix** in the other two notes. Without this string the three notes would disagree.

String X9 (sub) — OLD:
```text
the §8.4 motivation clause is LT2's check
```
NEW:
```text
the §8.4 motivation clause is the existing check on $R$, and it and LT2 differ both ways: its second branch ("states an empirical target") would admit a rule motivated by the Born weights themselves, which LT2 excludes, and LT2 asks for a named class only "ideally"
```

#### Suggested

**X10. "The minimal edit" is not unique.** With a two-member break set, weakening either member may suffice, so one $W'$ can have several minimal edits.

String X10 (sub) — OLD:
```text
- **(S2)** the minimal edit to $D$ that yields $W'$;
```
NEW:
```text
- **(S2)** the minimal edits to $D$ that yield $W'$ (in general several: where a break set has two members, weakening either may suffice; each is recorded);
```

**X11. The substitute family.**
- **The splitting arithmetic presupposes the 2-norm.**
  - Splitting $a$ into $n$ branches of $a/\sqrt n$ uses the 2-norm, the norm unitary evolution conserves. A split into $a/n$ would single out $p=1$.
  - So the arithmetic locates the break in the norm the splitting conserves; it does not derive it. That keeps both sides of the row's S3 question visible.
- **One family, not two.** Counting is the $p=0$ member (for nonzero amplitudes). With $|a|^2=0.3$ split in two, $p=0,1,2,3$ move from $0.5\to0.667$, $0.396\to0.481$, $0.3\to0.3$ and $0.219\to0.166$.
- **Neither substitute probes the equal-amplitude step.** Both agree with $W$ on equal amplitudes. That needs a $W'$ that weights equal-amplitude branches unequally when they differ only in features the axioms treat as irrelevant: a label- or macrostate-dependent rule.
  - Albert's (2010) fatness rule also weights equal-amplitude branches unequally.
  - But Wallace (2010, §9) locates its break at diachronic consistency, not at the equivalence lemma [#257].
- **Physics-side precedents:** Aaronson 2004; Galley and Masanes 2018 [search].

String X11a (sub) — OLD:
```text
So the candidate break points are additivity under splitting, and the norm's role in the equivalence lemma (erasure with state supervenience)
```
NEW:
```text
The split into $n$ branches of amplitude $a/\sqrt n$ already uses the 2-norm (a split into $a/n$ would single out $p=1$), so the arithmetic locates the break in the norm the splitting conserves (in quantum mechanics, the norm unitary evolution conserves) rather than deriving it. The candidate break points are therefore additivity under splitting, and the norm's role in the equivalence lemma (erasure with state supervenience). Uniform branch counting is the $p=0$ member of the family (for nonzero amplitudes), and the same payoff-neutral split moves the normalised odds of every $p\ne2$, branch counting included; physics-side results on what breaks when the norm or the Born rule is changed inside quantum theory are a further comparison point (Aaronson 2004; Galley and Masanes 2018) **[L]**
```

String X11b (sub) — OLD:
```text
**Cost.** Exact premises and which lemma uses each **[L]**
```
NEW:
```text
**Missing substitutes.** Both rows agree with $W$ on equal amplitudes (readiness §1.1's condition (a) holds for every $|a|^p$ and for counting), so neither probes the step critic question 2 asks about. That needs a $W'$ that weights equal-amplitude branches unequally when they differ only in features the axioms treat as irrelevant, such as a label- or macrostate-dependent rule. Albert's (2010) fatness rule (Born weight times the agent's mass) also weights equal-amplitude branches unequally, but Wallace (2010, §9) locates its break at diachronic consistency rather than at the equivalence lemma.

**Cost.** Exact premises and which lemma uses each **[L]**
```

**X12. Part of S1 for DW is already published** (§2.4). The critics mainly dispute S3, so a run on DW engages an existing exchange.

String X12 (sub) — OLD:
```text
**Running the test (outline).**
```
NEW:
```text
**Running the test (outline).** Part of S1 for DW is already published: Wallace (2010, §9) argues that the rival rules proposed "all contradict the Born rule, and so all violate the decision-theoretic axioms", and for each says which axiom or combination it violates (for Price's rule: continuity, or no counterexample); the critics below mainly dispute S3. A run on DW therefore engages that exchange rather than opening it, and adds most where it supplies S2 and a stated S3 criterion.
```

**X13. Paper 1's own line on Deutsch and Wallace** belongs in the framing caution (Paper 1 §9, verified in the file).

String X13 (sub) — OLD:
```text
Paper 1 says these objects "are not Everett worlds";
```
NEW:
```text
Paper 1 says these objects "are not Everett worlds" and that it "does not argue against Deutsch and Wallace in order to occupy their problem" (§9);
```

**X14. A panel of cases, offered as an option** (§4.3, questions 1 and 5).

String X14 (sub) — OLD:
```text
No side-by-side may suggest an Everettian alternative.
```
NEW:
```text
No side-by-side may suggest an Everettian alternative. Within that limit, one option is a panel rather than DW alone, in one record format: Zurek (2005); Saunders (2021), the case nearest (M2) (a count at a grain of equal-norm units); Sebens and Carroll (2018); Bohmian equivariance (Dürr, Goldstein and Zanghì 1992, the nearest neighbour of v0.9's adopted co-existence reading; Goldstein and Struyve 2007); Gleason (1957); frequency-operator arguments (Hartle 1968; Farhi, Goldstone and Gutmann 1989; critique: Caves and Schack 2005); MERW; and Paper 1's trivial scheme as a known-failure control (its failure itself needs the S3 judgement; see the cost of T-b). Cost: more Literature work **[L]**, an S3 judgement for every case, and a case whose pass the parties agree on, which may not exist; gain: calibration (critic question 1) and no two-party comparison (critic question 5).
```

**X15. Pre-emptive table: an empty break column is not, by T-a's definitions, a verdict.**
- In the EPP1 and (M2) rows, "Nothing upstream" and "Nothing" look like the slide-in signature.
- The T-a definitions apply to a derivation of $W$, and table (ii) has none.
- Whether declared postulates are tested in their own right is critic question 3, left open.

String X15 (sub) — OLD:
```text
**[PJ]**: no row is a pass or a fail.
```
NEW:
```text
**[PJ]**: no row is a pass or a fail. The T-a definitions are stated for a derivation of $W$, and table (ii) has none, so by those definitions an empty break column ("Nothing upstream", "Nothing") records that the item is a declared postulate or named extra: it is neither a "slides in" verdict for $W$ nor its absence. Whether a declared postulate is tested in its own right, so that an empty column would count, is critic question 3, left open **[PJ]**.
```

**X16. The Dizadji-Bahmani attribution is readiness's gloss** (§4.1).

String X16 (sub) — OLD:
```text
readiness §1.1 notes that (b) "excludes branch counting by assumption" (Dizadji-Bahmani 2015)
```
NEW:
```text
readiness §1.1 says (b) "excludes branch counting by assumption", citing Dizadji-Bahmani (2015), whose stated target is branching indifference: he argues that Wallace has not shown it to be rational, that branch counting, which violates it, is a rational alternative, and that Wallace's arguments against branch counting are unpersuasive **[L]**
```

**X17. The Wallace 2010 label merges a preprint and a chapter, and the caveat should say what is unchecked** (§4.2).

String X17 (sub) — OLD:
```text
the axiom statements below follow the preprint version (Wallace 2010, arXiv:0906.2718, §§4–7)
```
NEW:
```text
the axiom statements below follow the preprint (arXiv:0906.2718, "A formal proof of the Born rule from decision-theoretic assumptions", §§4–7), published as Wallace (2010), "How to prove the Born rule", in *Many Worlds?*, pp. 227–263; quotations and section numbers cited to Wallace (2010) here are the preprint's. The book adds appendices with formal proofs of supporting results (App. C, and App. D, "Proof of the Utility Equivalence Lemma"); whether the chapter's or the book's wording, numbering, axiom names and lemmas match the preprint's is not checked **[L]**
```

**X18. "Readiness scan" is misattributed.** The readiness refresh says: "That weights can depend on nothing but the tree is §1.2's structural point, not a scan result."

String X18 (sub) — OLD:
```text
Weights follow tree shape only (readiness scan)
```
NEW:
```text
Weights follow tree shape only (readiness §1.2, a structural point; the readiness scan shows, on one unadopted instance, a germ parameter entering through tree shape alone)
```

**X19. (R-b)'s "counterfactual dependence of the output on the inputs" is ambiguous.** In the usual sense (vary the inputs, see whether the output varies) it runs the wrong way. The swap asks whether the inputs fix the output.

String X19 (sub) — OLD:
```text
It checks counterfactual dependence of the output on the inputs, which LT2 does not;
```
NEW:
```text
It checks whether the inputs fix the output (whether a different output is consistent with them, and what must change if not), which LT2 does not;
```

**X20. A fourth relation option is worth recording:** the test as the operational form of the scope ruling's single question.
- It is Suggested, not Required. It overlaps (R-b), which already makes the test separate from LT1–LT4.
- Its cost is in X5's line.

String X20 (sub) — OLD:
```text
LT4's second setup adds independent breaks.
```
NEW:
```text
LT4's second setup adds independent breaks;
- **(R-d)** the operational form of the litmus test's single question ("was the Born rule put in by hand?", "Scope and outcomes"): a detector for the failure outcome, with LT1–LT4 kept as the conditions for genuine emergence ("YES on all four").
```

**X21. The Zeno row is stale, and its value list was incomplete even at the Read-at.**
- (Z-v) and (Z-viii) are requirements, not readings.
- Counting (Z-iv) has limit $0$ on C35 with $X$ a single history.
- "Instance pins unchanged" holds under (A).

String X21 (sub) — OLD:
```text
| (Z-0)–(Z-v) | Only C35 moves (undefined, $1/2$, $1$). Instance pins are unchanged (C7) |
```
NEW:
```text
| (Z-0)–(Z-ix) of the Zeno note ((Z-v) and (Z-viii) are requirements, not readings) | Of the C-rows, only C35 moves: undefined, $1/2$ or $1$ under v0.9's three readings, and $0$ as the counting limit of (Z-iv) with $X$ a single history; the note's further toys give other values (for example $2/3$ on V2 under (Z-iii)). Instance pins are unchanged under (A) (C7) |
```

**X22. The note has no reference list**, though it cites works that are in neither v0.9 nor readiness. The list below has only what the note and these strings cite. **[L]** marks entries Literature has not yet checked.

String X22 (sub) — OLD:
```text
5. Can a companion paper run the test on DW without staging the framing v0.9 §2 excludes?
```
NEW:
```text
5. Can a companion paper run the test on DW without staging the framing v0.9 §2 excludes?

## References (beyond v0.9 and readiness)

- Aaronson, S. (2004). Is quantum mechanics an island in theoryspace? arXiv:quant-ph/0401062 **[L]**.
- Albert, D. Z. (2010). Probability in the Everett picture. In Saunders, Barrett, Kent and Wallace (eds), *Many Worlds?*, OUP, 355–368.
- Baker, D. J. (2007). Measurement outcomes and probability in Everettian quantum mechanics. *Stud. Hist. Phil. Mod. Phys.* 38(1), 153–169 **[L]**.
- Caves, C. M., and Schack, R. (2005). Properties of the frequency operator do not imply the quantum probability postulate. *Ann. Phys.* 315, 123–146; arXiv:quant-ph/0409144 **[L]**.
- Farhi, E., Goldstone, J., and Gutmann, S. (1989). How probability arises in quantum mechanics. *Ann. Phys.* 192, 368–382 **[L]**.
- Galley, T. D., and Masanes, Ll. (2018). Any modification of the Born rule leads to a violation of the purification and local tomography principles. *Quantum* 2, 104 **[L]**.
- Gleason, A. M. (1957). Measures on the closed subspaces of a Hilbert space. *J. Math. Mech.* 6, 885–893 **[L]**.
- Goldstein, S., and Struyve, W. (2007). On the uniqueness of quantum equilibrium in Bohmian mechanics. *J. Stat. Phys.* 128, 1197–1209; arXiv:0704.3070 **[L]**.
- Greaves, H. (2004). Understanding Deutsch's probability in a deterministic multiverse. *Stud. Hist. Phil. Mod. Phys.* 35(3), 423–456 **[L]**.
- Hartle, J. B. (1968). Quantum mechanics of individual systems. *Am. J. Phys.* 36(8), 704–712 **[L]**.
- Kent, A. (2010). One world versus many: the inadequacy of Everettian accounts of evolution, probability, and scientific confirmation. In *Many Worlds?*, 307–354; arXiv:0905.0624.
- Maudlin, T. (2014). Critical study: David Wallace, *The Emergent Multiverse*. *Noûs* 48(4), 794–808.
- Price, H. (2010). Decisions, decisions, decisions: can Savage salvage Everettian probability? In *Many Worlds?*, 369–390.
- Read, J. (2018). In defence of Everettian decision theory. *Stud. Hist. Phil. Mod. Phys.* 63, 136–140 **[L]**.
- Wallace, D. (2003). Everettian rationality: defending Deutsch's approach to probability in the Everett interpretation. *Stud. Hist. Phil. Mod. Phys.* 34(3), 415–439; arXiv:quant-ph/0303050 **[L]**.
- Wallace, D. (2010). How to prove the Born rule. In *Many Worlds?*, 227–263; preprint arXiv:0906.2718.
```

#### Nit

**X23. The Read-at line is stale.** The Zeno note was revised after it in #259 and #261, and the readiness refresh in #259.

String X23 (sub) — OLD:
```text
**Read at:** main `f8917fb` (#254 merged):
```
NEW:
```text
**Read at:** main `f8917fb` (#254 merged; the Zeno note was revised after it in #259 and #261, and the readiness refresh in #259):
```

**X24. The arrival row's label.** v0.9's notation table says (a)/(b) are "unrelated to the flag $a$".

String X24 (sub) — OLD:
```text
| Arrival flag, (a)/(b) (§8.2 item 7; C6, C30, C33) |
```
NEW:
```text
| Arrival rule (A) (§8.2 item 7; C5, C6) and realisation (a)/(b) (§8.2; C16, C30, C33) |
```

**X25. The arrival row uses "tree" where it means completed histories**, as M6 corrects in the MERW note.

String X25 (sub) — OLD:
```text
They shape the tree (countable or continuum, C33/C16), not the weight rule
```
NEW:
```text
They shape the tree (under (a), on the instance, a finite state graph with countable completed histories, C33; without (a), a countably infinite state graph with a continuum of completed histories, C16), not the weight rule
```

**X26. The MERW row's pointer.** Its "truncation" is O1's.

String X26 (sub) — OLD:
```text
MERW route (§9; C36; MERW note O2–O5)
```
NEW:
```text
MERW route (§9; C36; MERW note O1–O5)
```

**X27. The gap range.** Gap 0 is keeping type (ii).

String X27 (sub) — OLD:
```text
which waits on readiness gaps 1–6.
```
NEW:
```text
which waits on readiness gaps 0–6.
```

**X28. (R-c)'s first clause** can name its reason.

String X28 (sub) — OLD:
```text
LT1's amplitude work elsewhere adds uses that break under $p\ne2$;
```
NEW:
```text
LT1's amplitude work elsewhere adds uses that break under $p\ne2$ (unitary evolution conserves $\sum|a|^2$ but in general not $\sum|a|^p$, and for $p\ne2$ no nontrivial linear map preserves the $p$-norm; Aaronson 2004 **[L]**);
```

**X29. The C14 pointer can be sharper.**
- On C14's generation-regular tree the per-vertex weight is also the count at every depth cut. So "$2/3$ against $1/2$" does show cut dependence, but only indirectly.
- C13 shows it directly.

String X29 (sub) — OLD:
```text
Weights depend on it (C14: $2/3$ against $1/2$)
```
NEW:
```text
Weights depend on it (C13: the $A$-prefix count is $3/5$ at depth 2 and $1/2$ at depth 3; C14: $2/3$ at a proper-time cut against $1/2$, the per-vertex weight and, on that generation-regular tree, the count at every depth cut)
```

**X30. Balance in the S3 column.** Read 2018 defends the programme in general.

String X30 (sub) — OLD:
```text
a critical study of Wallace 2012)
```
NEW:
```text
a critical study of Wallace 2012; for the programme in general, besides Wallace, Read 2018 **[L]**)
```

### 5.4 Outside the targets, and what verification changed (no string)

**Outside the targets.**
- **Readiness §1.1, Dizadji-Bahmani.** Its "The rival is ruled out by an axiom, not an argument (Dizadji-Bahmani 2015)" overstates him. On his own account he engages Wallace's arguments against branch counting and finds them unpersuasive [search]. The same gloss reaches the substitution note (X16).
- **Readiness §1.1 item 4.** It cites "Wallace (2012), §5.8.1" for the incoherence objection. The fullest statement is in ch. 3, §3.11, pp. 99–102 [search]; §5.8.1 is the survey.
- **Readiness §1.1, Schlosshauer and Fine.** Its list ("additivity", "'equal amplitude' as the unit of fine-graining") could be confirmed only in part [search].
- **Readiness §1.1, Vaidman.** "Vaidman's measure is postulated" fits Vaidman 1998. Vaidman 2012 and McQueen and Vaidman 2019 argue for it from symmetry and locality [search].
- **Readiness gap 4.** It still lists "(Z-0)–(Z-viii)", though #261 added (Z-ix).
- **#253 M2.** The string restored "O1–O4 supply no object that superposes or cancels". M9 revisits its first clause, and Literature should be told.
- **The substitution note's "main paper"** (Status line) is not defined: v0.9, or a later version? No string, since David's ruling is not in the repository.

**What the verification round changed in substance.** The draft had four errors that the skeptics caught:
1. **"Through O2 no square arises."** False. A non-symmetric graph can have $\psi^{\rm L}=\psi^{\rm R}$, and two exact examples are in §1. M3, X8, §3 (Q1, Q3, Q4) and §4.3 (Q4) now say "only where the two coincide".
2. **"The seven states are all depth-13 apastra, first reached at $L=29$."** Wrong in detail. They are six depth-13 apastra and one depth-14 periastron, first reached at 28 arcs.
3. **The LT3 tilt was stated one way.** Same-vertex splitting and grain refinement can move the other way (B3).
4. **Three statements leaned on the conjecture or on David's calls.**
   - One cell said LT2 is "the only test that can return a failure".
   - §4.1 said Wallace's branch-number argument is "the kind of break David says a genuine derivation should show".
   - X15's first form settled critic question 3.

   All three are now neutral.

The skeptics also added seven items:
- X9 (the substitution note's "§8.4 is LT2's check");
- M5c (R3's closing sentence);
- the escaped pipes in M7, without which that table row would gain two cells;
- M18 (the Scope line's exception for Parry 1964);
- M26 ("dead ends drop out" is vacuous on the instance);
- M27 (R2's bold line says "grain" where it varies a cut);
- X25 (the arrival row's "tree" where completed histories are meant).

---

## 6. Unchecked

- **The pinned workspace scripts.** None was run, and none is in the repository: `merw_rule.py`, `merw_toy.py`, `kr.py`, `c33r.py`. Their SHA-256 pins are unverified. Every figure in §1 comes from independent code.
- **The 87,357 / 14,477 classifier variant.** It was not reproduced, so the cause of R3's one-state difference is unknown.
- **The sampled C33 and C34 figures** (seeded runs) were not re-run. The exact jump law agrees with them.
- **The Jordan structure beyond the geometric multiplicity.**
  - The Weyr characteristic for $k\ge2$ is certified over GF($p$) only; it matches the combinatorial count.
  - Index 15 rests on the exact $L^{14}$ walk growth, GF($p$) ranks and Rothblum's theorem (from secondary statements). It is not certified over $\mathbb Q$.
- **Two general claims, computed on the instance only:**
  - that every (a)-admissible Kretschmann edge lands outside its source orbit's range;
  - that the target's radial width falls along every jump.

  A general version of the first is close to #230's F11, which is David's call.
- **The trivial-scheme reading in B1 and §2.1** is an argument, not a computation. It assumes decoherent, orthogonal branches.
- **The grain toy in B3** ($1/3$ each against $1/2,1/4,1/4$) is a computation. That re-describing one decision as two counts as "refining the grain" is an interpretation.
- **All literature full texts.** No full text could be reached. Everything marked [search] rests on web-search extracts. In particular:
  - Wallace 2012:
    - axiom names, wording and grouping (including Mandolesi's Restriction, Composition and Indolence);
    - section numbers beyond 5.3–5.5, 5.8.1 and 5.8.2;
    - the appendices, and §3.11's pages;
    - whether App. D's "Utility Equivalence Lemma" is the preprint's equivalence lemma.
  - Barnum et al.'s own statement of the hidden assumption.
  - The irrational-ratio step in Deutsch 1999.
  - Dizadji-Bahmani's full argument.
  - Maudlin 2014's content.
  - Schlosshauer and Fine's full list of assumptions.
  - Vaidman 2012's pages, and Vaidman 2020's section-level criteria.
  - Saunders 2021 §8 verbatim, and whether any external critique of it exists.
  - Mandolesi's version of Wallace.
  - Parry 1964's theorem text, and the Lind–Marcus section.
  - Rothblum 1975 and Schneider 1986 (confirmed through secondary statements and numerics, not the papers).
  - Vere-Jones's R-recurrence statements, and Gurevich's original papers.
  - Galley and Masanes 2018 beyond its title and abstract.
  - The authorship of arXiv:0707.2832.
- **Bibliographic data from search metadata only,** content beyond abstracts not read:
  - Wallace 2003 (volume 34, pages 415–439; an alternative title also appears in search);
  - Baker 2007; Greaves 2004; Read 2018; Aaronson 2004;
  - Goldstein and Struyve 2007; Gleason 1957; Caves and Schack 2005;
  - Hartle 1968; Farhi, Goldstone and Gutmann 1989;
  - Worrall 1985; Mayo 1991.
- **Records the strings rely on without re-reading the source:**
  - Wallace 2010 §9's quotations ("violates the combination …", "There is no such thing as 'branch count'", "all contradict the Born rule …") come from #257, which read the preprint in full;
  - Burda et al.'s equations come from #251.
- **David's original wording and the relays** (Chief of Staff; the Physics Lead's chats at about 11:20, 11:39 and 11:48 ET) are not in the repository and were not checked.
- **The PR bodies** of #248–#257 were not read. The squash messages were seen in `git log`.

---

## 7. Provenance

- **Reviewer:** Claude Opus 5.5, an Anthropic model, acting as an independent external critic in a Claude Code session. The serving model was confirmed from session metadata.
- **Date:** 2026-10-11.
- **Repository:** `nous-clawds4/physics`, `main` at `05b74bc`.
- **Process:** one author pass, then two multi-agent workflows, each agent also Claude Opus 5.5.
  - **Workflow 1** ran nine agents in parallel:
    - two independent rebuilds of C33's graph;
    - one toy and linear-algebra agent;
    - three literature agents, using web search only;
    - three blind critics, one per note.
  - **Workflow 2** ran seven agents:
    - six adversarial skeptics, two per note (correctness and evidence; rules and neutrality);
    - a completeness critic.

  I rebuilt the graph a third time myself, merged the results, and checked the strings mechanically.
- **Tools:** Python 3.13 with numpy 2.5, scipy 1.18, sympy 1.14, mpmath 1.3 and networkx 3.7, in a scratch virtual environment outside the repository; exact rational and big-integer arithmetic; exact ranks over GF($p$); HiGHS linear programs. The scratch scripts are not part of this PR.
- **Repository changes:** this file only. No existing file was edited.
