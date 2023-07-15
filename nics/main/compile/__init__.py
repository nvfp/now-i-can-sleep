import os

from mykit.kit.keycrate import KeyCrate

from nics.main.constants import SETTINGS_KEYS
from nics.main.compile.inspect import inspect_the_container, inspect_the_dock
from nics.main.compile.docking import docking
from nics.main.compile.writer import customize_template_with_user_data


def run(container, dock):
    """
    `container`: The 'docs/' folder (in main branch)
    `dock`: The 'docs' branch
    """

    ## Inspection
    inspect_the_container(container)
    inspect_the_dock(dock)

    ## Parse settings
    cfg = KeyCrate(os.path.join(container, 'settings.txt'), True, True, SETTINGS_KEYS, SETTINGS_KEYS)

    ## Docking
    docking(dock)

    ## Rewrites the template using user-provided data
    customize_template_with_user_data(container, dock, cfg)