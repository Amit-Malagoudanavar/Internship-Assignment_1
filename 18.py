
# 18.Write a program to accept the lower bound number and the upper bound number from the user and print the prime numbers between them.
a=int(input('Enter the lower bound value:'))
b=int(input('Enter the upper bound value:'))
print('The prime numbers between',a,'and',b,'are:',end='')
for i in range(a,b+1):
    n=i
    count=0
    for i in range(1,n):
        if n%i==0:
            count=count+1
        else:
            count=count
    if count<=1:
        print(n,end=' ')