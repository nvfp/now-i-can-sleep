# *now-i-can-sleep*

[![Run tests](https://github.com/nvfp/now-i-can-sleep/actions/workflows/run-tests.yml/badge.svg)](https://github.com/nvfp/now-i-can-sleep/actions/workflows/run-tests.yml)
[![Rebuild docs](https://github.com/nvfp/now-i-can-sleep/actions/workflows/rebuild-docs.yml/badge.svg)](https://github.com/nvfp/now-i-can-sleep/actions/workflows/rebuild-docs.yml)

GitHub repo documentation builder. Builds automatically each time you update the doc!

![banner](_etc/assets/banner.jpg)


## Usage

Copy this `./.github/workflows/rebuild-docs.yml` file and change the values to your own.

```yml
name: Rebuild docs

on:
  push:
    branches:
      - main  # EDITME
    paths:
      - 'docs/**'  # EDITME
  workflow_dispatch:

jobs:
  run:
    steps:
      - uses: nvfp/now-i-can-sleep@v3
        with:

          ## EDIT THESE
          nics_docs_dir_relpth: ./docs
          author: Foo Bar
          google_analytics_tracking_id: abcdefg

    runs-on: ubuntu-latest
    permissions: { pages: write, id-token: write }
    environment: { name: Documentation }
```

You can put the folder containing the documentation files anywhere, but this example is in the `./docs` folder. The `docs` folder would look like this:

```txt
docs/
└── pages/
    └── changelog.md
    └── page_1.md
    └── page_99.md
└── favicon.ico
```

The two items, `pages/` and `favicon.ico`, are needed. You can put anything else inside `docs/` (NICS will ignore them), but don't put anything besides markdown files inside `docs/pages/`.


## Links

- [Thank you💙](https://nvfp.github.io/thank-you)
- [Documentation](https://nvfp.github.io/now-i-can-sleep)
- [Changelog](https://nvfp.github.io/now-i-can-sleep/changelog)


## License

This project is licensed under the MIT License.
