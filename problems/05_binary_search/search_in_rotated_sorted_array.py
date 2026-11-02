"""
Search in Rotated Sorted Array  (LeetCode #33, Medium)

Problem
    A sorted list of distinct integers has been rotated at an unknown pivot
    (e.g. [0,1,2,4,5,6,7] -> [4,5,6,7,0,1,2]). Return the index of `target`,
    or -1. Must be O(log n).

Example
    nums = [4,5,6,7,0,1,2], target = 0 -> 4

Approach
    Binary search. At any midpoint, at least one half is properly sorted.
    Check whether the target lies within the sorted half's range; if so search
    there, otherwise search the other half.

Complexity
    Time O(log n), Space O(1)
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def test_search():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([3, 1], 1) == 1
    assert search([5, 1, 3], 5) == 0
