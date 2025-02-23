import git
from pathlib import Path
import os
import json

from core import route

def listHooks(self, repopath):
    
    hooksPath = route.StandardHooks(route.OverlordDir())

    #hooksdir = Path(repopath)

    hooks = os.listdir(hooksPath)

    for hook in hooks:
        print(hook)
    with open( Path(__file__).parent / "StandardHooks.json", "w+" ) as record:
        record.write(json.dumps(hooks, indent=4))

def infectRepo(self, repopath):

    if( os.path.exists( repopath ) ):
        print("exist", repopath)
            
        self.repo=git.Repo( repopath )

            #print(  )
        hooksdir = Path(repopath)
        hooksdir = hooksdir / ".git" / "hooks"
        print( hooksdir )
        hooks = os.listdir(hooksdir)

        
                  
    else:
        
        print("not exist", repopath)
            