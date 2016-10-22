"""
Project: Project Euler - Problem 36: Double-base Palindromes
Author: Mandeep Bhutani
Date: 04/17/2015

Problem: The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def is_palindrome(i):
    return str(i) == str(i)[::-1]


def bin_palindrome(j):
    j = bin(j)
    return j[2:] == j[2:][::-1]


palindrome_sum = 0
for x in range(1, 1000000):
    if is_palindrome(x) and bin_palindrome(x):
        palindrome_sum += x
print(palindrome_sum)
