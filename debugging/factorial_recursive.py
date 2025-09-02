#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    ---------------------
    Computes the factorial of a non-negative integer using recursion.
    The factorial of a number n (denoted as n!) is the product of all 
    positive integers from 1 to n. By definition, 0! is 1.

    Parameters:
    -----------
    n : int
        A non-negative integer whose factorial is to be calculated.
        Must be 0 or greater. 

    Returns:
    --------
    int
        The factorial of the input number n.
        If n == 0, returns 1 (base case of recursion). Otherwise, returns
        n multiplied by factorial(n-1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the number from command-line arguments and calculate factorial
f = factorial(int(sys.argv[1]))
print(f)
