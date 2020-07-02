

import requests

from bs4 import BeautifulSoup
from pymongo import MongoClient

import pandas as pd
import json

mongo_client = MongoClient()
db = mongo_client.get_database('premier league')
collection = db.get_collection('data')

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/85.0.134 Chrome/79.0.3945.134 Safari/537.36',
          'authority': 'footballapi.pulselive.com',
          'method': 'GET',
          'path': '/football/stats/ranked/players/hit_woodwork?page=0&pageSize=20&compSeasons=274&comps=1&compCodeForActivePlayer=EN_PR&altIds=true',
          'scheme': 'https',
          'accept': '*/*',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'origin': 'https://www.premierleague.com',
          'referer': 'https://www.premierleague.com/stats/top/players/hit_woodwork',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'cross-site'}
r = requests.get(url,headers = header)
print(r.status_code)
soup = BeautifulSoup(r.text,'html.parser')

data = json.loads(r.text)
print(data)
collection.insert_many(data)