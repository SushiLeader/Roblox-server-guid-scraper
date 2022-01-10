import requests
import random
import json
import time
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

app = Flask(__name__)

guids = []
used_guids = []
resets = 0
def guid_scraper():
    global resets
    for i in range(3):
        page = random.randint(3000, 3500) + i
        data = requests.get(f'https://www.roblox.com/games/getgameinstancesjson?placeId=6284583030&startIndex={page}', cookies=json.load(open(r'config.json'))).json()
        for server in data['Collection']:
            guids.append(server['Guid'])
    resets = resets + 1
    print(f'reset timme : {resets}')

guid_scraper()
scheduler = BackgroundScheduler()
scheduler.add_job(func=guid_scraper, trigger="interval", seconds=10)
scheduler.start()


#API code
@app.route("/petsimx")
def home():
    global used_guids
    while True:
        obj = random.choice(guids)
        if obj not in used_guids:
            used_guids.append(obj)
            return obj

app.run(host='0.0.0.0', port=80)