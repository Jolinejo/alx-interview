#!/usr/bin/python3
"""
coin change module
"""


def makeChange(coins, total):
    """
    returns the fewest number of coins needed to meet a given amount total
    greedy
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    amount = 0
    for coin in coins:
        if total == 0:
            break
        amount += total // coin
        total -= (total // coin) * coin
    return amount if total == 0 else -1
