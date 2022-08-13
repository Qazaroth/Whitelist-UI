from config import whitelistFile
from pathlib import Path

from FileHandler import FileHandler
# from InquirerPy import inquirer

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


if __name__ == "__main__":
    print("What would you like to do?\n0 - Exit\n1 - Fetch current whitelist data\n2 - Update whitelist")
    # choice = inquirer.select(
    #     message="What would you like to do?\n1 - Fetch current whitelist data\n2 - Update whitelist",
    #     choices=[1, 2]
    # ).execute()
    choice = input()

    try:
        choice = int(choice)
    except:
        choice = 1

    whData = getWhitelistData()
    if choice == 1:
        clear()
        print("Format: Username - UUID")

        for i in whData:
            uuid = i.get("uuid", None)
            name = i.get("name", None)
            print("{}: {}".format(name, uuid))
    elif choice == 2:
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
            username = input("Username of Player you want to add (Case Sensitive): ")
            uuid = input("UUID of Player you want to add (Leave blank if unknown): ")

            if len(uuid) > 0:
                uuidList = uuid.split("-")

                if len(uuidList) >= 5:
                    res1 = requests.get("https://playerdb.co/api/player/minecraft/{}".format(uuid))
                    body1 = json.loads(res1.content.decode("utf8"))

                    if res:
                        bodyData = body1["data"]
                        bodyPlayerData = bodyData["player"]
                        bodyUsername = bodyPlayerData["username"]
                        bodyID = bodyPlayerData["id"]
                       
                        if username != bodyUsername or uuid != bodyID:
                            print("Either UUID or Username is incorrect!")
                            break

            res = requests.get("https://playerdb.co/api/player/minecraft/{}".format(username))
            body = json.loads(res.content.decode("utf8"))["data"]

            #print(body)

            bodyPlayerData = body["player"]
            bodyUsername = bodyPlayerData["username"]
            bodyID = bodyPlayerData["id"]
            uuid = bodyID

            toContinue = input("Continue adding more players? (Y/N) ")
            toContinue = toContinue.lower()

            data.append({"uuid": uuid, "name": username})

            addMore = toContinue == "y"

        print("Updating \"{}\"...".format(whitelistFile))
        fileHandler.writeFile(whitelistFile, json.dumps(data))
    else:
        exit()