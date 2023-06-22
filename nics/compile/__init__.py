import os
import re

## typehint
from pathlib import Path as _Path
from typing import Union, NoReturn

from mykit.kit.keycrate import KeyCrate
from mykit.kit.utils import printer


## typehint
AbsPath = Union[str, os.PathLike]


"""

reminder:

- keep the printers (debuggers) printing (don't comment them out)
  for easy debugging inside the GitHub Actions VM since we can't
  enable the debuggers there
"""


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
        out = ''

        ## Somehow, os.listdir is not ordered, but remember the order matters
        ## because nics allows users to arrange the order of the docs tree.
        ordered = sorted(os.listdir(pth))  # a list of files and folders inside `pth`
        printer(f'DEBUG: pth: {repr(pth)}  os.listdir(pth): {os.listdir(pth)}  ordered: {ordered}')

        def parse_relative_path() -> str:  # reminder: using function to prevent variable name clash
            rel = os.path.relpath(pth, tree)  # cut the path up to the tree/ path
            if rel == '.': rel = ''  # handle init case (where `pth` is the same as `tree`)
            return rel.replace(os.sep, '/')  # using forward slash (because some OS are using backslash)
        loc = parse_relative_path()  # must not contain spaces
        printer(f'DEBUG: loc: {repr(loc)}')

        for fd in ordered:  # reminder: fd (file or directory)
            printer(f'DEBUG: fd: {repr(fd)}')

            fd_pth = os.path.join(pth, fd)

            ## this guarantees a match as the tree/ contents have already been inspected
            res = re.match(r'(?:\d+ - )?(?P<name>[\w -]+)(?:.md)?', fd)
            name = res.group('name')

            if os.path.isdir(fd_pth):

                out += f'<button id="{loc}/{name}">> {name}</button>'
                out += f'<div class="child" id="{loc}/{name}-div">'
                out += recursion(fd_pth)
                out += '</div>'
            else:
                if os.path.isfile(fd_pth):

                    if fd == 'index.md':
                        printer('DEBUG: index.md is skipped!')
                        continue

                    out += f'<a href="{loc}/{name}">{name}</a>'
                else:
                    ## this one should never be called, i guess
                    raise AssertionError(f'fd_pth is not either a file or a dir: {repr(fd_pth)}')

        printer(f'DEBUG: ------------')
        return out

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