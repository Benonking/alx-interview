#!/usr/bin/python3
'''
Module 0-minOperations

'''


def minOperations(n):
    '''calculate the min operations to reach n '''
    count = 0
    root = 2

    if n < 2:
        return 0
    while root <= n+1:
        while n % root == 0:
            count += root
            n /= root
        root += 1
    return count
