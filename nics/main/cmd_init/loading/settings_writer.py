import logging
import os

from nics.main.constants import __version__


logger = logging.getLogger(__name__)


def get_text(
    author, custom_license, color_hue, lowercase_the_url, show_credit, char_map,
    git_name, git_email, gh_username, gh_repo_name, load, dock, container
):
    return f"""
#-- Welcome to NICS settings!
#-- Everything starts with "#--" is a comment.
#-- Documentation: https://nvfp.github.io/now-i-can-sleep


author: '{author}'
custom_license: {custom_license}
color_hue: {color_hue}
lowercase_the_url: {lowercase_the_url}
show_credit: {show_credit}
char_map: {char_map}


#-- The variables below are for NICS internal use only and shouldn't be modified.
_git_name: '{git_name}'
_git_email: '{git_email}'
_gh_username: '{gh_username}'
_gh_repo_name: '{gh_repo_name}'
_load: '{load}'
_dock: '{dock}'
_container: '{container}'
_nics_version: '{__version__}'
"""


def settings_writer(
    load_path,
    author, custom_license, color_hue, lowercase_the_url, show_credit, char_map,
    git_name, git_email, gh_username, gh_repo_name, load, dock, container
):
    logger.debug('Writing settings.txt file.')

    file_path = os.path.join(load_path, container, 'settings.txt')
    text = get_text(
        author, custom_license, color_hue, lowercase_the_url, show_credit, char_map,
        git_name, git_email, gh_username, gh_repo_name, load, dock, container
    )
    with open(file_path, 'w') as f:
        f.write(text)

    logger.debug(f'Done, created at {repr(file_path)}.')