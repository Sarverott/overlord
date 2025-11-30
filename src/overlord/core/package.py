from pathlib import Path
import os

from . import config

# from . import package
# from . import getArguments
from . import inject
from . import route

from ..toolset import toml

# from core import route


def loadPackData(self):
    self.package = toml.loadFile(route.PyProject())
