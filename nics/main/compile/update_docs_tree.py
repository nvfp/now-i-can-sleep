import os
import re
import shutil

from mykit.kit.utils import printer


def update_recursively(dock, D__PAGES, pth, base):
    printer(f'DEBUG: Updating docs-tree, pth: {repr(pth)}, base: {repr(base)}')

    for i in os.listdir(pth):
        pth2 = os.path.join(pth, i)

        ## <handling the index.md>
        if i == 'index.md':
            if base == '/':  # homepage
                dst = os.path.join(dock, 'index.md')
                text = (
                    '---\n'
                    'permalink: /\n'
                    'layout: main\n'
                    'title: Home\n'
                    '---\n\n'
                )
            else:
                dst = os.path.join(D__PAGES, os.sep.join(filter(lambda s:s!='', base.split('/'))), 'index.md')
                text = (
                    '---\n'
                    f'permalink: {base}\n'
                    'layout: main\n'
                    f"title: {list(filter(lambda s:s!='', base.split('/')))[-1]}\n"
                    '---\n\n'
                )
            with open(pth2, 'r') as f: text += f.read()
            with open(dst, 'w') as f: f.write(text)
            printer(f'DEBUG: Updated index.md from {repr(pth2)} to {repr(dst)}.')
            continue
        ## </handling the index.md>

        res = re.match(r'(?:\d+ -- )?(?P<name>[\w -.]+) -- (?P<url>[\w -]+)(?:\.md)?', i)
        name = res.group('name')
        url = res.group('url')

        if os.path.isdir(pth2):
            ## if the folder doesn't exist, create a new one.
            dir = os.path.join(D__PAGES, os.sep.join(filter(lambda s:s!='', base.split('/'))), name)
            if not os.path.isdir(dir):
                os.mkdir(dir)
                printer(f'DEBUG: Dir created: {repr(dir)}.')
            ## do it again
            update_recursively(dock, D__PAGES, pth2, base+url+'/')
        else:
            dst = os.path.join(D__PAGES, os.sep.join(filter(lambda s:s!='', base.split('/'))), f'{name}.md')
            text = (
                '---\n'
                f'permalink: {base}{url}/\n'
                'layout: main\n'
                f'title: {name}\n'
                '---\n\n'
            )
            with open(pth2, 'r') as f: text += f.read()
            with open(dst, 'w') as f: f.write(text)
            printer(f'DEBUG: Updated docs-tree file from {repr(pth2)} to {repr(dst)}.')


def update_docs_tree(dock, C_TREE, D__PAGES):

    ## delete the old '_pages' folder in docs branch
    if os.path.isdir(D__PAGES):  # reminder: initially, '_pages' doesn't exist
        printer(f'DEBUG: Deleting {repr(D__PAGES)} recursively.')
        shutil.rmtree(D__PAGES)
        os.mkdir(D__PAGES)

    update_recursively(dock, D__PAGES, C_TREE, '/')