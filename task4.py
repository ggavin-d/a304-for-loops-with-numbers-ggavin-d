"""
Help Jenny keep track of her expenses!
Each month, she needs to keep track of:
1. The current balance on her credit card
2. The total amount of her purchases
3. The total amount that she pays off
4. If she has an unpaid balance, then 2% of the current balance is charged to her

Write a program that asks her to enter in her total purchases as
well as how much she pays off.  Calculate any interest that she must add to her
balance and display her total balance at the end of the month.

A sample for the first few months is shown below:

Enter total purchases for month(1) : 100
Enter total payments for month(1)  : 75
2% interest has been charged: 0.5
Your closing balance is $25.5

Enter total purchases for month(2) : 100
Enter total payments for month(2)  : 75
2% interest has been charged: 1.01
Your closing balance is $51.51


while
    ask user and enter purchases
    ask user and enter payments
    previous balance + purchases - payments = closing balance
    interest = 2% of closing balance
    final closing balance = closing balance + interest



"""


months = 1
balance = 0

while months < 13:


    mpurchases = float(input(f"Enter total purchases for # of months:({months}) ")) 
    mpayments = float(input(f"Enter total payments for # of months:({months}) ")) 


    closingbalance = balance + mpurchases - mpayments
    interest = closingbalance * 0.02
    fclosingbalance = closingbalance + interest
    balance = balance+fclosingbalance


    print(f"2 percent interest has been charged: ${round(interest , 2)}")
    print(f"your closing balance is ${round(fclosingbalance , 2)}")
    print("<-------------------------------------->")
    months = months+1


