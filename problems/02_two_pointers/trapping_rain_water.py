"""
Trapping Rain Water  (LeetCode #42, Hard)

Problem
    Given bar heights of width 1, compute how many units of rain water are
    trapped between the bars.

Example
    [0,1,0,2,1,0,1,3,2,1,2,1] -> 6

Approach
    Water above bar i = min(max height to its left, max height to its right)
    - height[i]. With two pointers, whichever side has the smaller running max
    is the binding constraint, so we can settle that side's bar right away and
    move inward.

Complexity
    Time O(n), Space O(1)
"""
from typing import List


def trap(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water


def test_trap():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([]) == 0
    assert trap([3, 2, 1]) == 0
