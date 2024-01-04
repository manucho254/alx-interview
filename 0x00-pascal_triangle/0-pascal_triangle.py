#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n: int):
    """ function to create the pascal triangle
        Args:
            n (_type_): number of rows
        Return: an array of integers
    """
    triangle = []
    for x in range(n):
        tmp = []
        if x == 0:
            tmp.append(1)
        elif x == 1:
            tmp = triangle[0].copy()
            tmp.append(1)
        else:
            prev = triangle[x - 1]
            for i in range(len(prev) - 1):
                two_sum = prev[i] + prev[i + 1]
                tmp.append(two_sum)
            tmp.insert(0, 1)
            tmp.append(1)
        triangle.append(tmp)

    return triangle
