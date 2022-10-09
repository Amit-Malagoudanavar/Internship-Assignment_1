
# 13.Write a program to accept 3 numbers from the user and find the biggest of them.

num1=int(input('Enter the first number num1:'))
num2=int(input('Enter the second number num2:'))
num3=int(input('Enter the third number num3:'))

if num1>num2:
    if num1>num3:
        print('The biggest of the 3 numbers entered is:',num1)
    else:
        print('The biggest of the 3 numbers entered is:',num3)
else:
    if num2>num3:
        print('The biggest of the 3 numbers entered is:',num2)
    else:
        print('The biggest of the 3 numbers entered is:',num3)