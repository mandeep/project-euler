"""
Project: Project Euler - Problem 40: Champernowne's Constant
Author: Mandeep Bhutani
Date: 04/07/2015

Problem: An irrational decimal fraction is created by concatenating the
positive integers: 0.123456789101112131415161718192021...It can be seen that
the 12th digit of the fractional part is 1. If dn represents the nth digit
of the fractional part, find the value of the following expression:
d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000.

Analysis: Create a variable named champernowne that concatenates all
integers from 1 to 200,000. Then use an index slice to find the fractional
parts listed in the expression variable.

References: https://en.wikipedia.org/wiki/Champernowne_constant
"""
champernowne = "".join([str(number) for number in range(1, 200000)])
expression = (1, 10, 100, 1000, 10000, 100000, 1000000)

result = 1
for fraction in expression:
    result *= int(champernowne[fraction-1])
print(result)
