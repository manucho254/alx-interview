#!/usr/bin/python3
""" coin change problem 
"""


def makeChange(coins, total):
    """making change problem"""
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for j in coins:
            if i >= j:
                dp[i] = min(dp[i - j] + 1, dp[i])

    return dp[total] if dp[total] != total + 1 else -1
