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
        # Parse response as json
        data = response.json()  # Fix the variable name here
        # To return exchange rate between base and target currencies
        return data["rates"][target]
    except Exception as e:
        print(f"Error getting exchange rates: {e}")
        return None


# Function to convert amount using the given exchange rate
def convert_amount(amount, rate):
    # Multiply amount by rate and return result
    return amount * rate


# Main loop
while True:
    # Print available options
    print("Choose a cryptocurrency:")
    print("1. ETH")
    print("2. GALA")

    # Get user input
    user_input = input("Enter your choice (1 or 2): ")

    # Check if input is a number 
    if not user_input.isdigit():
        print("That's not an option, try agaian.")
        continue

    # Convert user input an integer
    user_choice = int(user_input)

    # Set crypto based on user choice
    if user_choice == 1:
        crypto_name = "ETH"
        crypto_id = "ethereum"
    elif user_choice == 2:
        crypto_name = "GALA"
        crypto_id = "gala"
    else:
        print("Not an option, try again.")
        continue

    # Get cryptocurrency price in USD 
    crypto_usd_price = get_price(crypto_id)

    if crypto_usd_price is None:
        print("Can't continue due to errors.")
    else:
        while True:
            # Get amount of cryptocurrency to convert
            user_amount = input(
                f"Enter amount of "
                f"{crypto_name} to convert: "
            )
        if not user_amount.replace(".", "", 1).isdigit():
            print("Only numbers and one '.' allowed, try again.")
            continue
        break

    # Convert the user input to float
    crypto_to_convert = float(user_amount)

    # Get exchange rates
    usd_rate = get_rate("USD", "USD")
    eur_rate = get_rate("USD", "EUR")
    sek_rate = get_rate("USD", "SEK")

# Convert the cryptocurrency amout to different currencies
usd_value = convert_amount(crypto_to_convert, crypto_usd_price * usd_rate)
eur_value = convert_amount(crypto_to_convert, crypto_usd_price * eur_rate)
sek_value = convert_amount(crypto_to_convert, crypto_usd_price * sek_rate)
if usd_value is None or eur_value is None or sek_value is None:
    print("Can't continue, due to errors.")

