# Habit Tracker - A simple habit tracker


import datetime as dt
import requests

USERNAME = "amar1709"
TOKEN = "basbdn52mnmssnmnsonnm43"

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN, 
    "username": USERNAME, 
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create a new user

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" :"graph1",
    "name" : "Reading Graph",
    "unit" : "Pages",
    "type" : "int",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#Upload a new graph

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = dt.datetime.now()
graph_endpoint_update = f"{graph_endpoint}/{graph_config['id']}"

update_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? - ")
}

# Change the quantity to whatever you want to update

response = requests.post(graph_endpoint_update, json=update_config, headers=headers)
print(response.text)

# change_info_endpoint = f"{graph_endpoint_update}/{today.strftime('%Y%m%d')}"

# change_info_config = {
#     "quantity": "50"
# }

# Edit the quantity to whatever you already have

# response = requests.put(change_info_endpoint, json=change_info_config, headers=headers)
# print(response.text)

# Delete the quantity

# response = requests.delete(change_info_endpoint, headers=headers) # delete
# print(response.text)

    