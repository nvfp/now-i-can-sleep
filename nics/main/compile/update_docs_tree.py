import os
import re
import shutil

from mykit.kit.utils import printer


def update_recursively(dock, D__PAGES, pth, base):

    for i in os.listdir(pth):

        ## <handling the index.md>
        if i == 'index.md':
            src = os.path.join(pth, 'index.md')
            if base == '/':  # homepage
                dst = os.path.join(dock, 'index.md')
                text = (
                    '---\n'
                    'permalink: /\n'
                    'layout: main\n'
                    'title: Home\n'
                    '---\n\n'
                )
                with open(src, 'r') as f: text += f.read()
                with open(dst, 'w') as f: f.write(text)
            else:
                dst = os.path.join(D__PAGES, os.sep.join(filter(lambda s:s!='', base.split('/'))), 'index.md')
                text = (
                    '---\n'
                    f'permalink: {base}\n'
                    'layout: main\n'
                    f"title: {list(filter(lambda s:s!='', base.split('/')))[-1]}\n"
                    '---\n\n'
                )
                with open(src, 'r') as f: text += f.read()
                with open(dst, 'w') as f: f.write(text)
            continue
        ## </handling the index.md>

        pth2 = os.path.join(pth, i)

        res = re.match(r'(?:\d+ -- )?(?P<name>[\w -.]+) -- (?P<url>[\w -]+)(?:.md)?', i)
        name = res.group('name')
        url = res.group('url')

        if os.path.isdir(pth2):
            ## if the dir not exist -> create a new one
            dir = os.path.join(D__PAGES, os.sep.join(filter(lambda s:s!='', base.split('/'))), name )
            if not os.path.isdir(dir):
                printer(f'DEBUG: Creating new dir: {repr(dir)}.')
                os.mkdir(dir)
            update_recursively(dock, D__PAGES, pth2, base+name+'/')
        else:
            src = os.path.join(pth, i)
            dst = os.path.join(D__PAGES, os.sep.join(filter(lambda s:s!='', base.split('/'))), f'{name}.md')
            text = (
                '---\n'
                f'permalink: {base}{url}/\n'
                'layout: main\n'
                f'title: {name}\n'
                '---\n\n'
            )
            with open(src, 'r') as f: text += f.read()
            with open(dst, 'w') as f: f.write(text)


def update_docs_tree(dock, C_TREE, D__PAGES):

    ## delete the old '_pages' folder in docs branch
    if os.path.isdir(D__PAGES):  # reminder: initially, '_pages' doesn't exist
        printer(f'DEBUG: Deleting {repr(D__PAGES)} recursively.')
        shutil.rmtree(D__PAGES)
        os.mkdir(D__PAGES)

    update_recursively(dock, D__PAGES, C_TREE, '/')