from mojang import MojangAPI

import requests, json

def getMCPlayerData(username):
    uuid = MojangAPI.get_uuid(username)
    returnVal = {"code": "player.found", "message": "Successfully found player by given ID.", "data": {"player": {}}}

    if not uuid:
        return {"code": "player.invalid", "message": "User not found by given ID"}

    profile = MojangAPI.get_profile(uuid)

    returnVal["code"] = "player.found"
    returnVal["message"] = "Successfully found player by given ID."

    data = returnVal["data"]
    player = data["player"]

    player["meta"] = {"name_history": []}
    player["meta"]["name_history"] = [{"name": profile.name}]
    player["username"] = profile.name
    player["id"] = player["raw_id"] = uuid
    player["avatar"] = "https://crafthead.net/avatar/{}".format(uuid)

    returnVal["data"]["player"] = player
    returnVal["success"] = True

    return returnVal

def getMCPlayerData_old(inp):
    res = requests.get("https://playerdb.co/api/player/minecraft/{}".format(inp))

    return json.loads(res.content.decode("utf8"))

if __name__ == "__main__":
    u1 = "Qazaroth"
    u2 = "Qazaroth"

    acc1 = getMCPlayerData(u1) or "Invalid account"
    acc2 = getMCPlayerData_old(u2)
    
    print("{} : {}".format(u1, acc1))
    print("{} : {}".format(u2, acc2))