# Day 2 - Tip Calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
p = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
n = int(input("How many people to split the bill? "))
pay = (bill + (bill * p / 100)) / n
print(f"Each person should pay: $ {pay:.2f}")