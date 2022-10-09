

# 33. Write a program to generate following patterns.

'''
1 1
1 2 2 1
1 2 3 3 2 1
1 2 3 4 4 3 2 1

'''

for i in range(1,5):
    count=0
    for j in range(2*i):
        if j<(2*i)/2:
            count=count+1
            print(count,end=' ')
        else:
            print(count,end=' ')
            count=count-1
    print()