"""
Project: Project Euler - Problem 20: Factorial Digit Sum
Author: Mandeep Bhutani
Date: 2/1/2015

Problem:
n! means n * (n-1) * ... * 3 * 2 * 1
For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""
# First a function for a factorial needs to be defined. While there is a math.factorial function that
# could serve this purpose, a user defined function was chosen for this problem.
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

digits = [int(x) for x in str(factorial(100))] # Converting 100! into a list of integers
print sum(digits) # Printing the sum of the integers in digits