#!/bin/bash
set -e


echo "::group::Set up NICS working directory"


echo "INFO: copying $GH_REPO_NAME/$CONTAINER/ to __nics_work_dir__/"

cd ..
mkdir __nics_work_dir__
cp -r $GH_REPO_NAME/$CONTAINER/ __nics_work_dir__/

echo "INFO: Done."


echo "::endgroup::"