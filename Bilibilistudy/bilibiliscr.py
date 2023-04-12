import requests
import  json
import time

data={}

with open("constants.json",encoding='utf8') as f:
    regions = json.load(f)

for rid,regions in regions.items():
    print(rid,regions)
    #resp = requests.get(f"https://https://api.bilibili.com/x/web-interface/ranking/v2?rid={rid}") 热门排名
    resp = requests.get(f"https://api.bilibili.com/x/web-interface/ranking/region?day=7&original=0&rid={rid}")
    d = resp.json()
    if d['code'] == 0:
        data[rid] = {"region" : regions, "data":d['data']}
    time.sleep(0.5)

with open('data.json','w',encoding='utf8') as f:
    json.dump(data,f)