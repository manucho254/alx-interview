#!/usr/bin/python3


def makeChange(coins, total):
    """Get minimum number of coins
    Args:
        coins (_type_): coins array
        total (_type_): total amount
    Return:
        int: minimum number of coins if found else -1
    """
    if total <= 0:
        return 0

    cache = {}
    def dp(curAmt):
        if curAmt in cache:
            return cache[curAmt]
        elif curAmt > total:
            return float("inf")
        elif curAmt == total:
            return 0

        cache[curAmt] = min(dp(curAmt + x) + 1 for x in coins)
        return cache[curAmt]

    ans = dp(0)
    return ans if ans != float("inf") else -1
