# Day 31 Project: Flash Card Project Start

from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}
flip_timer = ""
# ---------------------------- WORDS Flash Cards ------------------------------- #
try:
    data = pd.read_csv("Day 31/flash-card-project-start/data/words_to_learn.csv")

except FileNotFoundError:
    initial_data = pd.read_csv("Day 31/flash-card-project-start/data/french_words.csv")
    to_learn = initial_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")

#print(to_learn)
def flash_cards():
    '''Generates a random word from the dataframe'''
    global word,flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French",fill = "black")
    canvas.itemconfig(card_word, text = word["French"], fill = "black")
    canvas.itemconfig(card_view, image = card_front)
    
    flip_timer = window.after(3000, flash_cards_answer)
    
def flash_cards_answer():    
    '''Has the answer for the word'''
    canvas.itemconfig(card_title, text="English", fill = "White")
    canvas.itemconfig(card_word, text = word["English"], fill = "White")
    canvas.itemconfig(card_view, image = card_back)


def isknown():
    '''knows the word'''
    try:
        to_learn.remove(word)
        
    except ValueError:
        pass
    else:
        data = pd.DataFrame(to_learn)
        data.to_csv("Day 31/flash-card-project-start/data/words_to_learn.csv",index=False)
    finally:
        flash_cards()

#flash_cards()

# ***********************UI SETUP***************************

window = Tk()
window.configure(background=BACKGROUND_COLOR,padx=50,pady=50)
window.title("Flash Card Project")
flip_timer = window.after(3000, flash_cards_answer)

canvas = Canvas(window, width=800, height=526 , bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="Day 31/flash-card-project-start/images/card_front.png")
card_back = PhotoImage(file="Day 31/flash-card-project-start/images/card_back.png")
card_view = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0,columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40,"italic"), fill="black")
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60,"bold"), fill="black")

wrong_img = PhotoImage(file="Day 31/flash-card-project-start/images/wrong.png")

right_img = PhotoImage(file="Day 31/flash-card-project-start/images/right.png")

wrong_button = Button(window, image=wrong_img, bg=BACKGROUND_COLOR,highlightthickness=0,command=flash_cards)
wrong_button.grid(row=2, column=0)
right_button = Button(window, image=right_img, bg=BACKGROUND_COLOR,highlightthickness=0,command=isknown)
right_button.grid(row=2, column=1)

window.mainloop()