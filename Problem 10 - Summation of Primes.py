"""
Title: Project Euler - Problem 10: Summation of Primes
Author: Mandeep Bhutani
Date: 2/24/2015

Problem: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for x in xrange(2, int(sqrt(n) + 1)):
        if n % x == 0:
            return False
    else:
        return True


def summation(s):
    result = 0
    for p in xrange(1, s):
        if is_prime(p) == True:
            result += p
    return result
print summation(2000000)
