import requests
import random
import json


gameid = 6284583030
def guid_scraper():
    guids = []
    for i in range(3):
        page = random.randint(3000, 3500) + i
        data = requests.get(f'https://www.roblox.com/games/getgameinstancesjson?placeId={gameid}&startIndex={page}', cookies=json.load(open(r'config.json'))).json()
        for server in data['Collection']:
            guids.append(server['Guid'])
    return guids

for a in guid_scraper():
    print(a)
