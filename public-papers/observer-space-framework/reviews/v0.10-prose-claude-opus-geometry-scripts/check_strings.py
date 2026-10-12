#!/usr/bin/env python3
"""Check the final OLD/NEW strings of reviews/v0.10-prose-claude-opus-geometry.md.
Final set: this review's strings (R1, R2, R3 incl. optional, S1-S4, N5, G1, G2)
plus Claude's #316 strings for N1, N2, N3, N4, N6 (confirmed as written).
Each OLD must occur exactly once in its file; all NEWs are then applied in
order and every later OLD must still occur exactly once.
Run from the repo root of public-papers/observer-space-framework."""
import re, sys
def blocks(text):
    out = []
    for m in re.finditer(r'^OLD(?: \(`([^`]+)`\))?:\n~~~\n(.*?)\n~~~\nNEW:\n~~~\n(.*?)\n~~~', text, re.S | re.M):
        out.append((m.group(1) or 'versions/v0.10-prose.md', m.group(2), m.group(3), m.start()))
    return out
mine = open('reviews/v0.10-prose-claude-opus-geometry.md').read()
claude = open('reviews/v0.10-prose-claude-opus.md').read()
sel = []
for tag in ['N1', 'N2', 'N3', 'N4', 'N6']:
    a = claude.index('**%s.' % tag)
    nxt = re.search(r'^\*\*(N\d|R\d|S\d)\.|^---', claude[a+5:], re.M)
    seg = claude[a:a+5+nxt.start()]
    for b in blocks(seg):
        sel.append((tag,) + b[:3])
for b in blocks(mine):
    sel.append(('G',) + b[:3])
files = {}
ok = True
for tag, f, old, new in sel:
    files.setdefault(f, open(f).read())
for tag, f, old, new in sel:
    n = files[f].count(old)
    print('%-3s %-30s count=%d  %s' % (tag, f.split('/')[-1], n, old[:60].replace('\n', ' ')))
    ok &= (n == 1)
cur = dict(files)
for tag, f, old, new in sel:
    n = cur[f].count(old)
    ok &= (n == 1)
    cur[f] = cur[f].replace(old, new, 1)
print('strings:', len(sel), 'all once, sequential apply ok:', ok)
sys.exit(0 if ok else 1)
