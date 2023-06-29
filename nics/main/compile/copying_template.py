import os
import shutil

from mykit.kit.utils import printer

from ..constants import TEMPLATE_DIR_PTH


def copying_template(dock):

    LAYOUTS = os.path.join(dock, '_layouts')
    SASS = os.path.join(dock, '_sass')
    SCRIPTS = os.path.join(dock, 'scripts')

    ## handle the case when the template already exists
    if os.path.isdir(LAYOUTS): shutil.rmtree(LAYOUTS)
    if os.path.isdir(SASS): shutil.rmtree(SASS)
    if os.path.isdir(SCRIPTS): shutil.rmtree(SCRIPTS)

    shutil.copytree(
        os.path.join(TEMPLATE_DIR_PTH, 'web', '_layouts'),
        LAYOUTS
    )
    shutil.copytree(
        os.path.join(TEMPLATE_DIR_PTH, 'web', '_sass'),
        SASS
    )
    shutil.copytree(
        os.path.join(TEMPLATE_DIR_PTH, 'web', 'scripts'),
        SCRIPTS
    )
    printer(f'INFO: Template copied.')