"""
Project: Project Euler - Problem 23: Non-abundant Sums
Author: Mandeep Bhutani
Date: 04/16/2015

Problem: A perfect number is a number for which the sum of its proper divisors is exactly equal
to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number. A number n is called deficient if the sum of its proper
divisors is less than n and it is called abundant if this sum exceeds n. As 12 is the smallest
abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. Find the sum of all the positive
integers which cannot be written as the sum of two abundant numbers.

"""
from math import sqrt


def is_abundant(n):
    total = []
    for i in range(1, int(sqrt(n)+1)):
        if n % i == 0:
            if i not in total:
                total.append(i)
                if (n // i) != n and (n // i) not in total:
                    total.append(n / i)
    return sum(total) > n

abundant_numbers = [x for x in range(1, 28123+1) if is_abundant(x)]
abundant_sums = set([(h + j) for h in abundant_numbers for j in abundant_numbers])
result = sum([k for k in range(1, 28123+1) if k not in abundant_sums])
print(result)
