from utils.config import serverPropertiesFile
from FileHandler import FileHandler
from Utils import clear

class PropertiesHandler:
    def __init__(self) -> None:
        self.__fileHandler = FileHandler()
        self.__properties = {}

        rawData = self.__fileHandler.readFile(serverPropertiesFile).splitlines()

        for data in rawData:
            if data[0] != "#":
                dataList = data.split("=")
                setting = dataList[0]
                value = dataList[1]

                if value.lower() == "false":
                    value = False
                elif value.lower() == "true":
                    value = True

                try:
                    value = int(value)
                except:
                    pass

                self.__properties[setting] = value

    def getProperties(self):
        return self.__properties

if __name__ == "__main__":
    ph = PropertiesHandler()

    print(ph.getProperties()["server-port"])