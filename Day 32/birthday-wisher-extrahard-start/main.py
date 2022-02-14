##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import os
import smtplib
import random
import datetime as dt
import pandas as pd


now = dt.datetime.now()
day = now.day
month = now.month
day_of_week = now.today().strftime("%A")

my_email = "abc123@mail.com" # Your email address
my_password = "12345678" # Change this to your password

data = pd.read_csv("Day 32/birthday-wisher-extrahard-start/birthdays.csv")

data = data.to_dict("records")

for row in data:
    if row["day"] == day and row["month"] == month:
        name = row["name"]
        email = row["email"]
        num = random.randint(1,3)
        with open (f"Day 32/birthday-wisher-extrahard-start/letter_templates/letter_{num}.txt") as contents:
            letter = contents.readlines()
            for line in letter:
                line = line.replace("[NAME]", name)
                with open(f"Day 32/birthday-wisher-extrahard-start/Output/ReadyToSend/{name}.txt", "a") as new_file:
                    new_file.write(line)
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            with open (f"Day 32/birthday-wisher-extrahard-start/Output/ReadyToSend/{name}.txt", "r") as contents:
                letter = contents.read()
            smtp.ehlo()
            smtp.starttls()
            smtp.login(my_email, my_password)
            smtp.sendmail(my_email, email, f"Subject: Happy Birthday {name}!\n\n{letter}")
            smtp.quit()
        os.remove(f"Day 32/birthday-wisher-extrahard-start/Output/ReadyToSend/{name}.txt")

#print(data)