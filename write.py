import sys
import logging
import git
import github
from github import Github
from git import Repo

#a=2
#b=2
a=int(input("enter value: "))
b=int(input("enter value: "))
if a+b>=4:
    def log_a():
        logging.basicConfig(filename='logname',
                                filemode='a',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                #format='%(message)s',
                                datefmt='%H:%M:%S',
                                level=logging.DEBUG)
    
        logging.info("{} th Running Urban Planning {}".format(a,b))
        logging.info("test")
        print (logging.info)
    log_a()
    print("true")
else:
    print ("false")

def git_push():
    #try:
    repo_dir = 'antu'
    g = Github("foysalrahman", "password")
    Repository = g.get_user().get_repo('antu')
    file_list = [
        'logname'
    ]
    commit_message = 'Add log'
    Repository.index.add(file_list)
    Repository.index.commit(commit_message)
    origin = repo.remote('origin')
    origin.push()
    #except:
    #    print('Some error occured while pushing the code2')    

git_push()


