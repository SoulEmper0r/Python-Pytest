import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4b4868b54b2eb1da205dbd21351b6b06'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': TOKEN }
trainer_id = '8280'

def test_status_code():
    response = requests.get(url= f'{URL}/pokemons')
    assert response.status_code == 200


def test_trainer_id():
    response = requests.get(url= f'{URL}/pokemons', params={'trainer_id': trainer_id, 'status':1})
    Json_trainer_id = response.json()["data"][0]["trainer_id"]
    assert Json_trainer_id == trainer_id

def test_trainer_name():
    response = requests.get(url= f'{URL}/trainers', params={'trainer_id': trainer_id})
    trainer_name = response.json()["data"][0]["trainer_name"]
    assert trainer_name == 'Александр'
