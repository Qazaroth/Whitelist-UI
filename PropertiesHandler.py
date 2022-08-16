from datetime import datetime
from utils.config import serverPropertiesFile, timezone
from FileHandler import FileHandler
from Utils import clear
from datetime import datetime

import pytz

months = ["Jan", "Feb", "Mar", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]

def parsePropertiesFile(rawData):
    if not rawData:
        return None

    data = rawData.splitlines()
    returnVal = {}

    for i in data:
        if i[0] != "#":
            iL = i.split("=")
            setting = iL[0]
            value = iL[1]

            if value.lower() not in ["false", "true"]:
                try:
                    value = int(value)
                except:
                    pass

            returnVal[setting] = value

    return returnVal or None

class PropertiesHandler:
    def __init__(self) -> None:
        self.__fileHandler = FileHandler()
        self.__properties = parsePropertiesFile(self.__fileHandler.readFile(serverPropertiesFile))

    def updateProperty(self, key, value):
        f = self.__properties.get(key, None)

        if f is not None:
            self.__properties[key] = value
            return True

        return False

    def updateProperties(self):
        propertyString = "#Minecraft server properties\n"
        # Weekday, 0 = Monday 6 = Sunday
        dt = datetime.now(pytz.timezone(timezone))
        day = days[dt.weekday()]

        m = dt.month - 2
        if m >= 0 and m < len(months):
            month = months[m]
        else:
            month = "You fucked up"

        date = dt.date()
        time = dt.time()

        propertyString += "#{} {} {} {}:{}:{} {} {}".format(
            day, month, date.day, 
            str(time.hour).zfill(2), str(time.minute).zfill(2), str(time.second).zfill(2),
            timezone, date.year)

        for key in self.__properties:
            value = self.__properties[key]

            propertyString += "\n{}={}".format(key, value)
        self.__fileHandler.writeFile(serverPropertiesFile, propertyString)

    def getProperties(self):
        self.__properties = parsePropertiesFile(self.__fileHandler.readFile(serverPropertiesFile))
        return self.__properties

if __name__ == "__main__":
    ph = PropertiesHandler()
    properties = ph.getProperties()

    ph.updateProperties()