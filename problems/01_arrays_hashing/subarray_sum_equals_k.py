"""
Subarray Sum Equals K  (LeetCode #560, Medium)

Problem
    Count the contiguous subarrays of `nums` whose elements sum to `k`.
    Values may be negative.

Example
    nums = [1, 1, 1], k = 2 -> 2

Approach
    Prefix sums: the sum of nums[i..j] equals prefix[j] - prefix[i-1]. So for
    each running sum `s`, the number of subarrays ending here that sum to k is
    the number of earlier prefixes equal to `s - k`. Keep a count map of
    prefixes seen, seeded with {0: 1} for subarrays starting at index 0.
    (A sliding window doesn't work because negatives break monotonicity.)

Complexity
    Time O(n), Space O(n)
"""
from collections import defaultdict
from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    seen = defaultdict(int)
    seen[0] = 1
    running = count = 0
    for num in nums:
        running += num
        count += seen[running - k]
        seen[running] += 1
    return count


def test_subarray_sum():
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1, -1, 0], 0) == 3
    assert subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4
