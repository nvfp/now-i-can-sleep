import json
import os
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


def customize(stored):
    
    ## Copying favicon
    shutil.move(os.path.join(stored, 'favicon.ico'), CWD)

    ## Writing _config.yml
    with open(os.path.join(stored, 'settings.json'), 'r') as fp:
        SETTINGS = json.load(fp)
    with open(os.path.join(CWD, '_config.yml'), 'w') as f: f.write(
        f"title: {Proto}"
        f"desc: {My test desc}"
        f"author: {}"
        f"google_analytics_tracking_id: {}"
        f"nics_ver: {3.0.0}"
        f"baseurl: {/now-i-can-sleep}"
        f"url: {https://nvfp.github.io}"
        'include: [_sass]\nsass: {style: compact, sass_dir: _sass}'
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
