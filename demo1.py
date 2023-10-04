import time
import hmac
import hashlib
import requests

def get_api_keys():
    with open('keys.txt', 'r') as f:
        api_key = f.readline().strip()
        api_secret = f.readline().strip()
    return api_key, api_secret

api_key, api_secret = get_api_keys()

def create_gift_card(token, amount):
    params = {
        'token': token,
        'amount': float(amount),
        'recvWindow': 5000,  # Adding recvWindow
        'timestamp': int(time.time() * 1000)
    }

    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    params['signature'] = signature

    headers = {
        'X-MBX-APIKEY': api_key,
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post('https://api.binance.com/sapi/v1/giftcard/createCode', json=params, headers=headers)
        response.raise_for_status()
        print(f"Gift Card created: {response.json()}")
    except requests.exceptions.HTTPError as e:
        print(f"Error: {str(e)}")
    except requests.exceptions.RequestException as e:
        print(f"Error: An internal server error occurred. Please try again later.")

token = input("Enter the token: ")
amount = input("Enter the amount: ")

create_gift_card(token, amount)
