#sines_argparse.py
#Sarah Vaca
#April 30, 2020

#import modules to use
import argparse
import pandas as pd

############################################################################################
####################################### ARGUMENTS ##########################################
############################################################################################

ap=argparse.ArgumentParser()
ap.add_argument("-r", "--READ", required=True, help="read a bedfile")
ap.ap.add_argument("-f", "--FAMILY", required=True, help="assign a family")
ap.ap.add_argument("-s", "--SIZE", required=True, type=int, help="enter the genome size")
args=vars(ap.parse_args())

#1. Use avan_rm.bed file in “/lustre/work/jenjense/python/Pandas”
#read in my bed file 
print("Read bed file...")
bed=pd.read_csv(args["READ"], sep= "\t")        

#2. Make sure it has proper column names
print("#########################")
print("Rename columns...")
column_names=["Scaffold", "Start", "Stop", "Element", "Score", "Strand", "Family", "Sub-Family", "Divergence"]
bed=pd.read_csv(args["READ"], names=column_names, sep= "\t")       

print("#########################")
#3.  Determine what families are in there (SINE, etc)
print("#########################")
print("What families are?")
families=bed.Family.unique()
print("The families in bedfile are: ", families)

print("#########################")
#4.  Create new dataframe from that file using only elements in family “SINE” 
print("#########################")
print("New dataframe form family SINEs")
data={"metulj","ZenoSINE"}
new=bed.loc[bed["Family"]==args["FAMILY"]]

print("#########################")
#5.  Drop columns “Strand” and “Score”
print("Drop columns Strand and Score..")
new_bed=new_bed.drop(["Strand", "Score"], axis=1 )

print("#########################")
#6.  Create new column “Length”
print("New column", "Length")
new_bed["Length"]=new_bed["Stop"]-new_bed["Start"]

print("#########################")
#Create new column “Proportion” which is Length/genome size ***new step ***
print("New column", "Proportion")
new_bed["Proportion"]=new_bed["Length"]/args["SIZE"]

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

#Create new column “Proportion” which is Length/genome size ***new step ***
new_bed.to_csv(“aVan.csv”)
