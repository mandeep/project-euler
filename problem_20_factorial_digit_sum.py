"""
Project: Project Euler - Problem 20: Factorial Digit Sum
Author: Mandeep Bhutani
Date: 2/1/2015

Problem:
n! means n * (n-1) * ... * 3 * 2 * 1
For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!

Analysis: First a function for a factorial needs to be defined.
While there is a math.factorial function that could serve this purpose,
a user defined function was chosen for this problem.
"""


def factorial(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product


def sum_factorial_digits(n):
    return sum(int(x) for x in str(factorial(100)))


print(sum_factorial_digits(100))
