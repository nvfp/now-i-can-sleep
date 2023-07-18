#!/bin/bash
set -e  # Exit the script immediately if any command exits with a non-zero status


echo "::group::Compile"


python -m pip install --upgrade pip
pip install -r $GITHUB_ACTION_PATH/requirements.txt

cd ..
python $GITHUB_ACTION_PATH/nics_compiler/compiler $(pwd)


echo "::endgroup::"