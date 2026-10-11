# Scripts for `../turning-type-lemma.md`

Run from any directory with Python 3.13.5, mpmath 1.3.0, sympy 1.14.0, scipy 1.18.1 and numpy 2.5.3. Each script finds its siblings through its own path. The expected outputs are in `expected/`; lines that report a run time in seconds will differ.

| script | origin (shared box) | invocation | expected output |
|---|---|---|---|
| `tt.py` | `g286/tt.py` (unchanged) | module | — |
| `proof286.py` | `g286/proof286.py` (unchanged) | `python proof286.py` | `proof286.txt` |
| `throat286.py` | `g286` (path line only) | `python throat286.py` | `throat286.txt` |
| `boundary286.py` | `g286` (path line only) | `python boundary286.py` | `boundary286.txt` |
| `sample286.py` | `g286` (path line only) | `python sample286.py 20000 20000` | `sample286_20000_20000.txt` |
| `census286.py` | `g286` (path line only) | `python census286.py 0.1` / `0.01` | `census286_0.1.txt` / `census286_0.01.txt` |
| `censusf286.py` | `g286` (path line only) | `python censusf286.py 0.1` / `0.01` / `0.001 22` | `censusf286_*.txt` (the capped `0.001 22` run needs about 8 GB of memory) |
| `census.py`, `r1.py` | `g201` (unchanged) | imported by `census286.py` | — |
| `c33r.py` | `g168/c33r.py` (path lines only) | `python c33r.py 0.01` | `c33r_0.01.txt` |
| `c33x.py` | `g168/c33x.py` (path line only) | run by `c33r.py` | — |
| `kr.py` | `g154/kr.py` (unchanged) | imported by `c33r.py` and `c33x.py` | — |
