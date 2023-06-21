import argparse
import os
import pkg_resources

from mykit.kit.utils import printer

from nics.compile import run as run_compile


try:
    __version__ = pkg_resources.get_distribution('nics').version
except pkg_resources.DistributionNotFound:
    ## this exception occurred during development (before the software installed via pip)
    __version__ = 'dev'


SOFTWARE_REPO = 'https://github.com/nvfp/now-i-can-sleep'
SOFTWARE_NAME = 'Now I Can Sleep'
SOFTWARE_DIST_NAME = 'nics'  # distribution name

ROOT_DIR_PTH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIST_DIR_PTH = os.path.join(ROOT_DIR_PTH, SOFTWARE_DIST_NAME)


def main():

    parser = argparse.ArgumentParser(
        prog=SOFTWARE_DIST_NAME,
        usage=(
            '\n'
            '├─ %(prog)s start\n'
            '├─ %(prog)s start step2\n'
            '├─ %(prog)s start step3\n'
            '└─ %(prog)s downl\n'
        ),
        formatter_class=argparse.RawTextHelpFormatter  # to use line breaks (\n) in the help message
    )

    ## version
    parser.add_argument(
        '-v', '--version', action='version', version=f'%(prog)s-{__version__}',
        help='show app\'s version then exit'
    )

    ## command parser
    subparsers = parser.add_subparsers(dest='cmd')

    ## start command
    start_parser = subparsers.add_parser('start', help='')
    start_parser.add_argument('arg1', type=int, help='')

    ## compile command (that users shouldn't run)
    compile_parser = subparsers.add_parser('_compile', help='')
    compile_parser.add_argument('input')
    compile_parser.add_argument('output')


    ## positional args
    # parser.add_argument(
    #     'cmd',
    #     choices=['start', 'update', '_compile'],
    #     help=argparse.SUPPRESS  # to hide the help message
    # )
    # parser.add_argument(
    #     'arg2',
    #     choices=[
    #         'step2', 'step3',
    #         ''
    #     ],
    #     nargs='?',
    #     help=argparse.SUPPRESS  # to hide the help message
    # )


    args = parser.parse_args()

    printer(f'INFO: running command {repr(args.cmd)}.')

    if args.cmd == '_compile':
        run_compile(args.input, args.output)