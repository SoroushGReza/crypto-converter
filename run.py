import requests
from key import EXCHANGERATE_API_KEY


def get_price(crypto):
    try:
        # Build API URL
        api_url = (f"https://api.coingecko.com/api/v3/simple/price?"
                   f"ids={crypto}&vs_currencies=usd")
                   # Send request to API
                   response = requests.get(api_url)
                   
