#!/usr/bin/python3
'''
Determine Winner of game

'''
from typing import List


def is_prime(num):
    '''
    identify if a number is prime
    '''
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def optimal_move(nums):
    '''
    select prime numbers from nums

    '''
    for num in range(2, max(nums) + 1):
        if is_prime(num):
            return num


def isWinner(x, nums):
    '''
    Args:
            x: the number of rounds
            nums: array of n
    Returns None if no winner or Winner is exists
    Assumptions : n and x will not be larger than 10000
                maria always plays first
    '''
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_player = "Maria"

        while n > 1:
            move = optimal_move(range(1, n + 1))

            if move is None:
                break

            n -= move
            current_player = "Ben" if current_player == "Maria" else "Maria"

        if current_player == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
