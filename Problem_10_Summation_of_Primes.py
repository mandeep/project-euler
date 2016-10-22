"""
Title: Project Euler - Problem 10: Summation of Primes
Author: Mandeep Bhutani
Date: 02/24/2015

Problem: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


result = sum(x for x in range(1, 2000000) if is_prime(x))
print(result)
