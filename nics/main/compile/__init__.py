import os

from mykit.kit.keycrate import KeyCrate
from mykit.kit.utils import printer

from ..constants import __version__, SOFTWARE_DIST_NAME, SETTINGS_KEYS
from .inspect import inspect_the_container, inspect_the_dock
from .rewrite_the_header import rewrite_the_header
from .rewrite_the_footer import rewrite_the_footer
from .rewrite_jekyll_config import rewrite_jekyll_config
from .copying_template import copying_template
from .update_404_and_favicon import update_404_and_favicon
from .update_assets import update_assets
from .update_docs_tree import update_docs_tree


def run(container, dock):
    ## `container`: the 'docs/' folder (in main branch)
    ## `dock`: the 'docs' branch
    printer(f"INFO: Running '_compile' command ({SOFTWARE_DIST_NAME}-v{__version__})")

    C_ASSETS = os.path.join(container, 'assets')
    C_TREE = os.path.join(container, 'tree')
    C_404 = os.path.join(container, '404.md')
    C_ICON = os.path.join(container, 'favicon.png')
    C_SETTINGS = os.path.join(container, 'settings.txt')

    D__INCLUDES = os.path.join(dock, '_includes')
    D__PAGES = os.path.join(dock, '_pages')
    D_HEADER = os.path.join(dock, '_includes', 'header.html')
    D_FOOTER = os.path.join(dock, '_includes', 'footer.html')
    D_ASSETS = os.path.join(dock, 'assets')
    D_404 = os.path.join(dock, '404.md')
    D_ICON = os.path.join(dock, 'favicon.png')
    D_JEKYLL_CONFIG = os.path.join(dock, '_config.yml')


    ## validate the requirements
    inspect_the_container(container)
    # inspect_the_dock()


    cfg = KeyCrate(C_SETTINGS, True, True, SETTINGS_KEYS, SETTINGS_KEYS)


    ## handle init case
    if not os.path.isdir(D__INCLUDES):
        os.mkdir(D__INCLUDES)
    rewrite_the_header(C_TREE, D_HEADER)
    rewrite_the_footer(D_FOOTER, cfg.show_credit)

    rewrite_jekyll_config(D_JEKYLL_CONFIG, cfg.author, cfg._gh_username, cfg._gh_repo)
    update_404_and_favicon(C_404, C_ICON, D_404, D_ICON)
    update_assets(C_ASSETS, D_ASSETS)

    copying_template(dock)
    # update_main_sass()


    update_docs_tree(dock, C_TREE, D__PAGES)