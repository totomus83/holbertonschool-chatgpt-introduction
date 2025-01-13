#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given number 'n' using recursion.
# The factorial of a non-negative integer 'n' is the product of all positive integers less than or equal to n.
# For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.

def factorial(n):
    # Parameters:
    # n (int): A non-negative integer whose factorial is to be computed.

    if n == 0:
        return 1  # The factorial of 0 is defined as 1.
    else:
        return n * factorial(n-1)  # Recursive call to calculate factorial.

# Calling the factorial function with a number provided as a command line argument
f = factorial(int(sys.argv[1]))

# Returns:
# The result of the factorial computation is returned and printed to the console.
print(f)
