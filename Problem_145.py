def is_reversible(number):
    reversed_sum = int(number) + int(str(number)[::-1])
    reversible = [int(x) for x in str(reversed_sum)]
    return all(x % 2 != 0 for x in reversible)

count_of_reversibles = 0
for i in range(1, 1000):
    if is_reversible(i):
        count_of_reversibles += 1
print(count_of_reversibles)
