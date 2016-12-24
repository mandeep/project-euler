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


def amicable(limit):
    result = 0
    for numbers in range(1, limit):
        sum_divisors = sum(i for i in range(1, numbers) if numbers % i == 0)
        sum_divisors_sum = sum(j for j in range(1, numbers) if sum_divisors % j == 0)
        if sum_divisors_sum == numbers and (sum_divisors - sum_divisors_sum) > 1:
            result += sum_divisors
            result += sum_divisors_sum
    return result

print(amicable(10001))
