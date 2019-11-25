"""
Project: Project Euler - Problem 4: Largest Palindrome Product
Author: Mandeep Bhutani
Date: 01/30/2015

Problem: A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is: 9009 = 91 * 99
Find the largest palindrome made from the product of two 3-digit numbers.

We estimate that the palindrome will consist of six digits as 999 * 999
consists of six digits and our palindrome is likely to be around here.
Thus, our palindrome exists in the form of 'abccba' and can be written
in the form of 100000a + 10000b + 1000c + 100c + 10b + 1a =
100001a + 10010b + 1100c = 11(9091a + 910b + 100c). Therefore, the product
x * y that produces our palindrome will be a multiple of 11, and one of either
x or y will be a product of 11. We can then use a step size of 11 to limit the amount
of numbers we check for palindromes.
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
    for x in range(121, number, 11):
        for y in range(x + 1, number):
            if is_palindrome(x * y):
                product = max(product, x * y)
                print(x, y)
    return product


print(largest_palindrome_product(1000))
