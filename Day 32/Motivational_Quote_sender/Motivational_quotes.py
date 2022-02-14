# Automatic Birthday Wisher Day 32

import smtplib

my_email = "obitouchiha0917@gmail.com"
password = "#ShinobiRoxx1720"



import datetime as dt
import random

now = dt.datetime.now()

year = now.year
month = now.month
day_of_week = now.today().strftime("%A")

# Try conditioning it to the day of the week...like quotes every monday - (simple if statements)

#print(day_of_week)

# date_of_birth = dt.datetime(year=2000, month=9, day=17, hour=20, minute=30, second=0)
# print(date_of_birth)

with open ("Day 32\Birthday Wisher (Day 32) start\quotes.txt","r") as data:
    quote_list = data.readlines()
    quote = random.choice(quote_list)
    
with smtplib.SMTP('smtp.gmail.com',587) as connection:
    connection.starttls()
    connection.login(user = my_email, password= password)
    connection.sendmail(from_addr= my_email, to_addrs="obitouchiha0917@gmail.com", msg=f"Subject:{day_of_week}'s Quote:\n\n{quote}")