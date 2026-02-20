"""
Full Pyramid Pattern
Prints a symmetric pyramid pattern using asterisks.
Uses nested loops to create leading spaces and asterisks.
Example for n=5:
    *
   ***
  *****
 *******
*********
"""

def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()

full_pyramid(5)
