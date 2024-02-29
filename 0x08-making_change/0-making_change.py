#!/usr/bin/python3


def makeChange(coins, total):
    """making change problem"""
    if total <= 0:
        return 0

    dp = [0] + [float("inf")] * total
    for i in range(1, total + 1):
        for j in coins:
            if i >= j:
                dp[i] = min(dp[i - j] + 1, dp[i])

    return dp[total] if dp[total] != float("inf") else -1
