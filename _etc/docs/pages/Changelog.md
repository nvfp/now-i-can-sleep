# Changelog

- 3.0.0 (Oct 15, 2023):
    - the simple and fresh version of NICS


this 3.0.0 was aborted
~~- 3.0.0 (Jul 15-18):~~
    - Refactored the `_compile` command by excluding it from the PyPI distribution to reduce package size. It's because the `_compile` method is only used during the GitHub workflow and not by the users.
    - New features:
        - If users don't provide them, NICS will automatically create/use default for: favicon, 404 page, and `index.md` for docs-tree folders.
        - Added an "Edit this page" button so people can make changes on GitHub.
        - New options: `custom_license`, `char_map`
        - Users can now use custom `container` name and `Dock` branch name.
        - Added `reinit` command that lets users easily reconfigure NICS environment after NICS major update.
        - Support `.ico` format for favicon.
    - Breaking changes:
        - New URL mapping scheme
        - New plans for how `cmd_init`, `cmd_upgrade`, and `cmd_reinit` will work in the future.

- 2.8.4 (UNSTABLE): Fixed `copying_template.py` debuggers.
- 2.8.3: Added debuggers to `copying_template.py`: Investigating an issue where `sass-code-highlighting.scss` didn't get copied.
- 2.8.2: Bug fixed: The trailing slash in the homepage URL couldn't be trimmed due to an error thrown by GitHub Pages during the build process. In other words, `foo.github.io/REPO/` couldn't be redirected to `foo.github.io/REPO`.
- 2.8.1: Reuploaded `2.8.0`: Fixed the invalid dependency syntax in `pyproject.toml`.
- 2.8.0 (Jul 12):
    - New features:
        - Trim trailing slash: Redirect `foo.github.io/lib/page/` to `foo.github.io/lib/page`.
    - Design updates:
        - Changed the main font
        - New syntax highlighting
        - The font size is set to 16px for both desktop and mobile
- 2.7.2 (July 8):
    - Improved debuggers
    - Added `encoding='utf-8'` for writings
- 2.7.1 (July 8):
    - Reupload the `2.7.0` (nvfp/fast-pypi-release bug; Upgraded it to 1.1.0)
- 2.7.0 (July 7):
    - Update `nics/main/_template/docs/` template
    - Update dependencies: `mykit==4.1.0` -> `mykit==6.0.0`
    - Update workflow file template (`nics/main/wizard/workflow_writer.py`)
- 2.5.0 (July 1):
    - New feature:
        - Use `use-repo-readme` keyword in `tree/index.md` to use repository `README.md` as documentation homepage
- 2.3.0 (July 1):
    - The `_compile` command will now erase everything before compiling
- 2.2.0 - 2.2.3 (July 1):
    - SCSS updates
- 2.1.2 (June 30, 2023):
    - Bug fixed: modified the regex into non-greedy ([#2](https://github.com/nvfp/now-i-can-sleep/pull/2/commits/e8af69495f8c6fb9871a2a8a4f5ee26c5b578638))
- 2.1.1 (June 30, 2023):
    - Bug fixed: `TypeError: update_header() missing 1 required positional argument: 'lowercase_the_url'` in `compile/__init__.py`
- 2.1.0 (June 30, 2023):
    - `nics init` command can now be used even when workflow file and docs/ folder already exist
- 2.0.0 (June 30, 2023):
    - Added `upgrade` command
    - Changed docs-tree naming format:
        - From `(<order> -- )?<name> -- <url>(.md)?` to `(<order> - )?<name>(.md)?`
        - The URL will be the lowercase and URL-safe version of the 'name'
    - Added `lowercase_the_url` option to settings