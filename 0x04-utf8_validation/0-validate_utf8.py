#!/usr/bin/python3
"""
Main file for testing
"""


def validUTF8(data):
    """Check if valid utf-8
    Args:
        data: array to check if values are valid utf-8
    Return:
        True if data is a valid UTF-8 encoding, else return False
    """

    val = 0
    for x in data:
        x %= 256
        if val > 0:
            if x >> 6 != 0b10:
                return False
            val -= 1
        elif x >> 7 == 0:
            continue
        elif x >> 5 == 0b110:
            val = 1
        elif x >> 4 == 0b1110:
            val = 2
        elif x >> 3 == 0b11110:
            val = 3
        else:
            return False
    return val == 0
