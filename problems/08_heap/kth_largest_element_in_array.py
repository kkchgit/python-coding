"""
Kth Largest Element in an Array  (LeetCode #215, Medium)

Problem
    Return the kth largest value in an unsorted list (kth in sorted order, not
    kth distinct).

Example
    nums = [3,2,1,5,6,4], k = 2 -> 5

Approach
    Keep a min-heap of size k: it holds the k largest values seen so far, and
    its root is the kth largest. Quickselect averages O(n) and is a good
    follow-up to mention, but its worst case is O(n^2).

Complexity
    Time O(n log k), Space O(k)
"""
import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def test_find_kth_largest():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
    assert find_kth_largest([-1, -1], 2) == -1
