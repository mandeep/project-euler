"""
Project: Project Euler - Problem 4: Largest Palindrome Product
Author: Mandeep Bhutani
Date: 01/30/2015

Problem: A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is: 9009 = 91 * 99
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math


def is_palindrome(n):
    length = math.floor(math.log10(n)) + 1
    exponent = 10 ** (length - 1)
    while n > 0:
        if n // exponent != n % 10:
            return False
        n %= exponent
        n //= 10
        exponent /= 100
    return True


def largest_palindrome_product(number):
    product = 101
    for x in range(100, number):
        for y in range(x + 1, number):
            if is_palindrome(x * y):
                product = max(product, x * y)
    return product


print(largest_palindrome_product(1000))
