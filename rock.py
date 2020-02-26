#rock.py
#Sarah Vaca
#February 25,2020

#Write a script that will play rock, scissors against the computer.
#You will nedd to import module to select computer's choice

import random

#Ask user to choose between rock, paper, scissors
#user input
user=input("rock, paper, scissors! 1, 2, 3!!")

#game options
ppt=("rock", "paper", "scissors")
print(ppt)

#Have computer randomly choose between rock, paper, scissors
computer=random.choice(ppt)

#Print results of the game 
print("Computer turn:" + computer)
if computer == "rock" and user == "paper":
    print("Great option!")
elif computer == "rock" and user == "scissors":
    print("Sorry! Try again")
elif computer == "paper" and user == "rock":
    print("Sorry! Try again")
elif computer == "paper" and user == "scissors":
    print("Great option!")
elif computer == "scissors" and user == "rock":
    print("Great option!")
elif computer == "scissors" and user == "paper":
    print("Sorry! Try again")
else:
    print("Tie!")
