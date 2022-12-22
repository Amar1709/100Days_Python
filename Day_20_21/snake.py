# Day 20 _ Snake game project

from turtle import Turtle


move_forward = 20
go_up = 90
go_down = 270
go_right = 0
go_left = 180

class Snake:
    
    def __init__(self):
        '''Initializes snake body'''
        self.length = 3
        self.snake_body = []
        self.build_snake()
        self.head_of_snake = self.snake_body[0]
    
    def build_snake(self):
        '''Builds initial snake body'''
        for i in range(self.length):
            new_part = Turtle(shape='square')
            new_part.fillcolor('white')
            new_part.penup()
            new_part.setpos((-1*20*i),0)
            self.snake_body.append(new_part)
    
    def extend_snake(self):
        '''Increases length of snake'''
        self.length+=1
        new_part = Turtle(shape='square')
        new_part.fillcolor('white')
        new_part.penup()
        new_part.setpos(self.snake_body[-1].position())
        self.snake_body.append(new_part)
    
    def move(self):
        '''Helps snake to move'''
        for part in range(self.length-1, 0, -1):
            new_x = self.snake_body[part - 1].xcor()
            new_y = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(new_x,new_y)
        self.head_of_snake.forward(move_forward)
        
    def up(self):
        '''Changes snake direction to up on keypress'''
        if self.head_of_snake.heading() != go_down:
            self.head_of_snake.setheading(go_up)
    def down(self):
        '''Changes snake direction to down on keypress'''
        if self.head_of_snake.heading() != go_up:
            self.head_of_snake.setheading(go_down)
    def right(self):
        '''Changes snake direction to right on keypress'''
        if self.head_of_snake.heading() != go_left:
            self.head_of_snake.setheading(go_right)
    def left(self):
        '''Changes snake direction to left on keypress'''
        if self.head_of_snake.heading() != go_right:
            self.head_of_snake.setheading(go_left)
        