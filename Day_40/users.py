import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/7bb1a45cd6cf0f688af1fdbd265027e1/flightDealsDay39&40PythonProject/users"

print("Welcome to Amar's Flight Club.")
print("We find the best flight deals and email you.")
firstName = input("What is your first name? => ")
lastName = input("What is your last name? => ")
email = input("What is your email? => ")
verifyEmail = input("Type your email again. => ")

if email == verifyEmail:
    print("You are in the club!")
    new_data = {
        "user": {
            "firstName": firstName,
            "lastName": lastName,
            "email": email
        }
    }
    response = requests.post(url=SHEETY_USERS_ENDPOINT, json=new_data)
    if response.text == "OK":
        print("Success! Your email has been added we look forward to sending you the best flight deals!")