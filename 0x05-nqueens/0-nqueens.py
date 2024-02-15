#!/usr/bin/python3

""" solving the n-qeens problem
"""
import sys


def get_n() -> int:
    """get the value of n from command line argument.
    Return:
          n as an integer
    """
    args = sys.argv

    # if len(args) == 1, it means that the second argument is missing.
    if len(args) == 1:
        print("Usage: nqueens N")
        sys.exit(1)

    if not args[1].isnumeric():
        print("N must be a number")
        sys.exit(1)

    n = int(args[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


n = get_n()


class Nqueens:
    """class Nqeens"""

    col, pos_diag, neg_diag = set(), set(), set()
    board = [["0"] * n for _ in range(n)]

    res = []

    def backtrack(self, start):
        """backtracking function to get all possible positions
        Args:
            start: starting position of the function
        """
        if start == n:  # base case because this will be a recursive function
            copy = ["".join(row) for row in self.board]
            self.res.append(copy)
            return

        for c in range(n):
            checks = (start + c) in self.pos_diag
            if c in self.col or checks or (start - c) in self.neg_diag:
                continue

            self.col.add(c)
            self.pos_diag.add(start + c)
            self.neg_diag.add(start - c)
            self.board[start][c] = "Q"

            self.backtrack(start + 1)  # recus

            # remove all previos records
            self.col.remove(c)
            self.pos_diag.remove(start + c)
            self.neg_diag.remove(start - c)
            self.board[start][c] = "0"


queens = Nqueens()
queens.backtrack(0)
res = queens.res

for x in res:
    tmp = []
    for i, val in enumerate(x):
        tmp.append([i, val.index("Q")])
    print(tmp)
