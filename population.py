#population
#Calculate population
#Sarah Vaca
#February 03,2020

#import modules
#Add any variables
#Ask fot input
#Calculation of population
#Print results

import math 

birth_sec = 7
death_sec = 13
inmigrant_sec = 35
population_year = 307357870
sec_year = 1440
sec_min = 60

print("birth sec", birth_sec)
print("death sec", death_sec)
print("inmigrant sec", inmigrant_sec)
print("population year", population_year)
print("sec year", sec_year)
print("sec min", sec_min)

birth_year = (sec_year / birth_sec)
death_year = (sec_year / death_sec)
inmigrant_year = (sec_year / inmigrant_sec)

print("birth year", birth_year)
print("death year", death_year)
print("inmigrant year", inmigrant_year)

#Inputs
birth_input = input("How many birth year? ")
death_input = input("How many death year? ")
inmigrant_input = input("How many inmigrant year? ")

#population = (population_year + birth_input + inmigrant_input) - (death_input)
#print(population)

birth_int = int(birth_input)
death_int = int(death_input)
inmigrant_int = int(inmigrant_input)
population = (population_year + birth_int + inmigrant_int) - (death_int)
print(population)
