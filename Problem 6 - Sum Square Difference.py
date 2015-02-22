"""
Project: Project Euler - Problem 6: Sum Square Difference
Author: Mandeep Bhutani
Date: 1/30/2015

Problem:
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def sum_squares():
    result = 0
    for x in range(1, 101):
        result += x ** 2
    return result


def square_sums():
    total = 0
    for x in range(1, 101):
        total += x
    total **= 2
    return total

print square_sums() - sum_squares()
