from mojang import MojangAPI

import requests, json

def getMCPlayerData(username):
    uuid = MojangAPI.get_uuid(username)

    if not uuid:
        return False

    profile = MojangAPI.get_profile(uuid)
    return profile

def getMCPlayerData_old(inp):
    res = requests.get("https://playerdb.co/api/player/minecraft/{}".format(inp))

    return json.loads(res.content.decode("utf8"))

if __name__ == "__main__":
    u1 = "q"
    u2 = "Qazaroth"

    acc1 = getMCPlayerData(u1) or "Invalid account"
    acc2 = getMCPlayerData(u2)
    
    print("{} : {}".format(u1, acc1))
    print("{} : {}".format(u2, acc2))