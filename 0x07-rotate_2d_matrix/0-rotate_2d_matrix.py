#!/usr/bin/python3
'''
Rotate 2d matrix by 90 degrees
'''


def rotate_2d_matrix(matrix):
    '''
    Rotate 2d matrix by 90 degrees clockwise
    Method: nested loops
    '''
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp


'''
Method 2: transpose

def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
'''
