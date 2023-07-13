import os
import shutil

from mykit.kit.utils import printer

from ..constants import TMPL_WEB_DIR_PTH


def copying_template(dock):

    SRC_LAYOUTS = os.path.join(TMPL_WEB_DIR_PTH, '_layouts')
    SRC_SASS    = os.path.join(TMPL_WEB_DIR_PTH, '_sass')
    SRC_SCRIPTS = os.path.join(TMPL_WEB_DIR_PTH, 'scripts')

    DST_LAYOUTS = os.path.join(dock, '_layouts')
    DST_SASS    = os.path.join(dock, '_sass')
    DST_SCRIPTS = os.path.join(dock, 'scripts')

    ## Debuggers
    printer(f'DEBUG: os.listdir(SRC_LAYOUTS): {os.listdir(SRC_LAYOUTS)}')
    printer(f'DEBUG: os.listdir(SRC_SASS): {os.listdir(SRC_SASS)}')
    printer(f'DEBUG: os.listdir(SRC_SCRIPTS): {os.listdir(SRC_SCRIPTS)}')

    ## Handle the case when the template already exists
    if os.path.isdir(DST_LAYOUTS): shutil.rmtree(DST_LAYOUTS)
    if os.path.isdir(DST_SASS): shutil.rmtree(DST_SASS)
    if os.path.isdir(DST_SCRIPTS): shutil.rmtree(DST_SCRIPTS)

    ## Copying
    shutil.copytree(SRC_LAYOUTS, DST_LAYOUTS)
    shutil.copytree(SRC_SASS, DST_SASS)
    shutil.copytree(SRC_SCRIPTS, DST_SCRIPTS)
    printer(f'INFO: Template copied.')