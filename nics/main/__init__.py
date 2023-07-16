import argparse

from mykit.kit.utils import printer

from nics.main.constants import __version__
from nics.main.wizard import run as run_init
from nics.main.upgrade import run as run_upgrade
from nics.main.compile import run as run_compile


def main():
    printer(f'INFO: Running NICS ({__version__}).')

    psr = argparse.ArgumentParser(
        prog='nics',
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

    ## The 'init' command
    subpsr.add_parser('init', help=argparse.SUPPRESS)

    ## The 'upgrade' command
    subpsr.add_parser('upgrade', help=argparse.SUPPRESS)

    ## The '_compile' command (not to be run by users)
    c = subpsr.add_parser('_compile', help=argparse.SUPPRESS)
    c.add_argument('container')
    c.add_argument('dock')

    args = psr.parse_args()

    printer(f'INFO: Running {repr(args.cmd)} command.')
    if args.cmd == 'init':
        run_init()
    elif args.cmd == 'upgrade':
        run_upgrade()
    elif args.cmd == '_compile':
        run_compile(args.container, args.dock)