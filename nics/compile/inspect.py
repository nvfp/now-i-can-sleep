import os
import re

from typing import Union, NoReturn


AbsPath = Union[str, os.PathLike]


def _check_format(name):
    res = re.match(r'(?:\d+ -- )?(?P<name>[\w -.]+) -- (?P<url>[\w -]+)(?:.md)?', name)
    if res is None:
        raise

def _inspect_tree_recursively(pth: AbsPath):
    
    for i in os.listdir(pth):
        
        subpth = os.path.join(pth, i)

        if os.path.isdir(subpth):

            ## check dir name format
            res = re.match(r'(?:\d+ -- )?(?P<name>[\w -.]+) -- (?P<url>[\w -]+)', i)
            if res is None:
                raise AssertionError(f'Dir name {repr(i)} format is invalid.')

            _inspect_tree_recursively(subpth)
        else:
            
            ## only .md files are allowed
            if not i.endswith('.md'):
                raise AssertionError(f"File {repr(i)} isn't an .md file.")

            ## check file name format
            if i != 'index.md':
                res = re.match(r'(?:\d+ -- )?(?P<name>[\w -.]+) -- (?P<url>[\w -]+)(?:.md)?', i)
                if res is None:
                    raise AssertionError(f'File name {repr(i)} format is invalid.')

def inspect_the_container(container: AbsPath) -> Union[None, NoReturn]:
    """
    These items are needed inside the container:
    - tree/
    - tree/index.md
    - settings.txt
    """

    ## tree/ folder
    if not os.path.isdir( os.path.join(container, 'tree') ):
        raise AssertionError("Couldn't find 'tree/' in the container.")

    ## homepage
    if not os.path.isfile( os.path.join(container, 'tree', 'index.md') ):
        raise AssertionError("Couldn't find 'tree/index.md' in the container.")

    ## settings file
    if not os.path.isfile( os.path.join(container, 'settings.txt') ):
        raise AssertionError("Couldn't find 'settings.txt' in the container.")

    ## inspecting the tree/
    _inspect_tree_recursively( os.path.join(container, 'tree') )


def inspect_the_dock(dock):
    """shallow inspection to ensure that we are on the correct branch"""

    # if not os.path.isdir( os.path.join(dock, '_includes') ):
    #     raise AssertionError("Folder '_includes' ")