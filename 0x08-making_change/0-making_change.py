#!/usr/bin/python3
"""
coin change module
"""
import sys


def minCoinsutil(coins, V, dp):
    """
    utility function
    """
    if V == 0:
        return 0
    if V < 0:
        return -1
    if dp[V] != -1:
        return dp[V]
    res = sys.maxsize

    for i in range(len(coins)):
        if coins[i] <= V:
            sub_res = minCoinsutil(coins, V-coins[i], dp)

            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1
            if sub_res == -1:
                return -1

    dp[V] = res
    return res


def makeChange(coins, total):
    """
    returns  the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    dp = [-1] * (total + 1)

    tot = minCoinsutil(coins, total, dp)
    if tot == sys.maxsize:
        return -1
    return tot
