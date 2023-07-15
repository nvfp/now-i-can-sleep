import os

from mykit.kit.utils import printer

from nics.main.constants import __version__


def get_text(cfg):
	return f"""
title: {cfg._gh_repo}
author: {cfg.author}

baseurl: /{cfg._gh_repo}
url: https://{cfg._gh_username}.github.io

show_credit: {cfg.show_credit}
nics_version: {__version__}


include: [_sass, pages]

sass:
    style: compact # possible values: nested expanded compact compressed
    sass_dir: _sass

# Redirection purposes
plugins:
    - jekyll-redirect-from
whitelist:
    - jekyll-redirect-from

# Syntax highlighting
markdown: kramdown
highlighter: rouge
kramdown:
    input: GFM
    syntax_highlighter: rouge
"""


def custom_config_yml(dock, cfg):
	printer('DEBUG: Rewriting _config.yml file.')

	text = get_text(cfg)
	with open(os.path.join(dock, '_config.yml'), 'w') as f:
		f.write(text)