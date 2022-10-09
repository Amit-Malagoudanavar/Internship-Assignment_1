
# 29. Write a program to generate following patterns.

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''

for i in range(1,6):
    count=0
    for j in range(1,i+1):
        count=count+1
        print(count,end=' ')
    print()
