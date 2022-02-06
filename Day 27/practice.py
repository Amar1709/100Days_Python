# Day 27 practice

# import tkinter as tk

# window = tk.Tk()
# window.title("Tkinter Practice")
# window.minsize(width=500, height=300)

# # Label

# my_label = tk.Label(text="Hello World",font=("Arial",20,"bold"))
# my_label.pack(expand=True, fill="both")

# window.mainloop()


# Unlimited Positional arguments - *args
# def add(*args):
#     print(sum(args))
#     # print(args) # args is a tuple

# add(1,2,3,4,5)

# Unlimited Keyword arguments - **kwargs
def calculate(n,**kwargs): 
    print(kwargs)   # kwargs is a dictionary
    # for key,value in kwargs:
    #     print(key)
    #     print(value)
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

calculate(2,add=7,multiply=5)