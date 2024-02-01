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
    word = ""
    for x in data:
        word += chr(x)

    try:
        word.encode("utf-8")
        word.encode("ascii")
        return True
    except:
        return False
