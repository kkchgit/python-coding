"""
Longest Increasing Subsequence  (LeetCode #300, Medium)

Problem
    Return the length of the longest strictly increasing subsequence of `nums`
    (elements in order, not necessarily adjacent).

Example
    [10, 9, 2, 5, 3, 7, 101, 18] -> 4   (2, 3, 7, 101)

Approach
    Patience sorting: tails[i] is the smallest possible tail of an increasing
    subsequence of length i + 1. For each number, binary search for the first
    tail >= it and replace that tail (or append if it's larger than all).
    The length of `tails` is the answer. The simpler O(n^2) DP, where dp[i] =
    1 + max(dp[j]) for j < i with nums[j] < nums[i], is included too.

Complexity
    Time O(n log n), Space O(n)
"""
from bisect import bisect_left
from typing import List


def length_of_lis(nums: List[int]) -> int:
    tails: List[int] = []
    for num in nums:
        i = bisect_left(tails, num)
        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num
    return len(tails)


def length_of_lis_quadratic(nums: List[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp, default=0)


def test_length_of_lis():
    for fn in (length_of_lis, length_of_lis_quadratic):
        assert fn([10, 9, 2, 5, 3, 7, 101, 18]) == 4
        assert fn([0, 1, 0, 3, 2, 3]) == 4
        assert fn([7, 7, 7, 7]) == 1
        assert fn([]) == 0
