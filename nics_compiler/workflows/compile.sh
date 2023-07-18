#!/bin/bash
set -e  # Exit the script immediately if any command exits with a non-zero status


echo "::group::Preparing"

python -m pip install --upgrade pip
pip install -r $GITHUB_ACTION_PATH/requirements.txt

echo "::endgroup::"


echo "::group::Compile"

cd ..
python $GITHUB_ACTION_PATH/nics_compiler/compiler $(pwd)/$GH_REPO_NAME $(pwd)/__nics_working_dir__

echo "::endgroup::"
