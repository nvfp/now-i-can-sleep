import os

## typehint
from pathlib import Path as _Path
from typing import Union, NoReturn

from mykit.kit.keycrate import KeyCrate
from mykit.kit.utils import printer


## typehint
AbsPath = Union[str, os.PathLike]


def header_writer(tree: AbsPath) -> str:

    header = (
        '<header>'

            '<h1>{{ page.title }}</h1>'

            '<div class="wrap">'

                '<button id="_root__nav">v Navigation</button>'
                '<div class="main" id="_root__nav-div">'
    )

    ## <build the nested divs recursively>

    def recursion(pth):

        printer(f'DEBUG: pth: {repr(pth)}  os.listdir(pth): {os.listdir(pth)}')

        for i in os.listdir(pth):

            printer(f'DEBUG: {repr(i)}')
            
            full_pth = os.path.join(pth, i)
            if os.path.isdir(full_pth):
                recursion(full_pth)
        
        printer(f'DEBUG: ------------')
        
        return 'x'

    header += recursion(tree)
    
    ## </build the nested divs recursively>

    header += (
                '</div>'
            
            '</div>'

        '</header>'
    )
    
    return header


def inspect_the_container(container: AbsPath) -> Union[None, NoReturn]:
    """
    Asserting the required core elements for deploying the pages.
    """
    
    ## settings.txt must exist
    if not os.path.isfile( os.path.join(container, 'settings.txt') ):
        raise AssertionError('The main settings file "settings.txt" is not found in the container.')

    ## tree/ folder must exist
    if not os.path.isdir( os.path.join(container, 'tree') ):
        raise AssertionError('The docs structure folder "tree/" is not found in the container.')


def inspect_the_tree():
    """
    The 'tree/' folder has a quite strict rules: only the necessary stuff should be there,
    and the names of files and folders should follow certain patterns.
    This makes things easier later on, with fewer checks needed.
    """


def run(container: AbsPath, target: AbsPath) -> None:
    """
    ## Params
    - `container`: the nics folder bundle
    - `target`: the branch
    """

    ## validate the requirements
    inspect_the_container(container)

    ## validate
    inspect_the_tree()


    printer(f'DEBUG: container: {repr(container)}.')
    printer(f'DEBUG: target: {repr(target)}.')

    printer(f'DEBUG: os.path.isdir(container): {os.path.isdir(container)}.')
    printer(f'DEBUG: os.path.isdir(target): {os.path.isdir(target)}.')

    printer(f'DEBUG: os.listdir(container): {os.listdir(container)}.')
    printer(f'DEBUG: os.listdir(target): {os.listdir(target)}.')

    settings = KeyCrate(
        os.path.join(container, 'settings.txt'),
        key_is_var=True, eval_value=True
    )
    
    printer(f'DEBUG: settings.export(): {settings.export()}')

    header = header_writer(container)

    printer(f'DEBUG: header: {header}')

    
    printer(f'INFO: start copying assets..')
    printer(f'INFO: start copying 404.md..')
    printer(f'INFO: start copying favicon.png..')