import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        quantity = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a2a2f320a5c1d38e81f502bcc3a112b4272a89ad7506f1c43bc7fb4f27e84282")
        content = response.json()
        price = float(content["data"]["priceUsd"])*quantity
        print(f"${price:,.4f}")


    except requests.RequestException:
        sys.exit("Could not retrieve price")


main() 

