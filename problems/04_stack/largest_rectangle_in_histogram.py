"""
Largest Rectangle in Histogram  (LeetCode #84, Hard)

Problem
    Given bar heights of width 1, return the area of the largest rectangle that
    fits entirely inside the histogram.

Example
    [2, 1, 5, 6, 2, 3] -> 10   (bars 5 and 6, height 5, width 2)

Approach
    Monotonic increasing stack of indices. When a shorter bar arrives, every
    taller bar on the stack can't extend further right, so pop it and compute
    its rectangle: its height times the distance between the current index and
    the new stack top (its left boundary). A sentinel 0 at the end flushes the
    stack.

Complexity
    Time O(n), Space O(n)
"""
from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    stack = []  # indices with increasing heights
    best = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            best = max(best, height * (i - left - 1))
        stack.append(i)
    return best


def test_largest_rectangle_area():
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_area([2, 4]) == 4
    assert largest_rectangle_area([1, 1, 1, 1]) == 4
    assert largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]) == 12
    assert largest_rectangle_area([]) == 0
