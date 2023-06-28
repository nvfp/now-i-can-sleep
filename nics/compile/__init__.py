import os
import re
import shutil
from typing import Union

from mykit.kit.keycrate import KeyCrate
from mykit.kit.utils import printer

from .inspect import inspect_the_container, inspect_the_dock


AbsPath = Union[str, os.PathLike]


def update_header(tree: AbsPath, header_pth):
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
    
    with open(header_pth, 'w') as file:
        file.write(header)



def update_footer(footer_pth, show_credit):

    text = (
        '<footer>'
            '<p id="copyright">&copy; {{ "now" | date: "%Y" }} {{ site.author.name }}</p>'
    )
    if show_credit:
        text += '<p id="credit">built with <a href="https://github.com/nvfp/now-i-can-sleep">now-i-can-sleep</a></p>'
    text += '</footer>'

    with open(footer_pth, 'w') as f:
        f.write(text)


def run(container: AbsPath, dock: AbsPath) -> None:
    """
    ## Params
    - `container`: the nics folder bundle
    - `dock`: the branch
    """

    C_ASSETS = os.path.join(container, 'assets')
    C_TREE = os.path.join(container, 'tree')
    C_404 = os.path.join(container, '404.md')
    C_ICON = os.path.join(container, 'favicon.png')
    C_SETTINGS = os.path.join(container, 'settings.txt')

    D_HEADER = os.path.join(dock, '_includes', 'header.html')
    D_FOOTER = os.path.join(dock, '_includes', 'footer.html')
    D_ASSETS = os.path.join(dock, 'assets')
    D_404 = os.path.join(dock, '404.md')
    D_ICON = os.path.join(dock, 'favicon.png')


    ## validate the requirements
    inspect_the_container(container)
    # inspect_the_dock()


    settings = KeyCrate(C_SETTINGS, True, True)


    update_header(C_TREE, D_HEADER)
    update_footer(D_FOOTER, settings.show_credit)


    ## <rewriting 404.md>
    
    if os.path.isfile(C_404):
        printer('DEBUG: Copying 404.md.')
        text = (
            '---\n'
            'permalink: /404.html\n'
            'layout: main\n'
            'title: Page not found\n'
            '---\n\n'
        )
        with open(C_404, 'r') as f:
            text += f.read()
        
        printer(f'DEBUG: writing to {repr(D_404)}')
        with open(D_404, 'w') as f:
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
                    
                    dst = os.path.join(dock, 'index.md')
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
                    
                    dst = os.path.join( dock, '_pages', os.sep.join(filter(lambda s:s!='', base.split('/'))), 'index.md')
                    printer(f'DEBUG: writing to {repr(dst)}')
                    with open(dst, 'w') as f: f.write(text)

                continue

            pth2 = os.path.join(pth, i)

            res = re.match(r'(?:\d+ -- )?(?P<name>[\w -.]+) -- (?P<url>[\w -]+)(?:.md)?', i)
            name = res.group('name')
            url = res.group('url')

            if os.path.isdir(pth2):
                
                ## if the dir not exist -> create a new one
                dir = os.path.join( dock, '_pages', os.sep.join(filter(lambda s:s!='', base.split('/'))), name )
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
                
                dst = os.path.join( dock, '_pages', os.sep.join(filter(lambda s:s!='', base.split('/'))), f'{name}.md')
                printer(f'DEBUG: writing to {repr(dst)}')
                with open(dst, 'w') as f: f.write(text)
    rewrite_the_docs_tree_recursively( os.path.join(container, 'tree'), '/' )

    ## </rewriting the docs>


    printer(f'INFO: start copying assets..')
    printer(f'INFO: Deleting {repr(D_ASSETS)} recursively..')
    shutil.rmtree(D_ASSETS)
    printer(f'INFO: Copying from {repr(C_ASSETS)} to {repr(D_ASSETS)}.')
    shutil.copytree(C_ASSETS, D_ASSETS)

    if os.path.isfile(C_ICON):
        printer(f'INFO: start copying favicon.png..')
        shutil.copy(C_ICON, D_ICON)