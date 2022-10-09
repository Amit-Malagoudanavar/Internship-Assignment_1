
# 31. Write a program to generate following patterns.

'''
19 38 57
76 95 114
133 152 171

'''

count=0
for i in range(1,4):
    for j in range(1,4):
        count=count+1
        print(19*count,end=' ')
    print()