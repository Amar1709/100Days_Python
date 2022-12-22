# Day 27 - Project - GUI - Tkinter - Miles to Kilometers

import tkinter as tk

# Fonts
FONT = ("Arial",12,"bold")

window = tk.Tk()
window.background = "gray"
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Function

def MilesToKm():
    miles = float(miles_entry.get())
    km = miles * 1.60934
    ans_label.config(text=f"{round(km,2)}")

# Labels

miles_label = tk.Label(text="Miles",font=FONT)
miles_label.grid(row=0,column=2)

text_label = tk.Label(text="is equal to",font=FONT)
text_label.grid(row=1,column=0)

ans_label = tk.Label(text="0",font=FONT) # Answer
ans_label.grid(row=1,column=1)
ans_label.config(padx=20, pady=20)

km_label = tk.Label(text="Km",font=FONT)
km_label.grid(row=1,column=2)

# Entry

miles_entry = tk.Entry(width=10)
miles_entry.grid(row=0,column=1)

# Button

calc_button = tk.Button(text="Calculate",command=MilesToKm)
calc_button.grid(row=2,column=1)

# Main Loop

window.mainloop()