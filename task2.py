#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  
Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""
import math
item1 = float(input("enter item 1 price"))
item2 = float(input("enter item 2 price"))
item3 = float(input("enter item 3 price"))
item4 = float(input("enter item 4 price"))
item5 = float(input("enter item 5 price"))

itemlist = [item1 , item2 , item3, item4, item5]
subtotal = item1+item2+item3+item4+item5

print("<----------------RECEIPT------------------>")

for prices in itemlist:

    gst = round(prices * 0.05 , 2)
    print(f"GST for this item is ${gst}")
    pst = round(prices * 0.07 , 2)
    print(f"PST for this item is ${pst}")
    print(f"item total cost after tax is ${round(prices + gst + pst , 2)}")
    print(">-----------------------------------------<")
    gsttotal = round(subtotal * 0.05 , 2)
    psttotal = round(subtotal * 0.07 , 2)

print("|-----------------TOTAL-------------------|")

print(f"your subtotal is ${subtotal}")
print(f"your gst is ${gsttotal}")
print(f"your pst is ${psttotal}")
print(f"your total concludes to ${subtotal + gsttotal + psttotal}")