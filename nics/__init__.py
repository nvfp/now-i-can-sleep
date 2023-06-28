import argparse

from .constants import __version__, SOFTWARE_DIST_NAME
from .wizard import run as run_init
from .compile import run as run_compile


def main():

    psr = argparse.ArgumentParser(
        prog=SOFTWARE_DIST_NAME,
        usage=(
            '\n'
            '└─ %(prog)s init'
        ),
        formatter_class=argparse.RawTextHelpFormatter  # to use line breaks (\n) in the help message
    )
    psr.add_argument(
        '-v', '--version', action='version', version=f'%(prog)s-{__version__}',
        help='show app\'s version then exit'
    )
    subpsr = psr.add_subparsers(dest='cmd')

    ## command 'init'
    subpsr.add_parser('init', help='')

    ## command '_compile' (that users shouldn't run)
    c = subpsr.add_parser('_compile', help='')
    c.add_argument('container')
    c.add_argument('dock')

    args = psr.parse_args()

    if args.cmd == 'init':
        run_init()
    elif args.cmd == '_compile':
        run_compile(args.container, args.dock)