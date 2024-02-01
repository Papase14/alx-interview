#!/usr/bin/python3
"""
Make a change
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make a given total.

    Parameters:
    - coins (list): A list of coin denominations available.
    - total (int): The target total amount.

    Returns:
    - int: The minimum number of coins needed to make the total amount.
    Returns -1 if it is not possible to make the total amount with the given coins.
    """
    if total < 0:
        return 0
    if total == 0:
        return 0

    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1
