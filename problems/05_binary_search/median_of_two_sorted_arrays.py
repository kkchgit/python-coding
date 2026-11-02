"""
Median of Two Sorted Arrays  (LeetCode #4, Hard)

Problem
    Given two sorted lists, return the median of their combined values in
    O(log(min(m, n))) time.

Example
    [1, 3] and [2] -> 2.0;   [1, 2] and [3, 4] -> 2.5

Approach
    Binary search a partition of the shorter list A. If we take i elements from
    A, we must take j = half - i from B so the left side has half the values.
    The partition is correct when A[i-1] <= B[j] and B[j-1] <= A[i]; then the
    median comes from the boundary values. Otherwise move i left or right.
    Infinity sentinels handle empty sides.

Complexity
    Time O(log(min(m, n))), Space O(1)
"""
from typing import List


def find_median_sorted_arrays(a: List[int], b: List[int]) -> float:
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    half = (m + n + 1) // 2
    lo, hi = 0, m
    inf = float("inf")

    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        a_left = a[i - 1] if i > 0 else -inf
        a_right = a[i] if i < m else inf
        b_left = b[j - 1] if j > 0 else -inf
        b_right = b[j] if j < n else inf

        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
    raise ValueError("inputs must be sorted")


def test_find_median_sorted_arrays():
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert find_median_sorted_arrays([], [1]) == 1.0
    assert find_median_sorted_arrays([0, 0], [0, 0]) == 0.0
    assert find_median_sorted_arrays([1, 4, 7, 9], [2, 3, 5]) == 4.0
