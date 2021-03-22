from pprint import pprint

import time

import datetime as dt

import requests

now = round(time.time())
two_days_before = round(now - 2*24*3600)  # 2 дня назад

answers_list = {'title':'link'}

page = 1

while True:
    time.sleep(0.3)
    url = 'https://api.stackexchange.com/2.2/questions/'
    params = {'page': page, 'pagesize': 100, 'fromdate': two_days_before, 'todate': now, 'tagged': 'python', 'site': 'stackoverflow' }
    response = requests.get(url, params=params)
    print('Page:', page,'Responce:',response, 'has_more:', response.json()['has_more'])
    for question in range(len(response.json()['items'])):
        #answers_list.append(response.json()['items'][question]['title'])
        answers_list[response.json()['items'][question]['title']] = response.json()['items'][question]['link']
    if response.json()['has_more'] == False:
        break
    page += 1

pprint(answers_list)
