import os
import random

from nics.main.cmd_init.loading.workflow_writer import workflow_writer
from nics.main.cmd_init.loading.copy_template import copy_template
from nics.main.utils.page404_maker import create_404_page_file
from nics.main.utils.favicon_maker import create_favicon_svg_file
from nics.main.cmd_init.loading.settings_writer import settings_writer


def loading(load_path, load, dock, container, author, git_name, git_email, gh_username, gh_repo_name):

    ## Write rebuild-docs.yml
    workflow_writer(load_path, load, dock, container, git_name, git_email, gh_repo_name)

    ## Copying template
    copy_template(load_path, container)

    ## Customize 404.md
    create_404_page_file(os.path.join(load_path, container, '404.md'), gh_username, gh_repo_name)

    ## Default user details
    custom_license = None
    color_hue = random.randint(0, 359)
    lowercase_the_url = True
    show_credit = True
    char_map = {}

    ## Customize favicon.svg
    create_favicon_svg_file(os.path.join(load_path, container, 'favicon.svg'), color_hue)

    ## Customize settings.txt
    settings_writer(
        load_path,
        author, custom_license, color_hue, lowercase_the_url, show_credit, char_map,
        git_name, git_email, gh_username, gh_repo_name, load, dock, container
    )