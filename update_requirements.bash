#!/bin/bash

# 1. Parse the requirements.txt file and find the pinned dependencies that were requested
awk '/via -r/{if (a && a !~ /via -r/) print a; print} {a=$0}' requirements.txt | awk -F '==' '{if (NR % 2) print $1}' > requirements_updated.in

# NOTE: the line below is an older command that does the same as the line above ...
# awk '/via -r/{if (a && a !~ /via -r/) print a; print} {a=$0}' requirements.txt | awk 'NR % 2' | awk -F '==' '{print $1}' > requirements_updated.in


# 2. NOTE: add a step where additional packages can be added ... these will need to be appended to the requirements_updated.in
# and they can be pinned or not pinned ...

# 3. recompile with the pinned dependencies
pip-compile requirements_updated.in -o requirements_updated.txt

# 4. report

if [ $? -eq 0 ]; then
    export REQ_UPDATE=1
else
    export REQ_UPDATE=0
fi