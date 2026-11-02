"""
Best Time to Buy and Sell Stock  (LeetCode #121, Easy)

Problem
    `prices[i]` is a stock's price on day i. Buy once and sell once on a later
    day to maximize profit. Return the max profit, or 0 if none is possible.

Example
    [7, 1, 5, 3, 6, 4] -> 5   (buy at 1, sell at 6)

Approach
    Track the cheapest price seen so far. Each day, the best sale ending today
    is price - cheapest. Keep the maximum.

Complexity
    Time O(n), Space O(1)
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    cheapest = float("inf")
    best = 0
    for price in prices:
        cheapest = min(cheapest, price)
        best = max(best, price - cheapest)
    return best


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([2, 4, 1]) == 2
    assert max_profit([]) == 0
