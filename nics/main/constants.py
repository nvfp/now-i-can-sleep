import os
import pkg_resources


try:
    __version__ = pkg_resources.get_distribution('nics').version
except pkg_resources.DistributionNotFound:  # This exception occurred during development (before the software installed via pip)
    __version__ = 'dev'


ROOT_DIR_PTH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIST_DIR_PTH = os.path.join(ROOT_DIR_PTH, 'nics')
MAIN_DIR_PTH = os.path.join(ROOT_DIR_PTH, 'nics', 'main')

TEMPLATE_DIR_PTH = os.path.join(MAIN_DIR_PTH, '_template')
TMPL_DOCS_DIR_PTH = os.path.join(TEMPLATE_DIR_PTH, 'docs')
TMPL_WEB_DIR_PTH = os.path.join(TEMPLATE_DIR_PTH, 'web')

SETTINGS_KEYS = [
    'author',
    'color_hue',
    'lowercase_the_url',
    'show_credit',
    
    '_email',
    '_gh_username',
    '_gh_repo',
    '_main_branch_name',
    
    '_nics_version',
]