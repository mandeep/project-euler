"""
Project: Project Euler - Problem 35: Circular Primes
Author: Mandeep Bhutani
Date: 04/17/2015

Problem: The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime. There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. How many circular primes are there below one million?
"""
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    else:
        return True


def is_circular_prime(m):
    m = str(m)
    total = [m[dex:] + m[:dex] for dex, number in enumerate(m)]
    return all([is_prime(int(k)) for k in total])


count = 13
for x in range(100, 1000000):
    if not any(char in "02468" for char in str(x)) and is_circular_prime(x):
        count += 1
print(count)
