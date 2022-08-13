from config import whitelistFile
from pathlib import Path

from FileHandler import FileHandler
# from InquirerPy import inquirer

import json, os

fileHandler = FileHandler()

def clear():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"

    os.system(command)


def getWhitelistData(raw=False):
    fileData = fileHandler.readFile(whitelistFile)

    if not fileData:
        return None
    
    if not raw:
        return json.loads(fileData)

    return fileData


if __name__ == "__main__":
    print("What would you like to do?\n1 - Fetch current whitelist data\n2 - Update whitelist")
    # choice = inquirer.select(
    #     message="What would you like to do?\n1 - Fetch current whitelist data\n2 - Update whitelist",
    #     choices=[1, 2]
    # ).execute()
    choice = input()

    try:
        choice = int(choice)
    except:
        choice = 1

    if choice == 1:
        whData = getWhitelistData()
        
        clear()
        print("Format: Username - UUID")

        for i in whData:
            uuid = i.get("uuid", None)
            name = i.get("name", None)
            print("{}: {}".format(name, uuid))
    # whData = getWhitelistData()
    
    # print(whData)
    # for i in whData:
    #     uuid = i.get("uuid", None)
    #     name = i.get("name", None)
    #     print("{}: {}".format(uuid, name))