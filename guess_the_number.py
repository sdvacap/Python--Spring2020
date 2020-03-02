#"Guess-the-Number" game
#Sarah Vaca
#February 24,2020

#Create a ”Guess-the-Number” game. 
#Include algorithm
#Include comments
#Make smart use of print statements and names
#User must guess a number randomly chosen by computer. Computer will tell user if it’s too high or too low and let the user try again.

#use random module 
#with an input ask the user to guess a number between 1 to 30
  
import random 

#game options
num=range(1,31)                 #numbers between 1 and 30
computer=random.choice(num)     #it use the module "random", so the computer would choice randomly a number between 1 and 30


#input
guess=input("I am thinking a number between 1 an 30. Which numnber is it?")     #input asking to guess a number
user=int(guess)

while computer !="user":
    print
    if user>computer:
        print("Too high! Please, try again")    #Tell the user the number is too high and then to try again        
        user=int(input("I am thinking a number between 1 an 30. Which numnber is it?"))#user=int(guess)
    elif user<computer:
        print("Too low! Please, try again")     #Tell the user if the number is too high amd then to try again 
        user=int(input("I am thinking a number between 1 an 30. Which numnber is it?"))#user=int(guess)
    else:
        print("Congratulations! You guess!")    #If the user guess the number
        break                                   #For show the message just one time  
