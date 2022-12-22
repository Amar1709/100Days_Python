
# Day 34 - Quizzler App - Tkinter

from tkinter import *
from tkinter import PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_COLOR = "#EEEDDE"
GREEN = "#65C18C"
RED = "#EF6D6D"
FONT = ("Verdana", 12, "italic")



class QuizInterface() :
    '''The QuizInterface class'''
    
    def __init__(self, quiz_brain: QuizBrain):
        '''Initializes the QuizInterface class'''
        
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR,padx=20,pady=20)
        
        self.score_label = Label(self.window, text="Score: 0", font=FONT, bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(self.window, width=300, height=250,background=CANVAS_COLOR,highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)
        self.ques_text = self.canvas.create_text(150, 125, width=280, text="What is the Question?", font=FONT) 
        
        right_img = PhotoImage(file="Day 34/quizzler-app-start/images/true.png")
        wrong_img = PhotoImage(file="Day 34/quizzler-app-start/images/false.png")
        
        self.true_button = Button(image=right_img,highlightthickness=0,command=self.true_choice)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=wrong_img,highlightthickness=0,command=self.false_choice)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
        
    def get_next_question(self):
        '''Gets the next question'''
        self.canvas.config(background=CANVAS_COLOR)
        if self.quiz.still_has_questions():
            self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=f"{self.quiz.question_number}. {self.quiz.q_text}") 
        else:
            self.canvas.itemconfig(self.ques_text, text="You've completed the Quiz!")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)
            
    
    def true_choice(self):
        '''User chooses the true option'''
        self.feedback('true')
        
    def false_choice(self):
        '''User chooses the false option'''
        self.feedback('false') 
        
    def feedback(self, user_choice):
        '''Checks the answer given by the user'''
        if self.quiz.check_answer(user_choice):
            self.canvas.config(background=GREEN)
        else:
            self.canvas.config(background=RED)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000,self.get_next_question)