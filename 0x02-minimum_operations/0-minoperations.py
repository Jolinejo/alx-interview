#!/usr/bin/python3
"""
min ops
"""

import math as mt

maxn = 100001

primes = [i for i in range(maxn)]


def sieve():

    for i in range(4, maxn, 2):
        primes[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(maxn))):
        if primes[i] == i:
            for j in range(i * i, maxn, i):
                if primes[j] == j:
                    primes[j] = i


sieve()


def get_factors(n):
    ret = []
    while n != 1:
        ret.append(primes[n])
        n = n // primes[n]

    return ret


def minOperations(n):
    listi = get_factors(n)
    sum = 0
    if n < 0:
        return 0
    for i in listi:
        sum += i
    return sum
