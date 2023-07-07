import requests

DEFAULT_ENDPOINT = 'https://api.tequila.kiwi.com/v2/search'

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            'apikey': 'iXWjdrB64cA26T0PMbXwJoB1VG75xvRp',
            'Content-Type': 'application/json',
        }
        self.parameters = {
            'fly_from': 'SOF',
            'fly_to': 'PRG',
            'date_from': '08/10/2023',
            'date_to': '15/10/2023'
        }
    def get_data(self):
        self.response = requests.get(DEFAULT_ENDPOINT,params=self.parameters,headers=self.headers)
        self.response.raise_for_status()
        self.ticket_data = self.response.json()
        return self.ticket_data