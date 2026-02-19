"""
Swap Two Numbers
Demonstrates Python's elegant tuple unpacking for swapping values without a temporary variable.
"""

def swap_numbers(a, b):
    a, b = b, a
    return a, b

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
num1, num2 = swap_numbers(num1, num2)
print("First number:", num1)
print("Second number:", num2)
