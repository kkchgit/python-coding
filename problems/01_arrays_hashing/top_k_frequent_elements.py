"""
Top K Frequent Elements  (LeetCode #347, Medium)

Problem
    Return the `k` values that appear most often in `nums`. The answer is unique;
    order doesn't matter.

Example
    nums = [1,1,1,2,2,3], k = 2 -> [1, 2]

Approach
    Bucket sort by frequency: count each value, then put values into buckets
    indexed by their count (a count can be at most n). Sweep buckets from high
    to low until we've collected k values. Beats the O(n log n) sort.

Complexity
    Time O(n), Space O(n)
"""
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


def test_top_k_frequent():
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 5, 5, 5, 6, 6, 6, 6], 2)) == [5, 6]
