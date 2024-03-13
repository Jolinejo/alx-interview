#!/usr/bin/python3
"""A module that contains n queens solver program.

"""
import sys


def solve(n):
    """solver func.

    Args:
        n(int)
    prints answer"""
    col = set()
    posDiag = set()
    negDiag = set()

    alxAns = []

    def backtrack(r):
        if r == n:
            print(alxAns)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            alxAns.append([r, c])

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            alxAns.remove([r, c])
    backtrack(0)


n = len(sys.argv)
if n != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)
solve(int(sys.argv[1]))
