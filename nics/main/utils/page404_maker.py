import os


def get_text(cfg):
    return f"""
## Sorry, it seems the page doesn't exists or no longer exists.

Do want to check it on the [homepage](https://{cfg._gh_username}.github.io/{cfg._gh_repo})?
"""


def create_404_page_file(pth, cfg):
    """
    `pth` is not limited to '404.md' or '/404/index.md'
    """

    ## Check
    if os.path.exists(pth):
        raise AssertionError(f'File/dir already exists: {repr(pth)}.')

    text = get_text(cfg)
    with open(pth, 'w') as f:
        f.write(text)