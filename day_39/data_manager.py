import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.response = requests.get('https://api.sheety.co/a059be9044a594a26f8f2101590ad391/flightDeals/prices')
        self.response.raise_for_status()
        self.data = self.response.json()
        self.count_of_prices = len(self.data['prices'])
        self.all_data = self.data['prices']

