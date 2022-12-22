# Day 10 - Calculator

from title import titleArt
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calc(choice,n1,n2):
    if choice=="+":
        result = add(a,b)
    elif choice=="-":
        result = subtract(a,b)
    elif choice=="*":
        result = multiply(a,b)
    else:
        result = divide(a,b)
    return result

if __name__=="__main__":
    titleArt()
    print('\n=====================================\n')
    
    a = int(input("What is your first number? "))
    print("\n+\n-\n*\n/")
    choice = input("\nPick an operation => ")
    b = int(input("What's the next number? "))
    
    result = calc(choice,a,b)
    
    while(True):
        print(f"\n{a}{choice}{b} = {result}") 
        ch2 = input(f"Type 'y' to continue calculating with {result} or type 'n' to start new calculation..(type 'end' to exit)  => ")
        if ch2=='y':
            os.system('cls')
            titleArt()
            print('\n=====================================\n')
            a = result
            print("\n+\n-\n*\n/")
            choice = input("\nPick an operation => ")
            b = int(input("What's the next number? "))
            result = calc(choice,a,b)
        
        elif ch2=='n':
            os.system('cls')
            titleArt()
            print('\n=====================================\n')
            a = int(input("What is your first number? "))
            print("\n+\n-\n*\n/")
            choice = input("\nPick an operation => ")
            b = int(input("What's the next number? "))
            result = calc(choice,a,b)
        
        else:
            print("\n====== Thank You ======\n")
            break
        
    