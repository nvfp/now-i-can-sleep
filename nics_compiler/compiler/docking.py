import logging
import os
import shutil

from nics.main.constants import TEMPLATE_WEB_DIR_PTH


logger = logging.getLogger(__name__)


def clean_up_the_dock(dock_path):
    """Erase everything in `dock_path`"""

    for stuff in os.listdir(dock_path):

        # Except .git folder
        if stuff == '.git': continue

        pth = os.path.join(dock_path, stuff)

        if os.path.isdir(pth):
            logger.debug(f'Deleting dir {repr(pth)} recursively.')
            shutil.rmtree(pth)
        else:
            logger.debug(f'Deleting file {repr(pth)}.')
            os.remove(pth)


def copy_the_template(dock_path):
    """Copy everything from 'nics/main/_template/web/' folder to `dock_path`"""

    for stuff in os.listdir(TEMPLATE_WEB_DIR_PTH):

        src = os.path.join(TEMPLATE_WEB_DIR_PTH, stuff)  # Source
        dst = os.path.join(dock_path, stuff)             # Destination

        if os.path.isfile(src):
            logger.debug(f'Copying file {repr(src)} to {repr(dst)}.')
            shutil.copy(src, dst)
        else:  # Directory
            logger.debug(f'Copying dir {repr(src)} to {repr(dst)}.')
            shutil.copytree(src, dst)


def docking(dock_path):
    clean_up_the_dock(dock_path)
    copy_the_template(dock_path)