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


#PATH_OF_GIT_REPO = r'/home/frahman/python'  # make sure .git folder is properly configured
#COMMIT_MESSAGE = 'comment from python script'

#repo_dir = 'antu'
#g = Github("antu0124@gmail.com", "Antu@0124")
#g = Github()
#Repository = g.get_user().get_repo('antu')
#Repository = g.get_user().get_repo(PATH_OF_GIT_REPO)
#print(Repository)
#file_list = [
#        'logname'
#]
#commit_message = 'Add log'
#Repository.index.add(file_list)
#pygit.add(file_list)
#Repository.index.commit(commit_message)
#origin = repo.remote('origin')

PATH_OF_GIT_REPO = r'/home/frahman/python'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        print(repo)
        #file_list = [
        #'report.txt'
        #]
        repo.git.add(update=True)
        #repo.git.add(file_list)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='master')
        origin.push()
    except:
        print('Some error occured while pushing the code')
git_push()    