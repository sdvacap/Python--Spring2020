#Restriction Enzyme 
#Sarah Vaca
#March 02,2020

#ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT
#The sequence contains a recognition site for the EcoRI restriction enzyme, which cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk)
#Write a program which will calculate the size of the two fragments that will be produced when the DNA sequence is digested with EcoRI

###STEP 1
#Create a variable for the sequence 
sequence=("ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT")
print(sequence)
###STEP 2
#Find the motif G*AATTC in the sequence and cut between G and A, to obtain two fragments 
position=sequence.find("GAATTC")            #find the motif "GAATTC" inside the sequence
RE=sequence.replace("GAATTC","G AATTC")     #replace "GAATTC" for "G AATTC", so you will know were the RE will cut
print(RE)                                   #print the sequence with the space, you will see where the RE will cut 

fragments=RE.split(" ")                     #split the sequence with a space 
print(fragments[0])                         #shows the first fragment
print(fragments[1])                         #shows the second fragment


###STEP 3
#Calcutate the size of the first fragment
frag1=len(fragments[0])                     #calculate the size of the first fragment
print("The size of the first fragment is", frag1)
 
#Calcutate the size of the second fragment
frag2=len(fragments[0])                     #calculate the size of the second fragment
print("The size of the second fragment is", frag2)  
