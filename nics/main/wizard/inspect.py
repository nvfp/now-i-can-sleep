import os
import sys

from mykit.kit.utils import printer


def inspect(CONTAINER_DIR_PTH, WORKFLOW_FILE_PTH):
    
    ## the container ('docs/' folder) should not exist
    if os.path.isdir(CONTAINER_DIR_PTH):
        printer(f'ERROR: Folder {repr(CONTAINER_DIR_PTH)} already exists.')
        sys.exit(1)

    ## the GitHub Action workflow file 'rebuild-docs.yml' should not exist
    if os.path.isfile(WORKFLOW_FILE_PTH):
        printer(f'ERROR: File {repr(WORKFLOW_FILE_PTH)} already exists.')
        sys.exit(1)