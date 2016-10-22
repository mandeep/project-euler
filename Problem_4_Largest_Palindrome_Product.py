"""
Project: Project Euler - Problem 4: Largest Palindrome Product
Author: Mandeep Bhutani
Date: 01/30/2015

Problem: A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is: 9009 = 91 * 99
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(something):
    return str(something) == str(something)[::-1]

result = 1
for x in range(100, 1000):
    for y in range(100, 1000):
        if is_palindrome(x * y) and (x * y) > result:
            result = (x * y)
print(result)
