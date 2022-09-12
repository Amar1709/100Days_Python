# TipCalculator

bill = float(input("What is the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

pay = round((bill + (bill * tip / 100)) / people, 2)

print(f"Each person should pay: ${pay}")