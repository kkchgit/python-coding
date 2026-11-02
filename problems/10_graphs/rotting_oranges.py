"""
Rotting Oranges  (LeetCode #994, Medium)

Problem
    Grid cells are 0 (empty), 1 (fresh orange) or 2 (rotten). Each minute,
    fresh oranges next to a rotten one (up/down/left/right) become rotten.
    Return the minutes until no fresh orange remains, or -1 if that never
    happens.

Example
    [[2,1,1],[1,1,0],[0,1,1]] -> 4

Approach
    Multi-source BFS: put every rotten orange in the queue at time 0 and
    expand level by level, where each level is one minute. Count fresh oranges
    up front; if any are left at the end, some were unreachable.

Complexity
    Time O(m * n), Space O(m * n)
"""
from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue, fresh = deque(), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    while queue and fresh:
        minutes += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
    return -1 if fresh else minutes


def test_oranges_rotting():
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert oranges_rotting([[0, 2]]) == 0
    assert oranges_rotting([[0]]) == 0
