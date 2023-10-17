import os


def validations(nics_dir):

    if not os.path.isdir(nics_dir): raise AssertionError('not a dir')

    if 'favicon.ico' not in os.listdir(nics_dir):
        raise AssertionError("favicon.ico not found")

    if 'pages' not in os.listdir(nics_dir):
        raise AssertionError("pages/ not found")

    PAGES = os.path.join(nics_dir, 'pages')
    if len(os.listdir(PAGES)) == 0:
        raise AssertionError("pages/ folder shouldn't be empty")

    for stuff in os.listdir(PAGES):
        stuff_pth = os.path.join(PAGES, stuff)
        if not (os.path.isfile(stuff_pth) and stuff.lower().endswith('.md')):
            raise AssertionError("Only Markdown files allowed in the `pages/` folder.")
