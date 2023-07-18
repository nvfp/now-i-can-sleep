import logging


logger = logging.getLogger(__name__)


def get_text(gh_username, gh_repo_name):
    return f"""
## Sorry, it seems the page doesn't exists or no longer exists.

Do want to check it on the [homepage](https://{gh_username}.github.io/{gh_repo_name})?
"""


def create_404_page_file(file_path, gh_username, gh_repo_name):
    logger.debug('Writing 404 page file.')

    text = get_text(gh_username, gh_repo_name)
    with open(file_path, 'w') as f:
        f.write(text)
    
    logger.debug(f'404 page created at {repr(file_path)}.')