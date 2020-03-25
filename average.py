#average.py
#Calculate average
#Sarah Vaca
#February 24,2020

#Part 1
#Using a for loop and range, calculate the mean of all the numbers between 1 and 20 (include number 1 to 20)
#Calculation of sum
#Print results

#enter number to calculate sum 0   #ANSWER
sum=0
for num in range(1,21):
    sum=sum+num                                        #sum of 0 plus each number in the range(1,21)    
print("Sum of numbers is: ", sum)   
#Sum of numbers from 1 to 20 = TOTAL 210 ANSWER

#Calculation of average
#Print results
sum = 0
for num in range(1,21):
    sum = sum+num;
    average = sum / 20
print("Average is: ", average)


#Part 2
#Do the same thing without a loop with fewer lines of code(HINT: might have to use a command in a module)
#Try to make your code clean 
#use the module "statistics"

import statistics

average=statistics.mean(range(1,21))        #for calculate the average of the number between 1 an 20
print(average)                              
