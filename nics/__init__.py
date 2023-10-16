import os

from .core import engine


NICS_DIR = os.environ['NICS_DIR']


def main():

    print(NICS_DIR)

    engine()
