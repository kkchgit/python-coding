"""
Container With Most Water  (LeetCode #11, Medium)

Problem
    `height[i]` is the height of a vertical line at x = i. Pick two lines that,
    together with the x-axis, hold the most water. Return that area.

Example
    [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49

Approach
    Start with the widest container (both ends). The area is limited by the
    shorter line, so moving the taller line inward can never help: width
    shrinks and the height cap stays the same. Always move the shorter side.

Complexity
    Time O(n), Space O(1)
"""
from typing import List


def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


def test_max_area():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
