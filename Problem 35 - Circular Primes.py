"""
Project: Project Euler - Problem 35: Circular Primes
Author: Mandeep Bhutani
Date: 4/17/2015

Problem: The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime. There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. How many circular primes are there below one million?
"""
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    else:
        return True


def is_circular_prime(m):
    m = str(m)
    if len(m) == 3:
        return is_prime(int(m)) and is_prime(int(m[1] + m[2] + m[0])) and \
            is_prime(int(m[2] + m[0] + m[1]))
    elif len(m) == 4:
        return is_prime(int(m)) and is_prime(int(m[1] + m[2] + m[3] + m[0])) and \
            is_prime(int(m[2] + m[3] + m[0] + m[1])) and is_prime(int(m[3] + m[0] + m[1] + m[2]))
    elif len(m) == 5:
        return is_prime(int(m)) and is_prime(int(m[1] + m[2] + m[3] + m[4] + m[0])) \
            and is_prime(int(m[2] + m[3] + m[4] + m[0] + m[1])) and is_prime(int(m[3] + m[4] + m[0] + m[1] + m[2])) \
            and is_prime(int(m[4] + m[0] + m[1] + m[2] + m[3]))
    elif len(m) == 6:
        return is_prime(int(m)) and is_prime(int(m[1] + m[2] + m[3] + m[4] + m[5] + m[0])) \
            and is_prime(int(m[2] + m[3] + m[4] + m[5] + m[0] + m[1])) and is_prime(int(m[3] + m[4] + m[5] + m[0] + m[1] + m[2])) \
            and is_prime(int(m[4] + m[5] + m[0] + m[1] + m[2] + m[3])) and is_prime(int(m[5] + m[0] + m[1] + m[2] + m[3] + m[4]))

count = 13
for x in xrange(100, 1000000):
    if not any(char in "02468" for char in str(x)) and is_circular_prime(x) == True:
        count += 1
print count
