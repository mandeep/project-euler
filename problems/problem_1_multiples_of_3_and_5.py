"""
Project: Project Euler - Problem 1: Multiples of 3 and 5
Author: Mandeep Bhutani
Date: 01/28/2015

Problem:
If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

sum_multiples_of_3 = 3 * (999 // 3 * (999 // 3 + 1) // 2)
sum_multiples_of_5 = 5 * (995 // 5 * (995 // 5 + 1) // 2)
sum_multiples_of_15 = 15 * (990 // 15 * (990 // 15 + 1) // 2)

print(sum_multiples_of_3 + sum_multiples_of_5 - sum_multiples_of_15)
