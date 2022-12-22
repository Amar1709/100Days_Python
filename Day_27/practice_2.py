# Day 27 practice - GUI

import tkinter as tk

window = tk.Tk()
window.title("Tkinter Practice")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label and Button

def button_clicked():
    my_label.configure(text=entry.get())

def button_clicked2():
    my_label.configure(text="I said don't click me!")

my_label = tk.Label(text="Hello World",font=("Arial",20,"bold"))

my_label.grid(row=0,column=0)

my_label.config(padx=30, pady=10)



# Entry

entry = tk.Entry(font=("Arial",12,"bold"),width=10)
entry.grid(row=2,column=3)

my_button = tk.Button(text="Click Me",font=("Arial",8,"bold"),command=button_clicked)
my_button.grid(row=1,column=1)

my_button2 = tk.Button(text="Don't Click Me",font=("Arial",8,"bold"),command=button_clicked2)
my_button2.grid(row=0,column=2)

window.mainloop()