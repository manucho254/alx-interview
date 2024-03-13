#!/usr/bin/python3
""" print game """


def isWinner(x, nums):
    """get winner

    Args:
        x (int): round number
        nums (list): an array of n
    """
    maria, ben = 0, 0

    for j in range(x):
        primes = get_primes(nums[j])
        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    return None


def get_primes(n):
    """get primes
    Args:
        n (_type_): range to get primes
    """
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    arr = []
    while p * p <= n:

        # If prime[p] is not
        # changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            arr.append(p)

    return arr
