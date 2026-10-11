# Pressure test: Claude's critique of the Zeno-mass note and the Born-readiness v0.9 refresh (#258)

**Read at:** `main` `56ad9b7`. **Target record:** `reviews/zeno-and-born-readiness-claude-opus.md` (#258). **Reference:** `versions/v0.9-prose.md` (unchanged since `e493913`), the T1–T3 table of v0.9 §11, `notes/zeno-mass-scoping.md` and `reviews/born-rule-readiness.md` (refresh section) at `56ad9b7`; neither target changed between #258's read (`f920ca3`) and `56ad9b7` except the refresh's "See also" line (#254), which no string touches.
**Verdicts:** CONFIRM (applied as written), QUALIFY (applied with the amendment stated), REJECT, FOR DAVID (neutral options; nothing applied). Nothing here picks a Zeno reading or decides T1–T3, (M1)/(M2), #139 or any F-item, and nothing edits v0.9.

## 1. Recomputed independently (`/workspace/g258`, scripts in Pins)

| Quantity | #258 | Here |
|---|---|---|
| V2 (built from Z1b's description), $w(X)$ under (Z-0)/(Z-i), (Z-ii), (Z-iii), (Z-vi), (Z-vii) | undefined, $1/2$, $2/3$, undefined, $1/2$ | the same; $z=1/4$ |
| (Z-vi) on C35 / V0 / V1 | undefined / $1/2$ / undefined | the same |
| (Z-vii) on C35 / V0 / V1 | $1$ / $1/2$ / undefined | the same |
| (Z-viii) (Zeno mass $0$ under the reading's own weights) | met by (Z-iii), (Z-vi) where defined; (Z-vii) only if pruning removes every Zeno history | the same: Zeno mass under (Z-vii) is $0$ on C35, V0, V2 and $0.2097$ on V3; under (Z-ii) it is $z$ |
| V3 ($2^k$ chain arms + 1 escape arm per chain vertex) | $z=0.2097$; (Z-vii) $1/2$; (Z-iii) $0.6327$ | $z=0.209711$; $1/2$; $0.6327$ |
| Counts: V0 / V1 $\tau$-cuts | $1/(k+2)$ / $1/2$ | the same |
| Depth-cut counts on C35, $X$ single / binary / ternary | $\to0$ / $1/2$ / $\to1$ | $1/(1+2^{n-1})$; $1/2$ at every $n$; $0.999549$ at $n=20$ |
| Retimed $1-2^{-k}\mapsto k$, $X$ single, $T\to1^-$ | $1/2$ | $1/2$ (no $Y$ vertex before $\tau=1$) |
| T3 example, one decision, $m=2$, (Z-iii) | jumps $1/2$ / $4/5$ | $z=1/3$: $1/2$; $z=1/6$: $4/5$ |
| C5-type law, no arrival rule | more than $n$ jumps: $(2/3)^{n+1}$ | the same |
| C5 Zeno set non-empty | asserted | "toward 10" all-jump chain: 3000 jumps, all bound periastra, $r\in[9.892616,10.107436]$ ($c=0.01$) |
| C7 minimum | $111.59018528548905654$ at $5+\sqrt7$ | the same (40 digits); $r^2-10r+18=0$ at the argmin |
| Darwin $T_2(p)$ | formula, $>0$ for $p>6$ | matches $(T-T_0)/e^2$ at $p=7,8,12,30$ (e.g. $122.2463$ at $e=0.01$ vs $122.2318$, $p=8$); cubic $\ge2.51$ on $(6,200]$ |
| Eccentric half periods | $112.47109$, $127.72176$, $212.56700$ | the same |
| $[10,20]$ | $E^2=108/115$, $L^2=400/23$ | exact, the same |
| Rule targets (six rows) | as tabled | all six the same, kinds and (a) verdicts included |
| C33 census, $c=0.01$ | 29,119 orbits; 14,478 stuck = 5/1,726/12,747 at depths 12/13/14; max apastron $25.3669$; 0 of 58,238 turning points with two edges | the same; `kr.classify` gives 14,477 (12,746 at depth 14); the one disagreement is target $17.14796096$ from $16.900001$ (plunge vs bound) |
| $E[\text{decisions}]$, law sum, $3^{-10}$, $E[J/D]$ at $c=0.1$ | $27.6835$, $3^{12}$, $1.6935\times10^{-5}$, $\ln2$ | the same |

**T≥1 cut (Z3).** Per-vertex, dead ends kept: $X$ $1/2$ on C35 and V2. §9's alternative conditions *per vertex* on survival (v0.9 §9 *Dead ends*), which is arm pruning: $X$ gets $1$ on C35 (equal there to (Z-iii)) but $1/2$ on V2, where (Z-iii) gives $2/3$. #258's "(Z-iii)'s value on C35" is true but names the wrong convention in general.

**Mapping claims (Z4).** *T1 via C5:* v0.9 §8.2 says "one history can take infinitely many branch points at a single value of accumulated $\tau$ (C5)"; item 8's first sentence makes such a history Zeno; the T1 row's "Drop (A)" side cites C5. The mass-$0$ law and non-emptiness recompute (table). *T3 via (Z-iii):* §9 derives Binomial$(n,m/(1+m))$ "since each decision jumps with weight $m/(1+m)$ independently of the past"; (Z-iii) changes that weight where $z>0$ (example recomputed); the T3 row's "Show jumps negligible: (J1)/(J2)" side rests on it. Both mappings hold; neither decides T1 or T3. Side note: C5's displayed outward-only chain stays in the bound sector for 25 jumps and then reaches an unbound periastron, still a turning point, so without an arrival rule it goes on; C5 is unaffected.

Not recomputed: C34's and C33's sampled figures, C31 step 13, C16's derivative, C2, C23 (checked present in v0.9 only), the scan.

## 2. Verdicts

| Item | Verdict | Reason / amendment |
|---|---|---|
| Z1 (Z-vi), (Z-vii), V2, Z1c | CONFIRM | V2 and V3 recompute; both conventions statable; "kept or conditioned away" is v0.9 §8.3's wording |
| Z2 "(Z-0) status quo" | CONFIRM | v0.9 §8.3 leaves the range open; C35 lists three values |
| Z3 structure, (Z-viii), $T\ge1$ | QUALIFY | Z3b applied as written. Z3a amended: §9's survivors-only alternative gives (Z-vii)'s value ($1$ on C35, $1/2$ on V2), not (Z-iii)'s in general |
| Z4 (c) mapping | QUALIFY | Mapping confirmed (§1). Amended form: the three new readings get (c)-table rows (F-cells ours, parallel to (Z-i), (Z-iii), (Z-v)), and the "none" T-cells point to the T1/T3 paragraph, so table and text agree |
| Z5 "under (A)" | CONFIRM | C7 reads "under (A)"; C5 gives a null, non-empty Zeno set without an arrival rule |
| Z6 $X$'s subtree | CONFIRM | depth counts recompute for single, binary, ternary $X$ |
| Note S1–S4, N1, N2 | CONFIRM | S2: "cut criterion" is C13 in this repo; S3 values recompute; N1: $z_X$ formula checked on C35/V1/V2 |
| #258 §3 answers 1–5 | CONFIRM | used to update the note's critic questions; the Doob $h$-transform remark is not applied (unsourced) |
| B1 l.46 | CONFIRM | `git diff b327a7b f920ca3` shows the l.46 edit; the pre-refresh body is otherwise unchanged, and this PR changes nothing above the refresh |
| B2 C15, C16, C36 | CONFIRM | v0.6 C15 "cofinal constancy sufficient", C16 "numerical evidence, not a proof", v0.7-outline C36 "only in the long-path limit" all differ from v0.9 |
| B3 C18/C23 | CONFIRM | C23's vertex at $z=0.671$ |
| B4 scope of C33/C16/C5 | CONFIRM | §2: '"(a) has a model" does not mean "(a) has an ongoing branching model"'; §8.2/C4: (a) "selects no countable star" |
| B5 "only" | CONFIRM | a scan shows sufficiency on its instance |
| B6 l.56, l.66, l.67 | CONFIRM | §11's quoted sentence verified; item 12 kept ($E[J/D]=\ln2$ vs pooled $1/2$ recomputed) |
| B7 cost symmetry | QUALIFY | applied, extended with (Z-vi)–(Z-viii) and the note's S1 mirror costs |
| S1 gating | QUALIFY | applied; the domain-keeping readings listed as (Z-ii), (Z-iii), (Z-vi), (Z-vii) |
| S2 C38, couplings, typicality | CONFIRM | quotes verified in §6.1, §8.2, §8.4, §11 |
| S3 hard-gate clause (1) | CONFIRM | §8.5 "trivial maps or a continuum of successors" |
| S4 F11 to gap 3, F7 | CONFIRM | moves a pointer and carries both of F11's clauses; decides nothing |
| S5 Open/Waits-on | QUALIFY | S5a and the F6 half of S5b applied. Removing (Z-0)–(Z-v) not applied: the refresh's brief named the Zeno options as a waits-on item. The rule sentence now says they are a note's options, not calls, and the list runs to (Z-viii). See FD2 |
| S6 DW, Zurek | CONFIRM | C12 count $3/4$, $1/4$; §10 text verbatim. The old map's DW (a) row is not reworded (pre-refresh body) |
| N1–N5 | CONFIRM | N4 amended to "(Z-0)–(Z-viii)" |
| #258 §5 answers 1–5 | CONFIRM | used to update the refresh's critic questions |
| §6: #247 F2 aside | CONFIRM | "Bertrand" occurs twice in v0.9 |
| §6/§7: item 8 and single-$\tau$ accumulation | FOR DAVID | FD1 |

## 3. FOR DAVID (FD1 and FD2 now Lead ruling (2026-10-11, delegated); see each "Resolution" line)

- **FD1. Does §8.2 item 8 cover infinitely many branch points at one $\tau$ (C5)?** (i) Leave item 8 as written: its literal reading covers C5's chains, and the T1 link now in the note stands. (ii) Add a sentence saying strict alternation alone covers the single-$\tau$ case: this removes the T1 link and is itself a convention touching T1. Either is a v0.9 edit; none is made.
  - **Resolution.** **Lead ruling (2026-10-11, under David's delegation of 12:34 PM ET; relayed, not signed)**: option (i). §8.2 item 8 is left as written; there is no v0.9.1 edit, and the T1 link stands.
- **FD2. Zeno options in gap 4's "Waits on".** (i) Keep them listed, marked as a note's options. This is the current text after commit 2 (S5b amended, the rule sentence, the list extended to (Z-viii)), applied pending David's call because the refresh's brief named them as a waits-on item. (ii) Drop them, per #258 S5b.
  - **Resolution.** **Lead ruling (2026-10-11, under David's delegation of 12:34 PM ET; relayed, not signed)**: option (i). The Zeno options stay listed in readiness gap 4, as currently written.

## 4. Applied in commit 2

Note: Z1a–Z1d, Z2, Z3a (amended), Z3b, Z4 (amended: table rows and T-cells plus the T1/T3 paragraph), Z5, Z6a–c, S1a, S1b, S2, S3, S4, N1, N2; a "Revised" line; critic questions 1–5 rewritten for the answered points; two pins added. Readiness refresh: B1a, B1b, B2, B3, B4a–d, B5, B6 (items 11–12), B7 (amended), S1 (amended), S2a–c, S3, S4a, S4b, S5a, S5b (amended) with the rule sentence, S6, N1–N3, N4 (amended), N5; a "Revised" line; critic questions 1, 2, 4, 5 rewritten (3 unchanged); one pin line. **Above the refresh: no change** (checked by diff of ll.1–130). All 63 OLDs occurred once (`apply.py`).

**Numbers** (`numcheck.py`): no value-number removed from either file. New in the note: $0.2097$, $0.6327$, $1/4$, $2/3$, $4/5$ and further $1/2$s (all `zeno2.py`). New in the refresh: $0.6672$, $0.5015$, $0.4999$ (v0.9 C33/C34 pins, already in the old map), $3/4$, $1/4$ (C12; `zeno2.py`), $2/3$, $1/2$ (§9, C33), $0.1$, $0.01$ ($c$ values), $31$, $60$ (scan record), $11$ (a pointer). Integers below 10 are not tracked.

**Words:** note 1,118 → 2,238; refresh section 1,182 → 2,222 (file 3,892 → 4,932).

## Pins

On the shared machine, outside the repository (SHA-256): `zeno2.py` `ce3d90881cc64acb705af77d3c6db61dc6035d309925ff4463378ddad60a2096`; `schw.py` `d7f803f3b4cfe4f37ed594c0c38b23449a4d947e14591abe4d12a381b2e33430`; `census.py` `7111bc0362039664a7586dc510d90e6df910878dc47937038356e6d3c2d2ac67`; `robust.py` `6072e85a485ecd52541964d65632a37b56327757cc4b64722bb1776e8bb016d5` (g168/`c33r.py`'s classifier); `c5chain.py` `f6e912ebf6c3fb691530e4c94ce59110d70f282051cb980f82db4b630c877929`; `strings.py` `0e796099a30c972caaff8f68e985f520c795d43a2a4bf0d60bce7c6d9e215ee6`; `apply.py` `9899dc32b12b0825501e446a0f6334de7a364577b0466515284e3f60789a8ee3`; `numcheck.py` `e33201d050e81eac6d2785f927726095142c01cee271988f218e1975f26f590b` with `numsrc.txt` `2fb571ff4cd8159d2e5689a04925c24a517a7193a86daa91a63bd32a2dc33529`. Imports `g154/kr.py` `0432cc20f56afbc3ad862b16de8f825bf9e1d4a490cde07ad8e5740f9d872dee`.
