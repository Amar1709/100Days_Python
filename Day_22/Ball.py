# Day 22 - Pong game project

from turtle import Turtle

class Game_Ball(Turtle):
    
    def __init__(self):
        '''Initialize the ball'''
        super().__init__()
        self.shape('circle')
        self.penup()
        self.fillcolor('RoyalBlue1')
        self.setpos(0,0)
        
    def move_direction(self,direction):
        '''Move the ball in the direction'''
        if direction == 'NE':
            self.move_NE()
        elif direction == 'SE':
            self.move_SE()
        elif direction == 'SW':
            self.move_SW()
        elif direction == 'NW':
            self.move_NW()
      
    
    def move_NE(self):
        '''Move the ball to the North East'''
        self.goto(self.xcor()+10,self.ycor()+10)
    
    def move_SE(self):
        '''Move the ball to the South East'''
        self.goto(self.xcor()+10,self.ycor()-10)
    
    def move_SW(self):
        '''Move the ball to the South West'''
        self.goto(self.xcor()-10,self.ycor()-10)
    
    def move_NW(self):
        '''Move the ball to the North West'''
        self.goto(self.xcor()-10,self.ycor()+10)
    
    def out_of_bounds(self):
        '''Check if the ball is out of bounds'''
        self.setpos(0,0)
        