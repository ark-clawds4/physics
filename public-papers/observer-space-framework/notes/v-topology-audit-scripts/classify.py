# v-topology audit: grep v0.9.1-prose.md and Paper 1 for closeness words and classify every hit (rules + line overrides).
# Usage (from the repo root): python classify.py  -> prints the per-hit table and the counts. Deterministic.
import re, sys
from collections import Counter
FILES = (('v0.9.1', 'public-papers/observer-space-framework/versions/v0.9.1-prose.md'), ('Paper 1', 'papers/observer-space-ontology.md'))
PAT = re.compile(r'\b(discontinu\w*|continu\w*|nearby|near\w*|close\w*|distance\w*|limit\w*|converge\w*|neighbo\w*|open sets?|topolog\w*|metric\w*|smooth\w*|jump\w*)', re.I)
ST, CV, EN, OP, ILL = 'fine: spacetime', 'fine: curvelet', 'fine: ordinary/combinatorial', 'fine: flagged open', 'ILL-POSED on V'
def near_rule(doc, ln, ctx):
    c = ctx.lower()
    if 'near at the vertex' in c: return ILL
    if 'any jump near' in c: return ILL
    if any(k in c for k in ('near-horizon', 'near-flat', 'near-circular')): return ST
    return OP
def verdict(doc, ln, w, ctx, tight=''):
    w = w.lower(); c = ctx.lower()
    if w.startswith('discontinu'): return ILL
    if w.startswith(('nearness',)): return OP
    if w in ('nearby', 'nearest'): return EN
    if w.startswith('near'): return near_rule(doc, ln, tight)
    if w.startswith('metric') or w.startswith('smooth'): return ST
    if w.startswith('topolog'): return OP if 'named topology' in c else ST
    if w == 'continuum': return EN
    if w.startswith('continuation'):
        if doc == 'Paper 1' and ln in (67, 73): return CV
        if doc == 'v0.9.1' and ln == 186: return CV
        if doc == 'v0.9.1' and ln == 294: return EN
        if doc == 'v0.9.1' and ln == 411: return OP
        return ST
    if w.startswith('continuous'):
        if 'world switching' in c: return EN
        if doc == 'v0.9.1' and ln == 476: return CV
        return EN
    if w.startswith('continu'):
        if 'continued metric' in c or 'continues a jet' in c or 'continuing the jet' in c: return ST
        return EN
    if w.startswith('jump'):
        if 'extrinsic curvature' in c or 'jump path' in c or 'jump length' in c: return ST
        return EN
    if w.startswith('distance'):
        return EN if ('from the cut' in c or 'from a distance' in c) else ST
    if w.startswith('close'):
        return ST if 'timelike' in c else EN
    return EN      # neighbo*, limit*, converge* (trees, related work, idiom)
rows = []
for doc, f in FILES:
    sec = '(front matter)'
    for ln, l in enumerate(open(f), 1):
        if l.startswith('#'): sec = l.strip('#').strip()
        for m in PAT.finditer(l):
            a, b = max(0, m.start() - 45), min(len(l), m.end() + 45)
            ctx = l[a:b].replace('\n', ' ').replace('|', '/')
            rows.append((doc, ln, sec.split(' ')[0].rstrip('.'), m.group(1), ctx, verdict(doc, ln, m.group(1), l[max(0, m.start()-80):m.end()+80], l[max(0, m.start()-10):m.end()+16])))
print('| # | doc | line | § | word | context | verdict |'); print('|---|---|---|---|---|---|---|')
for i, r in enumerate(rows, 1): print(f'| {i} | {r[0]} | {r[1]} | {r[2]} | {r[3]} | …{r[4]}… | {r[5]} |')
cnt = Counter(r[5] for r in rows); print(); print('Total', len(rows), dict(sorted(cnt.items())))
for d in ('v0.9.1', 'Paper 1'): print(d, dict(sorted(Counter(r[5] for r in rows if r[0] == d).items())))
