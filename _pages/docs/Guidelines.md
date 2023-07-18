---
permalink: /docs/guidelines/
layout: main
title: Guidelines
---

# Guidelines

- The settings file `/docs/settings.txt` should exist.
- The homepage markdown file `/docs/tree/index.md` should exist.
- Custom 404 page `/docs/404.md` is optional; NICS will create one for you if it doesn't exist.
- Custom favicon `/docs/favicon.svg` is optional. It should be in either `.svg` or `.png` format and sized at 16x16 pixels. If it doesn't exist, the default favicon will be used.
- You can add some extra files/folders to the `/docs/` folder because NICS won't look at anything except for:
    - `/docs/tree/`
    - `/docs/404.md`
    - `/docs/favicon.svg` or `/docs/favicon.png`
    - `/docs/settings.txt`
- Ordering:

    You can use numbers to organize the docs-tree, like:
    - `/docs/tree/1 - Page1.md`  <- file
    - `/docs/tree/2 - Page2.md`  <- file
    - `/docs/tree/3 - Pages`  <- folder

    But it's optional. You can also go with:
    - `/docs/tree/page1.md`  <- file
    - `/docs/tree/page2.md`  <- file
    - `/docs/tree/pages`  <- folder
- Assets:

    Any files that are ***not*** markdown files (`.md`) are considered ***assets***. These files are typically used within markdown files. For example:

    Let's say we have these files:
    - `/docs/tree/page.md`
    - `/docs/tree/image.jpg`

    Here, `image.jpg` is an asset that you can use in `page.md` like this:

    ```markdown
    # page.md

    An image (remember to use a relative path):

    ![Image](image.jpg)
    ```
- File and folder naming conventions for URL mapping:

    Allowed characters:
    - Letters and numbers: `a-z`, `A-Z`, `0-9`
    - Hyphens (`-`)

    Mapping characters (for URL):
    - Space (` `) is mapped to hyphen (`-`)
    - Underscore (`_`) is mapped to hyphen (`-`)
    - Backtick (`` ` ``) is mapped to an empty string
    - Tilde (`~`) is mapped to hyphen (`-`)
    - Exclamation mark (`!`) is mapped to an empty string
    - At symbol (`@`) is mapped to `"at"`
    - Tag (`#`) is mapped to an empty string
    - Dollar sign (`$`) is mapped to an empty string
    - Percent symbol (`%`) is mapped to `"percent"`
    - Caret (`^`) is mapped to an empty string
    - Ampersand (`&`) is mapped to `"and"`
    - Brackets (`()`, `[]`) and braces (`{}`) are all mapped to an empty string
    - Equal sign (`=`) is mapped to an empty string
    - Plus sign (`+`) is mapped to `"plus"`
    - Comma (`,`) is mapped to an empty string
    - Period (`.`) is mapped to hyphen (`-`)
    - Semicolon (`;`) is mapped to hyphen (`-`)
    - Apostrophe (`'`) is mapped to an empty string

    Examples ✔️:
    - `/docs/tree/a guide for app.js.md` will have the URL `USERNAME.github.io/REPO/a-guide-for-app-js`
    - `/docs/tree/Foo & Bar.md` will have the URL `USERNAME.github.io/REPO/Foo-and-Bar`
    - `/docs/tree/Build, Test, and Deploy.md` will have the URL `USERNAME.github.io/REPO/Build-Test-and-Deploy`

    If two or more hyphens occur, they will be replaced with a single hyphen:
    - `/docs/tree/Foo. bar.md` will have the URL `USERNAME.github.io/REPO/Foo-bar` instead of `USERNAME.github.io/REPO/Foo--bar`
    - `/docs/tree/Foo. ~bar.md` will have the URL `USERNAME.github.io/REPO/Foo-bar` instead of `USERNAME.github.io/REPO/Foo---bar`

    Any characters not listed above will result in an error if used.
- The `index.md` file for folders, like `/docs/tree/pages/index.md`, is optional. If it doesn't exist, NICS will generate one automatically.
- Prevent URL conflicts: If you have `/docs/tree/page.md`, don't create a `/docs/tree/page` folder. This would result in both having the same URL `USERNAME.github.io/REPO/page`.

> Note: these guidelines are for the latest version of NICS. Keep in mind that guidelines may vary for different versions. If you need to read the guidelines for a specific version, you can find them by searching for that version in the [releases](https://github.com/nvfp/now-i-can-sleep/releases) section on GitHub.