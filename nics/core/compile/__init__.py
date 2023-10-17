import os
import re
import shutil
import tempfile


CWD = os.environ['GITHUB_WORKSPACE']

TEMPLATE_DIR = os.path.join(os.environ['GITHUB_ACTION_PATH'], 'nics', 'template')


def store(nics_dir):
    DIR = tempfile.mkdtemp()
    shutil.move(nics_dir, DIR)

    ## The above operations will move nics_dir into DIR. Let's say the folder contains the
    ## documentation file named FOO. We want DIR/FOO, not just DIR. So we do the following below.
    FOLDER = os.listdir(DIR)[0]
    return os.path.join(DIR, FOLDER)


def prepare():
    
    ## Copy the template
    shutil.copytree(TEMPLATE_DIR, CWD)

    ## Remove the files that will be replaced soon
    os.remove(os.path.join(CWD, '_config.yml'))
    os.remove(os.path.join(CWD, 'favicon.ico'))

    ## Clear the pages/ folder
    PAGES = os.path.join(CWD, 'pages')
    shutil.rmtree(PAGES)
    os.mkdir(PAGES)

    ## Remove unnecessary files
    os.remove(os.path.join(CWD, '.gitignore'))


def customize(stored):
    
    ## Copying favicon
    shutil.move(os.path.join(stored, 'favicon.ico'), CWD)

    ## Writing _config.yml
    with open(os.path.join(CWD, '_config.yml'), 'w') as f: f.write(
        f"title: {os.environ['GITHUB_REPOSITORY']}\n"
        f"desc: {os.environ['GITHUB_REPOSITORY']} documentation\n"
        f"author: {os.environ['NICS_INPUT_AUTHOR']}\n"
        f"google_analytics_tracking_id: {os.environ['NICS_INPUT_GATID']}\n"
        f"nics_ver: {os.environ['GHACTION_REF']}\n"
        
        f"baseurl: /{os.environ['GITHUB_REPOSITORY'].split('/')[1]}\n"
        f"url: https://{os.environ['GITHUB_ACTOR']}.github.io\n"
        
        'include: [_sass]\nsass: {style: compact, sass_dir: _sass}'
    )

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

def compile(nics_dir):

    ## Store the nics_dir files inside a temporary folder
    stored = store(nics_dir)

    ## Cleanup
    shutil.rmtree(CWD)

    ## Prepare
    prepare()

    ## Customize
    customize(stored)
