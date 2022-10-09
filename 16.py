
# 16.Write a program to accept a number and determine whether it is a prime number or not.

count=0

num=int(input('Enter any number:'))
for i in range(1,num):
    if num%i==0:
        count=count+1
    else:
        count=count
if num==1:
    print('1 is neither prime nor composite')
elif count>1:
    print('The entered number',num,'is not a prime number')
else:
    print('The entered number',num,'is a prime number')