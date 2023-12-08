#!/usr/bin/python3
'''
Determine Winner of game
'''
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime
    game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'

# def is_prime(num):
#     '''
#     check for prime number
#     '''
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True


# def optimal_move(nums):
#     '''
#     select the smallest prime number
#     '''
#     for num in range(2, max(nums) + 1):
#         if is_prime(num):
#             return num


# def isWinner(x, nums):
#     '''
#     Args:
#         x: number of rounds palyed
#         nums: an array of n
#     Returns: name of winner or None
#     Assumptions: n and x will not be larger than 10000
#                 Maria always plays first
#     '''
#     maria_wins = 0
#     ben_wins = 0

#     for n in nums:
#         current_player = "Maria"

#         while n > 1:
#             move = optimal_move(range(1, n + 1))

#             if move is None:
#                 break

#             n -= move
#             current_player = "Ben" if current_player == "Maria" else "Maria"

#         if current_player == "Maria":
#             ben_wins += 1
#         else:
#             maria_wins += 1

#     if maria_wins > ben_wins:
#         return "Maria"
#     elif maria_wins < ben_wins:
#         return "Ben"
#     else:
#         return None
