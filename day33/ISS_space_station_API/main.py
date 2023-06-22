import time
import requests
import datetime as dt
import smtplib

response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()

iss_data = response.json()['iss_position']

# longitude = float(iss_data['longitude'])
# latitude = float(iss_data['latitude'])

longitude = 24
latitude = 44
parameters = {
    'lat': 42.922040,
    'lng': 22.930060,
    'formatted': 0
}

response_from_ss = requests.get('https://api.sunrise-sunset.org/json',params=parameters)
response_from_ss.raise_for_status()

data = response_from_ss.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0]) + 3
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0]) + 3

time_now = dt.datetime.now()
hour_now = time_now.hour

def its_up():
    if longitude > parameters['lng'] - 5 or longitude < parameters['lng'] + 5 and latitude > parameters['lat'] + 5 \
            or latitude < parameters['lat'] - 5:
        return True
def its_night():
    if hour_now >= sunset or hour_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if its_night() and its_up():
        my_email = 'martinkirilov402@gmail.com'
        password = 'cuuvwcxxrenfmoqh'
        with smtplib.SMTP('smtp.gmail.com',port='587') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
            to_addrs='marutinkirilov@abv.bg',
            msg='Subject:You can see the International Space Station\n\nLook up.')
            connection.close()


git



