# Day 21 - Snake game project

from turtle import Turtle

align = 'center'
font_type = ('Courier',14,'normal')

class ScoreBoard(Turtle):
    
    def __init__(self):
        '''Initializing the score variables'''
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.count = 0
        self.print_score()
        
    def end_game(self):
        '''Triggers GAME OVER sequence'''
        self.goto(0,0)
        self.write(arg="GAME OVER!",move = False, align=align, font=font_type)
        
    def print_score(self):
        '''Prints the score each time'''
        self.write(arg=f"SCORE: {self.count}",move = False, align=align, font=font_type)
        
    def thank_you_screen(self):
        '''Triggers THANK YOU sequence'''
        self.goto(0,0)
        self.write(arg="Thank You for Playing!",move = False, align=align, font=font_type)
    
    def Invalid_screen(self):
        '''Triggers Invalid Screen sequence'''
        self.goto(0,0)
        self.write(arg="Invalid Choice!",move = False, align=align, font=font_type)