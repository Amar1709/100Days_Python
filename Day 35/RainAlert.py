#Day 35 Python - Rain Alert

#Upload it on a cloud service to automatically run it every day.

#update environment variables

from twilio.rest import Client
import requests

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'

# LAT = 19.218330
# LONG = 72.978088

LAT = 39.103119
LONG = -84.512016

api_key = "597145e24a94cf40351d25fd9250b624"
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"

parameters = {'lat': LAT, 'lon': LONG, 'appid': api_key, 'exclude': 'minutely,daily,current'}

will_rain = False
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)
    
    message = client.messages \
                .create(
                     body="It's going to rain today please take an umbrella☔",
                     from_='+14129230688',
                     to='+919307274812'
                 )
    print(message.status)