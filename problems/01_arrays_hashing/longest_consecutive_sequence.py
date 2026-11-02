"""
Longest Consecutive Sequence  (LeetCode #128, Medium)

Problem
    Given an unsorted list of integers, return the length of the longest run of
    consecutive values (e.g. 1,2,3,4). Must run in O(n).

Example
    [100, 4, 200, 1, 3, 2] -> 4   (the run 1,2,3,4)

Approach
    Put everything in a set. Only start counting from numbers that begin a run
    (x - 1 not in the set), then step upward while x + 1 exists. Each number is
    visited at most twice, so the total work is linear.

Complexity
    Time O(n), Space O(n)
"""
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    values = set(nums)
    best = 0
    for x in values:
        if x - 1 not in values:  # x starts a run
            length = 1
            while x + length in values:
                length += 1
            best = max(best, length)
    return best


def test_longest_consecutive():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1, 2, 0, 1]) == 3
