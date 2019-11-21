import sys
import logging
import git
import github
from git import Repo
from github import Github
from git import Repo

#a=2
#b=2
a=int(input("enter value: "))
b=int(input("enter value: "))
if a+b>=4:
    def write_a():
        with open("report.txt","a") as f:
            f.write("numbers are{} and {}".format(a,b))
    write_a()
    print("true")
else:
    print ("false")


#PATH_OF_GIT_REPO = r'https://github.com/foysalrahman/antu.git'  # make sure .git folder is properly configured
#COMMIT_MESSAGE = 'comment from python script'

repo_dir = 'antu'
g = Github("foysalrahman", "Antu@0124")
Repository = g.get_user().get_repo('antu')
file_list = [
        'logname'
]
commit_message = 'Add log'
Repository.index.add(file_list)
Repository.index.commit(commit_message)
origin = repo.remote('origin')