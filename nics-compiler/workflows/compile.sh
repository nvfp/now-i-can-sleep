#!/bin/bash

# Exit the script immediately if any command exits with a non-zero status
set -e


echo "::group::Compile"

python -m pip install --upgrade pip
pip install nics==$NICS_VERSION
nics -v

echo "::endgroup::"