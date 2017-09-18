"""
Project: Project Euler - Problem 34: Digit Factorials
Author: Mandeep Bhutani
Date: 03/12/2015

Problem: 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of
their digits. Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Analysis: Factorial(9) is used as the upper bound
"""
from math import factorial


def factorial_digits(n):
    summation = 0
    while n > 0:
        summation += factorial(n % 10)
        n //= 10
    return summation


summation = 0
for number in range(3, factorial(9)):
    factorial_sum = factorial_digits(number)
    if factorial_sum == number:
        summation += number

print(summation)
