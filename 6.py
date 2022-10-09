
# 6.Write a program to accept a number, if it is negative then covert it to a positive number.

num=int(input('Enter the number: '))
if num<0:
    print('The result is: ',abs(num))
if num>=0:
    print('The result is: ',num)
