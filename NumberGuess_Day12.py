# Day 12 Code - Number Guessing Game
import random

from matplotlib.pyplot import flag
# Title
print('''                       _                   
                      | |                  
 _ __  _   _ _ __ ___ | |__   ___ _ __ ___ 
| '_ \| | | | '_ ` _ \| '_ \ / _ \ '__/ __|
| | | | |_| | | | | | | |_) |  __/ |  \__\_
|_| |_|\__,_|_| |_| |_|_.__/ \___|_|  |___/

''')

print("\n\nWelcome to the Number Guessing Game : ")
diff =int(input("Choose your difficulty(1-2) - \n1.Easy\t2.Hard\nYour Choice - "))

answer = int(random.randint(0,100))
flag = False


def Game(lives):
    flag = False
    
    while lives!=0:
        guess= int(input(f"You have {lives} guesses remaining...guess the number - "))
        
        if guess == answer:
            flag = True
            break
        
        elif guess > answer:
            print("Too high...Guess Again\n")
            lives -=1
        
        else:
            print("Too low...Guess Again\n")
            lives -=1

    return flag

def Hard():
    lives = 5
    flag = Game(lives)
    return flag
    
def Easy():
    lives = 10
    flag = Game(lives) 
    return flag  

if diff != 1 and diff != 2:
    print("Wrong Choice.")
    exit()

else:

    if diff == 1:
        flag = Easy()
    else:
        flag = Hard()
        
    if flag:
        print(f"\nGreat job...{answer} is the right guess\nYou Win!")
    else:
        print(f"\nSorry...you ran out of guesses...{answer} was the right answer\nYou Lose!")