# DO NOT LEAVE ANY OF THE VARIABLES BELOW AS NONE OR EMPTY. IT WILL BREAK THE SYSTEM

# Path to server files
serverPath = "server"

timezone = "Asia/Singapore"

# Leave below as it is or "" if default
# Otherwise, change them to whatever you have renamed their file name to be.
whitelistFileName = ""
serverPropertiesFileName = "server.properties"

checkUUID = False
checkPlayer = True
enableLogging = False

# Toggles CLI mode or web interface mode. Default: Web Interface
isCLI = False

# Name of your minecraft server
logo="MC Server"

# Change the value of secret to anything you want, just do not share it or expose it
secret = "verysecretkey"

# Port for the web server to be running on. Default: 25585
# Set it as None to use default port
webPort = None

# DO NOT CHANGE ANYTHING HERE
import os
whitelistFile = ""
serverPropertiesFile = ""

files = {"whitelist": "whitelistFile", "server": "serverPropertiesFile"}

for f in os.listdir(serverPath):
    filePath = "{}\\{}\\{}".format(os.getcwd(), serverPath, f)
    l = f.split(".")
    
    fnList = l[0].split("_")

    if fnList[-1].lower() != "backup":
        v = files.get(l[0], None)
        
        if v is not None:
            exec('{}="{}"'.format(v, filePath.replace("\\", "/")))
