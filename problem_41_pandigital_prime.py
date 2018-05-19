"""
Project: Project Euler - Problem 41: Pandigital Prime
Author: Mandeep Bhutani
Date: 01/15/2016

Problem: We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?

Analysis: To find the upper limit of the pandigital search, the divisibility of 3 is used to sum the
digits in pandigitals: 987654321, 87654321, 7654321, 654321, and 54321. All of these pandigitals are
divisible by 3 except 7654321, thus it is used as our upper bound. As a check, the next largest
pandigital, 12345678, is divisible by 2 since the last digit is divisible by 2.
"""
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def is_pandigital(m):
    pandigital = "".join([str(o) for o in range(1, len(str(m))+1)])
    return "".join(sorted(str(m))) == pandigital


for p in range(7654321, 2143, -1):
    if is_prime(p) and is_pandigital(p):
        print(p)
        break
