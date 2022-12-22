import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# print(rock)

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# print(paper)

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# print(scissors)

choice = int(input("What do you choose?\n1 - Rock\n2 - Paper\n3 - Scissors\nEnter choice - "))

List = [rock,paper,scissors]

comp_choice = random.randint(0,2)

print("Your play")
print(List[choice -1])

print("\n\nComputer's play")
print(List[comp_choice])

if (List[choice-1] ==rock and List[comp_choice] ==scissors) or (List[choice -1]==scissors and List[comp_choice] ==paper) or (List[choice -1] ==paper and List[comp_choice]==rock):
    print("You win")
    
else:
    print("You lose")
    