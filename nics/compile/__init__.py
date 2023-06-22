import os

## typehint
from pathlib import Path as _Path
from typing import Union, NoReturn

from mykit.kit.keycrate import KeyCrate
from mykit.kit.utils import printer


## typehint
AbsPath = Union[str, os.PathLike]


def header_writer(tree: AbsPath) -> str:
    """
    reminder:
    - index.md will not be included in the header
    """

    header = (
        '<header>'

            '<h1>{{ page.title }}</h1>'

            '<div class="wrap">'

                '<button id="_root__nav">v Navigation</button>'
                '<div class="main" id="_root__nav-div">'
    )

    ## <build the nested divs recursively>

    def recursion(pth) -> str:

        thedivs = ''

        stuff = sorted(os.listdir(pth))

        printer(f'DEBUG: pth: {repr(pth)}  os.listdir(pth): {os.listdir(pth)}  stuff: {stuff}')

        for i in stuff:

            printer(f'DEBUG: i: {repr(i)}')
            
            full_pth = os.path.join(pth, i)
            
            if os.path.isdir(full_pth):

                thedivs += f'<button id="{i}">> {i}</button>'
                thedivs += f'<div class="child" id="{i}-div">'
                thedivs += recursion(full_pth)
                thedivs += '</div>'
            else:
                if os.path.isfile(full_pth):

                    if i == 'index.md':
                        printer('DEBUG: index.md is skipped!')
                        continue

                    thedivs += f'<a href="file0">{i}</a>'
                else:
                    ## this one should never be called, i guess
                    raise AssertionError(f'full_pth is not either a file or a dir: {repr(full_pth)}')

        printer(f'DEBUG: ------------')
        
        return thedivs

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

    
    ## <rewriting the header.html>
    
    header = header_writer( os.path.join(container, 'tree') )

    printer(f'DEBUG: header: {header}')
    
    header_pth = os.path.join(target, '_includes', 'header.html')
    printer(f'DEBUG: header_pth: {repr(header_pth)}')

    printer(f'INFO: rewriting header.html...')
    with open(header_pth, 'w') as file:
        file.write(header)

    ## </rewriting the header.html>


    printer(f'INFO: start copying assets..')
    printer(f'INFO: start copying 404.md..')
    printer(f'INFO: start copying favicon.png..')