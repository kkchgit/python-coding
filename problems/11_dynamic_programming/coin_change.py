"""
Coin Change  (LeetCode #322, Medium)

Problem
    Given coin denominations (unlimited supply of each) and an `amount`,
    return the fewest coins that make up the amount, or -1 if impossible.

Example
    coins = [1, 2, 5], amount = 11 -> 3   (5 + 5 + 1)

Approach
    Bottom-up DP: dp[a] = fewest coins for amount a = 1 + min(dp[a - c]) over
    coins c <= a. dp[0] = 0, and "infinity" marks unreachable amounts.
    Greedy (always take the biggest coin) fails, e.g. coins [1, 3, 4] with
    amount 6 gives 4+1+1 instead of 3+3.

Complexity
    Time O(amount * len(coins)), Space O(amount)
"""
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1


def test_coin_change():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1, 3, 4], 6) == 2
