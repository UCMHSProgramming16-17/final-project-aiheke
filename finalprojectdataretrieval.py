#lets set up the system, get some csv and requests in here
import csv
import requests

csvf = open('pokemontypes.csv', 'w')
csvw = csv.writer(csvf, delimiter=',')
f = open('pokemontypenumbers.csv', 'w')
w = csv.writer(f, delimiter=',')

csvw.writerow(['Type','Name of Pokemon'])
w.writerow(['Type','# of Pokemon'])


#assembling the url
endpoint = 'http://pokeapi.co/api/v2/'
location = 'type/'

x = 1
while x <= 17:
    url = endpoint + location + str(x)
    
    r = requests.get(url)
    print(r.url)
    
    data = r.json()
    pokemontype = data['name']
     
    y = 0
    typepokemon = data['pokemon']
    for pokemon in typepokemon:
        namepokemon = typepokemon[y]['pokemon']['name']
        csvw.writerow([pokemontype, namepokemon])
        y += 1
    w.writerow([pokemontype,y])
        
        
    
    x += 1

    
    
