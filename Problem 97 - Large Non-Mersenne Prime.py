"""
Title: Project Euler - Problem 97: Large Non-Mersenne Prime
Date: 02/03/2015

Problem: The first known prime found to exceed one million digits was discovered in 1999,
and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits.
Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.
However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.
Find the last ten digits of this prime number.

Analysis: By using modular exponentiation we can calculate the last ten digits of the
exponent rather easily.

References: https://en.wikipedia.org/wiki/Modular_exponentiation
"""
mod = 10 ** 10
prime = (28433 * pow(2, 7830457, mod) + 1) % mod
print(str(prime)[-10:])
