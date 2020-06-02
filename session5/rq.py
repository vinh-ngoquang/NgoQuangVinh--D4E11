import requests
from pymongo import MongoClient
mongo_client = MongoClient()
db = mongo_client.get_database('d4e11')
collection = db.get_collection('police_call')
requests.get('https://data.baltimorecity.gov/resource/xviu-ezkt.json')
client = requests.get('https://data.baltimorecity.gov/resource/xviu-ezkt.json')
data = client.json()
collection.insert_many(data)

total_false_call = collection.count({'priority': 'Non-Emergency'})
total_call = collection.count()
print(total_false_call, total_call)
print(total_false_call*100/total_call)



all_districts = collection.distinct('district')
print(all_districts)


count_call_by_district = {}
for district in all_districts:
    count_call_by_district[district] = collection.count({'district':district})
print(count_call_by_district)

max = 0
name = ''
for key in count_call_by_district:
    if count_call_by_district[key] > max:
        max = count_call_by_district[key]
        name = key
print(name, max)
