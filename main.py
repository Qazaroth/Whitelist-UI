from config import whitelistFile
from pathlib import Path

import json

if __name__ == "__main__":
    whitelistPath = Path(whitelistFile)

    if whitelistPath.exists():
        whFile = open(whitelistFile, "r")
        whRawData = whFile.read()
        whData = json.loads(whRawData)

        for i in whData:
            uuid = i.get("uuid", None)
            name = i.get("name", None)
            print("{}: {}".format(uuid, name))