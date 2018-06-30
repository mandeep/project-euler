"""
Project: Project Euler - Problem 145: How Many Reversible Numbers Are There Below One Billion?
Author: Mandeep Bhutani
Date: 10/24/2016

Problem: Some positive integers n have the property that the
sum [ n + reverse(n) ] consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such
numbers reversible; so 36, 63, 409, and 904 are reversible. Leading
zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?
"""


def is_reversible(number):
    reversed_number = str(number)[::-1]
    if reversed_number[0] == '0':
        return False
    reversed_sum = number + int(reversed_number)
    reversible = [int(x) for x in str(reversed_sum)]
    return all(x % 2 != 0 for x in reversible)

print(len([i for i in range(1, 100000000) if is_reversible(i)]))
