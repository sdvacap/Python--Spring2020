#littlelists.py
#Sarah Vaca
#April 13, 2020

#For each task: 1) do in loop and 2) do in list comprehension

#“The quick brown fox jumped over the lazy dog”

string=(“The quick brown fox jumped over the lazy dog”)
print(string)

###1. Count the number of spaces in the above string. 
###LOOP###
#count=0
#for w in string:           #it let me know if the loop is working 
#    print(w) 
#       if w == ' ':
#           print('true')
count=0
for w in string:
    if w == ' ':
        count=count+1
        
print('The number of spaces in the string is:', count)        

###COMPREHENSSION###
spaces=[w for w in string if w == ' ']
print('The number of spaces in the string is:', len(spaces))

###############################################################################

###2. Find all the words that have the letter “o” in the above string  
palabras=string.split(' ')          #transform each word in strings
print(palabras)

###LOOP###
words=[]   
for i in palabras:                  #loop to finf the letter "o" in each word
    if i.count('o')>0:
        words.append(i)
        
print('The words that have the letter "o" are:', words)        
###COMPREHENSSION###
words=[i for i in palabras if i.count('o')>0]
print('The words that have the letter "o" are:', words)

###############################################################################

###3. Find all the words that have at least 5 letters in the above string
###LOOP###
letters=[]
for i in palabras:
    if len(i)>4:
        letters.append(i)
print('The words that have at least 5 letters are:', letters)

###COMPREHENSSION###
letters=[i for i in palabras if len(i)>4]  
print('The words that have at least 5 letters are:', letters)

################################################################################

###4. Find all the numbers from 1 to 1000 that have a “3” in it. Ex: 23, 37, 903
###LOOP###
numlist=list(range(1,1001))             #list of numbers 1 - 1000

#loop to convert the numbers into strings
numbers=[]
for i in numlist:                   
    numbers.append(str(i))
    
print(numbers)

#loop to find all numbers that have a '3'                
new_numbers=[]
for i in numbers:
    if i.count('3')>0:
            new_numbers.append(i)
            
print('Numbers from 1 to 1000 that have a 3 are:', new_numbers)            
        
###COMPREHENSSION###
numbers=[i for i in range(1,1001) if str(i).count('3')>0]
print('Numbers from 1 to 1000 that have a 3 are:', numbers)
