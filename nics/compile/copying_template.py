import os
import shutil

from ..constants import TEMPLATE_DIR_PTH


def copying_template(dock):

    x = os.path.join(TEMPLATE_DIR_PTH, '_layouts')
    print(123, x)
    print(345, os.path.isdir(x))
    print('ASSETS_DIR_PTH: ', TEMPLATE_DIR_PTH)
    print('os.path.isdir(ASSETS_DIR_PTH): ', os.path.isdir(TEMPLATE_DIR_PTH))
    print('os.listdir(ASSETS_DIR_PTH): ', os.listdir(TEMPLATE_DIR_PTH))

    shutil.copytree(
        os.path.join(TEMPLATE_DIR_PTH, '_layouts'),
        os.path.join(dock, '_layouts')
    )

    shutil.copytree(
        os.path.join(TEMPLATE_DIR_PTH, '_sass'),
        os.path.join(dock, '_sass')
    )

    shutil.copytree(
        os.path.join(TEMPLATE_DIR_PTH, 'scripts'),
        os.path.join(dock, 'scripts')
    )