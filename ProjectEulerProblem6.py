"""
Project: Project Euler - Problem 6: Sum square difference
Author: Mandeep Bhutani
Date: 1/30/2015

Problem:
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def first():
    total = 0
    for y in range(101):
        total += y ** 2
    return total

def second():
    result = 0
    for x in range(101):
        result += x
        resultant = result ** 2
    return resultant
    
print second() - first()