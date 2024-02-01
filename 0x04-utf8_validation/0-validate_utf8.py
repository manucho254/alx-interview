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
    # word = ""
    sizes = []
    for x in data:
        # word += chr(x)
        sizes.append(len(chr(x).encode('utf-8')))
        
    for i in sizes:
        if i > 1:
            return False
        
    return True
