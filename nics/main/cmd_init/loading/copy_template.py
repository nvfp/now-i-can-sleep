import logging
import os
import shutil

from nics.main.constants import TEMPLATE_DOCS_DIR_PTH


logger = logging.getLogger(__name__)


def copy_template(load_path, container):
    logger.debug('Copying doc template.')

    src = TEMPLATE_DOCS_DIR_PTH
    dst = os.path.join(load_path, container)
    shutil.copytree(src, dst)

    logger.debug(f'Done, copied from {repr(src)} to {repr(dst)}.')