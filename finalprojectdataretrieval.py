import requests

endpoint = 'http://pokeapi.co/api/v2/'
location = 'generation/'

url = endpoint + location

r = requests.get(url)
print(r.url)

data = r.json()

generations = data['results']

y = 0
for gen in generations:
    print(gen['name'])
    print(gen['url'])