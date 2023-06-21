import os

from mykit.kit.utils import printer


def run(docs, target):
    """
    ## Params
    - `docs`: the docs/ bundle
    - `target`: the branch
    """

    printer(f'DEBUG: docs: {repr(docs)}.')
    printer(f'DEBUG: target: {repr(target)}.')

    printer(f'DEBUG: os.path.isdir(docs): {os.path.isdir(docs)}.')
    printer(f'DEBUG: os.path.isdir(target): {os.path.isdir(target)}.')

    printer(f'DEBUG: os.listdir(docs): {os.listdir(docs)}.')
    printer(f'DEBUG: os.listdir(target): {os.listdir(target)}.')

    for i in os.walk(docs):
        print(i)