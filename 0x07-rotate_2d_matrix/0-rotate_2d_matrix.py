#!/usr/bin/python3
"""
Matrix rotation module
"""


def rotate_2d_matrix(matrix):
    """
    recives a matrix and rotates it 90 degrees clockwise
    """
    n = len(matrix)
    rotated = [[matrix[n-1-j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated[i][j]
