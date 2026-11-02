"""
Number of Islands  (LeetCode #200, Medium)

Problem
    In a grid of "1" (land) and "0" (water), count the islands: groups of land
    connected horizontally or vertically.

Example
    ["11000","11000","00100","00011"] -> 3

Approach
    Scan every cell. When you find unvisited land, that's a new island: flood
    it with BFS, marking each cell as water so it isn't counted again. BFS with
    an explicit queue avoids recursion limits on large grids.

Complexity
    Time O(m * n), Space O(min(m, n)) for the BFS queue
"""
from collections import deque
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue
            count += 1
            grid[r][c] = "0"
            queue = deque([(r, c)])
            while queue:
                cr, cc = queue.popleft()
                for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))
    return count


def _grid(rows):
    return [list(r) for r in rows]


def test_num_islands():
    assert num_islands(_grid(["11110", "11010", "11000", "00000"])) == 1
    assert num_islands(_grid(["11000", "11000", "00100", "00011"])) == 3
    assert num_islands(_grid(["0"])) == 0
    assert num_islands(_grid(["101", "010", "101"])) == 5
