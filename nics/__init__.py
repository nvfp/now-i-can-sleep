import os

from .core import engine


NICS_DIR = os.path.join(os.environ['GITHUB_WORKSPACE'], os.path.abspath(os.path.normpath(os.environ['NICS_DIR'])))


def main():

    print(NICS_DIR)
    print('---')
    print(os.listdir(NICS_DIR))

    engine()
