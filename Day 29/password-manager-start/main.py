
# Day 29 project: Password Manager 
# Day 30 upgrades made

import random,json
from tkinter import *
from tkinter import messagebox
import pyperclip

BG = "#E9DAC1"
FONT = ("Verdana", 8, "bold")
FONT2 = ("Verdana", 10)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator 
def generate_password():
    '''Generates a random password'''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    
    entry_3.insert(0,password)

#print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    '''Saves the password to the password file'''
    website = entry_1.get()
    email_id = entry_2.get()
    password = entry_3.get()
    
    new_data = {website:{'email_id':email_id, 'password':password}}
    
    if len(website) == 0 or len(email_id) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please enter all the fields")
    
    else:
        is_ok = messagebox.askokcancel(title = "Confirm",message= f"Do you want to save this password?\n\nWebsite: {website}\nEmail ID: {email_id}\nPassword: {password}")
        
        if is_ok:
            # with open("Day 29/password-manager-start/passwords.txt", "a") as file:
            #     file.write(f"\n{entry_1.get()}\t||\t{entry_2.get()}\t||\t{entry_3.get()}")
            #     messagebox.showinfo("Success", "Password saved successfully and copied to clipboard")
            #     pyperclip.copy(password) #copies the password to the clipboard
            try:
                with open ("Day 29\password-manager-start\passwords.json",'r') as json_file:
                    data = json.load(json_file) #loads the json file
            
            except FileNotFoundError:
                with open ("Day 29\password-manager-start\passwords.json",'w') as json_file:
                    json.dump(new_data, json_file, indent=4)
                messagebox.showinfo("Success", "Password saved successfully and copied to clipboard")
            
            else:
                data.update(new_data) #updates the data
                with open ("Day 29\password-manager-start\passwords.json", "w") as json_file:
                    json.dump(data,json_file,indent=4) # saves the data to the json file
                messagebox.showinfo("Success", "Password saved successfully and copied to clipboard")
            
            finally:
                pyperclip.copy(password) #copies the password to the clipboard
                entry_1.delete(0, END)
                entry_3.delete(0, END)
                
# ---------------------------- PASSWORD FINDER ------------------------------- #

def search_password():
    '''Searches the password from the password file'''
    try:
        with open ("Day 29\password-manager-start\passwords.json",'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No passwords saved yet")
    else:
        website = entry_1.get()
        if website in data:
            messagebox.showinfo(f"{website}", f"\nEmail: {data[website]['email_id']}\nPassword: {data[website]['password']}")
            pyperclip.copy(data[website]['password'])
            entry_3.insert(0,data[website]['password'])
        else:
            messagebox.showerror("Error", "No password found for this website")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx =30 ,pady =30 ,bg=BG)
#window.minsize(width=400, height=400)
window.title("Password Manager")


canvas = Canvas(width=200, height=200,bg=BG, highlightthickness=0)
lock_image = PhotoImage(file="Day 29\password-manager-start\logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

label_1 = Label(window, text="Website: ", font=FONT2, bg=BG,highlightthickness=0)
label_1.grid(row=1, column=0)
label_1.config(padx=5, pady=5)

label_2 = Label(window, text="Email/Username: ", font=FONT2, bg=BG,highlightthickness=0)
label_2.grid(row=2, column=0)
label_2.config(padx=5, pady=5)

label_3 = Label(window, text="Password: ", font=FONT2, bg=BG,highlightthickness=0)
label_3.grid(row=3, column=0,columnspan=1)
label_3.config(padx=5, pady=5)

entry_1 = Entry(window, font=FONT2,width=21)
entry_1.focus()
entry_1.grid(row=1, column=1,columnspan=1)

entry_2 = Entry(window, font=FONT2,width=35)
entry_2.grid(row=2, column=1,columnspan=2)
entry_2.insert(0, "amar@xyz.com")


entry_3 = Entry(window, font=FONT2,width=21)#show="*"
entry_3.grid(row=3, column=1)


generate_pass = Button(window, text="Generate", font=FONT, bg=BG,width=12,command=generate_password) #command=generate_password
generate_pass.grid(row=3, column=2,columnspan=1)
generate_pass.config(padx=5, pady=5)

add_button = Button(window, text="Add", font=FONT, bg=BG,width=36,command=add_password) #command=add_password
add_button.grid(row=4, column=1,columnspan=2)
add_button.config(padx=10, pady=10)

search_button = Button(window, text="Search", font=FONT, bg=BG,width=12,command=search_password) #command=search_password
search_button.grid(row=1, column=2,columnspan=1)
search_button.config(padx=5, pady=5)

window.mainloop()