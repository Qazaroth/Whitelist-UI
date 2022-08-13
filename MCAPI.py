import requests, json

def getMCPlayerData(inp):
    res = requests.get("https://playerdb.co/api/player/minecraft/{}".format(inp))

    return json.loads(res.content.decode("utf8"))