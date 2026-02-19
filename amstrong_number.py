"""
Armstrong Number Checker
An Armstrong number is a number that is equal to the sum of its digits each raised to the power of the number of digits.
Example: 407 = 4³ + 0³ + 7³ = 64 + 0 + 343 = 407
"""

def armstrong_number(num):
    num_str = str(num)
    num_digit = len(num_str)
    armstrong_sum = sum(int(digit)**num_digit for digit in num_str)
    return armstrong_sum == num

number = int(input("Enter the number: "))
if armstrong_number(number):
    print(f"{number} is an armstrong number")
else:
    print(f"{number} is not an armstrong number")
