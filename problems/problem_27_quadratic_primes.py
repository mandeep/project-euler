"""
Project: Project Euler - Problem 27: Quadratic Primes
Author: Mandeep Bhutani
Date: 12/24/2015

Problem:
Euler discovered the remarkable quadratic formula: n² + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the
consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form: n² + an + b, where |a| < 1000 and |b| < 1000
where |n| is the modulus/absolute value of n, e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces
the maximum number of primes for consecutive values of n, starting with n = 0.
"""
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    elif n % 2 == 0:
        return n == 2
    elif n % 3 == 0:
        return n == 3
    for i in range(5, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def find_coefficient_product(bound):
    maximum_number, max_a, max_b = 0, 0, 0
    for a in range(-bound, bound):
        for b in range(0, bound):
            n = 0
            while is_prime(n ** 2 + (a * n) + b):
                n += 1
            if n > maximum_number:
                maximum_number = n
                max_a, max_b = a, b
    return max_a * max_b


print(find_coefficient_product(1000))
