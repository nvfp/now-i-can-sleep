from mykit.kit.utils import printer


def _writer(author, gh_username, gh_repo):
    return f"""
#-- Welcome to NICS settings!
#----------------------------

#-- Everything starts with "#--" is a comment.
#-- Read documentation at https://nvfp.github.io/now-i-can-sleep


author: '{author}'
color_hue: 28
show_credit: True


#-- The below variables are for NICS internal use only and should not be changed.

_gh_username: '{gh_username}'
_gh_repo: '{gh_repo}'
"""


def settings_writer(pth, author, gh_username, gh_repo):
    printer(f'INFO: Writing settings file.')

    text = _writer(author, gh_username, gh_repo)
    with open(pth, 'w') as f:
        f.write(text)

    printer(f'INFO: Done, {repr(pth)} is created.')