import requests
from key import EXCHANGERATE_API_KEY


# Function to get the USD price of a cryptocurrency
def get_price(crypto):
    try:
        # Build API URL
        api_url = (f"https://api.coingecko.com/api/v3/simple/price?"
                   f"ids={crypto}&vs_currencies=usd")
                   # Send request to API
                   response = requests.get(api_url)
                   # Parse response as JSON
                   data = response.json()
                   # Return the USD price of the cryptocurrency
                   return data[crypto]["usd"]
                except Exception as e:
                    print(f"Error getting {crypto} price: {e}")
                    return None


# Function to get xchange rate between two currencies
def get_rate(base, target):
    try:
        # Build API URL
        api_url = (
            f"https://api.exchangerate-api.com/v4/latest/{base}"
            f"?access_key={EXCHANGERATE_API_KEY}"
        )
        # Send request to API
        response = requests.get(api_url)
        # Parse responsen as json
        data = responsen.json()