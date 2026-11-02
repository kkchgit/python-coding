"""
Koko Eating Bananas  (LeetCode #875, Medium)

Problem
    `piles[i]` bananas sit in pile i. Each hour Koko picks one pile and eats up
    to `k` bananas from it. Return the smallest integer speed k that lets her
    finish all piles within `h` hours.

Example
    piles = [3, 6, 7, 11], h = 8 -> 4

Approach
    "Binary search on the answer": the hours needed only go down as k goes up,
    so search k in [1, max(piles)] for the first speed that finishes in time.
    Hours at speed k = sum(ceil(p / k)).

Complexity
    Time O(n log max(piles)), Space O(1)
"""
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
    def hours(k: int) -> int:
        return sum((p + k - 1) // k for p in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo


def test_min_eating_speed():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    assert min_eating_speed([1], 1) == 1
