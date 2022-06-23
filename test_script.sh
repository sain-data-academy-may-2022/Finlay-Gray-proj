#!/bin/bash

set -eu

python3 -m pytest

if [[ $? -eq 0 ]]
then
    echo "Tests passed"
    git add .
    got commit -m $1
    echo "tests failed"
fi