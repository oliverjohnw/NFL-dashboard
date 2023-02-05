#!/bin/bash
# 1. Parse the requirements.txt file and find the pinned dependencies that were requested
awk '/via -r/{if (a !~ /via -r/) print a; print} {a=$0}' requirements.txt | awk "NR % 2" > requirements_updated.in

# N2. OTE: add a step where additional packages can be added ... these will need to be appended to the requirements_updated.in
# and they can be pinned or not pinned ...

# 3. recompile with the pinned dependencies
pip-compile requirements_updated.in -o requirements_updated.txt

# 4. report: $? gives the exit code of the last command; 0 means success ... if it didn't succeed print an error

if [ $? -neq 0]; then
    echo "The added packages cannot be added to the pinned versions of these packages ... :("
    export REQ_ADD=0
else
    export REQ_ADD=1
fi