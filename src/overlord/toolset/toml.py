import tomllib

def loadFile(tomlpath):

    data = None
    
    with open(tomlpath, "rb") as file:
        data = tomllib.load( file )

    return data