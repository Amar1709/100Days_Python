
# Day 28 Pomodoro - Timer using Tkinter

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFEEAD"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
REPS = 0
TICKS = ""
timer_clock = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    '''Resets the timer'''
    window.after_cancel(timer_clock)
    canvas.itemconfig(timer_text, text="00:00")
    TICKS = ""
    tick_label.config(text=TICKS, fg=GREEN,bg=YELLOW)
    timer_label.config(text="Timer", fg=GREEN,bg=YELLOW)
    global REPS
    REPS = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    '''Starts the timer'''
    global REPS
    REPS+=1
    if REPS%8 == 0:
        timer_label.config(text="Break", fg=RED,bg=YELLOW)
        count_down(LONG_BREAK_MIN*60)
    elif REPS %2 == 0:
        timer_label.config(text="Break", fg=PINK,bg=YELLOW)
        count_down(SHORT_BREAK_MIN*60)   
    else:
        timer_label.config(text="Work", fg=GREEN,bg=YELLOW)
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    '''Counts down from count to 0'''
    global TICKS
    count_min = count // 60
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer_clock
        timer_clock = window.after(1000, count_down, count-1)
    else:
        if REPS % 2 != 0:
            TICKS += "✔"
            tick_label.config(text=TICKS, fg=GREEN,bg=YELLOW)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=100, pady=50,bg=YELLOW)
window.minsize(width=500, height=300)
window.title("Pomodoro Timer")


canvas = Canvas(width=300, height=300,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day 28/pomodoro-start/tomato.png")
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(150, 178, text="00:00", font=(FONT_NAME, 25, "bold"),fill="white")
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0, column=1)
timer_label.config(padx=20, pady=20)


start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"),highlightthickness=0,command=start_timer) #command=start_timer
start_button.grid(row=2, column=0)
start_button.config(padx=5, pady=5)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"),highlightthickness=0,command=reset_timer) #command=reset_timer
reset_button.grid(row=2, column=2)
reset_button.config(padx=5, pady=5)

tick_label = Label(font=(FONT_NAME, 20, "bold"),fg=GREEN,bg=YELLOW)
tick_label.grid(row=3, column=1)

window.mainloop()