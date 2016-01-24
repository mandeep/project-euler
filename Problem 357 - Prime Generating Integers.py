from math import sqrt


def is_prime(m):
    if m < 2:
        return False
    for j in range(2, int(sqrt(m)+1)):
        if m % j == 0:
            return False
    return True


def find_divisors(n):
    result = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            result.append(i)
            result.append(n / i)
    return result


def prime_generating(o):
    return all(is_prime(k + (o // k)) for k in find_divisors(o))


result = 0
for number in range(1, 100000000+1):
    if prime_generating(number):
        result += number
print(result)
