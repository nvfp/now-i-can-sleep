import os
import shutil
import sys

from mykit.kit.utils import printer

from ..constants import TEMPLATE_DIR_PTH
from .workflows_writer import workflows_writer
from .settings_writer import settings_writer


def inspect(docs, workflows):
    
    ## docs/
    if os.path.isdir(docs):
        printer(f"ERROR: 'docs/' folder already exists.")
        sys.exit(1)
    
    ## workflows
    if os.path.isfile(workflows):
        printer(f"ERROR: 'rebuild-docs.yml' file already exists.")
        sys.exit(1)


def run():

    CWD = os.getcwd()

    WORKFLOWS = os.path.join(CWD, '.github', 'workflows', 'rebuild-docs.yml')
    DOCS = os.path.join(CWD, 'docs')
    SETTINGS = os.path.join(CWD, 'docs', 'settings.txt')
    
    inspect(DOCS, WORKFLOWS)

    author = input('Enter your name: ')
    email = input('Enter your email: ')
    gh_username = input('Enter your GitHub username: ')
    gh_repo = input('Enter this GitHub repository name: ')

    workflows_writer(WORKFLOWS, author, email)
    
    printer(f"INFO: Copying 'docs/' folder.")
    shutil.copytree( os.path.join(TEMPLATE_DIR_PTH, 'docs'), DOCS )
    printer(f'INFO: Done, {repr(DOCS)} is created.')

    settings_writer(SETTINGS, author, gh_username, gh_repo)