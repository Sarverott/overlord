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
#
paracite = Overlord(os.getcwd())
#
#
print(paracite, paracite.config["self"]["configPath"])



print(paracite.repoPath)

paracite.infectRepo(paracite.repoPath)

print(paracite.listHooks(paracite.repoPath))
