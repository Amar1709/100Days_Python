# Day 11 Project: Blackjack Capstone

import random as r
from title import titleArt
import os

titleArt()

def startGame():
    '''This function starts the game and returns the dealer and player cards'''
    print("Welcome to Blackjack!")
    print("The rules are simple: get as close to 21 as possible without going over.")
    print("Dealer hits until she reaches 17. Aces count as 1 or 11.")
    print("Let's play!")
    
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    
    dealer = []
    player = []
    
    dealer.append(r.choice(cards))
    dealer.append(r.choice(cards))
    
    player.append(r.choice(cards))
    player.append(r.choice(cards))
    
    tally = [dealer, player]
    return tally
    

def calculateScore(cards):
    '''This function calculates the score of the cards'''
    if sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def drawCard(cards):
    '''This function draws a card'''
    cards.append(r.choice(cards))
    return cards

def compare(dealerScore, playerScore):
    '''This function compares the scores and returns the result'''
    if dealerScore == playerScore:
        return "Draw"
    elif dealerScore == 0:
        return "Lose, opponent has Blackjack"
    elif playerScore == 0:
        return "Win with a Blackjack"
    elif playerScore > 21:
        return "You went over. You lose"
    elif dealerScore > 21:
        return "Opponent went over. You win"
    elif playerScore > dealerScore:
        return "You win"
    else:
        return "You lose"
    
        
if __name__ == "__main__":
    '''This is the main function'''
    player_wins = 0
    dealer_wins = 0
    while(True):
        tally = startGame()
        dealerScore = calculateScore(tally[0])
        playerScore = calculateScore(tally[1])
        print (f"\nYour cards: {tally[1]}, current score: {playerScore}")
        print(f"\nDealer's first card: {tally[0][0]}")
        choice = input("\nDo you want to draw a card? Type 'y' or 'n': ")
        if choice == 'y':
            drawCard(tally[1])
            playerScore = calculateScore(tally[1])
        else:
            print("You chose to pass...")
        print(f"\n\nYour final hand: {tally[1]}, final score: {playerScore}")
        if dealerScore < 17:
            drawCard(tally[0])
            dealerScore = calculateScore(tally[0])
        print(f"\n\nDealer's final hand: {tally[0]}, final score: {dealerScore}\n")
        result = compare(dealerScore, playerScore)
        print(f"\n***** {result} *****\n")
        
        # pause the program
        os.system('pause')
        # clear the screen
        os.system('cls')
        
        if result == "You win" or result == "Win with a Blackjack" or result == "Opponent went over. You win":
            player_wins += 1
        elif result == "You lose" or result == "Lose, opponent has Blackjack" or result == "You went over. You lose":
            dealer_wins += 1
        else:
            pass
        titleArt()
        print(f"\n***** Score: Player: {player_wins} | Dealer: {dealer_wins} *****\n")
        choice = input("Do you want to play again? Type 'y' or 'n': ")
        if choice == 'y':
            os.system('cls')
            continue
        else:
            print("\n**** Thanks for playing! ****\n")
            break
        