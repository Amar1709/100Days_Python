import requests
from datetime import datetime
import smtplib

my_email = "abc123@mail.com" # Your email address
my_password = "abc12345"    # your password

#MY_LAT = 19.218330 # Your latitude
#MY_LONG = 72.856270 # Your longitude

# MY_LAT = 35.689487  # Tokyo
# MY_LONG = 139.691711

MY_LAT = input("Enter your latitude: ")
MY_LONG = input("Enter your longitude: ")

def is_currently_overhead(lat, long):
    """
    Returns True if the ISS is overhead the given latitude and longitude,
    False otherwise.
    """
    # Write your code here.
    lat = float(lat)
    long = float(long)
    
    lat_low = int(lat - 5)
    lat_high = int(lat + 5)
    long_low = int(long - 5)
    long_high = int(long + 5)
    
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    iss_position = [data['iss_position']['latitude'], data['iss_position']['longitude']]
    
    print(iss_position) # print the current position of the ISS
    
    if int(float(iss_position[0]))<=lat_high and int(float(iss_position[0]))>=lat_low and int(float(iss_position[1]))<=long_high and int(float(iss_position[1]))>=long_low:
        return True
    else:
        return False


#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = str(datetime.now())
hour_now = int(time_now.split(" ")[1].split(":")[0])

print(hour_now)
print(sunrise)
print(sunset)

if hour_now<sunrise or hour_now>sunset: # if the current hour is before the sunrise or after the sunset
    if is_currently_overhead(MY_LAT, MY_LONG):  # if the ISS is overhead the given latitude and longitude
        with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            connection.login(user = my_email, password= my_password)
            connection.sendmail(from_addr= my_email, to_addrs=my_email, msg=f"Subject: ISS is overhead (LOOK UP!)\n\nThe ISS is overhead your location.") 
    else:
        print("The ISS is not overhead your location.")

else:
    print("Not dark enough")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
