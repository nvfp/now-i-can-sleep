import os
import shutil

from mykit.kit.utils import printer

from ..constants import TMPL_WEB_DIR_PTH


def copying_template(dock):

    LAYOUTS = os.path.join(dock, '_layouts')
    SASS = os.path.join(dock, '_sass')
    SCRIPTS = os.path.join(dock, 'scripts')

    ## Debuggers
    printer(f'DEBUG: os.listdir(LAYOUTS): {os.listdir(LAYOUTS)}')
    printer(f'DEBUG: os.listdir(SASS): {os.listdir(SASS)}')
    printer(f'DEBUG: os.listdir(SCRIPTS): {os.listdir(SCRIPTS)}')

    ## handle the case when the template already exists
    if os.path.isdir(LAYOUTS): shutil.rmtree(LAYOUTS)
    if os.path.isdir(SASS): shutil.rmtree(SASS)
    if os.path.isdir(SCRIPTS): shutil.rmtree(SCRIPTS)

    shutil.copytree(
        os.path.join(TMPL_WEB_DIR_PTH, '_layouts'),
        LAYOUTS
    )
    shutil.copytree(
        os.path.join(TMPL_WEB_DIR_PTH, '_sass'),
        SASS
    )
    shutil.copytree(
        os.path.join(TMPL_WEB_DIR_PTH, 'scripts'),
        SCRIPTS
    )
    printer(f'INFO: Template copied.')