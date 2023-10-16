# *now-i-can-sleep*

GitHub repo documentation builder. Builds automatically each time you update the doc!

![banner](_etc/assets/banner.jpg)


## Usage

```yml
name: Rebuild docs (NICS)

on:
  push:
    branches:
      - main  # EDITME: your default branch name
    paths:
      - './docs/**'  # EDITME: The relative path (relative to the root) to the folder containing the documentation files.
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: nvfp/now-i-can-sleep@v3
        with:
          nics_docs_dir_relpth: ./docs  # EDITME: The relative path (relative to the root) to the folder containing the documentation files.
        env:
          GH_TOKEN: ${{ github.token }}
```


## Links

- [Thank you💙](https://nvfp.github.io/thank-you)
- [Documentation](https://nvfp.github.io/now-i-can-sleep)
- [Changelog](https://nvfp.github.io/now-i-can-sleep/changelog)


## License

This project is licensed under the MIT License.
