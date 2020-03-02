#AT Content
#Sarah Vaca
#March 02,2020

#Write a program that will print out the AT content of this DNA sequence:
#ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT 

#Use normal mathematical symbols like add (+), subtract (-), multiply (*), divide (/) and parentheses to carry out calculations on numbers in Python

###STEP 1
#create the variable for the sequence
sequence=("ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT")     

###STEP 2
#for calculate the As content in the sequence 
print("The As content in the sequence is",sequence.count("A"))  
#for calculate the Ts content in the sequence                                                  
print("The Ts content in the sequence is",sequence.count("T"))

###STEP 3         
#use "count" to calculate the TA content in the sequence                                                 
print("The AT content in the sequence is", sequence.count("A")+sequence.count("T"))
