# Day 22 - Pong game project

from turtle import Turtle


class Score(Turtle):
    
    def __init__(self):
        '''Initialize the score'''
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.l_score = 0
        self.r_score = 0
        self.update_score()
    
        
    def update_score(self):
        '''Update the score'''
        self.clear()
        self.goto(-100,200)
        self.write(arg=f'{self.l_score}',align='center',font=('Courier',30,'normal'))
        self.goto(100,200)
        self.write(arg=f'{self.r_score}',align='center',font=('Courier',30,'normal'))
        
    def l_point(self):
        '''Add a point to the left score'''
        self.l_score += 1
        self.update_score()
    
    def r_point(self):
        '''Add a point to the right score'''
        self.r_score += 1
        self.update_score()
    
    def game_over(self,winner):
        '''Display the winner'''
        self.clear()
        self.goto(0,0)
        self.write(arg=f'GAME OVER {winner} wins!',align='center',font=('Courier',30,'normal'))