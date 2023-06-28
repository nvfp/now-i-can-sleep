import os
import shutil

from ..constants import ASSETS_DIR_PTH


def copying_template(dock):

    x = os.path.join(ASSETS_DIR_PTH, 'template', '_layouts')
    print(x)
    print(os.path.isdir(x))
    print(ASSETS_DIR_PTH)
    print(os.listdir(ASSETS_DIR_PTH))

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