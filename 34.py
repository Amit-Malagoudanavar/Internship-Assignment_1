

# 34. Write a program to generate following patterns.

'''
19 0 0
0 19 0
0 0 19

'''


for i in range(1,4):
    for j in range(1,4):
        if j==i:
            print(19,end=' ')
        else:
            print(0,end=' ')
    print()