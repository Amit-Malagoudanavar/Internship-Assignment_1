
# 12.In a shopping mall, privileged customers (if they have a membership card) are being given a 10% discount on the billed amount, and the others are being given a 3% discount. Write a program to accept the billing amount and confirm the membership card from the customer; calculate and display the net amount to be paid by the customer.

bill_amt=float(input('Enter the bill amount: '))
card=input('Do you have a membership card?(Y/N)')
if card=='Y':
    discount=((10/100)*bill_amt)
    net_amt=bill_amt-discount
    print('Thank you! Your total bill amount is Rs',bill_amt,'discount is Rs',discount,'and net amount payable is Rs',net_amt)

else:
    discount=((3/100)*bill_amt)
    net_amt=bill_amt-discount
    print('Thank you! Your total bill amount is Rs',bill_amt,'discount is Rs',discount,'and net amount payable is Rs',net_amt)