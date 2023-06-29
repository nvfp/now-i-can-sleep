import os
import shutil

from ..constants import TEMPLATE_DIR_PTH


def copying_template(dock):


    ## handle the case when the template already exists
    if os.path.isdir( os.path.join(dock, '_layouts') ):
        shutil.rmtree( os.path.join(dock, '_layouts') )
    if os.path.isdir( os.path.join(dock, '_sass') ):
        shutil.rmtree( os.path.join(dock, '_sass') )
    if os.path.isdir( os.path.join(dock, 'scripts') ):
        shutil.rmtree( os.path.join(dock, 'scripts') )


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