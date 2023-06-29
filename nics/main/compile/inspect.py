import os
import re


def _inspect_tree_recursively(pth):

    for i in os.listdir(pth):        
        pth2 = os.path.join(pth, i)

        if os.path.isdir(pth2):
            ## check dir name format
            if re.match(r'(?:\d+ -- )?[\w -.]+ -- [\w -]+', i) is None:
                raise AssertionError(f'Dir name {repr(i)} format is invalid.')
            ## inspect the dir
            _inspect_tree_recursively(pth2)
        else:
            ## only .md files are allowed
            if not i.endswith('.md'):
                raise AssertionError(f"File {repr(i)} isn't an .md file.")
            ## check file name format
            if i != 'index.md':
                if re.match(r'(?:\d+ -- )?[\w -.]+ -- [\w -]+\.md$', i) is None:
                    raise AssertionError(f'File name {repr(i)} format is invalid.')


def inspect_the_container(container):

    ## 'tree/' folder
    if not os.path.isdir( os.path.join(container, 'tree') ):
        raise AssertionError("Couldn't find 'tree/' in the container.")

    ## homepage 'tree/index.md' file
    if not os.path.isfile( os.path.join(container, 'tree', 'index.md') ):
        raise AssertionError("Couldn't find 'tree/index.md' in the container.")

    ## settings file
    if not os.path.isfile( os.path.join(container, 'settings.txt') ):
        raise AssertionError("Couldn't find 'settings.txt' in the container.")

    ## inspecting the 'tree/' folder
    _inspect_tree_recursively( os.path.join(container, 'tree') )