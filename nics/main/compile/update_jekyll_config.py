from mykit.kit.utils import printer


def _writer(author, gh_username, gh_repo):
	return f"""

# website

baseurl: /{gh_repo}
url: https://{gh_username}.github.io/{gh_repo}


# personal

title: {gh_repo}
author:
  name: {author}


# internal

include: [_pages, _sass, scripts]

permalink: pretty

sass:
  style: compact # possible values: nested expanded compact compressed
  sass_dir: _sass
"""


def update_jekyll_config(D_JEKYLL_CONFIG, author, gh_username, gh_repo):

	text = _writer(author, gh_username, gh_repo)
	with open(D_JEKYLL_CONFIG, 'w') as f: f.write(text)
	printer(f"INFO: Updated Jekyll '_config.yml' file {repr(D_JEKYLL_CONFIG)}.")