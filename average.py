#average.py
#Calculate average
#Sarah Vaca
#February 24,2020

#Part 1
#Using a for loop and range, calculate the mean of all the numbers between 1 and 20 (include number 1 to 20)
#Calculation of sum
#Print results

n=input('enter number to calculate sum')
#enter number to calculate sum 0   #ANSWER
n_s=int(n)
print(n_s)
#0  #ANSWER
sum=0
for num in range(1,21):
    sum=sum+num                                        #sum of 0 plus each number in the range(1,21)    
    print("Sum of first ", n_s, "numbers is: ", sum)   #it mean is going to print the first n      numbers, and the sum of those numbers would be n 
#Sum of numbers from 1 to 20 = TOTAL 210 ANSWER

#Calculation of average
#Print results

print ("calculate the average of first n numbers")
#calculate the average of first n numbers
n = input("Enter Number ")
#Enter Number 20
n = int (n)
average = 0
sum = 0
for num in range(1,21):
    sum = sum+num;
    average = sum / n
    print("Average of first ", n, "numbers is: ", average)


#Part 2
#Do the same thing without a loop with fewer lines of code(HINT: might have to use a command in a module)
#Try to make your code clean 
#use the module "statistics"

import statistics

n=list(range(1,21))     #list of the numbers between 1 and 20
print(n)

print(statistics.mean(n))       #for calculate the average of the number between 1 an 20
