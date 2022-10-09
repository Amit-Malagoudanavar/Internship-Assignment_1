
# 28. Write a program to generate following patterns.

'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

'''

for i in range(5,0,-1):
    count=0
    for i in range(i,0,-1):
        count=count+1
        print(count,end=' ')
    print()
