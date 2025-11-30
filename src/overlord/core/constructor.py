import git
import os

# from . import *


from . import config
from . import package

# from . import getArguments
from . import inject
from . import route

# from dataclasses import dataclass


class Overlord:
    paths = route

    listHooks = inject.listHooks
    loadConfig = config.load
    infectRepo = inject.infectRepo
    loadPackData = package.loadPackData

    gitDesc = inject.upwriteDescription

    def createCraftStorage():
        os.mkdir()

    def __init__(self, projectPath):
        # self.path = Path(__file__).parent.parent.parent.resolve()
        self.repoPath = projectPath
        self.loadConfig(projectPath)
        self.loadPackData()

        self.gitDesc()


# print(paracite.repo)
