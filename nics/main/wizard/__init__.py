import os
import shutil
import sys

from mykit.kit.utils import printer, print_screen

from ..constants import TEMPLATE_DIR_PTH
from .workflows_writer import workflows_writer
from .settings_writer import settings_writer


def inspect(container_dir_pth, workflow_file_pth):
    
    ## the container ('docs/' folder) should not exist
    if os.path.isdir(container_dir_pth):
        printer(f"ERROR: Folder {repr(container_dir_pth)} already exists.")
        sys.exit(1)

    ## the GitHub Action workflow file 'rebuild-docs.yml' should not exist
    if os.path.isfile(workflow_file_pth):
        printer(f"ERROR: File {repr(workflow_file_pth)} already exists.")
        sys.exit(1)


def run():

    CWD = os.getcwd()

    WORKFLOW_FILE_PTH = os.path.join(CWD, '.github', 'workflows', 'rebuild-docs.yml')
    CONTAINER_DIR_PTH = os.path.join(CWD, 'docs')
    SETTINGS_FILE_PTH = os.path.join(CWD, 'docs', 'settings.txt')

    inspect(CONTAINER_DIR_PTH, WORKFLOW_FILE_PTH)

    print_screen(
        'Welcome to NICS!\n'
        '================\n\n'
    )

    author = input('Enter your name: ')
    email = input('Enter your email: ')
    gh_username = input('Enter your GitHub username: ')
    gh_repo = input('Enter this GitHub repository name: ')
    main_branch_name = input("Your main branch name (e.g. 'master'): ")

    ## if the dirs don't exist
    if not os.path.isdir( os.path.join(CWD, '.github') ):
        os.mkdir( os.path.join(CWD, '.github') )
        printer(f"INFO: Dir {repr( os.path.join(CWD, '.github') )} is created.")
    if not os.path.isdir( os.path.join(CWD, '.github', 'workflows') ):
        os.mkdir( os.path.join(CWD, '.github', 'workflows') )
        printer(f"INFO: Dir {repr( os.path.join(CWD, '.github', 'workflows') )} is created.")

    workflows_writer(WORKFLOW_FILE_PTH, author, email, gh_repo, main_branch_name)
    
    printer(f"INFO: Copying 'docs/' folder.")
    shutil.copytree( os.path.join(TEMPLATE_DIR_PTH, 'docs'), CONTAINER_DIR_PTH )
    printer(f'INFO: Done, {repr(CONTAINER_DIR_PTH)} is created.')

    settings_writer(SETTINGS_FILE_PTH, author, gh_username, gh_repo)

    print_screen(
        'Everything is done, now follow these last steps:\n'
        '1. foo\n'
        '2. \n'
    )