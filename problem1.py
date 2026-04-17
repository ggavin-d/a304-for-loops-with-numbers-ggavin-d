#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""

l = int(input('enter length'))
w = int(input('enter width'))

for i in range(l): # printing vertical rows range = number of vertrows
    print()
    for i in range(w): # printing vertical rows range = number of vertrows
        print('*', end='')