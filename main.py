from config import *

from FileHandler import FileHandler

import json, os, requests

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


def getMCPlayerData(inp):
    res = requests.get("https://playerdb.co/api/player/minecraft/{}".format(inp))

    return json.loads(res.content.decode("utf8"))

def listWhitelistData(whData):
    clear()
    print("Format: Username - UUID")

    if whData and len(whData) > 0:
        for i in whData:
            uuid = i.get("uuid", None)
            name = i.get("name", None)

            if uuid == "":
                uuid = "Not specified"

            print("{} - {}".format(name, uuid))
    else:
        print("No one whitelisted.")

def addToWhitelist(whData):
    clear()
    addMore = True
    data = []

    if whData and len(whData) > 0:
        for i in whData:
            uuid = i.get("uuid", None)
            name = i.get("name", None)

            data.append({"uuid": uuid, "name": name})

    while addMore:
        clear()
        print("""
        Q in any of the input to stop.""")
        username = input("Username of Player you want to add (Case Sensitive): ")

        if username.lower() == "q":
            addMore = False
            break
        
        if checkUUID:
            uuid = input("UUID of Player you want to add (Leave blank if unknown): ")

            if uuid.lower() == "q":
                addMore = False
                break

            if len(uuid) > 0:
                uuidList = uuid.split("-")

                if len(uuidList) >= 5:
                    a = getMCPlayerData(uuid)

                    b = a["data"]
                    c = b["player"]
                    d = c["username"]
                    e = c["id"]
                        
                    if username != d or uuid != e:
                        print("Either UUID or Username is incorrect!")
                        break

            rawBody = getMCPlayerData(username)
            body = rawBody["data"]

            bodyPlayerData = body["player"]
            bodyID = bodyPlayerData["id"]
            uuid = bodyID
        else:
            uuid = ""

        toContinue = input("Continue adding more players? (Y/N) ")
        toContinue = toContinue.lower()

        data.append({"uuid": uuid, "name": username})

        addMore = toContinue == "y"

    print("Updating \"{}\" if there are any changes made.".format(whitelistFile))
    fileHandler.writeFile(whitelistFile, json.dumps(data))

def cli():
    print("""
        What would you like to do?
        \n0 - Exit
        \n1 - Fetch current whitelist data
        \n2 - Add to whitelist
        \n3 - Remove from whitelist
        """)
    choice = input()

    try:
        choice = int(choice)
    except:
        choice = 1

    whData = getWhitelistData()
    if choice == 1:
        listWhitelistData(whData)
    elif choice == 2:
        addToWhitelist(whData)
    elif choice == 3:
        listWhitelistData(whData)

        if whData and len(whData) > 0:
            uname = input("Who do you want to remove from whitelist? (Accepts either Username or UUID) ")

            data = []
            uuids = []
            names = []

            for i in whData:
                uuid = i.get("uuid", None)
                name = i.get("name", None)

                uuids.append(uuid)
                names.append(name)

            if uname in uuids or uname in names:
                for i in whData:
                    uuid = i.get("uuid", None)
                    name = i.get("name", None)

                    if name != uname and uuid != uname:
                        data.append(i)
            else:
                print("Invalid player {}.".format(uname))
    else:
        exit()

if __name__ == "__main__":
    cli()