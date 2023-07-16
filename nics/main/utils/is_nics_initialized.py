import os


def is_nics_initialized(dir_path):
    """
    Shallow check if `dir_path` has been previously initialized with NICS.
    Return True if clues are found, False otherwise.
    """

    clues = []

    ## Inspect /.github/workflows/rebuild-docs.yml
    if os.path.isfile(os.path.join(dir_path, '.github', 'workflows', 'rebuild-docs.yml')):
        clues.append(True)
    else:
        clues.append(False)

    ## Inspect /docs/settings.txt
    if os.path.isfile(os.path.join(dir_path, 'docs', 'settings.txt')):
        clues.append(True)
    else:
        clues.append(False)

    ## Inspect /docs/tree/index.md
    if os.path.isfile(os.path.join(dir_path, 'docs', 'tree', 'index.md')):
        clues.append(True)
    else:
        clues.append(False)

    return all(clues)  # True if all in `clues` are True