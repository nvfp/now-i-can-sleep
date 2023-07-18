

def get_user_details():

    ## Intro
    print('Welcome to NICS!')
    
    class usr: ...

    usr.load = input('Enter the main branch name (e.g. master): ')
    usr.dock = input('Enter the documentation branch name (e.g. docs): ')
    usr.container = input('Enter the documentation folder name (e.g. docs): ')
    
    usr.author = input('Enter your name: ')
    usr.git_name = input('Enter your git username: ')
    usr.git_email = input('Enter your git email: ')
    
    usr.gh_username = input('Enter your GitHub username: ')
    usr.gh_repo_name = input('Enter this GitHub repository name: ')

    return usr