import os

from mykit.kit.keycrate import KeyCrate
from mykit.kit.utils import printer


def header_writer(docs) -> str:
    
    header = (
        '<header>'

            '<h1>{{ page.title }}</h1>'

            '<div class="wrap">'

                '<button id="_root__nav">v Navigation</button>'
                '<div class="main" id="_root__nav-div">'
    )

    for pth, dirs, files in os.walk(docs):

        printer(f'DEBUG: pth: {pth}')
        printer(f'DEBUG: dirs: {dirs}')
        printer(f'DEBUG: files: {files}')
        printer(f'DEBUG: ---------')

    header += (
                '</div>'
            
            '</div>'

        '</header>'
    )
    
    return header


def run(docs, target):
    """
    ## Params
    - `docs`: the docs/ bundle
    - `target`: the branch
    """

    printer(f'DEBUG: docs: {repr(docs)}.')
    printer(f'DEBUG: target: {repr(target)}.')

    printer(f'DEBUG: os.path.isdir(docs): {os.path.isdir(docs)}.')
    printer(f'DEBUG: os.path.isdir(target): {os.path.isdir(target)}.')

    printer(f'DEBUG: os.listdir(docs): {os.listdir(docs)}.')
    printer(f'DEBUG: os.listdir(target): {os.listdir(target)}.')

    settings = KeyCrate(
        os.path.join(docs, '_nics', 'settings.txt'),
        key_is_var=True, eval_value=True
    )
    
    printer(f'DEBUG: settings.export(): {settings.export()}')

    header = header_writer(docs)

    printer(f'DEBUG: header: {header}')