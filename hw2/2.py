# Write programm, which find the smallest positive integer X, such that the product of its digits will be equal to N.
# Input: integer N from 9 to 10000.
# Output: integer X.
from math import sqrt, pow


def is_simple(number):
    if number <= 2:
        return True
    dividers = [(number % i) for i in range(2, number)]
    return not (0 in dividers)


def find_dividers(N):
    if N < 2:
        return []
    elif N == 2:
        return [2]
    else:
        for i in range(9, 1, -1):
            if N % i == 0:
                return [i] + find_dividers(N // i)
                break
    return [0]


def find_smallest(N):
    if is_simple(N):
        return 0
    dividers = find_dividers(N)
    if 0 in dividers:
        return 0
    x = 0
    for index, element in enumerate(dividers):
        x = x + element * pow(10, index)
    return int(x)


#function calling
print(find_smallest(288))
