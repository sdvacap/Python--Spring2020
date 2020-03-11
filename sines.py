#Sines 
#Sarah Vaca
#March 9, 2020

#1. Use avan_rm.bed file in “/lustre/work/jenjense/python/Pandas”
#cd /lustre/work/jen
#cp aVan_rm.bed /lustre/work/svaca/python
#cd /lustre/work/svaca/python

#2. Make sure it has proper column names
#nano aVan_rm.bed

#3.  Determine what families are in there (SINE, etc)
##import modules
import pandas as pd
print("#########################")
#read in my bed file 
print("Read bed file...")
sines=pd.read_bed("aVan_rm.bed")        #read in my bed file 
print(aVan_rm())

print("#########################")
print("What families are?")
sines.Family.unique()

#4.  Create new dataframe from that file using only elements in family “SINE” 
print("#########################")
print("New dataframe form family SINEs")
data={"metulj","ZenoSINE"}
new_sines=pd.DataFrame(data)
print(new_sines)

print("#########################")
#5.  Drop columns “Strand” and “Score”
print("Drop columns Strand and Score..")
sines.drop(["Strand”, "Score"], axis=1 )
print(sines)

print("#########################")
#6.  Create new column “Length”
print("New column "Length")
length=["127", "341", "123","132"]
sines["Length"]=length
print("sines")

print("#########################")
#7.  Determine min, max, and mean for all SINEs
print("What is the minimum, maximun and mean for all SINEs?")
print(sines["Family"].min(), sines["Family"].max())
print(sines["Family"].sum()/len(sines))
print(sines["Family"].mean())


#print("#########################")
#8.  Determine min, max, and mean length for each sub-family of SINE (metulj and ZenoSINE)
#print("What is the minimum, maximun and mean length for each sub-family of SINE?")
#print("sines")

#print("#########################")
