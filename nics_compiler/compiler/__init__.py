import argparse
import logging
import os

from mykit.kit.keycrate import KeyCrate

from nics.main.constants import __version__, SETTINGS_KEYS
from nics.main.utils.ensure_a_git_repo import ensure_a_git_repo
from nics_compiler.compiler.docking import docking
# from nics_compiler.compiler.customize import customize_template_with_user_data


logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)


def run(dock_path, container_path):
    print(f'DEBUG: dock_path: {repr(dock_path)}.')
    print(f'DEBUG: container_path: {repr(container_path)}.')
    print(f'DEBUG: abs path of dock_path: {repr(os.path.abspath(dock_path))}.')
    print(f'DEBUG: abs path of container_path: {repr(os.path.abspath(container_path))}.')

    ## Check
    ensure_a_git_repo(dock_path)

    ## Parse settings
    cfg = KeyCrate(os.path.join(container_path, 'settings.txt'), True, True, SETTINGS_KEYS, SETTINGS_KEYS)

    ## Docking
    docking(dock_path)

    ## Rewrite the template using user-provided data
    # customize_template_with_user_data(dock_path, container_path, cfg)


def main():
    logger.debug(f'Running the NICS ({__version__}) compiler.')
    parser = argparse.ArgumentParser()
    parser.add_argument('dock_path')
    parser.add_argument('container_path')
    args = parser.parse_args()
    run(args.dock_path, args.container_path)