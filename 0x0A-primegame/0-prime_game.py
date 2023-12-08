#!/usr/bin/python3
'''
Determine Winner of game
'''


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def optimal_move(nums):
    for num in range(2, max(nums) + 1):
        if is_prime(num):
            return num


def isWinner(x, nums):
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
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
