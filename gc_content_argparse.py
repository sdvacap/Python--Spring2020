#gc_content_argparse.py
#Sarah Vaca
#April 27, 2020

#import modules to use
import argparse
import random
import matplotlib.pyplot as plt

#########################################################################
############################### ARGUMENTS ###############################
#########################################################################

ap=argparse.ArgumentParser()
ap.add_argument("-l", "--LENGHT", required=True, type=int, help="enter the lenght of a entire sequence")
ap.add_argument("-p", "--SMALLSIZE", required=True, type=int, help="enter the size of a small sequence")
args=vars(ap.parse_args())

##1. Argparse the size of your random sequence
bases=['A','G','T','C']
seq=random.choices(bases, k=args["LENGHT"])
DNA=''.join(seq)
print('The size of your random seq is \n', DNA)

##2. Argparse the size of your smaller sequences
#break the random seq in smaller sequences
#bp=DNA[bp:bp+arg["SMALLSIZE"]]                                    
small_seq=[]
for bp in range (0, args["LENGHT"], arg["SMALLSIZE"]):
    small_seq.append(DNA[bp:bp+arg["SMALLSIZE"]])

print('The size of your small seq is \n' , small_seq)

#Function to calculate the GC content
def GC_calculator(sequence):
    G=sequence.count(G)
    C=sequence.count(C)
    G_C=(G+C)/arg["SMALLSIZE"]
    return G_C

#Function to calculate the GC content for each smaller sequence 
GC_content=[]
for i in small_seq:
    GC_calculator(i)
print('The GC content for each smaller sequence is: \n', GC_content)    

##3. Create a histogram for Gccontent *** new step ***
img=plt.hist(GC_content)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('GC Content', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('GC Content Histogram', fontsize=10)
plt.show()
