#!/usr/bin/python3
""" Rotate a 2D matrix """

from typing import List


def rotate_2d_matrix(matrix: List[List]) -> None:
    """Rotate a 2d matrix by 90 degrees
    Args:
        matrix (List[List]): _description_
    """

    idx = 0
    length = len(matrix)

    while idx < length:
        tmp = []
        for x in range(length):
            tmp.append(matrix[x][idx])

        tmp.reverse()
        matrix.append(tmp)
        idx += 1

    # reverse matrix
    matrix.reverse()

    # remove length items at the end
    for _ in range(length):
        matrix.pop()

    # reverse array again
    matrix.reverse()
