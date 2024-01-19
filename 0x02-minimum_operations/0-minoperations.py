#!/usr/bin/python3
""" solving minimum operations problem
"""
from typing import List


def minOperations(n: int) -> int:
    """
    Args:
        n (_type_): _description_
    Return:
        sum of all prime factors
    """
    if n <= 1:
        return 0

    operations = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            operations.append(divisor)
            n = n / divisor
        else:
            divisor += 1

    return sum(operations)
