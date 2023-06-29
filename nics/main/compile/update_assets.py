import os
import shutil

from mykit.kit.utils import printer


def update_assets(C_ASSETS, D_ASSETS):
    ## 'assets/' folder to store items used in markdown files
    printer(f"DEBUG: Start copying 'assets/' folder.")

    if os.path.isdir(D_ASSETS):
        printer(f'INFO: Deleting {repr(D_ASSETS)} recursively.')
        shutil.rmtree(D_ASSETS)

    printer(f'INFO: Copying from {repr(C_ASSETS)} to {repr(D_ASSETS)}.')
    shutil.copytree(C_ASSETS, D_ASSETS)