#! /bin/bash

# Get absolute path of script's directory,
# in case our working directory is different
benchdir=$(dirname "$0")

python $benchdir/bench2025.py $benchdir/../tests/data/2025/day0.test.in 10 10
