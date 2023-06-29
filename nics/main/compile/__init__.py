import os
import re
import shutil

from mykit.kit.keycrate import KeyCrate
from mykit.kit.utils import printer

from ..constants import __version__, SOFTWARE_DIST_NAME, SETTINGS_KEYS
from .inspect import inspect_the_container, inspect_the_dock
from .rewrite_the_header import rewrite_the_header
from .rewrite_the_footer import rewrite_the_footer
from .rewrite_jekyll_config import rewrite_jekyll_config
from .copying_template import copying_template
from .update_404_and_favicon import update_404_and_favicon


def run(container, dock):
    ## `container`: the 'docs/' folder (in main branch)
    ## `dock`: the 'docs' branch
    printer(f"INFO: Running '_compile' command ({SOFTWARE_DIST_NAME}-v{__version__})")

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
    D_JEKYLL_CONFIG = os.path.join(dock, '_config.yml')


    ## validate the requirements
    inspect_the_container(container)
    # inspect_the_dock()


    settings = KeyCrate(C_SETTINGS, True, True, SETTINGS_KEYS, SETTINGS_KEYS)


    ## handle init case
    if not os.path.isdir( os.path.join(dock, '_includes') ):
        os.mkdir(os.path.join(dock, '_includes'))
    if not os.path.isdir( os.path.join(dock, '_pages') ):  # os.mkdir needs the '_pages' folder to already exist before creating the folders inside.
        os.mkdir(os.path.join(dock, '_pages'))


    rewrite_the_header(C_TREE, D_HEADER)
    rewrite_the_footer(D_FOOTER, settings.show_credit)

    rewrite_jekyll_config(D_JEKYLL_CONFIG, settings.author, settings._gh_username, settings._gh_repo)

    copying_template(dock)

    update_404_and_favicon(C_404, C_ICON, D_404, D_ICON)



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
    if os.path.isdir(D_ASSETS):  # handle init case
        printer(f'INFO: Deleting {repr(D_ASSETS)} recursively..')
        shutil.rmtree(D_ASSETS)
    printer(f'INFO: Copying from {repr(C_ASSETS)} to {repr(D_ASSETS)}.')
    shutil.copytree(C_ASSETS, D_ASSETS)

    