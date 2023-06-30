import os


def inspect_the_container(container):

    ## homepage 'tree/index.md' file must exist
    if not os.path.isfile( os.path.join(container, 'tree', 'index.md') ):
        raise AssertionError("Couldn't find 'tree/index.md' in the container.")

    ## settings file must exist
    if not os.path.isfile( os.path.join(container, 'settings.txt') ):
        raise AssertionError("Couldn't find 'settings.txt' in the container.")