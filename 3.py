
# 3.Write a program to accept the following details of an employee: empno, name and monthly salary; calculate the yearly salary and display the result.

empno=int(input('Enter the empno: '))
name=input('Enter the employee name: ')
salary=int(input('Enter the monthly salary: '))
year_salary=12*salary
print('Hi',name,'! Your employee id is',empno,'monthly salary is Rs',salary,'and yearly salary is Rs',year_salary)