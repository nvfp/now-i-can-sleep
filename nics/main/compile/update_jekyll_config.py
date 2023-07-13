from mykit.kit.utils import printer


def _writer(author, gh_username, gh_repo):
	return f"""

# ~~ Website ~~

baseurl: /{gh_repo}
url: https://{gh_username}.github.io


# ~~ Personal ~~

title: {gh_repo}
author:
  name: {author}


# ~~ Internal ~~

include: [_pages, _sass, scripts]

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


def update_jekyll_config(D_JEKYLL_CONFIG, author, gh_username, gh_repo):

	text = _writer(author, gh_username, gh_repo)
	with open(D_JEKYLL_CONFIG, 'w') as f: f.write(text)
	printer(f"INFO: Updated Jekyll '_config.yml' file {repr(D_JEKYLL_CONFIG)}.")