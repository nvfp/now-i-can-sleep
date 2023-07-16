import os


def ensure_a_git_repo(dir_path):

    if not os.path.isdir(dir_path):
        raise NotADirectoryError(f'Not a dir: {repr(dir_path)}')

    if '.git' not in os.listdir(dir_path):
        raise NotADirectoryError(f'.git folder not found in {repr(dir_path)}.')