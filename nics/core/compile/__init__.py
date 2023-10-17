import json
import os
import re
import shutil
import tempfile


CWD = os.environ['GITHUB_WORKSPACE']

TEMPLATE_DIR = os.path.join(os.environ['GITHUB_ACTION_PATH', 'nics', 'template'])


def store(nics_dir):
    DIR = tempfile.mkdtemp()
    shutil.move(nics_dir, DIR)
    return DIR


def prepare():
    
    ## Copy the template
    shutil.move(TEMPLATE_DIR, CWD)

    ## Remove the files that will be replaced soon
    os.remove(os.path.join(CWD, '_config.yml'))
    os.remove(os.path.join(CWD, 'favicon.ico'))

    ## Clear the pages/ folder
    PAGES = os.path.join(CWD, 'pages')
    shutil.rmtree(PAGES)
    os.mkdir(PAGES)
    print(f"DEBUG: os.listdir(PAGES): {os.listdir(PAGES)}")

    ## Remove unnecessary files
    os.remove(os.path.join(CWD, '.gitignore'))


def customize(stored):
    
    ## Copying favicon
    shutil.move(os.path.join(stored, 'favicon.ico'), CWD)

    ## Writing _config.yml
    REPO = os.environ['GITHUB_REPOSITORY'].split('/')[1]
    with open(os.path.join(CWD, '_config.yml'), 'w') as f: f.write(
        f"title: {REPO}\n"
        f"desc: {REPO} documentation\n"
        f"author: {os.environ['NICS_INPUT_AUTHOR']}\n"
        f"google_analytics_tracking_id: {os.environ['NICS_INPUT_GATID']}\n"
        f"nics_ver: {os.environ['GHACTION_REF']}\n"
        
        f"baseurl: /{REPO}\n"
        f"url: https://{os.environ['GITHUB_ACTOR']}.github.io\n"
        
        'include: [_sass]\nsass: {style: compact, sass_dir: _sass}'
    )
    print('vvvvvvvvvvvvvvvv _config.yml vvvvvvvvvvvvvvvv')
    with open(os.path.join(CWD, '_config.yml'), 'r') as f: print(f.read())
    print('^^^^^^^^^^^^^^^^ _config.yml ^^^^^^^^^^^^^^^^')

    ## Rendering the pages
    PAGES = os.path.join(stored, 'pages')
    for md in os.listdir(PAGES):
        md_pth = os.path.join(PAGES, md)

        ## Read
        with open(md_pth, 'r') as f:
            md_content = f.read()

        ## Write
        with open(os.path.join(CWD, 'pages', md), 'w') as f:
            
            TITLE = md[:-3]
            PERMALINK = ''
            for char in TITLE:
                if re.match(r'[a-zA-Z0-9]', char):
                    PERMALINK += char.lower()
                else:
                    PERMALINK += '-'

            ## checks
            if re.search(r'-{2,}', PERMALINK):
                print(f"WARNING: Two or more consecutive hyphens found in this URL {repr(PERMALINK)}; this may not be the one you intended.")
            
            ## Write
            f.write(
                "---\n"
                "layout: main\n"
                f"title: {TITLE}\n"
                f"permalink: /{PERMALINK}\n"
                "---\n\n"
                + md_content
            )

def compile():

    ## Store the nics_dir files inside a temporary folder
    stored = store()
    print(f"DEBUG: os.listdir(stored): {os.listdir(stored)}")

    ## Cleanup
    print(f"DEBUG: before: os.listdir(CWD): {os.listdir(CWD)}")
    shutil.rmtree(CWD)
    print(f"DEBUG: after: os.listdir(CWD): {os.listdir(CWD)}")

    ## Prepare
    prepare()
    print(f"DEBUG: after prepare: os.listdir(CWD): {os.listdir(CWD)}")

    ## Customize
    customize(stored)
    print(f"DEBUG: after customize: os.listdir(CWD): {os.listdir(CWD)}")
    print(f"DEBUG: after customize: os.listdir(pages): {os.listdir(os.path.join(CWD, 'pages'))}")
