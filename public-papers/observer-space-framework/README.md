# Observer space and graph joins (public paper)

This folder holds the **public-facing** framework paper intended for the wider physics community.

It is deliberately **not** under `papers/`, which is crowded with in-house notes (lock leftovers, kill-passes, internal theorems). Those remain internal. This paper is the readable cut of the ontology and launching pad.

## Layout

| Path | Role |
|---|---|
| `versions/` | Numbered drafts (`v0.1-outline.md`, …, `v0.7-outline.md`, `v0.7-prose.md`, `v0.7.1-prose.md`, `v0.8-outline.md`, `v0.8-prose.md`, `v0.8.1-prose.md`, `v0.9-prose.md`) |
| `reviews/` | External and in-house reviews; each file **must** name the version it reviews |

Living working definitions stay in the repo-root file [`mathematical-framework.md`](../../mathematical-framework.md). Where that file disagrees with a numbered draft, the draft wins for review purposes.

## Status

- **Current draft:** [`versions/v0.9-prose.md`](versions/v0.9-prose.md) (v0.9 prose, from v0.8.1 on Claude's full review #229 and Geometry's pressure test #230; changelog and preservation table [`versions/v0.9-changelog.md`](versions/v0.9-changelog.md); panel: Geometry #233 PASS, Literature #232 PASS with notes; Claude re-review #235 HOLD (narrow), PASS with R1 applied; adopted with R1, S1–S6 and N1–N8 applied; open items for David in #230 §4)
- In review: [`versions/v0.9.1-prose.md`](versions/v0.9.1-prose.md) (v0.9.1 prose, status patch of v0.9 recording David's (M1) ruling at L3, relayed, not signed; brief in #266; pending panel; v0.9 stays current until adoption)
- Prior prose: [`versions/v0.8.1-prose.md`](versions/v0.8.1-prose.md) (v0.8.1 prose, patch of v0.8 prose with the Lead's rulings on Claude #201 and Geometry #203; batch check Literature #207 HOLD (narrow; its §11 fix applied); targeted Claude re-review PASS in #211 (`reviews/v0.8.1-prose-claude-opus-5.5.md`, cover #208, claim check #209 HOLD (narrow)); Geometry pressure test #212; #211's non-gating notes N1–N3 applied in the Lead's adoption edit)
- Patched by v0.8.1: [`versions/v0.8-prose.md`](versions/v0.8-prose.md) (v0.8 prose, presentation and hygiene, under the v0.8 outline; merged #183; panel: Geometry #184 PASS, Literature #186 PASS with notes, fix diff Geometry #188 PASS; external review: Claude #201 HOLD (narrow), cover `reviews/v0.8-prose-claude-cover.md`; Geometry pressure test #203; not adopted)
- Latest outline: [`versions/v0.8-outline.md`](versions/v0.8-outline.md) (presentation and hygiene outline; merged #177; panel: Geometry #179 PASS, Literature #180 PASS; expanded as v0.8 prose, patched as v0.8.1)
- Earlier prose: [`versions/v0.7.1-prose.md`](versions/v0.7.1-prose.md) (patch of v0.7 prose with the #168/#169 fixes; panel check of the diff PASS: Geometry #171 at `36f7986`, Literature #172 at `193e7a2`, later nits checked by Literature; targeted Claude re-review PASS in #175 (`reviews/v0.7.1-prose-claude-opus-5.5.md`); Geometry pressure test #176)
- Earlier prose: [`versions/v0.7-prose.md`](versions/v0.7-prose.md) (prose panel: Geometry #162 PASS with notes, Literature #161 PASS with notes; fixes #163; external review: Claude #168 HOLD (narrow); Geometry pressure test #169)
- Prior outline: [`versions/v0.7-outline.md`](versions/v0.7-outline.md) (merged #156; panel: Geometry #157, Literature #158)
- Prior outline: [`versions/v0.6-outline.md`](versions/v0.6-outline.md) (panel: Geometry #131, Literature #132, Ontology #133)
- Earlier prose: [`versions/v0.6-prose.md`](versions/v0.6-prose.md) (Claude #154 PASS; Geometry #155); [`versions/v0.5-prose.md`](versions/v0.5-prose.md)
- Reviews: see [`reviews/`](reviews/)
- Born rule and Einstein’s field equations are **goals**, not theorems of this version.
- Do not treat this folder as a claim that either has been derived.

## How to review

See [`reviews/README.md`](reviews/README.md).