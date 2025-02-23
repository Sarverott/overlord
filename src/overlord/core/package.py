from pathlib import Path
import os


from toolset import toml

from core import route

def loadPackData(self):
    self.package = toml.loadFile(route.PyProject())



