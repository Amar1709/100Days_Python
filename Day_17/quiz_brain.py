# Day 17 project - Quiz

import random
from time import sleep
from art import logo, end_logo

from unicodedata import name
from os import system,name

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.total = len(q_list)
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
       
    def next_question(self):
        current_question = random.choice(self.question_list)
        self.question_number += 1
        choice = input(f"Q{self.question_number}. {current_question.text}? ('True'/'False') : ")
        self.check_answer(choice,current_question)
        
    def check_answer(self,choice,current_question):
        if choice == current_question.answer:
            self.score += 1
            print("You got this right!")
            print(f"Your score is {self.score}")
            self.question_list.remove(current_question)
        
        else:
            print(f"The correct answer is: {current_question.answer}")
            print("Sorry you got this wrong!")
            sleep(1)
            clear()
            print(f"{logo}\n")
            print(f"Your final score is {self.score}/{self.total}\n")
            print(f"{end_logo}")
            exit()