from binance.spot import Spot as Client

# Set up the client with your API key and secret
api_key = "DutmnemngmgLDKph8GfwBUPx5LuAcoBMpTaBgXqXRhrnPnUHkU3thggOLV3mCCvw"
api_secret = "t4vwpHczIvtiwWZ9E1qPcplZGQ5AAq89M6v900TZhzdLiq8aXcjCgOwUyCkbA7ob"
client = Client(api_key, api_secret)

# Prompt the user to input the token for the gift card
crypto = input("What token do you want to choose? ")
if not crypto:
    crypto = 'ETH' # Default to ETH if no token is entered

# Prompt the user to input the amount of the token for the gift card
number = float(input("What amount of {} do you want to send? ".format(crypto)))


params = {
    'token': crypto,
    'amount': number
}

# Create the gift card
response = client.gift_card_create_code(**params)

# Print the response
print(response)
