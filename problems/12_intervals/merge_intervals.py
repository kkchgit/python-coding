"""
Merge Intervals  (LeetCode #56, Medium)

Problem
    Merge all overlapping intervals and return the non-overlapping result.

Example
    [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]

Approach
    Sort by start. Walk through, and if an interval starts before (or exactly
    when) the last merged one ends, extend that one's end; otherwise start a
    new merged interval.

Complexity
    Time O(n log n), Space O(n) for the output
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    merged: List[List[int]] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def test_merge():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert merge([[5, 6], [1, 2]]) == [[1, 2], [5, 6]]
    assert merge([]) == []
