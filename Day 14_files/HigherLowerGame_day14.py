# Day 14 - Higher and Lower Game

from unicodedata import name
from gameData import data
from art import logo, vs
import random

# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')

def data_transfer():
    data_copy = []

    for item in data:
        data_copy.append(item)
    return data_copy

R = {}
score = 0
ans = False

while(True):
    clear()
    data_copy = data_transfer()
    print(logo)
    if score>0:
        print(f"You're right! Current score: {score}.")
    R = random.choice(data_copy)
    print(f"Compare A: {R['name']}, a {R['description']}, from {R['country']}.")
    print(vs)
    data_copy.remove(R)
    R2 = random.choice(data_copy)
    print(f"Against B: {R2['name']}, a {R2['description']}, from {R2['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B' : ")
    
    if choice == 'A' and (R['follower_count']>R2['follower_count']):
        score+=1
        continue
    
    elif choice == 'B' and (R2['follower_count']>R['follower_count']):
        score+=1
        continue

    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break

exit()