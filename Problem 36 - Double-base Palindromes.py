"""
Project: Project Euler - Problem 36: Double-base Palindromes
Author: Mandeep Bhutani
Date: 4/17/2015

Problem: The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
palindrome_sum = 0
for x in xrange(1, 1000000):
    if str(bin(x))[2:] == str(bin(x))[2:][::-1] and str(x) == str(x)[::-1]:
        palindrome_sum += x
print palindrome_sum
