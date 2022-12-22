# Day 22 - Pong Game Project

from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,position):
        '''Initialize the paddle'''
        super().__init__()
        self.paddle_build()
        self.goto(x=position,y=0)
        
    
    def paddle_build(self):
        '''Build the paddle'''
        self.fillcolor('white')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1,outline=1)
    
    def up(self):
        '''Move the paddle up'''
        if self.ycor() < 250:
            self.sety(self.ycor()+20)
    
    def down(self):
        '''Move the paddle down'''
        if self.ycor() > -250:
            self.sety(self.ycor()-20)