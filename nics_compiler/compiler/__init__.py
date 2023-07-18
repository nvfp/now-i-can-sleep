import argparse
import os

from mykit.kit.keycrate import KeyCrate

from nics.main.constants import SETTINGS_KEYS
from nics_compiler.compiler.docking import docking
from nics_compiler.compiler.customize import customize_template_with_user_data


def run(dock, container):
    """
    `dock_path`: the abs path to the folder that holds the branch (Dock branch) for the doc website
    `container`: the abs path to the folder that holds the documentation files (in Load branch)
    """

    ## Parse settings
    cfg = KeyCrate(os.path.join(container, 'settings.txt'), True, True, SETTINGS_KEYS, SETTINGS_KEYS)

    ## Docking
    docking(dock)

    ## Rewrite the template using user-provided data
    customize_template_with_user_data(container, dock, cfg)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dock_path')
    parser.add_argument('container')
    args = parser.parse_args()
    run(args.load, args.dock, args.container)