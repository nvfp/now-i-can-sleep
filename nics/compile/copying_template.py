import os
import shutil

from ..constants import TEMPLATE_DIR_PTH


def copying_template(dock):

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