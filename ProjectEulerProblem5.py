"""
Title: Project Euler - Problem 5: Smallest Multiple
Author: Mandeep Bhutani
Date: 2/1/2015

Problem: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder. What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?

References: http://en.wikipedia.org/wiki/Least_common_multiple;
http://en.wikipedia.org/wiki/Greatest_common_divisor;
http://en.wikipedia.org/wiki/Euclidean_algorithm

Description: It is more efficient to find the least common multiple of two or more positive
integers by first dividing the greatest common divisor of those integers prior to multiplying.
"""
from fractions import gcd # Importing the gcd module to find the gcd of two or more integers.

print reduce(lambda a,b: (a * b) / gcd(a,b), range(1,21)) # Add 1 to range since range is inclusive

# Using list comprehension of lambda a,b since it handles the reduce function well. 
# Because lcm(a,b,c) = lcm(a,b),c; we can add range(1,21) to the lcm calculation.