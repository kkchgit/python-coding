"""
Meeting Rooms II  (LeetCode #253, Medium)

Problem
    Given meeting time intervals [start, end), return the minimum number of
    conference rooms needed so that no two overlapping meetings share a room.

Example
    [[0,30],[5,10],[15,20]] -> 2

Approach
    Sort meetings by start and keep a min-heap of end times for rooms in use.
    If the earliest-ending room is free by the time the next meeting starts,
    reuse it (pop); then push the new meeting's end. The heap's peak size is
    the answer. An alternative: sort starts and ends separately and sweep
    with two pointers.

Complexity
    Time O(n log n), Space O(n)
"""
import heapq
from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    ends: List[int] = []
    for start, end in sorted(intervals):
        if ends and ends[0] <= start:
            heapq.heappop(ends)
        heapq.heappush(ends, end)
    return len(ends)


def test_min_meeting_rooms():
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([[1, 5], [2, 6], [3, 7], [4, 8]]) == 4
    assert min_meeting_rooms([[1, 5], [5, 10]]) == 1
    assert min_meeting_rooms([]) == 0
