import logging
import os
import sys

from mykit.kit.keycrate import KeyCrate

from nics.main.constants import SETTINGS_KEYS


logger = logging.getLogger(__name__)


def gather_settings(load_path, container):
    
    ## The settings.txt file
    file_path = os.path.join(load_path, container, 'settings.txt')

    old = KeyCrate(file_path, True, True)

    class cfg: ...

    for key in SETTINGS_KEYS:
        try:
            setattr(cfg, key, old[key])
        except AttributeError:
            setattr(cfg, key, input(f'Enter the value of this new option {repr(key)}: '))

    return cfg