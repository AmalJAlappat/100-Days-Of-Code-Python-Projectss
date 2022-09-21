import requests
from pprint import pprint

SHEETY_PRICE_ENDPOINT = "https://api.sheety.co/032d728cbd8393a7d4ba096a031e05cf/flightClub/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/032d728cbd8393a7d4ba096a031e05cf/flightClub/users"


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.sheet_data = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICE_ENDPOINT)
        data = response.json()

        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            newdata = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICE_ENDPOINT}/{city['id']}", json=newdata)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        print(self.customer_data)
        return self.customer_data

