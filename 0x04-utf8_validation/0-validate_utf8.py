#!/usr/bin/python3
"""
validate
"""


def validUTF8(data):
    """
    fun cto validate
    """
    def count_char(num):
        """
        count nums
        """
        mask = 1 << 7
        i = 0
        while num & mask:
            mask >>= 1
            i += 1
        return i
    i = 0
    while i < len(data):
        j = count_char(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            checl = count_char(data[i])
            if checl != 1:
                return False
            i += 1
    return True
