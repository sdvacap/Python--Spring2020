#functions.py
#Sarah Vaca
#April 21, 2020

#Write a script with a function that will calculate the GC content for a DNA sequence

###1. Create a random DNA sequence that is 5,000 bp long – STRING, no spaces, no commas
import random 
seq=random.choices("AGTC", k=5000)

','.join(seq)                                   #join the bases by comma
bp_DNA=','.join(seq)
bp_DNA.replace(',','')                          #replace the comma with nothing
DNA=bp_DNA.replace(',','')
print('Random DNA seq is \n', DNA)

###2. Break the sequence into smaller sequences 100 bp long
bp=DNA[bp:bp+100]                                    #   

small_seq=[]
for bp in range (0, len(DNA), 100):
    small_seq.append(bp)
    
print('Small sequence of 100bp long: \n' , small_seq)
    
###3. In a loop, use the GC function you created to calculate the GC content for each smaller sequence

#Function to calculate the GC content
def GC_calculator(sequence):
    G=sequence.count(G)
    C=sequence.count(C)
    G_C=(G+C)/100
    return G_C

#Function to calculate the GC content for each smaller sequence 
GC_content=[]
for i in small_seq:
    GC_calculator(i)
print('The GC content for each smaller sequence is: \n', GC_content)    
