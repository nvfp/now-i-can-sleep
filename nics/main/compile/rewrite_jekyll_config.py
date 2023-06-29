



def rewrite_jekyll_config(pth, author, gh_username, gh_repo):

    text = f"""

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

    with open(pth, 'w') as f:
        f.write(text)