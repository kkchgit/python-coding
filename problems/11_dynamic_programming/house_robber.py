"""
House Robber  (LeetCode #198, Medium)

Problem
    Houses along a street hold `nums[i]` money. You can't rob two adjacent
    houses. Return the most money you can take.

Example
    [2, 7, 9, 3, 1] -> 12   (2 + 9 + 1)

Approach
    best(i) = max(best(i-1), best(i-2) + nums[i]): either skip house i, or rob
    it on top of the best up to two houses back. Roll the two previous values
    forward. Follow-up #213 (houses in a circle): run this twice, once without
    the first house and once without the last.

Complexity
    Time O(n), Space O(1)
"""
from typing import List


def rob(nums: List[int]) -> int:
    prev2 = prev1 = 0  # best up to i-2, best up to i-1
    for money in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + money)
    return prev1


def test_rob():
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([2, 1, 1, 2]) == 4
    assert rob([]) == 0
