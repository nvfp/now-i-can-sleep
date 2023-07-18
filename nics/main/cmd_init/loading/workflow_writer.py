import logging
import os

from nics.main.constants import __version__


logger = logging.getLogger(__name__)


def get_text(load, dock, container, git_name, git_email, gh_repo_name):
    return f"""
# This file was generated by NICS ({__version__}).
# Documentation: https://github.com/nvfp/now-i-can-sleep

name: Rebuild documentation

on:
  push:
    branches:
      - {load}

    paths:
      - '{container}/**'  # Only rebuild if '{container}/' folder is modified

      # When using 'use-repo-readme' keyword in 'tree/index.md'
      - README.md
      - readme.md

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  NICS-rebuild:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Run
        uses: nvfp/now-i-can-sleep@{__version__}
        with:
          load: {load}
          dock: {dock}
          container: {container}
          git-name: {git_name}
          git-email: {git_email}
          gh-repo-name: {gh_repo_name}
          nics-version: {__version__}
"""


def workflow_writer(load, dock, container, git_name, git_email, gh_repo_name):
    logger.debug('Writing rebuild-docs.yml file.')

    file_path = os.path.join(load, '.github', 'workflows', 'rebuild-docs.yml')

    ## Handle missing intermediate directories
    workflows_dir = os.path.dirname(file_path)
    logger.debug(f'Creating dir {repr(workflows_dir)}.')
    os.makedirs(workflows_dir)

    text = get_text(load, dock, container, git_name, git_email, gh_repo_name)
    with open(file_path, 'w') as f:
        f.write(text)

    logger.debug(f'Done, {repr(file_path)} file is created.')