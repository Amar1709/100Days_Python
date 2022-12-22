# Day 33 - practice with the Sunset - Sunrise API

import requests
import datetime as dt

my_lat = 19.218330
my_long = 72.856270

param = {'lat': my_lat, 'lng': my_long , 'formatted' : 0}

response = requests.get('http://api.sunrise-sunset.org/json', params=param)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(sunrise.split('T')[1].split(':')[0]) # print the hour of sunrise
print(sunset.split('T')[1].split(':')[0])  # print the hour of sunset

time = str(dt.datetime.now())
print(time.split(' ')[1].split(':')[0]) # print the current hour

#print(data)