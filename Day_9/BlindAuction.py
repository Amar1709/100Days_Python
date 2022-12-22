# Day 9 - Blind Auction
from title import titleArt
import os
titleArt()
print('\n=====================================\n')
print('Welcome to the secret auction program.')
print('-------------------------------------\n')
dict = {}
while(True):
    name = input('What is your name? => ')
    bid = float(input('What is your bid? => $ '))
    dict[name] = bid
    choice = input('\nAre there any other bidders? Type "yes" or "no": ')
    if choice == 'yes':
        os.system('cls')
        titleArt()
        print('\n=====================================\n')
        continue
    else:
        os.system('cls')
        titleArt()
        print('\n=====================================\n')
        break
    
print(f'The winner is: {max(dict, key=dict.get)} with a bid of ${max(dict.values())}')