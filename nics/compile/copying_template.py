import os
import shutil

from ..constants import ASSETS_DIR_PTH


def copying_template(dock):

    shutil.copytree(
        os.path.join(ASSETS_DIR_PTH, 'template', '_layouts'),
        os.path.join(dock, '_layouts')
    )

    shutil.copytree(
        os.path.join(ASSETS_DIR_PTH, 'template', '_sass'),
        os.path.join(dock, '_sass')
    )

    shutil.copytree(
        os.path.join(ASSETS_DIR_PTH, 'template', 'scripts'),
        os.path.join(dock, 'scripts')
    )