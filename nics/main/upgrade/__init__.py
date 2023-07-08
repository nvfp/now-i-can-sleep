import os
import sys

from mykit.kit.keycrate import KeyCrate
from mykit.kit.utils import printer

from ..constants import __version__, SETTINGS_KEYS
from ..wizard.workflow_writer import _writer as the_workflow_writer
from ..wizard.settings_writer import full_writer as the_settings_writer


def run():

    CWD = os.getcwd()

    WORKFLOW_FILE_PTH = os.path.join(CWD, '.github', 'workflows', 'rebuild-docs.yml')
    SETTINGS_FILE_PTH = os.path.join(CWD, 'docs', 'settings.txt')

    if not os.path.isfile(WORKFLOW_FILE_PTH):
        printer(f'ERROR: Workflow file not found: {repr(WORKFLOW_FILE_PTH)}')
        sys.exit(1)

    if not os.path.isfile(SETTINGS_FILE_PTH):
        printer(f'ERROR: Settings file not found: {repr(SETTINGS_FILE_PTH)}')
        sys.exit(1)

    ## parse the settings
    cfg = KeyCrate(SETTINGS_FILE_PTH, True, True, SETTINGS_KEYS, SETTINGS_KEYS)

    if __version__ == cfg._nics_version:
        printer(f'INFO: Everything is up to date.')
        sys.exit(0)

    if __version__.split('.')[0] != cfg._nics_version.split('.')[0]:
        printer(f"ERROR: Cannot upgrade across major versions. Please run 'nics init' instead.")
        sys.exit(1)


    text = the_workflow_writer(cfg.author, cfg._email, cfg._gh_repo, cfg._main_branch_name)
    with open(WORKFLOW_FILE_PTH, 'w', encoding='utf-8') as f: f.write(text)
    printer(f'INFO: Workflow file {repr(WORKFLOW_FILE_PTH)} is updated.')

    text = the_settings_writer(
        cfg.author, cfg.color_hue, cfg.lowercase_the_url, cfg.show_credit,
        cfg._email, cfg._gh_username, cfg._gh_repo, cfg._main_branch_name
    )
    with open(SETTINGS_FILE_PTH, 'w') as f: f.write(text)
    printer(f'INFO: Settings file {repr(SETTINGS_FILE_PTH)} is updated.')
    
    printer(f'INFO: Upgrade finished.')