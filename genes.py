#genes
#Sarah Vaca
#April 08, 2020

#GOAL: Determine length of large genes on mRNA strand
#Assumptions: Genes are recognized as segments of RNA separated by start codon AUG

###1. Generate a random RNA sequence into a STRING 1000 base pairs long
import random 
bases=['A','G','U','C']
seq=random.choices(bases, k=1000)

','.join(seq)                                   #join the bases by comma
RNA=','.join(seq)
RNA.replace(',','')                             #replace the comma with nothing
mRNA=RNA.replace(',','')
print('Random RNA seq is \n', mRNA)

###2. Create list of genes that are separated by start codon
genes=mRNA.split('AUG')                          #find AUG and split the seq
print('The list of genes is \n' , genes)

###3. Create list of large genes (>50bp) 
l_genes=[]
for i in genes:                                 #for each 'i' element in 'genes'
    if len(i)>50:                               #select the genes larger than 50bp
        l_genes.append(i)                       #add them to i
print('List of large genes is \n' , l_genes)
    
###4. Determine length of large genes
for i in l_genes:                               #for each 'i' element in l_genes
    print('The length of the gene is \n', len(i))       #show the length of genes larger than 50bp 
