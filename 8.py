
# 8.The Sports Club registration form has the following details: name, mobile number and age. Per the membership policy, the person should be at least 18 years old to become a member. Write a program to accept the details mentioned above; if the age is >18 years then display the entered details with a congratulatory message, else the following message should be displayed “Sorry! You need to be at least 18 years old to get membership.”

name=input('Enter the name: ')
mobile=int(input('Enter the mobile no. : '))
age=int(input('Enter the age: '))

if age<18:
    print('Sorry! You need to be at least 18 years old to get membership.')

if age>=18:
    print('\n',name,'\n',mobile,'\n',age)
    print('\nCongratulations',name,'for your successful registration.')