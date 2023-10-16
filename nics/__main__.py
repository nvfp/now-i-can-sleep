import os,sys;sys.path.append(os.environ['GITHUB_ACTION_PATH'])
print(os.listdir(os.environ['GITHUB_ACTION_PATH']))
from nics import main
if __name__=='__main__':main()