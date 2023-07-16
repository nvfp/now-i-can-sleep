import os
import shutil
import sys

from mykit.kit.utils import printer, print_screen

from ..constants import TMPL_DOCS_DIR_PTH
from .workflow_writer import workflow_writer
from .settings_writer import settings_writer


def run():

    CWD = os.getcwd()

    WORKFLOW_FILE_PTH = os.path.join(CWD, '.github', 'workflows', 'rebuild-docs.yml')
    CONTAINER_DIR_PTH = os.path.join(CWD, 'docs')
    SETTINGS_FILE_PTH = os.path.join(CWD, 'docs', 'settings.txt')

    ## already_use is True if the user has used NICS before and only wants to reinitialize; otherwise, False.
    already_use = False
    if os.path.isfile(WORKFLOW_FILE_PTH) and os.path.isdir(CONTAINER_DIR_PTH):
        already_use = True

    if not already_use:
        if os.path.isfile(WORKFLOW_FILE_PTH) or os.path.isdir(CONTAINER_DIR_PTH):
            printer(f'ERROR: Workflow file or docs/ folder already exist.')
            sys.exit(1)

    ## intro
    print_screen(
        'Welcome to NICS!\n'
        '================\n\n'
    )

    if already_use:
        print(
            'Workflow file and docs/ folder are found, will rewrite these following files:\n'
            f'- Workflow file {repr(WORKFLOW_FILE_PTH)}\n'
            f'- Settings file {repr(SETTINGS_FILE_PTH)}'
        )
        usr = input('Continue?  (Y/n): ')
        if usr not in ['', 'y', 'Y']:
            printer(f'INFO: Exited.')
            sys.exit(0)

    ## saving user's information
    author = input('Enter your name: ')
    email = input('Enter your email: ')
    gh_username = input('Enter your GitHub username: ')
    gh_repo = input('Enter this GitHub repository name: ')
    main_branch_name = input("Enter the main branch name (e.g., master): ")

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

    workflow_writer(WORKFLOW_FILE_PTH, author, email, gh_repo, main_branch_name)

    if not already_use:
        printer(f"INFO: Copying 'docs/' folder.")
        shutil.copytree(TMPL_DOCS_DIR_PTH, CONTAINER_DIR_PTH)
        printer(f'INFO: Done, {repr(CONTAINER_DIR_PTH)} is created.')

    settings_writer(SETTINGS_FILE_PTH, author, email, gh_username, gh_repo, main_branch_name)

    ## outro
    print_screen(f"""
Almost done, now you need to do these final steps:
1. Create docs branch
   - git commit -am "NICS init"
   - git checkout --orphan docs
   - git rm -rf .
   - git commit --allow-empty -m init
   - git push origin docs
2. Activate the GitHub Pages
   - Visit https://github.com/{gh_username}/{gh_repo}/settings/pages
   - Under 'Build and deployment' section,
     - For 'Source', select 'Deploy from a branch'
     - For 'Branch', select 'docs' branch
     - Click the 'Save' button
3. Back to {main_branch_name} branch
   - git checkout {main_branch_name}
   - git push

That's it! The documentation will be at https://{gh_username}.github.io/{gh_repo} .
Visit https://nvfp.github.io/now-i-can-sleep/usage/init-command to visually see the final steps above."""
    )