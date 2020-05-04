#Sines 
#Sarah Vaca
#March 17, 2020

#1. Use avan_rm.bed file in “/lustre/work/jenjense/python/Pandas”
#cd /lustre/work/jen
#cp aVan_rm.bed /lustre/work/svaca/python
#cd /lustre/work/svaca/python

#2. Make sure it has proper column names
#read in my bed file 
##import modules
import pandas as pd
print("Read bed file...")
bed=pd.read_csv("aVan_rm.bed", sep= "\t")        

print("#########################")
print("Rename columns...")
column_names=["Scaffold", "Start", "Stop", "Element", "Score", "Strand", "Family", "Sub-Family", "Divergence"]
bed=pd.read_csv("aVan_rm.bed", names=column_names, sep= "\t")       #give name to columns
print(bed.head())

#3.  Determine what families are in there (SINE, etc)
print("#########################")
print("What families are?")
families=bed.Family.unique()
print("The families in bedfile are: ", families)

#4.  Create new dataframe from that file using only elements in family “SINE” 
print("#########################")
print("New dataframe form family SINEs")
data={"metulj","ZenoSINE"}
new_bed=bed[bed["Family"]=="new_bed"]
print(new_bed.head())

print("#########################")
#5.  Drop columns “Strand” and “Score”
print("Drop columns Strand and Score..")
new_bed=new_bed.drop(["Strand", "Score"], axis=1 )
print(new_bed.head())

print("#########################")
#6.  Create new column “Length”
print("New column", "Length")
new_bed["Length"]=new_bed["Stop"]-new_bed["Start"]
print("New column created", "Length", "between Stop and Start")
print(new_bed.head())

print("#########################")
#7.  Determine min, max, and mean for all SINEs
print("What is the minimum, maximun and mean for all SINEs?")
print(new_bed["Length"].min())
print(new_bed["Length"].max())
print(new_bed["Length"].mean())

print("#########################")
#8.  Determine min, max, and mean length for each sub-family of SINE (metulj and ZenoSINE)
print("What is the minimum, maximun and mean length for each sub-family of SINE?")
print(new_bed.groupy("Sub-Family")["Length"].min())
print(new_bed.groupy("Sub-Family")["Length"].max())
print(new_bed.groupy("Sub-Family")["Length"].mean())
print("#########################")
