#bats species
#Sarah Vaca
#February 17, 2020

#Add any variables
#Ask for inputs

specie1=input("Name of your first bat")
print(specie1)
#specie1="Myotis austroriparius"

specie2=input("Name of your second bat")
print(specie2)
#specie2="Myotis septentrionalis"

specie3=input("Name of your third bat")
print(specie3)
#specie3="Eptesicus fuscus"

#calculate the first three letters of the genus and of the specie 
sp1_genus=specie1[:3]
sp1_specie=specie1.split(" ")[1][:3]
sp1=sp1_genus+sp1_specie

sp2_genus=specie2[:3]
sp2_specie=specie2.split(" ")[1][:3]
sp2=sp2_genus+sp2_specie

sp3_genus=specie3[:3]
sp3_specie=specie3.split(" ")[1][:3]
sp3=sp3_genus+sp3_specie

#Print results
print(sp1.upper(),sp2.upper(),sp3.upper(), sep='\n')
