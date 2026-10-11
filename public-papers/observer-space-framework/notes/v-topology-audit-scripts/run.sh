#!/bin/sh
# Reproduces expected/hits.md (deterministic; standard library only; Python 3.13.5). Reads v0.9.1 and Paper 1 at the checked-out commit.
cd "$(dirname "$0")/../../../.." && python public-papers/observer-space-framework/notes/v-topology-audit-scripts/classify.py
