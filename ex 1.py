from pprint import pprint

import requests

def test_request():
    url = 'https://superheroapi.com/api/2619421814940190/'
    params = {}
    headers = {'Authorization': '2619421814940190'}
    return requests.get(url, params=params, headers=headers)

def serch_hero_id_intell(name_list):
    dictonary = {}

    for name in name_list:
        Hero = requests.get('https://superheroapi.com/api/2619421814940190/search/' + name).json()
        id = Hero['results'][0]['id']
        Hero = requests.get('https://superheroapi.com/api/2619421814940190/' + id).json()
        intelligence = Hero['powerstats']['intelligence']
        dictonary.setdefault(name)
        dictonary[name] = {'id' : id, 'intelligence' : intelligence}
    return dictonary

def sorting(dictonary):
    dictonary2 = {}
    sorted_keys = []
    for name in dictonary.keys():
        dictonary2.setdefault(name)
        dictonary2[name] = int(dictonary[name]['intelligence'])
    print('intelligence: ', dictonary2)
    sorted_keys = sorted(dictonary2, key = dictonary2.get, reverse=True)
    #print(sorted_keys)
    return print('Наибольший intelligence у:', sorted_keys[0], '=', dictonary2[sorted_keys[0]])

name_list = ['Hulk', 'Captain America', 'Thanos']
dictonary = serch_hero_id_intell(name_list)
print('Запрашиваемые характеристики героев:')
pprint(dictonary)
sorting(dictonary)

