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
            f.write("numbers are {} and {}".format(a,b)+"\n")
    write_a()
    print("true")
else:
    print ("false")

PATH_OF_GIT_REPO = r'/home/frahman/python/.git/'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
#try:
    repo = Repo(PATH_OF_GIT_REPO)
    print(repo)
    file_list = [
    'report.txt'
    ]
    repo.git.add(update=True)
    repo.git.add(file_list)
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.push()
    #except:
     #   print('Some error occured while pushing the code')
git_push()    