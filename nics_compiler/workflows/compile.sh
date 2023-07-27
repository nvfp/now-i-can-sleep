#!/bin/bash
set -e  # Exit the script immediately if any command exits with a non-zero status


echo "::group::Debugging"

echo "pwd: '$(pwd)'"

echo "-- ls '$(pwd)'"
ls
echo "---"

echo "-- ls '$(pwd)/..'"
ls $(pwd)/..
echo "---"

echo "-- ls '$(pwd)/../__nics_work_dir__'"
ls $(pwd)/../__nics_work_dir__
echo "---"

echo "::endgroup::"


echo "::group::Preparing"

python -m pip install --upgrade pip
pip install -r $GITHUB_ACTION_PATH/requirements.txt

echo "::endgroup::"


echo "::group::Compile"

echo "DEBUG: pwd: '$(pwd)'"
python $GITHUB_ACTION_PATH/nics_compiler/compiler $(pwd) $(pwd)/../__nics_work_dir__

echo "::endgroup::"
