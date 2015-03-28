"""
Project: Project Euler - Problem 56: Powerful Digit Sum
Author: Mandeep Bhutani
Date: 3/13/2015

Problem: A googol (10^100) is a massive number: one followed by one-hundred
zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.
maximum digital sum?
"""
result = []
for a in xrange(1, 100):
    for b in xrange(1, 100):
        digit_sum = sum([int(c) for c in str(a ** b)])
        if digit_sum not in result:
                result.append(digit_sum)
print max(result)
