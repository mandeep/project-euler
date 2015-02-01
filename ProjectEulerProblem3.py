"""
Title: Project Euler - Problem 3: Largest Prime Factor
Date: 2/1/2015

Problem:  The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
n = 600851475143 
i = 2 # 2 is the smallest prime number, hence it is the first iterable.

# If n is not prime, there must be atleast one integer divisor less than the square root of n.
# Another way to write this is the square of i (a factor) must be less than n.
while i ** 2 < n: 
    while n % i == 0: # If n divided by i leaves no remainder, i is a factor.
        n /= i # The largest prime factor is the unknown. Once the initial while loop fails, 
        # the value of n is changed to n divided by its largest factor resulting in the
        # largest prime factor.
    i = i + 1 # Increases i until the square of i is greater than or equal to n.
print n