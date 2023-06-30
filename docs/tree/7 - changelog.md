# Changelog

- 2.1.0 (June 30, 2023):
    - `nics init` command can now be used even when workflow file and docs/ folder already exist
- 2.0.0 (June 30, 2023):
    - Added `upgrade` command
    - Changed docs-tree naming format:
        - From `(<order> -- )?<name> -- <url>(.md)?` to `(<order> - )?<name>(.md)?`
        - The URL will be the lowercase and URL-safe version of the 'name'
    - Added `lowercase_the_url` option to settings