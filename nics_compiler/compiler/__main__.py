import os
import sys

## To make Python recognize `nics` and `nics_compiler` dirs
project_root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(f'DEBUG: project_root_dir: {repr(project_root_dir)}.')
sys.path.append(project_root_dir)

from nics_compiler.compiler import main


if __name__ == '__main__':
    main()