
# 32. Write a program to generate following patterns.

'''
A B C
D E F
G H I

'''

n=ord('A')
for i in range(1,4):
    for j in range(1,4):
        print(chr(n),end=' ')
        n=n+1
    print()