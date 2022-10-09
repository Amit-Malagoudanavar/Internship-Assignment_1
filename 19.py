
# 19.Write a program to accept a number and print the Fibonacci series up to the entered number.

n=int(input('Enter the upper bound number to generate the Fibonacci numbers:'))
print('Fibonacci series up to the entered number is:',end=' ')
a=0
b=1
if n==0:
    print(a,end=' ')

if n>=1:
    print(a,b,end=' ')

for i in range(1,n):
    c=a+b
    a=b
    b=c
    if c>n:
        break
    print(c,end=' ')