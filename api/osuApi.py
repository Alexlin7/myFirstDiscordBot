from os import defpath
from discord.ext import commands
import requests
import json
from pprint import pprint

# with open('setting.json',mode='r',encoding='utf8') as jfile:
#     jdata = json.load(jfile)

API_URL = 'https://osu.ppy.sh/api/v2'
TOKEN_URL = 'https://osu.ppy.sh/oauth/token'

def get_token():
        with open('setting.json',mode='r',encoding='utf8') as jfile:
            jdata = json.load(jfile)

        data = {
            'client_id':jdata['client_id'],
            'client_secret':jdata['client_secret'],
            'grant_type':'client_credentials',
            'scope':'public'
        }

        response = requests.post(TOKEN_URL, data=data)

        return response.json().get('access_token')

class Osu():
    def get_best_beatmapset():
        token = get_token()

        headers = {
            'Content-Type':'application/json',
            'Accept':'application/json',
            'Authorization':f'Bearer {token}'
        }

        params = {
            'mode':'fruits',
            'limit':1
        }

        response = requests.get(f'{API_URL}/users/4841753/scores/best', params=params, headers=headers)
        beatmapset_data = response.json()[0].get('beatmapset')

        pprint(beatmapset_data, indent=2)
        return beatmapset_data



