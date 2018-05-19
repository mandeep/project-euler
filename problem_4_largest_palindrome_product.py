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


def largest_palindrome_product(number):
    product = 1
    for x in range(100, number):
        for y in range(x, number):
            if is_palindrome(x * y) and (x * y) > product:
                product = (x * y)
    return product


print(largest_palindrome_product(1000))
