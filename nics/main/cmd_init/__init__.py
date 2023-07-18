import os

from nics.main.utils.ensure_a_git_repo import ensure_a_git_repo
from nics.main.cmd_init.ensure_nics_env_can_be_installed import ensure_nics_env_can_be_installed
from nics.main.cmd_init.get_user_details import get_user_details
from nics.main.cmd_init.loading import loading
from nics.main.cmd_init.print_outro import print_outro


def run():

    CWD = os.getcwd()

    ## Check I
    ensure_a_git_repo(CWD)

    ## Get user details
    usr = get_user_details()

    ## Check II
    ensure_nics_env_can_be_installed(CWD, usr.container)

    ## Loading to the Container
    loading()

    ## Outro
    print_outro()