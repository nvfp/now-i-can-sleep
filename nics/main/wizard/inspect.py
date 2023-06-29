import os
import sys

from mykit.kit.utils import printer


def inspect(container_dir_pth, workflow_file_pth):
    
    ## the container ('docs/' folder) should not exist
    if os.path.isdir(container_dir_pth):
        printer(f"ERROR: Folder {repr(container_dir_pth)} already exists.")
        sys.exit(1)

    ## the GitHub Action workflow file 'rebuild-docs.yml' should not exist
    if os.path.isfile(workflow_file_pth):
        printer(f"ERROR: File {repr(workflow_file_pth)} already exists.")
        sys.exit(1)