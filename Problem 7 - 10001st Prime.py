"""
Title: Project Euler - Problem 7: 10001st Prime
Author: Mandeep Bhutani
Date: 3/3/2015

Problem: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13. What is the 10 001st prime number?
"""
from math import sqrt


def is_prime(n):
    for x in range(2, int(sqrt(n) + 1)):
        if n % x == 0:
            return False
    else:
        return True


def term(s):
    result = []
    p = 1
    counter = 0
    while counter < s:
        p += 1
        if is_prime(p) == True:
            result.append(p)
            counter += 1
    return result[-1]
print term(10001)
