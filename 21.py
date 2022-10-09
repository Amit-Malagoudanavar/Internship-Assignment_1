
# 21.Write a program to accept a number and find its factorial.

fact=1
n=int(input('Enter any number:'))
for i in range(1,n+1):
    fact=i*fact
print(fact,end=' ')