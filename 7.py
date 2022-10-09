
# 7.Write a program to accept the billing amount, if it is > 6000 then give a discount of 10% and display the net amount.

billing_amt=float(input('Enter the billing amount: '))
if billing_amt>6000:
    discount=((10/100)*billing_amt)
    net_amt=billing_amt-discount
    print('Your net billing amount: ',net_amt)
if billing_amt<=6000:
    print('Your net billing amount: ',billing_amt)
