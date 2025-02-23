import configparser
from pathlib import Path
import json

from core import route

#import venv
#import zipapp
#import io

def load(self, localConfig):

    configPath = route.DefaultConfig()

    with open(configPath) as struct:
        configData = json.loads(struct.read())

    self.config = configparser.ConfigParser()

    self.config.read_dict(configData)

    return [configPath, configData, self.config]



