from mykit.kit.utils import printer


def settings_writer(pth, author, gh_username, gh_repo):
    printer(f'INFO: Writing settings file.')

    text = f"""
#-- Welcome to NICS settings!
#----------------------------

#-- Everything starts with "#--" is a comment.
#-- Help: https://nvfp.github.io/now-i-can-sleep


author: '{author}'
color_hue: 28
show_credit: True


#-- The variables below should not be changed and are for NICS internal use only.

_gh_username: '{gh_username}'
_gh_repo: '{gh_repo}'
"""

    with open(pth, 'w') as f:
        f.write(text)

    printer(f'INFO: Done, {repr(pth)} is created.')