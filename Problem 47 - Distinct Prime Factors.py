"""
Title: Project Euler - Problem 2: Even Fibonacci Numbers
Author: Mandeep Bhutani
Date: 12/26/2015

Problem:
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""
from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for y in range(2, int(sqrt(x)) + 1):
        if x % y == 0:
            return False
    else:
        return True


def factors(n):
    factors = set()
    for i in range(2, n):
        if n % i == 0 and is_prime(i) == True:
            factors.add(i)
    return factors

i = 648
while True:
    i += 1
    if len(factors(i)) == 4 and len(factors(i + 1)) == 4 and len(factors(i + 2)) == 4 and len(factors(i + 3)) == 4:
        print(i)
        break
