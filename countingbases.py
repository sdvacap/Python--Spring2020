#students
#Sarah Vaca
#February 17, 2020

#Add any variables
#Ask for inputs
#Print results

#Calculate values

import random

bases=["A","C","T","G"]

sequence=random.choices(bases,k=100)

print(sequence)

#1) Calculate the number of G's
G_bp = sequence.count("G")

#2) Calculate the number of A's
A_bp = sequence.count("A")

#3) Calculate(together) the number of A's and C's
A_and_G_bp = sequence.count("A") + sequence.count("C")

#print results
print("Number of G's " + str(G_bp))
print("Number of A's " + str(A_bp))
print("Number of A's and G's " + str(A_and_G_bp))
