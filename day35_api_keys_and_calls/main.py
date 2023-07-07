import requests
from twilio.rest import Client

account_sid = 'ACe44d89dfdacb0db777437f591a8bab4b'
auth_token = 'b292468d9fac5ddfd0fb75e1903147e6'



api_endpoint = 'https://api.openweathermap.org/data/2.8/onecall'
api_key = '83c41149d17b52b805f400527a8c4777'


params = {
    'lat': 42.922039,
    'lon': 22.930059,
    'appid': api_key,
    'exclude': 'daily,current,minutely'
}
response = requests.get(api_endpoint, params=params)
weather_data = response.json()
hourly_data = weather_data['hourly']

will_rain = False

for obj in range(12):
    data = hourly_data[obj]
    weather_id = data['weather'][0]['id']
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    client.messages.create(body='It\'s going to rain today,maybe it is a good idea to bring an umbrella!☔☂',
                           from_='+14178072421',to='+359895787881')
    print('its raining')