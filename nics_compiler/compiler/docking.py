import os
import shutil

from mykit.kit.utils import printer

from nics.main.constants import TEMPLATE_WEB_DIR_PTH


def clean_up_the_dock(dock):
    """Erase everything in `dock`"""

    for stuff in os.listdir(dock):

        # Except .git folder
        if stuff == '.git': continue

        pth = os.path.join(dock, stuff)

        if os.path.isdir(pth):
            printer(f'INFO: Deleting dir {repr(pth)} recursively.')
            shutil.rmtree(pth)
        else:
            printer(f'INFO: Deleting file {repr(pth)}.')
            os.remove(pth)


def copy_the_template(dock):
    """Copy everything from 'nics/main/_template/web/' folder to `dock`"""

    for stuff in os.listdir(TEMPLATE_WEB_DIR_PTH):

        src = os.path.join(TEMPLATE_WEB_DIR_PTH, stuff)  # Source
        dst = os.path.join(dock, stuff)              # Destination

        if os.path.isfile(src):
            printer(f'INFO: Copying file {repr(src)} to {repr(dst)}.')
            shutil.copy(src, dst)
        else:  # Directory
            printer(f'INFO: Copying dir {repr(src)} to {repr(dst)}.')
            shutil.copytree(src, dst)


def docking(dock):
    clean_up_the_dock(dock)
    copy_the_template(dock)