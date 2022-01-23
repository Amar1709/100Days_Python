# Day 17 - Quiz Project

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo, end_logo
from time import sleep

from unicodedata import name
from os import system, name

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')


question_bank = []

for item in question_data:
    my_ques = Question(item["question"],item["correct_answer"])
    question_bank.append(my_ques)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    clear()
    print(f"{logo}\n")
    quiz.next_question()
    sleep(1)

clear()    
print(logo)
print("You have completed the quiz!\n")
print(f"Your final score is : {quiz.score}/{quiz.question_number}\n")
print(end_logo)