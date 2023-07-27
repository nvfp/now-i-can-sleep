import os
import pkg_resources


try:
    __version__ = pkg_resources.get_distribution('nics').version
except pkg_resources.DistributionNotFound:  # This exception occurred during development (before the software installed via pip)
    __version__ = 'dev'


ROOT_DIR_PTH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DIST_DIR_PTH = os.path.join(ROOT_DIR_PTH, 'nics')
MAIN_DIR_PTH = os.path.join(ROOT_DIR_PTH, 'nics', 'main')
NICS_COMPILER_DIR_PTH = os.path.join(ROOT_DIR_PTH, 'nics_compiler')

TEMPLATE_DOCS_DIR_PTH = os.path.join(ROOT_DIR_PTH, 'nics', 'main', 'template')
TEMPLATE_WEB_DIR_PTH  = os.path.join(ROOT_DIR_PTH, 'nics_compiler', 'template')

SETTINGS_KEYS = [
    'author',
    'custom_license',
    'color_hue',
    'lowercase_the_url',
    'show_credit',
    'char_map',
    '_git_name',
    '_git_email',
    '_gh_username',
    '_gh_repo_name',
    '_load',
    '_dock',
    '_container',
    '_nics_version',
]