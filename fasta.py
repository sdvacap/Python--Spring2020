#fasta.py
#Sarah Vaca
#May 5, 2020

#import modules to use
import argparse
from Bio import SeqIO
import matplotlib.pyplot as plt

#1. Argparse to read in fasta file “dIul.fa” AND the taxon name “dIul”
############################################################################################
####################################### ARGUMENTS ##########################################
############################################################################################

ap=argparse.ArgumentParser()
ap.add_argument("-f", "--FASTA", required=True, help="read the fasta file")
ap.add_argument("-n", "--NAME", required=True, help="read the taxon name file")
args=vars(ap.parse_args())

#2. Determine how many records are in the file
#for record in SeqIO.parse("dIul.fa", "fasta"):
#    print(record.id)
    
num_rec=[record for record in SeqIO.parse("dIul.fa", "fasta")]
    print('The number of records in the file is: \n' , len(num_rec))    

#3. What is the shortest record? What is the longest record? 
short=[record for record in SeqIO.parse("dIul.fa", "fasta")]
print('The shortest record is: \n', min(short, key=len)
long=[record for record in SeqIO.parse("dIul.fa", "fasta")]
print('The longest record is: \n' , max(long, key=len)

#4. Run your GC function on each record sequence
#Function to calculate the GC content
def GC_calculator(sequence):
    G=sequence.count("G")
    C=sequence.count("C")
    A=sequence.count("A")
    T=sequence.count("T")
    G_C=(G+C)/(G+C+A+T)
    return G_C
    
#Calculation of the GC content for each record sequence     
rec=[]
for record in SeqIO.parse("dIul.fa", "fasta"):
    rec.append(str(record))
    
print(rec)    

GC_content=[]
for i in rec:
    GC_calculator(i)
    print('The GC content for each record sequence is: \n', GC_content)    

#5. Plot a histogram of GC content (Hint: may need to save the results first)
plt.hist(GC_content)
plt.grid(axis="y", alpha=0.75)
plt.xlabel("GC Content", fontsize=10)
plt.ylabel("Frequency", fontsize=10)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title("GC Content Histogram", fontsize=10)
plt.savefig("GC_content_hist")
plt.show()

#6. Which record has most GC content? Which record has least GC content?
more=[record for record in SeqIO.parse("dIul.fa", "fasta") if GC_calculator(i) == max(GC_content)]
print('The record with most GC content: \n', record.id, GC_calculator(i))
less=[record for record in SeqIO.parse("dIul.fa", "fasta") if GC_calculator(i) == min(GC_content)]
print('The record with least GC content: \n', record.id, GC_calculator(i))

#7. Translate each record
trans_rec=[record.translate for record in SeqIO.parse("dIul.fa", "fasta")]
print(trans_rec)

#8. Which record has most Stop codons? Which record has least Stop codons?
stop=[]
for record in SeqIO.parse("dIul.fa", "fasta"):
      stop.append(record.seq.translate().count("*"))
    
print(stop)    

more_stop=[record for record in SeqIO.parse("dIul.fa", "fasta") if trans_rec == max(stop)]
print('The record with most Stop codons: \n', record.id, max(stop))
less_stop=[record for record in SeqIO.parse("dIul.fa", "fasta") if trans_rec == min(stop)]
print('The record with least Stop codons: \n', record.id, min(stop))
