import random

from mykit.kit.utils import printer

from ..constants import __version__


def full_writer(author, color_hue, lowercase_the_url, show_credit, email, gh_username, gh_repo, main_branch_name):
    return f"""
#-- Welcome to NICS settings!
#----------------------------

#-- Everything starts with "#--" is a comment.
#-- Read documentation at https://nvfp.github.io/now-i-can-sleep


author: '{author}'
color_hue: {color_hue}
lowercase_the_url: {lowercase_the_url}
show_credit: {show_credit}


#-- The below variables are for NICS internal use only and should not be changed.

_email: '{email}'
_gh_username: '{gh_username}'
_gh_repo: '{gh_repo}'
_main_branch_name: '{main_branch_name}'

_nics_version: '{__version__}'
"""


def _writer(author, email, gh_username, gh_repo, main_branch_name):
    return f"""
#-- Welcome to NICS settings!
#----------------------------

#-- Everything starts with "#--" is a comment.
#-- Read documentation at https://nvfp.github.io/now-i-can-sleep


author: '{author}'
color_hue: {random.randint(0, 359)}
lowercase_the_url: True
show_credit: True


#-- The below variables are for NICS internal use only and should not be changed.

_email: '{email}'
_gh_username: '{gh_username}'
_gh_repo: '{gh_repo}'
_main_branch_name: '{main_branch_name}'

_nics_version: '{__version__}'
"""


def settings_writer(pth, author, email, gh_username, gh_repo, main_branch_name):
    printer(f'INFO: Writing settings file.')

    text = _writer(author, email, gh_username, gh_repo, main_branch_name)
    with open(pth, 'w') as f:
        f.write(text)

    printer(f'INFO: Done, {repr(pth)} is created.')