

# 26. Write a program to generate following patterns.

'''
1 2 3
4 5 6
7 8 9

'''

count=0
for i in range(1,4):
    for i in range(1,4):
        count=count+1
        print(count,end=' ')
    print()