#!/bin/sh
# Reproduces expected/cit.txt (deterministic; no seed). Python 3.13.5 with mpmath 1.3.0.
cd "$(dirname "$0")"
python cit.py
