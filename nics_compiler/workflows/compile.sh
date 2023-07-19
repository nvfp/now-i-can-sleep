#!/bin/bash
set -e  # Exit the script immediately if any command exits with a non-zero status


echo "::group::Preparing"

python -m pip install --upgrade pip
pip install -r $GITHUB_ACTION_PATH/requirements.txt

echo "::endgroup::"


echo "::group::Compile"

echo "ls1---"
ls
echo "---"
cd ..
echo "ls2---"
ls
echo "---"
echo "ls3---"
ls __nics_work_dir__
echo "---"
python $GITHUB_ACTION_PATH/nics_compiler/compiler $(pwd)/$GH_REPO_NAME $(pwd)/__nics_work_dir__

echo "::endgroup::"
