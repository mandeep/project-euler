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


def sum_factorial_digits(n):
    summation = 0
    while n > 0:
        summation += factorial(n % 10)
        n //= 10
    return summation


def sum_factorial_sum(n):
    sum_factorial_sum = 0
    for number in range(3, n):
        factorial_sum = sum_factorial_digits(number)
        if factorial_sum == number:
            sum_factorial_sum += number
    return sum_factorial_sum

print(sum_factorial_sum(factorial(9)))
