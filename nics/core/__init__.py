import os


## Working directory
WD = os.environ['GITHUB_WORKSPACE']

def engine():
    print(123, WD)
    print(456, os.listdir(WD))
