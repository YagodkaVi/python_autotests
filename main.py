import requests

URL =  'https://pokemonbattle.ru/v2'
TOKEN = 'de95b952b30408f57eccc7a4ecb2434e'
HEADER = {'Content-Type' : 'application/json'}
body = {
    "name": "Малыш",
    "photo_id": -1
}

requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body)


URL =  'https://pokemonbattle.ru/v2'
TOKEN = 'de95b952b30408f57eccc7a4ecb2434e'
HEADER = {'Content-Type' : 'application/json'}
body = {
   "name": "New Name" 
    
}

requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body)




URL =  'https://pokemonbattle.ru/v2'
TOKEN = 'de95b952b30408f57eccc7a4ecb2434e'
HEADER = {'Content-Type' : 'application/json'}
body = {
    "pokemon_id": "9"
}
requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body)