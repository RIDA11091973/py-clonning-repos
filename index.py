import os, sys
import errno
from git import Repo
# Description:  This script will clone multiple source code repositories into a single directory
# If cloning via SSH, use the following link to enter pass phrase once:
# https://stackoverflow.com/questions/10032461/git-keeps-asking-me-for-my-ssh-key-passphrase 

# Generates progress bar for visual completion of clone
# https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = "=" * filled_len + "-" * (bar_len - filled_len)

    sys.stdout.write("[%s] %s%%%s\r" % (bar, percents, status))
    sys.stdout.flush()

# Creates a directory using the prompted name.  
# If the directory name is not unique, it will prompt the user to update the name accordingly
def create_folder(name):
	try:
	    os.mkdir(name)
	    return name
	except OSError as e:
	    if e.errno == errno.EEXIST:
	    	print('A directory named "' + name + '" already exists.  Please enter a unique directory name: ')
	        name = raw_input()
	        return create_folder(name)
	    else:
	        raise

directory_name = create_folder(raw_input('Enter a directory name: '))

# Comma delimited list of strings.  Add repositories here!
# i.e, repo_list = ['git://URL1', 'git://URL2', 'git://URL3']
repo_list = []

print('Cloning repositories to directory "'+ directory_name +'". Please wait...')
num_repos = len(repo_list)
for idx, repo in enumerate(repo_list):
    progress(idx + 1, num_repos)
    folder_name = repo.split('/')[-1]
    Repo.clone_from(repo, directory_name + '/' + folder_name.split('.git')[0])
print('\nSuccessfully cloned ' + str(len(repo_list)) + ' repositories!')