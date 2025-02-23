
from pathlib import Path

def DefaultConfig():
    return Path(__file__).parent / "defaultConfig.json"


def OverlordDir():
    output = Path(__file__) # REPO:/src/overlord/core/packageData.py
    output = output.parent # REPO:/src/overlord/core/
    output = output.parent # REPO:/src/overlord/
    output = output.parent # REPO:/src/
    output = output.parent # REPO:/
    return output # return path


    #projectPath = overlordPypackPath()


def PyProject():
    return OverlordDir() / "pyproject.toml" # REPO:/packageData.py

def GitHooksDir(projectDir):
    return Path(projectDir) / ".git" / "hooks"

def GitDescription(projectDir):
    return Path(projectDir) / ".git" / "description"