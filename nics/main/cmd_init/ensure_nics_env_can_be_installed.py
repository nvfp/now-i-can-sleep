import logging
import os
import sys


logger = logging.getLogger(__name__)


def ensure_nics_env_can_be_installed(cwd, container):

    ## /.github/workflows/rebuild-docs.yml
    pth = os.path.join(cwd, '.github', 'workflows', 'rebuild-docs.yml')
    if os.path.isfile(pth):
        logger.error(f'Cannot initialize NICS. This file already exists: {repr(pth)}.')
        sys.exit(1)

    ## /CONTAINER/
    pth = os.path.join(cwd, container)
    if os.path.isdir(pth):
        logger.error(f'Cannot initialize NICS. This folder already exists: {repr(pth)}.')
        sys.exit(1)