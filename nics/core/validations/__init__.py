import os


def validations(NICS_DIR):

    if not os.path.isdir(NICS_DIR):
        raise AssertionError(f"Not a dir: {repr(NICS_DIR)}.")
    
    FAVICON = os.path.join(NICS_DIR, 'favicon.ico')
    PAGES = os.path.join(NICS_DIR, 'pages')

    if not os.path.isfile(FAVICON):
        raise AssertionError("favicon.ico not found")

    if not os.path.isdir(PAGES):
        raise AssertionError("pages/ not found")

    if len(os.listdir(PAGES)) == 0:
        raise AssertionError("pages/ folder shouldn't be empty")

    for stuff in os.listdir(PAGES):
        stuff_pth = os.path.join(PAGES, stuff)
        if not (os.path.isfile(stuff_pth) and stuff.lower().endswith('.md')):
            raise AssertionError("Only Markdown files allowed in the `pages/` folder.")
