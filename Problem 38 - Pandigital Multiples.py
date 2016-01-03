"""
Title: Project Euler - Problem 38: Pandigital Multiples
Author: Mandeep Bhutani
Date: 01/02/2016

Problem: Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

Analysis: Three digit numbers concatenated with multiples are not large enough to be pandigital numbers. 
Five digit numbers concatenated with multiples are too large to be pandigital numbers. Therefore, we only need
to check four digit numbers multiplied by 1 and 2 since these two multiples are within the nine digit limit.
Since the largest pandigital is 987654321 and the lower limit pandigital given from the problem is 918273645,
we only need to test the range between the first four digits of these two numbers.
"""
from itertools import permutations


pandigitals = [str("".join(x)) for x in permutations("123456789") if str("".join(x)) > "918273645"]

for number in range(9876, 9182, -1):
    if str(number * 1) + str(number * 2) in pandigitals:
        print(str(number * 1) + str(number * 2))
        break
