# Day 23 - Turtle Crossing Game (Capstone Project)

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        '''Initialize the player'''
        super().__init__()
        self.fillcolor('black')
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def move_player_Up(self):
        '''Move the player up'''
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
    
    def move_player_Down(self):
        '''Move the player down'''
        if self.ycor() > -FINISH_LINE_Y:
            self.backward(MOVE_DISTANCE)
    
    def reached_finish(self):
        '''Go to start position - Level up'''
        self.goto(STARTING_POSITION)
    
