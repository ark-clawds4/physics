#!/usr/bin/env bash
# Usage: bash run.sh   (needs python3 with mpmath 1.3.0; about 10 s)
set -euo pipefail
cd "$(dirname "$0")"
python3 sphere_germ.py > out.txt
diff out.txt expected/sphere_germ.out && echo "OK: output matches expected/sphere_germ.out"
(cd ../.. && python3 reviews/v0.10-prose-claude-opus-geometry-scripts/check_strings.py) > out_strings.txt
diff out_strings.txt expected/check_strings.out && echo "OK: output matches expected/check_strings.out"
rm -f out.txt out_strings.txt
