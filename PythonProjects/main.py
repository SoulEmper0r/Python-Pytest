import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4b4868b54b2eb1da205dbd21351b6b06'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': TOKEN }
trainer_id = 8280

Body_Create = {
    "name": "generate",
    "photo_id": -1
}


response = requests.post(url= f'{URL}/pokemons', headers= HEADER, json= Body_Create)

print(f'Body запроса на создание покемона: {response.text}')
response_data = response.json()
id_pokemon = response_data.get("id", None)
# print(f'id покемона: {id_pokemon}')

response = requests.get(url= f'{URL}/pokemons', params={'trainer_id': trainer_id, 'status':1})
print(f'Получаю своих покемонов: {response.text}')

# print(response.text)
response_data = response.json()
pokemon_name = response.json()["data"][0]["name"]
print(f'Имя созданного покемона: {pokemon_name}')


Body_Put = {
    "pokemon_id": str(id_pokemon),
    "name": "generate", 
    "photo_id": -1
}

response = requests.put(url= f'{URL}/pokemons', headers= HEADER, json= Body_Put)
print(f'Body запроса на изменение имени: {response.text}')

response = requests.get(url= f'{URL}/pokemons', params={'trainer_id': trainer_id, 'status':1})

response_data = response.json()
new_pokemon_name = response.json()["data"][0]["name"]
print(f'Новое имя покемона: {new_pokemon_name}')


Body_Add = {
    "pokemon_id": str(id_pokemon)
}

response = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json= Body_Add)

print(f'Body запроса ловлю покемона: {response.text}')


# print(f'Status Code: {response.status_code}')
# print(f'Headers: {response.headers}')
# print(f'Body: {response.text}')