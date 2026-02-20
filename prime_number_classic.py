"""
Prime Number Checker
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Uses a simple trial division algorithm.
"""

print("-Prime Number-")
num = int(input("Enter the number: "))
i = 2
is_prime = True

if num < 2:
    is_prime = False
else:
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print("number is prime")
else:
    print("not prime")
