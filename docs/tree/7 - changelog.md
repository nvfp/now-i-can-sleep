# Changelog

- 2.2.0 (July 1):
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