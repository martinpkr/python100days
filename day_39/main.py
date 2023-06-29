from flight_search import FlightSearch
from data_manager import DataManager
import datetime as dt
from notification_manager import NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_from_sheets = DataManager()
now = dt.datetime.now()
now_str = now.strftime('%d/%m/20%y')
future_date = now + dt.timedelta(days=3*30)
future_date_str = str(future_date.strftime('%d/%m/20%y'))

for destination in data_from_sheets.all_data:
    search = FlightSearch()
    search.parameters['fly_from'] = 'SOF'
    search.parameters['fly_to'] = destination['iataCode']
    search.parameters['date_from'] = now_str
    search.parameters['date_to'] = future_date_str
    data = search.get_data()
    best_price = [ticket['price'] for ticket in search.ticket_data['data']]
    if best_price[0] < destination['lowestPrice']:
        link = data['data'][0]['deep_link']
        print(link)
        date_depart = data['data'][0]['local_departure']
        price = best_price[0]
        destination_name = destination['city']
        wanted_price = destination['lowestPrice']

        whole_massage = f'There is a flight from Sofia to {destination_name} lower than {wanted_price} EUR. For {price} you can travel to {destination_name} on {date_depart} ---> {link}'
        notification = NotificationManager()
        notification.get_notified(whole_massage)
