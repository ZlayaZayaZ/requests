import requests
import json

url = 'https://superheroapi.com/api/'
token = str('2619421814940190')

hulk_text = requests.get(url + token + '/search/Hulk').text
capitan_america_text = requests.get(url + token + '/search/Captain America').text
thanos_text = requests.get(url + token + '/search/Thanos').text
hulk = json.loads(hulk_text)
capitan_america = json.loads(capitan_america_text)
thanos = json.loads(thanos_text)
list_superhero = [hulk, capitan_america, thanos]
superhero_intelligence = dict()
for superh in list_superhero:
  superhero_intelligence[superh['results'][0]['name']] = superh['results'][0]['powerstats']['intelligence']
print(superhero_intelligence)
max_intelligence = 0
intelligence_hero = ''
for key, value in superhero_intelligence.items():
  if int(value) > max_intelligence:
    max_intelligence = int(value)
    intelligence_hero = key
print(intelligence_hero)