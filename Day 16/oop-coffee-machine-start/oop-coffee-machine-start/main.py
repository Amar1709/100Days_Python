# Day 16 Project - Coffee Machine OOP version

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo, icon_image

print(f"{logo}\n\n{icon_image}")

M1 = Menu()
money1 = MoneyMachine()
C1 = CoffeeMaker()

while(True):
    
    choice = input(f"\nWhat would you like?({M1.get_items()}): ")
    
    if choice == "exit":
        print("\nThank you for visiting!...")
        break
    
    elif choice == "report":
        C1.report()
        money1.report()
        continue
    
    else:
        drink = M1.find_drink(choice)
        
        if drink:
            
            if C1.is_resource_sufficient(drink):
                
                if money1.make_payment(drink.cost):
                    C1.make_coffee(drink)
                    continue
                
                else:
                    print("Sorry, you don't have enough money!")
                    continue
                    
            else:
                continue
    
