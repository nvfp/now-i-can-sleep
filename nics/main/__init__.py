import argparse

from .constants import __version__, SOFTWARE_DIST_NAME
from .wizard import run as run_init
from .upgrade import run as run_upgrade
from .compile import run as run_compile


def main():

    psr = argparse.ArgumentParser(
        prog=SOFTWARE_DIST_NAME,
        usage=(
            '\n'
            '├─ Run `%(prog)s init`   : Set up NICS environment\n'
            '└─ Run `%(prog)s upgrade`: Reconfigure NICS environment'
        ),
        formatter_class=argparse.RawTextHelpFormatter  # to use line breaks (\n) in the help message
    )
    psr.add_argument(
        '-v', '--version', action='version', version=f'%(prog)s-{__version__}',
        help='show software version'
    )
    subpsr = psr.add_subparsers(dest='cmd', help=argparse.SUPPRESS)  # `help=argparse.SUPPRESS` to hide the help message

    ## command 'init'
    subpsr.add_parser('init', help=argparse.SUPPRESS)

    ## command 'upgrade'
    subpsr.add_parser('upgrade', help=argparse.SUPPRESS)

    ## command '_compile' (that users shouldn't run)
    c = subpsr.add_parser('_compile', help=argparse.SUPPRESS)
    c.add_argument('container')
    c.add_argument('dock')

    args = psr.parse_args()

    if args.cmd == 'init':
        run_init()
    elif args.cmd == 'upgrade':
        run_upgrade()
    elif args.cmd == '_compile':
        run_compile(args.container, args.dock)