# Audit: is any closeness on $V$ implicit in v0.9.1?

*Standalone note answering David's questions as relayed by the Physics Lead (not signed). Written at main `7fdd4f0`; v0.9.1 and Paper 1 (`papers/observer-space-ontology.md`) are unedited. Bare § and C pointers are to v0.9.1. The topology options of #301 ((T0)–(T3)) are David's call; nothing here picks or leans.*

**Verdict.** The claim holds with one correction. v0.9.1 puts no topology or distance on $V$, so "continuous", "discontinuous", "near" and "distance between states" are undefined on $V$, and proper time lives only on segments. Along a single curvelet, however, continuity (indeed analyticity) is defined through `papers/geodesic-lifts.md` Thm 3.
Of the 290 hits, 283 are fine and 7 are ill-posed on $V$: six uses of "discontinuous" and one of "near". Each has a minimal rewording that needs no topology.

## 1. The claim against the record

| Candidate | What it is | Closeness on $V$? |
|---|---|---|
| Segment / curvelet $\gamma_{O^u}$ (§5) | "the unique curve in $V$ traced by the geodesic", analytic in the sense of Thm 3: each $J^k$ projection, in Fermi coordinates along the geodesic, is analytic in $\tau$ | **Along one curvelet only.** It fixes continuity in $\tau$ on that curve, and §8.1's "$C^\infty$ path" and §11's "continuous curve" use this sense. It does not compare states on different curvelets. |
| "Germ" (§4) | a jet at $p$, equivalently the patch $P(O)$; defined through neighbourhoods of $p$ in spacetime | **Spacetime structure.** Two germs are equal or not; nothing says how close. Analytic continuation uses the sheaf of germs over one world, whose étale topology lives over that spacetime, not on $V$. |
| (a) test (§8.2) | membership in $F(O)$, built from curvelets of $O$ | **None.** It is a yes/no relation. |
| Jump rule (§7) | analytic continuation along a spacelike path of length $\varepsilon$ | **Spacetime structure.** $\varepsilon$ and $\ell$ are spacetime lengths along the jump path, not distances between states in $V$. |
| "Kretschmann matching" | the rule continues along a path and does not match $K$ (#297). $K$ is a function on $V$ | **None.** Using $K$ to define closeness would be new structure. |
| Accumulated $\tau$, "segment" (§8.2 items 2, 8) | a label summed along a history | **None on $V$.** It orders a history's states and compares no two states. |
| §9 "limit", "converge" | depth-$n$ counts on trees | **None.** These are combinatorial and measure-theoretic. |
| (J2), §11's T3 "near" (§9, §11; not #301's (T3)) | explicitly ask for "a named topology *on curvelets*" and leave "near" open | **Absent by the record's own statement.** |

The Fermi-slice topology (`papers/obs-as-a-space.md` Thm 16) exists in `papers/` but is not adopted or cited by v0.9.1 (#299, #301).

**Corrected claim.** v0.9.1 defines no topology or distance on $V$. "Continuous" and "discontinuous" are therefore undefined *between* states, but continuity in $\tau$ along a single segment is defined (Thm 3). Thm 3 gets it from the inverse-limit (Fréchet) topology on jets, taken in Fermi coordinates along that one geodesic. The same jet-space topology underlies (T1)'s inverse-limit variant (`papers/fermi-distance.md`), but v0.9.1 uses it only along one curve and never passes it to $V$, so this neither adopts nor favours (T1). Proper time is defined only along segments, and jumps carry none (§8.2 item 2). The distances the record does use ($\varepsilon$, $\ell$, axis distance) are spacetime lengths. "Smooth segments" is right, and the record's own sense is stronger: segments are analytic. Histories carry one further structure: (M1)'s measure (ruled by David at L3, 2026-10-10, relayed, not signed) is defined on cylinder sets of finite prefixes (§9). Sharing a long prefix is a closeness of histories only in that measure-theoretic sense; v0.9.1 uses no topology on histories, and none on $V$ follows from it.

## 2. The grep

The search ran over v0.9.1-prose.md and Paper 1 for: discontinu, continu, nearby, near, close, distance, limit, converge, neighbo, open set, topolog, metric, smooth and jump. Hits are matched at word starts, which drops 13 substring-only hits (symmetric, geometric, isometric). Every hit was read in context.

| Verdict | v0.9.1 | Paper 1 | Total |
|---|---|---|---|
| fine: spacetime (metric, smooth, global topology, analytic continuation, $\ell$, near-horizon) | 55 | 30 | 85 |
| fine: one curvelet (segments; §11's "continuous curve"; Paper 1's $O(\tau)$) | 4 | 2 | 6 |
| fine: ordinary English or combinatorial ("jump" as a type-(ii) edge, the continue arm, "continuum" as cardinality, neighbours, tree limits, Continuous World Switching (CWS, §8.1)) | 164 | 16 | 180 |
| fine: flagged open in the text ("near" in quotes, nearness/T3, (J2)'s named topology) | 12 | 0 | 12 |
| **ill-posed on $V$** | 7 | 0 | 7 |

Paper 1 has no ill-posed hit. §11 line 483's "without making any jump near" is counted as flagged open, because v0.9.1's next sentence marks it: "Whether that meets the no-teleport intuition depends on what "near" means, which is a question for *Mathematical Foundations* and an open call." The per-hit table (290 rows) is `notes/v-topology-audit-scripts/expected/hits.md`.

**Ill-posed hits, with minimal rewordings** (each one replaces "discontinuous" or "near" with what §5 defines: a type-(ii) jump leaves the curvelet):

| § (line) | Phrase | Rewording |
|---|---|---|
| §1 (55) | "histories are now discontinuous, and their jumps carry no proper time" | "histories now include type-(ii) jumps, which leave the curvelet and carry no proper time" |
| §5 (184) | "At a type-(ii) jump a history is **discontinuous in oriented observer space**." | "At a type-(ii) jump a history **leaves its curvelet in oriented observer space**." |
| §8.2 (278) | "Joins are discontinuous type-(ii) jumps plus incidence in a graph." | "Joins are type-(ii) jumps plus incidence in a graph." |
| §11 (474) | "Short jumps: near at the vertex, not (J2)." | "Short jumps: near at the vertex only in some topology on germs there (none is named; the counterpart of (J2)'s named topology), not (J2)." |
| §11 (474) | "whether a short discontinuous move counts as teleporting is open" | "whether a short jump counts as teleporting is open" |
| §11 (483) | "each jump is still discontinuous in oriented observer space" | "each jump still leaves its curvelet" |
| C10 (550) | "Type (ii) is discontinuous in oriented observer space, not necessarily in $\mathrm{Obs}$ (§5)" | "Type (ii) leaves the oriented curvelet, and need not change the lump in $\mathrm{Obs}$ (§5)" |

None of these rewordings changes a claim, a number or an option. They are offered for v0.10 and are not applied here.

## Pins

`notes/v-topology-audit-scripts/`. Run with `sh run.sh` (Python 3.13.5, standard library only; it calls `python` from the repository root). The run is deterministic, with no seed. `classify.py` `aca8745614a4`, `run.sh` `f3d20e7aab11`, `expected/hits.md` `76eac3330442`. The verdicts are rules plus line-specific cases, written after reading every hit; the script reproduces the table, not the reading.

## Critic questions

1. Under any Hausdorff topology on $V$ in which curvelets are continuous, a jump at fixed accumulated $\tau$ is discontinuous. Should v0.10 keep "discontinuous" with that conditional, or use "leaves its curvelet" throughout?
2. Is §8.1's "the path in $V$ is $C^\infty$" adequately read in the one-curvelet sense, or does it presuppose more?
