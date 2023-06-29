import os
import shutil
import sys

from mykit.kit.utils import printer, print_screen

from ..constants import TEMPLATE_DIR_PTH
from .inspect import inspect
from .workflows_writer import workflows_writer
from .settings_writer import settings_writer


def run():

    CWD = os.getcwd()

    WORKFLOW_FILE_PTH = os.path.join(CWD, '.github', 'workflows', 'rebuild-docs.yml')
    CONTAINER_DIR_PTH = os.path.join(CWD, 'docs')
    SETTINGS_FILE_PTH = os.path.join(CWD, 'docs', 'settings.txt')

    ## inspection
    inspect(CONTAINER_DIR_PTH, WORKFLOW_FILE_PTH)

    ## intro
    print_screen(
        'Welcome to NICS!\n'
        '================\n\n'
    )
    usr = input('Continue?  (Y/n): ')
    if usr not in ['', 'y', 'Y']:
        printer('INFO: Exited.')
        sys.exit(0)

    ## saving user's information
    author = input('Enter your name: ')
    email = input('Enter your email: ')
    gh_username = input('Enter your GitHub username: ')
    gh_repo = input('Enter this GitHub repository name: ')
    main_branch_name = input("Your main branch name (e.g., master): ")

    ## handle the case where the '.github/workflows/' directory does not exist yet
    def handle_workflow_dirs():
        pth = os.path.join(CWD, '.github')
        if not os.path.isdir(pth):
            os.mkdir(pth)
            printer(f"INFO: Folder {repr(pth)} is created.")
        pth = os.path.join(CWD, '.github', 'workflows')
        if not os.path.isdir(pth):
            os.mkdir(pth)
            printer(f"INFO: Folder {repr(pth)} is created.")
    handle_workflow_dirs()

    workflows_writer(WORKFLOW_FILE_PTH, author, email, gh_repo, main_branch_name)
    
    printer(f"INFO: Copying 'docs/' folder.")
    shutil.copytree( os.path.join(TEMPLATE_DIR_PTH, 'docs'), CONTAINER_DIR_PTH )
    printer(f'INFO: Done, {repr(CONTAINER_DIR_PTH)} is created.')

    settings_writer(SETTINGS_FILE_PTH, author, gh_username, gh_repo)

    ## outro
    print_screen(
        'Everything is done, now follow these last steps:\n'
        '1. foo\n'
        '2. \n'
    )