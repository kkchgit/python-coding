"""
Two Sum  (LeetCode #1, Easy)

Problem
    Given an integer list `nums` and an integer `target`, return the indices of
    the two elements that add up to `target`. Exactly one answer exists and an
    element can't be used twice.

Example
    nums = [2, 7, 11, 15], target = 9  ->  [0, 1]

Approach
    Walk the list once, remembering each value's index in a hash map. For each
    number, the partner we need is `target - num`; if we've already seen it,
    we're done. Checking before inserting stops an element pairing with itself.

Complexity
    Time O(n), Space O(n)
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
