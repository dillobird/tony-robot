import os
import requests
from dotenv import load_dotenv
import xmltodict
import json

load_dotenv()

REDIRECT_URI = os.getenv('YAHOO_REDIRECT_URI')
CLIENT_ID = os.getenv('YAHOO_CLIENT_ID')
CLIENT_SECRET = os.getenv('YAHOO_CLIENT_SECRET')
AUTH_CODE = os.getenv('YAHOO_AUTH_CODE')
LEAGUE_ID = os.getenv('YAHOO_LEAGUE_ID')


def get_yahoo_auth_code():
    return

def get_yahoo_token():
    TOKEN_URL = os.getenv('YAHOO_TOKEN_URL')

    # Specify the grant type in the POST data
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'code': AUTH_CODE,
        'grant_type': 'authorization_code',
    }

    # Make the POST request to get the token
    response = requests.post(TOKEN_URL, data=data)

    # Handle response
    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens.get('access_token')
        # You can store the access_token securely for future requests
        return access_token
    else:
        print(f"Failed to get token: {response.status_code}, {response.text}")
        return None


def get_weekly_summary():
    access_token = get_yahoo_token()
    print(f"Bearer {access_token}")

    headers = {'Authorization': f'Bearer {access_token}'}
    url = f'https://fantasysports.yahooapis.com/fantasy/v2/league/{LEAGUE_ID}/scoreboard?week=1'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = xmltodict.parse(response.text)
        print(f"Data: {json.dumps(data)}")
        return data
    else:
        print(f"Failed to get scoreboard: {response.status_code}, {response.text}")
        return None