#!/usr/bin/python3
"""
min ops
"""


def minOperations(n):
    sum = 0
    i = 2
    if n <= 0:
        return 0
    while n > 1:
        while n % i == 0:
            n = n // i
            sum += i
        i += 1
    return sum
