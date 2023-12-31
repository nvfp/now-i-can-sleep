# *now-i-can-sleep*

[![Run tests](https://github.com/nvfp/now-i-can-sleep/actions/workflows/run-tests.yml/badge.svg)](https://github.com/nvfp/now-i-can-sleep/actions/workflows/run-tests.yml)
[![Rebuild docs](https://github.com/nvfp/now-i-can-sleep/actions/workflows/rebuild-docs.yml/badge.svg)](https://github.com/nvfp/now-i-can-sleep/actions/workflows/rebuild-docs.yml)

GitHub repo documentation builder. Builds automatically each time you update the doc!

![banner](_etc/assets/banner.jpg)

[Documentation](https://nvfp.github.io/now-i-can-sleep)


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
      - uses: nvfp/now-i-can-sleep@v4
        with:

          ## EDIT THESE
          src: ./docs
          author: Foo Bar
          analytics: abcdefg

    runs-on: ubuntu-latest
    permissions: { pages: write, id-token: write }
    environment: { name: Documentation }
```

Read the parameters' description [here](https://github.com/nvfp/now-i-can-sleep/blob/main/action.yml).

You can put the folder-containing-the-documentation-files (`src`) anywhere. But, this example is in the `./docs` folder. The `docs` folder would look like this:

```txt
docs/
└── pages/
    └── page_1.md
    └── page_2.md
    └── Usage.md
    └── foo.md
    └── BAR.md
    └── baz.MD
    └── This is Title.md
    └── ...
└── favicon.ico
```

- There are two items that are needed: `pages/` and `favicon.ico`.
- Besides `pages/` and `favicon.ico`, you can put anything you like inside `docs/` (NICS will ignore them).
- Inside `pages/`, only markdown files are allowed.
- The page's title will be derived from the file name, and the URL will mirror the file name, converted to lowercase and with spaces replaced by hyphens. For example, `Foo is Bar.md`'would have a title of `Foo is Bar` and a URL of `foo-is-bar`.

The last step is to configure the GitHub Pages deployment settings for your GitHub repository. You can do this by visiting [https://github.com/OWNER/REPO/settings/pages](https://github.com/OWNER/REPO/settings/pages) and selecting 'GitHub Actions' under the 'Build and Deployment' setting.


## License

This project is licensed under the MIT License.


<!-- 

## Dev-docs:
- the test suite should require no dependencies to make development easier.

-->
