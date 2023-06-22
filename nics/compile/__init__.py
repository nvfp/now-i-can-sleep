import os

from mykit.kit.keycrate import KeyCrate
from mykit.kit.utils import printer


def header_writer(container) -> str:

    header = (
        '<header>'

            '<h1>{{ page.title }}</h1>'

            '<div class="wrap">'

                '<button id="_root__nav">v Navigation</button>'
                '<div class="main" id="_root__nav-div">'
    )

    ## <build the nested divs recursively>

    def recursion(pth):

        printer(f'DEBUG: pth: {repr(pth)}')

        for i in os.listdir(pth):

            printer(f'DEBUG: {repr(i)}')
            
            full_pth = os.path.join(pth, i)
            if os.path.isdir(full_pth):
                recursion(full_pth)
        
        printer(f'DEBUG: ------------')
        
        return 'x'

    header += recursion(container)
    
    ## </build the nested divs recursively>

    header += (
                '</div>'
            
            '</div>'

        '</header>'
    )
    
    return header


def run(container, target):
    """
    ## Params
    - `container`: the nics folder bundle
    - `target`: the branch
    """

    printer(f'DEBUG: container: {repr(container)}.')
    printer(f'DEBUG: target: {repr(target)}.')

    printer(f'DEBUG: os.path.isdir(container): {os.path.isdir(container)}.')
    printer(f'DEBUG: os.path.isdir(target): {os.path.isdir(target)}.')

    printer(f'DEBUG: os.listdir(container): {os.listdir(container)}.')
    printer(f'DEBUG: os.listdir(target): {os.listdir(target)}.')

    settings = KeyCrate(
        os.path.join(container, '_nics', 'settings.txt'),
        key_is_var=True, eval_value=True
    )
    
    printer(f'DEBUG: settings.export(): {settings.export()}')

    header = header_writer(container)

    printer(f'DEBUG: header: {header}')

    
    printer(f'INFO: start copying assets..')