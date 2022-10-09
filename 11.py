
# 11.Write a program to accept two numbers num1 and num2; when one is subtracted from the other, the result should always be a positive number.

num1=int(input('Enter the first number num1:'))
num2=int(input('Enter the second number num2:'))

if num1-num2<0:
    print('The result (difference) is:',abs(num1-num2))
else:
    print('The result (difference) is:',num1-num2)