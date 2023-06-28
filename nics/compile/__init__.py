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

    ## reminder: `base` is the X in foo.com/baseurl/{X}page
    ##           (e.g. nvfp.github.io/mykit/docs/guide/foo, then X='docs/guide/')
    def build_the_nested_divs_recursively(pth, base) -> str:
        out = ''

        for fd in sorted(os.listdir(pth)):  # reminder: the file/dir `fd` order in `pth` matters.
            if fd == 'index.md': continue  # index.md will not be shown in navigation bar
            fd_pth = os.path.join(pth, fd)

            res = re.match(r'(?:\d+ -- )?(?P<name>[\w -.]+) -- (?P<url>[\w -]+)(?:.md)?', fd)
            name = res.group('name')
            url = res.group('url')

            if os.path.isdir(fd_pth):
                out += f'<button id="{base.replace("/", "-")}{url}">> {name}</button>'  # remember to replace all slashes to hyphens
                out += f'<div class="child" id="{base.replace("/", "-")}{url}-div">'  # remember to replace all slashes to hyphens
                out += build_the_nested_divs_recursively(fd_pth, base+url+'/')
                out += '</div>'
            else:
                out += '<a href="{{ site.baseurl }}/' + f'{base}{url}">{name}</a>'

        return out
    header += build_the_nested_divs_recursively(tree, '')

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


    # printer(f'DEBUG: container: {repr(container)}.')
    # printer(f'DEBUG: target: {repr(target)}.')

    # printer(f'DEBUG: os.path.isdir(container): {os.path.isdir(container)}.')
    # printer(f'DEBUG: os.path.isdir(target): {os.path.isdir(target)}.')

    # printer(f'DEBUG: os.listdir(container): {os.listdir(container)}.')
    # printer(f'DEBUG: os.listdir(target): {os.listdir(target)}.')

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


    ## <rewriting 404.md>
    
    page404_pth = os.path.join(container, '404.md')
    if os.path.isfile(page404_pth):
        printer('DEBUG: Copying 404.md.')
        text = (
            '---\n'
            'permalink: /404.html\n'
            'layout: main\n'
            'title: Page not found\n'
            '---\n\n'
        )
        with open(page404_pth, 'r') as f:
            text += f.read()
        
        dst = os.path.join(target, '404.md')
        printer(f'DEBUG: writing to {repr(dst)}')
        with open(dst, 'w') as f:
            f.write(text)

    ## </rewriting 404.md>


    ## <rewriting the docs>

    def rewrite_the_docs_tree_recursively(pth, base):
        for i in os.listdir(pth):

            if i == 'index.md':

                if base == '/':  # homepage
                    text = (
                        '---\n'
                        'permalink: /\n'
                        'layout: main\n'
                        'title: Home\n'
                        '---\n\n'
                    )
                    src = os.path.join( pth, 'index.md' )
                    printer(f'DEBUG: src: {repr(src)}')
                    with open(src, 'r') as f: text += f.read()
                    
                    dst = os.path.join(target, 'index.md')
                    printer(f'DEBUG: writing to {repr(dst)}')
                    with open(dst, 'w') as f: f.write(text)
                else:
                    text = (
                        '---\n'
                        f'permalink: {base}\n'
                        'layout: main\n'
                        f"title: {list(filter(lambda s:s!='', base.split('/')))[-1]}\n"
                        '---\n\n'
                    )
                    src = os.path.join( pth, 'index.md' )
                    printer(f'DEBUG: src: {repr(src)}')
                    with open(src, 'r') as f: text += f.read()
                    
                    dst = os.path.join( target, '_pages', os.sep.join(filter(lambda s:s!='', base.split('/'))), 'index.md')
                    printer(f'DEBUG: writing to {repr(dst)}')
                    with open(dst, 'w') as f: f.write(text)

                continue

            pth2 = os.path.join(pth, i)

            res = re.match(r'(?:\d+ -- )?(?P<name>[\w -.]+) -- (?P<url>[\w -]+)(?:.md)?', i)
            name = res.group('name')
            url = res.group('url')

            if os.path.isdir(pth2):
                
                ## if the dir not exist -> create a new one
                dir = os.path.join( target, '_pages', os.sep.join(filter(lambda s:s!='', base.split('/'))), name )
                if not os.path.isdir(dir):
                    printer(f'DEBUG: Creating new dir: {repr(dir)}.')
                    os.mkdir(dir)

                rewrite_the_docs_tree_recursively(pth2, base+name+'/')
            else:
                text = (
                    '---\n'
                    f'permalink: {base}{url}/\n'
                    'layout: main\n'
                    f'title: {name}\n'
                    '---\n\n'
                )
                src = os.path.join( pth, i )
                printer(f'DEBUG: src: {repr(src)}')
                with open(src, 'r') as f: text += f.read()
                
                dst = os.path.join( target, '_pages', os.sep.join(filter(lambda s:s!='', base.split('/'))), f'{name}.md')
                printer(f'DEBUG: writing to {repr(dst)}')
                with open(dst, 'w') as f: f.write(text)
    rewrite_the_docs_tree_recursively( os.path.join(container, 'tree'), '/' )

    ## </rewriting the docs>


    printer(f'INFO: start copying assets..')
    printer(f'INFO: start copying favicon.png..')