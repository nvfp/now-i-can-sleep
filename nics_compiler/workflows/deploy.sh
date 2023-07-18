#!/bin/bash

# 'set -e' doesn't have to be set (to turn off the error when committing with no changes)
# set -e


echo "::group::Commit the changes on Dock branch"


git config user.name "$GIT_NAME"
git config user.email "$GIT_EMAIL"
git add .
git commit -m "NICS rebuilds the docs — $(date +'%Y %b %e, %l:%M %p')"
git push


echo "::endgroup::"