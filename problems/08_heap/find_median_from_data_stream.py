"""
Find Median from Data Stream  (LeetCode #295, Hard)

Problem
    Design a structure with add_num(num) and find_median() that returns the
    median of all numbers added so far.

Example
    add 1, add 2 -> median 1.5; add 3 -> median 2.0

Approach
    Two heaps: a max-heap `low` for the smaller half (stored negated, since
    heapq is a min-heap) and a min-heap `high` for the larger half. Keep
    len(low) == len(high) or one more. The median is then low's top, or the
    average of both tops.

Complexity
    add_num O(log n), find_median O(1), Space O(n)
"""
import heapq


class MedianFinder:
    def __init__(self):
        self.low = []   # max-heap via negation
        self.high = []  # min-heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        # move low's largest to high so every low value <= every high value
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2


def test_median_finder():
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2.0


def test_median_finder_unsorted_input():
    mf = MedianFinder()
    for n in (5, 15, 1, 3):
        mf.add_num(n)
    assert mf.find_median() == 4.0
    mf.add_num(8)
    assert mf.find_median() == 5.0
