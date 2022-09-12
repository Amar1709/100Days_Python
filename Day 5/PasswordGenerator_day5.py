#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass_letters = ''
pass_symbols = ''
pass_numbers = ''

password_final = ''

for i in range (nr_letters):
  pass_letters = pass_letters + random.choice(letters)
for i in range (nr_symbols):
  pass_symbols = pass_symbols + random.choice(symbols)
for i in range (nr_numbers):
  pass_numbers = pass_numbers + random.choice(numbers)

password_final = pass_letters + pass_symbols + pass_numbers

print(f"Your password is: {password_final}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_final2 = ''

Rword = ''
n = len(password_final)

password_final = list(password_final)
for i in range (n):
  Rword = random.choice(password_final)
  password_final2 = password_final2 + Rword 
  password_final.remove(Rword)

print(f"Your password is: {password_final2}")