#!/usr/bin/python3
"""
 Island perimeter problem
"""


def island_perimeter(grid):
    """Get island perimeter

    Args:
        grid (_type_): square grid
    """

    if not grid:
        return 0

    m, n, Perimeter = len(grid), len(grid[0]), 0

    for i in range(m):
        for j in range(n):
            Perimeter += 4 * grid[i][j]
            if i > 0:
                Perimeter -= grid[i][j] * grid[i - 1][j]
            if i < m - 1:
                Perimeter -= grid[i][j] * grid[i + 1][j]
            if j > 0:
                Perimeter -= grid[i][j] * grid[i][j - 1]
            if j < n - 1:
                Perimeter -= grid[i][j] * grid[i][j + 1]

    return Perimeter
