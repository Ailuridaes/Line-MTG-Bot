import requests
from models.card import Card
from models.ruling import Ruling
from api_errors import GetCardError

_api_uri = 'https://api.scryfall.com'

def get_card(cardname, set=''):
    resp = requests.get(f'{_api_uri}/cards/named', params={'fuzzy': cardname, 'set': set})
    if resp.status_code == 404:
        error_message = ''
        if resp.json().get('type') == 'ambiguous':
            error_message = f'Multiple matches were found for "{cardname}". Please try again with a more specific query.'
        else:
            error_message = f'No matches were found for "{cardname}". Please try again.'
        raise GetCardError(error_message)
    return Card(resp.json())

def get_card_ruling(card):
    resp = requests.get(card.rulings_uri)
    if resp.status_code == 404:
        raise GetCardError(f'Error retrieving rulings for "{card.name}"')
    return [Ruling(card.name, r) for r in resp.json()['data']]
