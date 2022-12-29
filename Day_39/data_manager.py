import requests

SHEETY_PRICES_ENDPOINT ="https://api.sheety.co/7bb1a45cd6cf0f688af1fdbd265027e1/flightDealsDay39&40PythonProject/prices"

class DataManager:
    '''This class is responsible for talking to the Google Sheet.'''
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        '''This method is responsible for getting the data from Google Sheet.'''
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        '''This method is responsible for updating the Google Sheet with IATA Codes.'''
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

# response = requests.get(url=SHEETY_PRICES_ENDPOINT)
# data = response.json()
# pprint(data)

