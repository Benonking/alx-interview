#!usr/bin/python3
"""
Module 0-pascal_triangle
Methods:
  pascal_triangle: return a list of ints representing pascals tringle of size n
"""


def pascal_triangle(n: int):
    '''
    Metnod definition
    '''
    tri = [[1]]
    if n <= 0:
        return []
    for i in range(n - 1):
        temp = [0] + tri[-1] + [0]
        row = []
        for j in range(len(tri[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        tri.append(row)
    return tri
