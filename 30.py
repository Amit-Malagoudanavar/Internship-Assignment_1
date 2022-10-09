
# 30. Write a program to generate following patterns.

'''
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1

'''

for i in range(1,6):
    count=0
    for j in range(0,2*i-1):
        if j<(2*i-1)/2:
            count=count+1
            print(count,end=' ')
        else:
            count=count-1
            print(count,end=' ')
    print()