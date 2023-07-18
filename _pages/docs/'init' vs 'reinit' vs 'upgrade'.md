---
permalink: /docs/init-vs-reinit-vs-upgrade/
layout: main
title: 'init' vs 'reinit' vs 'upgrade'
---

## commitment

- The format of these things should never be changed again in the future:
    - `/tree/*`
    - `/favicon.png` or `/favicon.svg` or `/favicon.ico`
    - `/404.md`
- Whatever option has already been added to `settings.txt` should ***never*** be removed in future updates.


### `init` command

Fresh initialization of the NICS environment, where NICS has never been used before. This process is **unrelated** to any update scenario.


### `reinit` command

First, remember that only `settings.txt` and `rebuild-docs.yml` will be changed during NICS updates.

The `reinit` command is used during major NICS updates (which requires user involvement), where new option(s) are added to `settings.txt` and require users to input corresponding values for those new options.

Apart from that, the `reinit` command seamlessly handles other necessary tasks such as rewriting `settings.txt` and/or `rebuild-docs.yml`, which don’t require user involvement.


### `upgrade` command

Unlike the `reinit` command that requires user involvement, this command works seamlessly.

this command work in situations there NICS minor/patches updates that only:
- changes for the backend (which totally has nothing to do with users local NICS env)
- or changes for users local NICS env BUT without adding/removing any options from `settings.txt`

But, this command should mostly just update the NICS version number in `rebuild-docs.yml` and `settings.txt`.