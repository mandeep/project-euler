"""
Project: Project Euler - Problem 16: Power Digit Sum
Author: Mandeep Bhutani
Date: 2/3/2015

Problem:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

Description: In Python, the shortest way to find the sum of digits in an integer
is to convert the integer into a string and then add the digits of the string into a list.
Once in a list the digits need to be converted back to an integer and then summed. With list
comprehension this can all be achieved in a single line.
"""
print sum([int(x) for x in str(2**1000)])
