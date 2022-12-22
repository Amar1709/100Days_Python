# Day 15 project - Coffee Machine

from data import MENU, resources
from art import icon_image, logo

print(f"{logo}\n")
print(icon_image)

money = 0

while(True):
    supplies = False
    budget = 0
    scarcity = ""

    choice = input("\nWhat would you like? (espresso / latte / cappuccino) : ")
    
    if choice in MENU:
        
        if (MENU[choice]['ingredients']['water']) <= resources["water"]:
            if MENU[choice]["ingredients"]["milk"] <= resources["milk"]:
                if MENU[choice]["ingredients"]["coffee"] <= resources["coffee"]:
                    supplies = True
                else:
                    supplies = False
                    scarcity = 'coffee'
            else:
                supplies = False
                scarcity = 'milk'
        else:
            supplies = False
            scarcity = 'water'
        
        if supplies:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickels = int(input("how many nickels?: "))
            pennies = int(input("how many pennies?: "))
            
            budget = float((quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies* 0.01))
            
            if budget >= float(MENU[choice]["cost"]):
                change = round(float(budget - MENU[choice]["cost"]),2)
                print(f"Here is ${change} in change")
                print(f"Here is your {choice} ☕. Enjoy!")
                
                resources["water"] -= MENU[choice]["ingredients"]["water"]
                resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                
                money +=  float(MENU[choice]["cost"])
                continue
            
            else:
                print("Sorry, you don't have enough resources!")
                continue
                
        else:
            print(f"Sorry there is not enough {scarcity}")
            continue
    
    elif choice == "report":
        print(f"\nWater: {resources['water']}ml")
        print(f"\nMilk: {resources['milk']}ml")
        print(f"\nCoffee: {resources['coffee']}g")
        print(f"\nMoney = ${money}")
    
    elif choice == "exit":
        print(f"\nThank you for visiting!...\nTotal money = ${money}")
        break
    
    else:
        print("Invalid choice...please try again...")
        continue
        