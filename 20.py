
# 20.Write a program to accept a number from the user and print its multiplication table (upto “times 10”).

n=int(input('Enter the number to generate its multiplication table:'))
print('Multiplication table for',n,'is :')
for i in range(1,10+1):
    mul=n*i
    print(n,'*',i,'=',mul)