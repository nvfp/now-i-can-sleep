import os

# from .core.validations import validations
# from .core.compile import compile


NICS_DIR = os.path.join(os.environ['GITHUB_WORKSPACE'], os.path.abspath(os.path.normpath(os.environ['NICS_DIR'])))


def main():

    print(f"os.environ['GITHUB_ACTION_REF']: {os.environ['GITHUB_ACTION_REF']}")

    ## Validating...
    # validations(NICS_DIR)

    # ## Compile
    # compile(NICS_DIR)
