import git
from pathlib import Path
import os
import json

from . import config
from . import package
#from . import getArguments
#from . import inject
from . import route

import hashlib


def RecordHooks(repopath):
    hooksPath = route.GitHooksDir(repopath)

    #hooksdir = Path(repopath)

    hooks = os.listdir(hooksPath)
    hooksRecord = dict()
    for hook in hooks:
        with open( os.path.join(hooksPath, hook), "rb") as hookContent:
            hooksRecord[hook] = hashlib.file_digest(hookContent, "sha512")
            hooksRecord[hook] = hooksRecord[hook].hexdigest()
            hooksRecord[hook] = str(hooksRecord[hook])

    with open( Path(__file__).parent / "standard_githook_hash.json", "w+" ) as record:
        record.write(json.dumps(hooksRecord, indent=4))
    return (hooksRecord)


def RecordMeetedHooks(repopath):
    
    hooksPath = route.GitHooksDir(repopath)

    #hooksdir = Path(repopath)

    hooks = os.listdir(hooksPath)
    hooksRecord = dict()
    for hook in hooks:
        with open( os.path.join(hooksPath, hook), "r") as hookContent:
            hooksRecord[hook] = hookContent.read()
            
    with open( os.path.join(hooksPath, ".backup_hooks_entumbed.json"), "w+" ) as record:
        record.write(json.dumps(hooksRecord, indent=4))
    return (
        str(repopath), 
        str(os.path.join(repopath, "data", "githooks.lastrepo.json"))
        #str(Path(__file__).parent / "standard_githook_hash.json")
    )



def RecordStandardHooks(repopath):
    
    hooksPath = route.GitHooksDir(repopath)

    #hooksdir = Path(repopath)

    hooks = os.listdir(hooksPath)
    hooksRecord = dict()
    for hook in hooks:
        with open( os.path.join(hooksPath, hook), "r") as hookContent:
            hooksRecord[hook] = hookContent.read()
            
    with open( os.path.join(repopath, "data", "standard_githooks.json"), "w+" ) as record:
        record.write(json.dumps(hooksRecord, indent=4))
    return (
        str(hooksPath), 
        str(os.path.join(repopath, "data", "standard_githooks.json")),
        str(Path(__file__).parent / "standard_githook_hash.json")
    )


def listHooks(self):
    hooksPath = route.GitHooksDir(route.OverlordDir())
    self.githooks = os.listdir(hooksPath)

def upwriteDescription(self):

    content = f"{self.package["project"]["name"]};\t {self.package["project"]["description"]}\n"
    lineLength = len(content)
    for (urllabel, repourl) in self.package["project"]["urls"].items():
        content = content + f"\n > {urllabel.upper()}: {repourl}"
    content = content + "\n\n" + ("-"*lineLength) + "\n\n"
    
    content = content + "see README.md"

    with open(route.GitDescription(self.repoPath), "w") as gitDesc:
        
        gitDesc.write(content)



def infectRepo(self, repopath):

    if( os.path.exists( repopath ) ):
        print("exist", repopath)
            
        self.repo=git.Repo( repopath )

            #print(  )
        hooksdir = route.GitHooksDir(repopath)
        print( hooksdir )
        hooks = os.listdir(hooksdir)

        hooks
        
                  
    else:
        
        print("not exist", repopath)
            