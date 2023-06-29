from mykit.kit.utils import printer

from ..constants import __version__


def workflows_writer(pth, author, email):
    printer(f'INFO: Writing GitHub workflows.')

    text = f"""

name: Rebuild docs

on:
  push:
    branches:
      - main

    paths:
      - 'docs/**'  # only rebuild docs webpage if docs/ folder is modified

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:

      - name: 📂Checkout main branch
        uses: actions/checkout@v3
        with:
          ref: main

      - name: 🛠️ Creating NICS working directory
        run: |
          cd ..
          mkdir __nics_work_dir__
          cd __nics_work_dir__
          cp -r ../mykit/docs/ .

      - name: 🐍Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: 🐱Installing NICS
        run: |
          python -m pip install --upgrade pip
          pip install nics=={__version__}

      - name: 📂Checkout docs branch
        uses: actions/checkout@v3
        with:
          ref: docs

      - name: ⚙️ Compile
        run: |
          cd ..
          cd __nics_work_dir__
          nics _compile "$(pwd)/docs" "$(pwd)/../mykit"

      - name: 🚀Deploy
        run: |
          git config user.name "{author} (via NICS)"
          git config user.email "{email}"
          git add .
          git commit -m "NICS rebuild the docs"
          git push
"""

    with open(pth, 'w') as f:
        f.write(text)

    printer(f'INFO: Done, {repr(pth)} is created.')