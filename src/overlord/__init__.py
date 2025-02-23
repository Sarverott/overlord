#
#
#
#import yaml
#
#from git import Repo
import os 
#import configparser
#
from core.constructor import Overlord
from core.inject import RecordStandardHooks, RecordHooks
import json
#
paracite = Overlord(os.getcwd())
#
#
print(paracite, paracite.config["self"]["configPath"])

def printNice(data):
    print(json.dumps(data, indent=4))

print(paracite.repoPath)

paracite.infectRepo(paracite.repoPath)

printNice(RecordStandardHooks( paracite.repoPath))
printNice(RecordHooks(paracite.repoPath))

printNice(paracite.package)