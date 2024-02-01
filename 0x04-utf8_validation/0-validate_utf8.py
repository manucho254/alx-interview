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

    try:
        for x in data:
            char = chr(x)
            new_val = char.encode("utf-8")
            new_val.decode("ascii")

        return True

    except UnicodeDecodeError:
        return False
