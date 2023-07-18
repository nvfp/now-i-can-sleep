import logging
import os
import sys

from nics.main.constants import __version__


logger = logging.getLogger(__name__)


def check_rebuild_docs_yml_existence(load_path):

    file_path = os.path.join(load_path, '.github', 'workflows', 'rebuild-docs.yml')

    if not os.path.isfile(file_path):
        logger.error(f'File {repr(file_path)} not found.')
        sys.exit(1)


def check_container_clues(load_path, container):

    ## The homepage file
    file_path = os.path.join(load_path, container, 'tree', 'index.md')
    if not os.path.isfile(file_path):
        logger.error(f'File {repr(file_path)} not found.')
        sys.exit(1)

    ## The settings.txt file
    file_path = os.path.join(load_path, container, 'settings.txt')
    if not os.path.isfile(file_path):
        logger.error(f'File {repr(file_path)} not found.')
        sys.exit(1)


def check_upgrade_status(ver):

    if ver == __version__:
        print('Fantastic! Everything is already up to date.')
        sys.exit(0)