"""
Title: Project Euler - Problem 33: Digit Cancelling Fractions
Author: Mandeep Bhutani
Date: 01/05/2016

Problem: The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

Analysis: Since all fractions with a numerator and denominator ending in 0 are 
considered trivial, we only need to search for fractions that are equal to
the first digit of the numerator divided by the second digit of the denominator
as long as the other digits in both numbers are equal to each other.
"""
from fractions import Fraction

numbers = [(numerator, denominator) for numerator in range(10, 100) for denominator in range(10, 100) if (numerator / denominator) < 1]

result = 1
for num, den in numbers:
    division = num / den
    if int(str(den)[1]) > 1 and division == int(str(num)[0]) / int(str(den)[1]) and str(num)[0] != str(num)[1] and int(str(num)[1]) == int(str(den)[0]):
        result *= Fraction(num, den)
print(result)
