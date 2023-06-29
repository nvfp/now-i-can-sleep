import os
import shutil

from mykit.kit.utils import printer


def update_404_and_favicon(C_404, C_ICON, D_404, D_ICON):

    ## 404 page
    printer(f"DEBUG: Attempting to copy '404.md'.")
    if os.path.isfile(C_404):
        printer(f'DEBUG: Rewriting 404.md from {repr(C_404)} to {repr(D_404)}.')
        text = (
            '---\n'
            'permalink: /404.html\n'
            'layout: main\n'
            'title: Page not found\n'
            '---\n\n'
        )
        with open(C_404, 'r') as f: text += f.read()
        with open(D_404, 'w') as f: f.write(text)
        printer(f'INFO: 404.md is rewritten.')

    ## favicon
    printer(f"DEBUG: Attempting to copy 'favicon.png'.")
    if os.path.isfile(C_ICON):
        printer(f'DEBUG: Copying favicon from {repr(C_ICON)} to {repr(D_ICON)}.')
        shutil.copy(C_ICON, D_ICON)
        printer(f'INFO: Favicon is renewed.')