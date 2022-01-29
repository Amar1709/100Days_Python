
from turtle import Turtle


# Day 23 - Turtle Crossing Game (Capstone Project)

FONT = ("Courier", 16, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        '''Initialize the scoreboard'''
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        self.score = 1
        self.update_score()
    
    def update_score(self):
        '''Update the score on the screen'''
        self.clear()
        self.write(arg=f"Level: {self.score}",align='center', font=FONT)
    
    def increase_score(self):
        '''Increase the score'''
        self.score += 1
        self.update_score()
    
    def game_over(self):
        '''Display game over message'''
        self.clear()
        self.goto(0,0)
        self.write(arg=f"GAME OVER!\n\nYour Score = {self.score - 1}",align='center',font=FONT)
