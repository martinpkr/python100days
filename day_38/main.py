import requests
import datetime

API_ENDPOINT = ' https://trackapi.nutritionix.com/'
AUTH_KEY = '612fd835a142362ce23ad4cf64916b9c'
APP_ID = '77c73485'
SHEETY_ENDPOINT = 'https://api.sheety.co/a059be9044a594a26f8f2101590ad391/pythonexercise/workouts'

user_input = input('What exercise you did today?: ')


#we need to export now date
now = datetime.datetime.now()
stringified_date = now.strftime('%d/%m/%Y')
stringified_time = now.strftime('%H:%M:%S')


headers = {
    'x-app-id': APP_ID,
    'x-app-key': AUTH_KEY,
    'Content-Type': 'application/json'
}

parameters = {
 "query": user_input,
 "gender": "male",
 "weight_kg": 60,
 "height_cm": 172.5,
 "age": 21
}


response = requests.post(f'{API_ENDPOINT}v2/natural/exercise', json=parameters, headers=headers)
response.raise_for_status()
data = response.json()['exercises'][0]
name = data['name']
duration = data['duration_min']
calories_burnt = data['nf_calories']


# response_sheet = requests.get('https://api.sheety.co/a059be9044a594a26f8f2101590ad391/pythonexercise/workouts')
# print(response_sheet)
sheety_headers = {
    'Authorization': "Basic TWFydGluUEs6QmFzaWNQYXNzMTIz"
}
sheety_body = {

    'workout': {
        'date': stringified_date,
        'time': stringified_time,
        'exercise': name,
        'duration': duration,
        'calories': calories_burnt,
    }

}

respons_sheet = requests.post(SHEETY_ENDPOINT, json=sheety_body,headers=sheety_headers)
respons_sheet.raise_for_status()

