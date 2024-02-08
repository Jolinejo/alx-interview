#!/usr/bin/python3
"""
12-pascal_triangle.py
"""


def pascal_triangle(n):
    """pascal trinagle func

    Args:
        n(int): number of line
    """
    if n <= 0:
        return []

    final = []
    final.append([1])
    for row in range(2, n+1):
        list = []
        for i in range(row):
            if i == 0:
                list.append(1)
            elif i == row - 1:
                list.append(1)
            else:
                sum = final[row - 2][i - 1] + final[row - 2][i]
                list.append(sum)
        final.append(list)
    return final
