"""
Daily Temperatures  (LeetCode #739, Medium)

Problem
    For each day, return how many days you'd wait for a warmer temperature, or
    0 if no warmer day comes.

Example
    [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]

Approach
    Monotonic decreasing stack of indices still waiting for a warmer day. When
    today is warmer than the day on top, that day's wait is resolved; pop it
    and record the gap. Each index is pushed and popped once.

Complexity
    Time O(n), Space O(n)
"""
from typing import List


def daily_temperatures(temps: List[int]) -> List[int]:
    answer = [0] * len(temps)
    stack = []  # indices with unresolved waits, temps decreasing
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


def test_daily_temperatures():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
    assert daily_temperatures([50, 50]) == [0, 0]
