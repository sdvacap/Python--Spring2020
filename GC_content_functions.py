#functions.py
#Sarah Vaca
#April 21, 2020

#Write a script with a function that will calculate the GC content for a DNA sequence

###1. Create a random DNA sequence that is 5,000 bp long – STRING, no spaces, no commas
import random 

seq=random.choices(['A','G','T','C'], k=5000)
DNA=''.join(seq)
print('Random DNA seq is \n', DNA)

###2. Break the sequence into smaller sequences 100 bp long                                  
small_seq=[]
for bp in range (0, len(DNA), 100):
    small_seq.append(DNA[bp:bp+100])
    
#small_seq=[DNA[bp:bp+100] for bp in range (0, 5000, 100)]    
print('Small sequence of 100bp long: \n' , small_seq)
    
###3. In a loop, use the GC function you created to calculate the GC content for each smaller sequence

#Function to calculate the GC content
#def GC_calculator(small_seq):
#    G_C=((small_seq.count("G"))+(small_seq.count("C")))/100
#    return (G_C * 100)     
            

def GC_calculator(small_seq):
    G=small_seq.count('G')
    C=small_seq.count('C')
    G_C=(G+C)/len(small_seq)
    return (G_C)

#def bp_count(seq, allowed_bases=['G','C']):
#    seq=seq.upper()
#    total_dna_bases=0
#    for base in allowed_bases:
#        total_dna_bases
#    dna_fraction=total_dna_bases / len(seq)
#    return(dna_fraction * 100)    

#Function to calculate the GC content for each smaller sequence 
GC_content=[GC_calculator(i) for i in small_seq]
print('The GC content for each smaller sequence is: \n', GC_content)    
