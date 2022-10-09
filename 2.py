# 2.Write a program to accept the weight of 3 persons, calculate the total weight, determine the average weight and display these details
w1=float(input('Enter the weight of the first person:'))
w2=float(input('Enter the weight of the second person:'))
w3=float(input('Enter the weight of the third person:'))
sum=w1+w2+w3
avg=sum/3
print('The sum of weight of the 3 persons is',sum,' Kgs and the average weight is',avg)