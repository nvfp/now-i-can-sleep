import logging
import os
import re
import sys


logger = logging.getLogger(__name__)


def where_is_the_container(load_path):

    ## /.github/workflows/rebuild-docs.yml
    file_path = os.path.join(load_path, '.github', 'workflows', 'rebuild-docs.yml')

    with open(file_path, 'r') as f:
        text = f.read()

    res = re.search(r'container: (?P<container>.*)', text)
    if res is None:
        logger.debug(f'Cannot find container {repr(container)} in {repr(file_path)}.')
        logger.error(
            "Cannot find 'container' in rebuild-docs.yml. "
            "Looks like NICS has not been initialized for this repository. Try 'nics init' instead."
        )
        sys.exit(1)
    else:
        container = res.group('container')
        logger.debug(f'Parsed container {repr(container)} from {repr(file_path)}.')
        return container