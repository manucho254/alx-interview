#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__("0-island_perimeter").island_perimeter
numIslands = __import__("test").numIslands

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    print(island_perimeter(grid))
    print(numIslands(grid))
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    print(island_perimeter(grid))
    print(numIslands(grid))
