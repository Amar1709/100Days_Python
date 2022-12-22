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
        with open('Day 20 & 21 _ SnakeGame\high_score.txt') as file:
            self.high_score = int(file.read())
        self.print_score()
        
    def end_game(self):
        '''Triggers GAME OVER sequence'''
        if self.high_score <= self.count:
            self.high_score = self.count
            with open('Day 20 & 21 _ SnakeGame\high_score.txt','w') as file:
                file.write(f"{self.high_score}")
        self.goto(0,0)
        self.write(arg="GAME OVER!",move = False, align=align, font=font_type)
        
    def print_score(self):
        '''Prints the score each time'''
        self.write(arg=f"SCORE: {self.count}\t\tHIGH SCORE: {self.high_score}",move = False, align=align, font=font_type)
        
    def thank_you_screen(self):
        '''Triggers THANK YOU sequence'''
        self.goto(0,0)
        self.write(arg="Thank You for Playing!",move = False, align=align, font=font_type)
    
    def Invalid_screen(self):
        '''Triggers Invalid Screen sequence'''
        self.goto(0,0)
        self.write(arg="Invalid Choice!",move = False, align=align, font=font_type)
        