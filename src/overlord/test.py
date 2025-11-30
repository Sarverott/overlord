#
#
#
# import yaml
#
# from git import Repo
import os

# import configparser
#
from core.constructor import Overlord
from core.inject import RecordStandardHooks, RecordHooks, RecordMeetedHooks
import json
from pathlib import Path

#
paracite = Overlord(os.getcwd())
#
#
print(paracite, paracite.config["self"]["configPath"])


def printNice(data):
    print(json.dumps(data, indent=4))


print(paracite.repoPath)

paracite.infectRepo(paracite.repoPath)

printNice(RecordStandardHooks(paracite.repoPath))
printNice(RecordHooks(paracite.repoPath))

# print(RecordMeetedHooks(input("path: ")))

printNice(paracite.package)


import configparser

# todo : void-physics
# pseudocode formal idea

base_overlord = {
    "darkpoint": {
        "values": "[BLANK]",
        "name": json.dumps(["overlord", "$"]),
        "type": json.dumps(["project", ""]),
        "operators": "[BLANK]",
        "read": json.dumps(["verbal comment", ""]),
        "opera": json.dumps(["verbal comment", ""]),
        "locate": json.dumps(["<[path]>", "//host", "@userspace", "::cloudscopal"]),
        "incidentions": "[BLANK]",
        "logs": "[BLANK]",
        "runners": "[BLANK]",
        "services": "[BLANK]",
        "containers": "[BLANK]",
        "domainability": "[BLANK]",
        "categories": "[BLANK]",
        "where": json.dumps(["*locate", ""]),
        "why": json.dumps([]),
        "what": json.dumps([]),
    },
    "bos": {
        "cat": "bos-use",
        "ID": "<bos-identifier>",
        "type": "project",
        "initial_NOW": "",
        "chronokey": "hash(CONTEXT.NOW)",
        "version": "0.3.0.0",
        "project-name": json.dumps(paracite.package["project"]["name"]),
        "project-info": json.dumps(paracite.package["project"]["description"]),
    },
    "setternet": {"cat": "org-sec", "coverable": "encrypted"},
    "about this project": {
        "cat": "info-data",
        "classes": "python, pip, package, publish",
        "state": "chaotical",
        "lastCommitHash": "gitCommitHash",
    },
    "repositories and releasing": {
        "cat": "dev-eng",
        "HEAD": "content",
        "header": "hash from head",
        "branch": "master",
    },
    "soc-med": {"x": "x"},
}


def Selfdefine():
    iniCreated = configparser.ConfigParser()

    iniCreated.read_dict(base_overlord)
    inipath = str(Path(paracite.repoPath) / ".space.ini")
    with open(inipath, "w") as bosFile:
        iniCreated.write(bosFile)


Selfdefine()
