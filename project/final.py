import requests
import pandas as pd
import json
from functools import reduce

criteria = [
    'clean_sheet',
    'goals_conceded',
    'saves',
    'penalty_save',
    'punches',
    'total_high_claim',
    'total_keeper_sweeper',
    'keeper_throws',
    'goal_kicks'
    ]
season_num = [274,210,79,54,42,27,22,21,20,19,18,17,16,15,14,13,12,11,10]
x = 0 #season_num
page_size = 1000
page_num = 0

# # general information:
for y in range(9):
    l = []
    url = f'https://footballapi.pulselive.com/football/stats/ranked/players/{criteria[y]}?page={page_num}&pageSize={page_size}&compSeasons={season_num[x]}&comps=1&compCodeForActivePlayer=EN_PR&altIds=true'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/85.0.134 Chrome/79.0.3945.134 Safari/537.36',
               'authority': 'footballapi.pulselive.com',
               'method': 'GET',
               'path': f'/football/stats/ranked/players/{criteria[y]}?page={page_num}&pageSize={page_size}&compSeasons={season_num[x]}&comps=1&compCodeForActivePlayer=EN_PR&altIds=true',
               'scheme': 'https',
               'accept': '*/*',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
               'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'origin': 'https://www.premierleague.com',
              'referer': 'https://www.premierleague.com/stats/top/players/goals',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'cross-site'}
    r = requests.get(url,headers = headers)
    print(f'crawling {criteria[y]} done!')
    data = json.loads(r.text)
    #print(data)
    for i in range(len(data['stats']['content'])):
        l.append([data['stats']['content'][i]['owner']['playerId'],data['stats']['content'][i]['value']])
        #print(l)
    exec(f"{criteria[y]} = pd.DataFrame(l,columns = ['player_id','{criteria[y]}'])")


goalkeeper = [clean_sheet,goals_conceded,saves,penalty_save,punches,total_high_claim,total_keeper_sweeper,keeper_throws,goal_kicks]
goolkeeper = reduce(lambda x, y: pd.merge(x, y, left_on = 'player_id',right_on = 'player_id', how = 'outer'), goalkeeper)
goalkeeper = goalkeeper.fillna(0)
goalkeeper.to_csv('C:/Users/vinhsoo/Desktop/D4E/goalkeeper.csv',index = False)


