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
sequence.count("G")

#2) Calculate the number of A's
sequence.count("A")

#3) Calculate(together) the number of A's and C's
sequence.count("A") + sequence.count("C")
