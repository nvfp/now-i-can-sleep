import os

from nics.main.utils.ensure_a_git_repo import ensure_a_git_repo
from nics.main.cmd_upgrade.checks import check_rebuild_docs_yml_existence, check_container_clues, check_upgrade_status
from nics.main.cmd_upgrade.where_is_the_container import where_is_the_container
from nics.main.cmd_upgrade.gather_settings import gather_settings
from nics.main.cmd_init.loading.workflow_writer import workflow_writer
from nics.main.cmd_init.loading.settings_writer import settings_writer


def run():
    
    load_path = os.getcwd()

    ## Check
    ensure_a_git_repo(load_path)

    ## Check
    check_rebuild_docs_yml_existence(load_path)

    ## Get container
    CONTAINER = where_is_the_container(load_path)

    ## Check
    check_container_clues(load_path, CONTAINER)

    ## New settings key-value pairs
    cfg = gather_settings(load_path, CONTAINER)

    ## Check
    check_upgrade_status(cfg._nics_version)

    ## Update rebuild-docs.yml
    workflow_writer(
        load_path,
        cfg._load, cfg._dock, cfg._container, cfg._git_name, cfg._git_email, cfg._gh_repo_name
    )

    ## Update settings.txt
    settings_writer(
        load_path,
        cfg.author, cfg.custom_license, cfg.color_hue, cfg.lowercase_the_url, cfg.show_credit, cfg.char_map,
        cfg._git_name, cfg._git_email, cfg._gh_username, cfg._gh_repo_name, cfg._load, cfg._dock, cfg._container
    )

    ## For end-users
    print('Upgrade complete!')