import click
import json
#pip install GitPython

from git import Repo
from git.cmd import GitCommandError

MAXL=4096

repo = Repo("..")
results = []

#repo.git.rebase("--abort")
try:            
    repo.git.rebase("--abort")
except GitCommandError as e:
    #print(e)
    pass

def sample(a):
    alen = len(a)
    sample = a[0:min(alen,MAXL)]
    return dict(
        len = alen,
        sample = sample
    )


@click.command()
@click.argument('ref')
def evaluate_branch(ref): #return 0 - 1    
    return _evaluate_branch(ref)

def _evaluate_branch(ref): #return 0 - 1    
    # checkout ref
    branches = repo.git.branch("-r","--all","--contains", ref)
    aref = repo.commit(ref)

    repo.head.reference = aref
    repo.head.reset(index=True, working_tree=True)



    error = ""
    
    try:
        repo.git.rebase("upstream/master")
    except GitCommandError as e:
        error = str (e)
    except Exception as e:
        error = str(e)
    print(json.dumps(dict( ref=ref,
                       diff=sample(repo.git.diff("upstream/master")),
                           rebase_error=sample(error),
                           branches=sample(branches),
                           
                          )
                     ),
          
          )
    #repo.git.commit("")
    try:            
        repo.git.rebase("--abort")
    except GitCommandError as e:
        #print(e)
        pass
        
    # rebase changes and look for errors/merge
    # run install
    # lint
    # look at changes from master
    # evaluate new files vs old files
    # modification of existing code, quality
    # introduction of new code, quality
    # introduction of new libraries, functions, packages, instructions
    # execution of new instructions vs old, compare runtime profiles
    # static analysis : ast node historgram, bytecode histogram, module and funciton sizes and counts,
    # compare internals to baseline
    # compare files changes against baseline and test individual file changes or groups of changes
    # strace, ltrace, tcpdump, mitmproxy
    # turn on all logging via modificaitons to base libraries
    # Running docker files to build and test -- 
    # Running docker compose files
    # Running code on existing docker image build
    # capture errors
    return 0

            
if __name__ =="__main__":
    evaluate_branch()
