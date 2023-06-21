import os

from mykit.kit.utils import printer


def run(input, output):
    """
    ## Params
    - `input`:
    - `output`:
    """

    printer(f'DEBUG: input: {repr(input)}.')
    printer(f'DEBUG: output: {repr(output)}.')

    printer(f'DEBUG: os.path.isdir(input): {os.path.isdir(input)}.')
    printer(f'DEBUG: os.path.isdir(output): {os.path.isdir(output)}.')

    printer(f'DEBUG: os.listdir(input): {os.listdir(input)}.')
    printer(f'DEBUG: os.listdir(output): {os.listdir(output)}.')