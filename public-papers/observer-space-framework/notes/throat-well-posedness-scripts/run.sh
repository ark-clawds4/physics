#!/bin/sh
# Reproduces expected/twp.txt (deterministic; no seed). Python 3.13.5 with mpmath 1.3.0 and sympy 1.14.0.
cd "$(dirname "$0")"
python twp.py
