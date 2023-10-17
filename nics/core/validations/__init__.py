import os


def validations(nics_dir):

    if not os.path.isdir(nics_dir): raise AssertionError('not a dir')

    if sorted(os.listdir(nics_dir)) != ['favicon.ico', 'pages', 'settings.txt']:
        raise AssertionError('The folder should only contain favicon.ico, pages, and settings.txt')

    PAGES = os.path.join(nics_dir, 'pages')
    if len(os.listdir(PAGES)) == 0: raise AssertionError("pages/ folder shouldn't be empty")

    for stuff in os.listdir(PAGES):
        stuff_pth = os.path.join(PAGES, stuff)
        if not os.path.isfile(stuff_pth): raise AssertionError(f"This {repr(stuff)} is not a file")
        if not stuff.endswith('.md'): raise AssertionError(f"This {repr(stuff)} is not a markdown")
