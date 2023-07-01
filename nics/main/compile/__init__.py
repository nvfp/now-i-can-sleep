import os
import shutil

from mykit.kit.keycrate import KeyCrate
from mykit.kit.utils import printer

from ..constants import __version__, SOFTWARE_DIST_NAME, SETTINGS_KEYS
from .inspect import inspect_the_container
from .update_header import update_header
from .update_footer import update_footer
from .update_jekyll_config import update_jekyll_config
from .update_404_and_favicon import update_404_and_favicon
from .copying_template import copying_template
from .update_sass_constants import update_sass_constants
from .update_docs_tree import update_docs_tree


def run(container, dock):
    ## `container`: the 'docs/' folder (in main branch)
    ## `dock`: the 'docs' branch
    printer(f"INFO: Running '_compile' command ({SOFTWARE_DIST_NAME}-v{__version__})")

    C_TREE = os.path.join(container, 'tree')
    C_404 = os.path.join(container, '404.md')
    C_ICON = os.path.join(container, 'favicon.png')
    C_SETTINGS = os.path.join(container, 'settings.txt')

    D__INCLUDES = os.path.join(dock, '_includes')
    D__PAGES = os.path.join(dock, '_pages')
    D_HEADER = os.path.join(dock, '_includes', 'header.html')
    D_FOOTER = os.path.join(dock, '_includes', 'footer.html')
    D_JEKYLL_CONFIG = os.path.join(dock, '_config.yml')
    D_404 = os.path.join(dock, '404.md')
    D_ICON = os.path.join(dock, 'favicon.png')
    D_SASS_CONSTANTS = os.path.join(dock, '_sass', 'constants.scss')

    ## inspection
    inspect_the_container(container)

    ## parse the settings
    cfg = KeyCrate(C_SETTINGS, True, True, SETTINGS_KEYS, SETTINGS_KEYS)

    ## erase everything
    for stuff in os.listdir(dock):
        if stuff == '.git': continue  # except git folder
        pth = os.path.join(dock, stuff)
        if os.path.isdir(pth):
            shutil.rmtree(pth)
            printer(f'Deleted dir {repr(pth)}.')
        else:
            os.remove(pth)
            printer(f'Deleted file {repr(pth)}.')


    if not os.path.isdir(D__INCLUDES):  # handle init case: initially, '_includes' folder doesn't exist in docs branch
        printer(f'DEBUG: Creating dir {repr(D__INCLUDES)}.')
        os.mkdir(D__INCLUDES)
    update_header(C_TREE, D_HEADER, cfg.lowercase_the_url)
    update_footer(D_FOOTER, cfg.show_credit)

    update_jekyll_config(D_JEKYLL_CONFIG, cfg.author, cfg._gh_username, cfg._gh_repo)
    update_404_and_favicon(C_404, C_ICON, D_404, D_ICON)

    copying_template(dock)
    update_sass_constants(D_SASS_CONSTANTS, cfg.color_hue)

    update_docs_tree(C_TREE, D__PAGES, cfg.lowercase_the_url, cfg._gh_username, cfg._gh_repo)