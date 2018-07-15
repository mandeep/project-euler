"""
Project: Project Euler - Problem 30: Digit Fifth Powers
Author: Mandeep Bhutani
Date: 03/29/2015

Problem: Surprisingly there are only three numbers that can be written as the
sum of fourth powers of their digits: 1634, 8208, and 9474. As 1 = 1^4, it is
not included. The sum of these numbers is 1634 + 8208 + 9474 = 19316. Find the
sum of all the numbers that can be written as the sum of fifth powers of their
digits.
"""


def separate_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits


def digit_powers(n):
    summation = 0
    for i in range(2, 500000):
        digits = separate_digits(i)
        total = [j ** n for j in digits]
        if sum(total) == i:
            summation += i
    return summation


print(digit_powers(5))
