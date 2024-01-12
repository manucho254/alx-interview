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
    if not isinstance(boxes, list):
        return False

    if len(boxes) <= 1:
        return True

    available_keys = {0: 0}
    all_boxes = [x for x in range(len(boxes))]
    # add all keys found in first box to available keys
    for x in boxes[0]:
        if x in all_boxes:
            available_keys[x] = x

    # for cases where keys are found in one box
    if list(available_keys.values()) == all_boxes:
        return True

    count = 10
    while count > 0:
        for box in range(1, len(boxes)):
            if box in available_keys.values():
                for k in boxes[box]:
                    if k in all_boxes:
                        available_keys[k] = k
        count -= 1

    return len(available_keys) == len(boxes)
