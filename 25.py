

# 25. Write a program to generate following patterns.

'''
1
2 3
4 5 6 7
8 9 10 11

'''
count=0
for i in range(1,5):
    for j in range(1,i+1):
        count=count+1
        print(count,end=' ')
    print()