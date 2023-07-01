from mykit.kit.utils import printer

from ..constants import __version__, SOFTWARE_DIST_NAME, SOFTWARE_REPO


def _writer(author, email, gh_repo, main_branch_name):
    return f"""

# This file was generated by {SOFTWARE_DIST_NAME}-v{__version__} .
# Please make sure to be careful when modifying the values below. For more information, visit: {SOFTWARE_REPO}

name: Rebuild docs

on:
  push:
    branches:
      - {main_branch_name}

    paths:
      - 'docs/**'  # only rebuild if 'docs/' folder is modified

      # if using `use-repo-readme` keyword in 'tree/index.md'
      - README.md
      - readme.md

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:

      - name: Checkout {main_branch_name} branch
        uses: actions/checkout@v3
        with:
          ref: {main_branch_name}

      - name: Creating NICS working directory
        run: |
          cd ..
          mkdir __nics_work_dir__
          cd __nics_work_dir__
          cp -r ../{gh_repo}/docs/ .

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: Installing NICS
        run: |
          python -m pip install --upgrade pip
          pip install nics=={__version__}

      - name: Checkout docs branch
        uses: actions/checkout@v3
        with:
          ref: docs

      - name: Compile
        run: |
          cd ..
          cd __nics_work_dir__
          nics _compile "$(pwd)/docs" "$(pwd)/../{gh_repo}"

      - name: Deploy
        run: |
          git config user.name "{author} (via NICS)"
          git config user.email "{email}"
          git add .
          git commit -m "NICS rebuilds the docs"
          git push
"""


def workflow_writer(pth, author, email, gh_repo, main_branch_name):
    printer(f'INFO: Writing GitHub workflow file.')

    text = _writer(author, email, gh_repo, main_branch_name)
    with open(pth, 'w') as f:
        f.write(text)

    printer(f'INFO: Done, {repr(pth)} is created.')