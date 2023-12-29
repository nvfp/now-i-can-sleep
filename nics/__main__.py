# import os
# import sys
# sys.path.append(os.environ['GITHUB_ACTION_PATH'])

import os

from nics.core.validations import validations
from nics.core.compile import compile


def main():

    IPT_SRC = os.environ['IPT_SRC']
    IPT_AUTHOR = os.environ['IPT_AUTHOR']
    IPT_ANALYTICS = os.environ['IPT_ANALYTICS']
    IPT_ACTION_REF = os.environ['IPT_ACTION_REF']

    ## Note: CWD_USER is the one for the user, while CWD_ACTION is for the NICS.
    CWD_USER = os.environ['GITHUB_WORKSPACE']
    CWD_ACTION = os.environ['GITHUB_ACTION_PATH']

    ## The directory that containing the NICS stuff.
    NICS_DIR = os.path.abspath(os.path.join(CWD_USER, os.path.normpath(IPT_SRC)))
    print(f"DEBUG: NICS_DIR: {repr(NICS_DIR)}.")

    ## Validating...
    validations(NICS_DIR)

    ## Compile
    compile(NICS_DIR)


if __name__ == '__main__':
    main()
