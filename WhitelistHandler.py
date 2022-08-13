from config import *
from FileHandler import FileHandler
from Utils import clear
from MCAPI import *

import json

class WhitelistHandler:
    def __init__(self) -> None:
        self.__fileHandler = FileHandler()

        fileData = self.__fileHandler.readFile(whitelistFile)
        if fileData:
            self.__whitelist = json.loads(fileData)

    def getWhitelistData(self, raw=False):
        fileData = self.__fileHandler.readFile(whitelistFile)

        if not fileData:
            return None

        self.__whitelist = json.loads(fileData)
        
        if not raw:
            return json.loads(fileData)

        return fileData

    def listWhitelistData(self):
        whData = self.getWhitelistData()
        self.__whitelist = whData
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

    def removeFromWhitelist(self, username=""):
        newWhitelist = []

        if username == "":
            return False

        for i in self.__whitelist:
            uuid = i.get("uuid", None)
            name = i.get("name", None)
            
            if username != name:
                newWhitelist.append(i)

        self.__whitelist = newWhitelist
        return True

    def addToWhitelist(self, username="", uuid=""):
        if username == "" and uuid == "":
            return False

        if checkPlayer:
            plrBodyRaw = getMCPlayerData(username)
            code = plrBodyRaw.get("code", None)

            if code != "player.found":
                return False

            plrDataRaw = plrBodyRaw["data"]
            plrData = plrDataRaw["player"]
            plrUsername = plrData["username"]
            plrUUID = ""

            if checkUUID:
                plrUUID = plrData["id"]
                uuidList = uuid.split("-")

                if len(uuidList) >= 5:
                    if uuid != plrUUID:
                        return False
            
            self.__whitelist.append({"uuid": plrUUID, "name": plrUsername})
        else:
            self.__whitelist.append({"uuid": uuid, "name": username})
            
        return True

    def updateWhitelist(self):
        self.__fileHandler.writeFile(whitelistFile, json.dumps(self.__whitelist))