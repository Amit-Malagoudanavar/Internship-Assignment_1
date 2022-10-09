
# 14.Write a program to accept the marks scored in three subjects; determine the sum and average of the entered marks. Grade is awarded based on following criteria.

sub1=int(input('Enter the marks scored in 1st subject: '))
sub2=int(input('Enter the marks scored in 2nd subject: '))
sub3=int(input('Enter the marks scored in 3rd subject: '))

total=sub1+sub2+sub3
avg=total/3

if avg<35:
    grade='C'
elif avg>=35 and avg<=60:
    grade='B'
else:
    grade='A'
print('Total marks: ',total,'\nAverage is: ',avg,'\nGrade: ',grade)