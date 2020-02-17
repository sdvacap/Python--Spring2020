#bats species
#Sarah Vaca
#February 17, 2020

#Add any variables
#Ask for inputs
#Print results

specie1="Myotis austroriparius"
specie2="Myotis septentrionalis"
specie3="Eptesicus fuscus"

sp1=specie1[:3] + specie1[7:10]
sp2=specie2[:3] + specie2[7:10]
sp3=specie3[:3] + specie3[10:13]

print(sp1.upper(),sp2.upper(),sp3.upper(), sep='\n')
