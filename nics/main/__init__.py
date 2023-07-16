import argparse

from nics.main.constants import __version__
from nics.main.cmd_init import run as run_init
from nics.main.cmd_upgrade import run as run_upgrade


def main():

    parser = argparse.ArgumentParser(
        usage=(
            '\n'
            '├─ Run `nics init`   : Set up NICS environment\n'
            '└─ Run `nics upgrade`: Reconfigure NICS environment'
        ),
        formatter_class=argparse.RawTextHelpFormatter  # to use line breaks (\n) in the help message
    )
    parser.add_argument('-v', '--version', action='version', version=f'nics-{__version__}', help='show software version')
    parser.add_argument('cmd', choices=['init', 'upgrade'], help=argparse.SUPPRESS)  # `help=argparse.SUPPRESS` to hide the default help message

    args = parser.parse_args()

    if args.cmd == 'init':
        run_init()
    elif args.cmd == 'upgrade':
        run_upgrade()