import os

from mykit.kit.utils import printer

from nics.main.constants import __version__


def get_text(author, color_hue, lowercase_the_url, show_credit, email, gh_username, gh_repo, main_branch_name):
    return f"""
#-- Welcome to NICS settings!
#-- Everything starts with "#--" is a comment.
#-- Documentation: https://nvfp.github.io/now-i-can-sleep


author: '{author}'
color_hue: {color_hue}
lowercase_the_url: {lowercase_the_url}
show_credit: {show_credit}


#-- The variables below are for NICS internal use only and shouldn't be modified.

_email: '{email}'
_gh_username: '{gh_username}'
_gh_repo: '{gh_repo}'
_main_branch_name: '{main_branch_name}'

_nics_version: '{__version__}'
"""


def settings_writer(cwd, author, color_hue, lowercase_the_url, show_credit, email, gh_username, gh_repo, main_branch_name):
    printer('INFO: Writing /docs/settings.txt file.')

    file_path = os.path.join(cwd, 'docs', 'settings.txt')
    text = get_text(author, color_hue, lowercase_the_url, show_credit, email, gh_username, gh_repo, main_branch_name)
    with open(file_path, 'w') as f:
        f.write(text)

    printer(f'INFO: Done, {repr(file_path)} file is created.')