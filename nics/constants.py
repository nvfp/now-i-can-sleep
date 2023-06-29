import os
import pkg_resources


try:
    __version__ = pkg_resources.get_distribution('nics').version
except pkg_resources.DistributionNotFound:  # this exception occurred during development (before the software installed via pip)
    __version__ = 'dev'


SOFTWARE_REPO = 'https://github.com/nvfp/now-i-can-sleep'
SOFTWARE_NAME = 'Now I Can Sleep'
SOFTWARE_DIST_NAME = 'nics'  # distribution name

ROOT_DIR_PTH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST_DIR_PTH = os.path.join(ROOT_DIR_PTH, SOFTWARE_DIST_NAME)

TEMPLATE_DIR_PTH = os.path.join(DIST_DIR_PTH, '_template')