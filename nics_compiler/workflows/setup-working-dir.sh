#!/bin/bash
set -e


echo "::group::Set up NICS working directory"


echo "INFO: copying $GH_REPO_NAME/$CONTAINER/ to __nics_work_dir__/"

cd ..
mkdir __nics_work_dir__
cp -r $GH_REPO_NAME/$CONTAINER/ __nics_work_dir__/

echo "INFO: Done."


echo "::endgroup::"


echo "::group::Debugging"
echo "-- GITHUB_WORKSPACE --"
ls $GITHUB_WORKSPACE
echo "-- GITHUB_WORKSPACE/.. --"
ls $GITHUB_WORKSPACE/..
echo "-- GITHUB_WORKSPACE/../__nics_work_dir__ --"
ls $GITHUB_WORKSPACE/../__nics_work_dir__
echo "::endgroup::"