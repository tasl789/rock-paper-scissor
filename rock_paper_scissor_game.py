""" 
WORKFLOW OF PROJECT:
1 - input from user(rock,paper,scissor) 
2 - computer choice(computer will choose randomly not conditionally)
3 - result print

Cases:
A - rock
rock - rock = tie
rock - paper = paper win
rock - scissor = rock win

B - paper 
paper - paper = tie 
paper - rock = rock win
paper - scissor = scissor win

C - scissor
scissor - scissor = tie
scissor - rock = rock win
scissor - paper = paper win
"""

import random

item_list = ["rock","paper","scissor"]

user_choice = input("Enter your move : rock ,paper, scissor = ")
computer_choice = random.choice(item_list)

print("user choice = ",user_choice)
print("computer choice = ",computer_choice)

if user_choice == computer_choice:
  print("both are chooses same: => tie")


elif user_choice == "rock":
  if computer_choice == "paper":
    print("paper covers rock => computer win")
  else:
    print("rock smashes scissor => you win")

elif user_choice == "paper":
  if computer_choice == "scissor":
    print("scissor cuts paper => computer win")
  else:
    print("paper covers rock => you win")

elif user_choice == "scissor":
  if computer_choice == "paper":
    print("scissor cuts paper => you win")
  else:
    print("rock smashes scissor => computer win")

# finally our code done play enjoy  and create rock,paper,scissor game using python code by tasleem sulthana....

# example of executing code and entered by user
#Enter your move : rock ,paper, scissor = rock
#user choice =  rock
#computer choice =  scissor
#rock smashes scissor => you win
