"""
Find Minimum in Rotated Sorted Array  (LeetCode #153, Medium)

Problem
    A sorted list of distinct values was rotated some number of times. Return
    its smallest element in O(log n).

Example
    [3, 4, 5, 1, 2] -> 1

Approach
    Compare the midpoint to the right end. If nums[mid] > nums[hi], the drop
    (and the minimum) is to the right of mid; otherwise the minimum is at mid
    or to its left. Converge until lo == hi.

Complexity
    Time O(log n), Space O(1)
"""
from typing import List


def find_min(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


def test_find_min():
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11
    assert find_min([2, 1]) == 1
