#!/usr/bin/python3
'''
Module 0-making_change
'''
from typing import List


def makeChange(coins, total):
    '''
    find the minimum number of coins to reach the target
    '''
    # dynamic programing solution
    if total <= 0:
        return 0
        # Initialize an array to store the minimum number
        # of coins for each value from 0 to total
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for total = 0
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for values from coin to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, total cannot be
    # met by any number of coins
    return dp[total] if dp[total] != float('inf') else -1

    # solution with memoization
    # memo = {}  # Dictionary for memoization

    # def minCoins(amount):
    #     if amount in memo:
    #         return memo[amount]
    #     if amount == 0:
    #         return 0
    #     if amount < 0:
    #         return float('inf')

    #     min_coins = float('inf')
    #     for coin in coins:
    #         subproblem = minCoins(amount - coin)
    #         if subproblem != float('inf'):
    #             min_coins = min(min_coins, subproblem + 1)

    #     memo[amount] = min_coins
    #     return min_coins

    # result = minCoins(total)
    # return result if result != float('inf') else -1
