#!/bin/sh
# Reproduces expected/cvse.txt (deterministic; no seed). Python 3.13.5, standard library only.
cd "$(dirname "$0")"
for args in "a 0.1 1000 stop" "a 0.01 1000 stop" "a 0.01 1000 through" "noa 0.1 8 stop" "noa 0.1 8 through" "noa 0.01 8 through"; do
  python cvse.py $args
done
