"""
Project: Project Euler - Problem 56: Powerful Digit Sum
Author: Mandeep Bhutani
Date: 3/13/2015

Problem: A googol (10^100) is a massive number: one followed by one-hundred
zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1. Considering
natural numbers of the form, a^b, where a, b < 100, what is their maximum digital sum?
"""
maximal_digit_sum = set()
for a in range(1, 100):
    for b in range(1, 100):
        digit_sum = sum([int(c) for c in str(a ** b)])
        maximal_digit_sum.add(digit_sum)
print(max(maximal_digit_sum))
