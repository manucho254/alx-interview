#!/usr/bin/python3
""" solving lockboxes problem
"""
from typing import List


def add_to_dict(dct: dict, arr: List) -> dict:
    """Add items to dictionary
    Args:
        dct (dict): dictionary to add values
        arr (List): values to add to dict
    Return:
        dict: a dictionary
    """
    for x in arr:
        if x > 0:  # don't need keys for box 0 since its open
            dct[x] = x

    return dct


def canUnlockAll(boxes: List[List]) -> bool:
    """method to determine if all boxes can be open
    Args:
        boxes (List[List]): _description_

    Returns:
        bool: _description_
    """
    if len(boxes) > 0:
        available_keys = {}
        opened_boxes = {0: True}

        # set all boxes open state to false
        for box in range(1, len(boxes)):
            opened_boxes[box] = False

        # add all keys found in first box to available keys
        for x in boxes[0]:
            available_keys[x] = x

        while len(available_keys) > 0:
            for box in range(1, len(boxes)):
                # remove key from available keys if box is already open
                if opened_boxes.get(box) and available_keys.get(box):
                    del available_keys[box]
                # mark box as open and remove key from available keys
                # also add all keys in box to available keys
                if available_keys.get(box) and not opened_boxes.get(box):
                    opened_boxes[box] = True
                    available_keys = add_to_dict(available_keys, boxes[box])
                    del available_keys[box]

        return all(opened_boxes.values())
    return False
