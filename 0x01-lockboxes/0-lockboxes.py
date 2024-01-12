#!/usr/bin/python3
""" solving lockboxes problem
"""
from typing import List


def canUnlockAll(boxes: List[List]) -> bool:
    """method to determine if all boxes can be open
    Args:
        boxes (List[List]): _description_

    Returns:
        bool: _description_
    """
    if len(boxes) > 0:
        available_keys = {0: 0}
        open = set()
        # add all keys found in first box to available keys
        for x in boxes[0]:
            available_keys[x] = x

        count = 100
        while count > 0:
            for box in range(1, len(boxes)):
                if box in available_keys:
                    for k in boxes[box]:
                        available_keys[k] = k
            count -= 1

        return len(available_keys) == len(boxes)
    return False
