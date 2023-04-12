import  json
import csv

data = {}

with open("data.json") as f:
    data = json.load(f)

with open("data_csv.csv","w",encoding='utf8') as csvfile:
    data_csv = csv.writer(csvfile)
    data_csv.writerow(['分区','播放数','投币数','收藏数','评论数','时长'])
    for d in data.values():
        if all(d['region'] in item['typename'] for item in d['data']):
            play = sum(item['play'] for item in d['data'])
            coins = sum(item['coins'] for item in d['data'])
            favorites = sum(item['favorites'] for item in d['data'])
            review = sum(item['review'] for item in d['data'])
            duration = sum(int(item['duration'].split(':')[0]) for item in d['data']) + sum(int(item['duration'].split(':')[1]) for item in d['data'])//60 # "5:22"
            data_csv.writerow([d['region'],play,coins,favorites,review,duration])