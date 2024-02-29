#!/usr/bin/python3
"""
module that finds the solution of fewest number
of coins needed to meet a given amount
"""


def makeChange(coins, total):
    """ function that finds the solution """
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    count = 0
    summ = 0
    rest = total
    flag = False
    while(rest > 0):
        flag = False
        for i in range(len(coins)):
            amount = int(rest / coins[i])
            if amount:
                flag = True
                summ += amount * coins[i]
                count += amount
                rest -= (amount * coins[i])
        if not flag:
            return -1
    return count if summ == total else -1
