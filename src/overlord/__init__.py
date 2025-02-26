""" OVERLORD """

import sys

from . import module as mode_module
from . import execute as mode_execute
from . import service as mode_service
from . import document as mode_document
#from . import test as mode_test



__all__ = [
    "execute", 
    "module",
    "document",
#    "test",
    "service",
    "core",
    "commands",
    "methods",
    "routes",
    "services",
    "toolset"
]


def module(*args):
    return mode_module.exports(*args)

def execute(*args):
    return mode_execute.exports(*args)

def service(*args):
    return mode_service.exports(*args)

def document(*args):
    return mode_document.exports(*args)

#def test(*args):
#    return mode_test.exports(*args)


#
#
#
#import yaml
#
#from git import Repo

#import configparser
#
#from core.constructor import 
#from core.inject import RecordStandardHooks, RecordHooks, RecordMeetedHooks
#import json
#from pathlib import Path
#
#def insert(path):
#    Overlord
#
#
if __name__ == "__main__":
    execute(sys.argv)
else:
    module()
