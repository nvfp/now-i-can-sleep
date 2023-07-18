import os

from nics.main.utils.ensure_a_git_repo import ensure_a_git_repo
from nics.main.cmd_init.ensure_nics_env_can_be_installed import ensure_nics_env_can_be_installed
from nics.main.cmd_init.get_user_details import get_user_details
from nics.main.cmd_init.loading import loading
from nics.main.cmd_init.print_outro import print_outro


def run():

    load_path = os.getcwd()

    ## Check I
    ensure_a_git_repo(load_path)

    ## Get user details
    usr = get_user_details()

    ## Check II
    ensure_nics_env_can_be_installed(load_path, usr.container)

    ## Loading to the Container
    loading(
        load_path,
        usr.load, usr.dock, usr.container,
        usr.author, usr.git_name, usr.git_email,
        usr.gh_username, usr.gh_repo_name
    )

    ## Outro
    print_outro(usr.load, usr.dock, usr.gh_username, usr.gh_repo_name)