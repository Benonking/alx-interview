#!/usr/bin/python3
"""
Module 0-pascal_triangle
Methods:
  pascal_triangle: return a list of ints representing pascals tringle of size n
"""


def pascal_triangle(n: int):
    '''
    Method definition
    '''
    if (n <= 0):
        return []
    tri = [[1]]

    for i in range(n - 1):  # num of rows
        temp = [0] + tri[-1] + [0]  # append 0's at end of prev row
        next_row = []  # next row
        for j in range(len(tri[-1]) + 1):
            next_row.append(temp[j] + temp[j + 1])
        tri.append(next_row)
    return tri
