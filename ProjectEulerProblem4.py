"""
Project: Project Euler - Problem 4: Largest palindrome product
Author: Mandeep Bhutani
Date: 1/30/2015

Problem: A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
Find the largest palindrome made from the product of two 3-digit numbers.
"""
result = [] # Add an empty list to append to later
for x in range(100,1000): # Checks all 3-digit numbers from 100 to 999
	for y in range(100,1000):
		if str(x * y) == str(x * y)[::-1]: # Checks for palindromes using an extended slice of a string.
			result.append(x * y) # Adds each palindrome product to the results list.
print max(result) # Prints the largest palindrome contained in the list.
