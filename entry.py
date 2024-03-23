import requests
import json

def createSession():
    headers = {
        'accept': 'application/json; charset=UTF-8',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'access-control-allow-credentials': 'true',
        'access-control-allow-headers': 'Accept, X-Access-Token, X-Application-Name, X-Request-Sent-Time',
        'access-control-allow-methods': 'GET, POST, DELETE, PUT, OPTIONS, HEAD',
        'access-control-allow-origin': '*',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'll-version': '2021-03-01',
        'origin': 'https://sobgame.club',
        'referer': 'https://sobgame.club/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    json_data = {
        'game_key': 'prod_ddf8d562b70e41dd9573214907c6cde9',
        'platform': 'guest',
        'game_version': '1.0.0.0',
    }

    response = requests.post('https://api.lootlocker.io/game/v2/session/guest', headers=headers, json=json_data)
    data = json.loads(response.text)
    return data

def setName(session, wallet):
    headers = {
        'accept': 'application/json; charset=UTF-8',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'access-control-allow-credentials': 'true',
        'access-control-allow-headers': 'Accept, X-Access-Token, X-Application-Name, X-Request-Sent-Time',
        'access-control-allow-methods': 'GET, POST, DELETE, PUT, OPTIONS, HEAD',
        'access-control-allow-origin': '*',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'll-version': '2021-03-01',
        'origin': 'https://sobgame.club',
        'referer': 'https://sobgame.club/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-session-token': session,
    }

    json_data = {
        'name': wallet,
    }

    response = requests.patch('https://api.lootlocker.io/game/player/name', headers=headers, json=json_data)
    print(response.text)

def setScore(session):
    headers = {
        'accept': 'application/json; charset=UTF-8',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'access-control-allow-credentials': 'true',
        'access-control-allow-headers': 'Accept, X-Access-Token, X-Application-Name, X-Request-Sent-Time',
        'access-control-allow-methods': 'GET, POST, DELETE, PUT, OPTIONS, HEAD',
        'access-control-allow-origin': '*',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'll-version': '2021-03-01',
        'origin': 'https://sobgame.club',
        'referer': 'https://sobgame.club/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-session-token': session,
    }

    json_data = {
        'member_id': '',
        'score': 150,
    }

    response = requests.post('https://api.lootlocker.io/game/leaderboards/21218/submit', headers=headers, json=json_data)
    print(response.text)

with open('wallets.txt', 'r') as file:
    wallets = file.read().splitlines()

for wallet in wallets:
    data = createSession()
    print(data['session_token'])
    session = data['session_token']
    #wallet = '0x22621Cd9eDe0De0d41Dbe4aaE0420CeAfbcb36f1'
    setName(session, wallet)
    setScore(session)