"""
Title: Project Euler - Problem 3: Largest Prime Factor
Author: Mandeep Bhutani
Date: 2/1/2015

Problem: The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def largest_prime_factor(n):
    i = 2

    # If n is not prime, atleast one divisor less than the root of n exists.
    # Another way to write this is the square of i must be less than n.
    while i * i < n:

        # Divide n by each of its prime factors until it equals its largest
        # prime factor
        while n % i == 0:
            n /= i
        i += 1
    return n
