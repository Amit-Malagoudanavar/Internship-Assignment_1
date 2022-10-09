
# 15.Write a program to generate the first 'N' natural numbers. Accept the value of 'N' from the user.

n=int(input('Enter the number of natural numbers to be generated:'))
print('The first',n,'natural numbers are',)
for i in range(1,n+1):
    print(i,end=' ')