"""
Title: Project Euler - Problem 21: Amicable Numbers
Author: Mandeep Bhutani
Date: 3/11/2015

Problem: Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n). If d(a) = b and d(b) = a, where a != b,
then a and b are an amicable pair and each of a and b are called amicable
numbers. For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220. Evaluate the sum of all the amicable
numbers under 10,000.

References: http://en.wikipedia.org/wiki/Amicable_numbers
"""


def amicable(x):
    result = []
    for numbers in range(1, x):
        first = [i for i in range(1, numbers) if numbers % i == 0]
        first_sum = sum(first)
        second = [j for j in range(1, numbers) if first_sum % j == 0]
        second_sum = sum(second)
        if second_sum == numbers and (first_sum - second_sum) > 1:
            result.append(first_sum)
            result.append(second_sum)
    return sum(result)
print(amicable(10001))
