"""
Word Search  (LeetCode #79, Medium)

Problem
    Given a grid of letters and a word, return True if the word can be traced
    through horizontally or vertically adjacent cells, using each cell at most
    once.

Example
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    "ABCCED" -> True,  "ABCB" -> False

Approach
    DFS from every cell. Mark a cell as visited by overwriting it temporarily,
    explore the four neighbors for the next letter, then restore the cell when
    backtracking. A quick letter-count check rules out impossible words early.

Complexity
    Time O(m * n * 4^L) for word length L, Space O(L) recursion
"""
from collections import Counter
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    available = Counter(ch for row in board for ch in row)
    if any(available[ch] < cnt for ch, cnt in Counter(word).items()):
        return False

    def dfs(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
            return False
        saved, board[r][c] = board[r][c], "#"
        found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1)
                 or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
        board[r][c] = saved
        return found

    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))


def _board():
    return [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]


def test_exist():
    assert exist(_board(), "ABCCED")
    assert exist(_board(), "SEE")
    assert not exist(_board(), "ABCB")
    assert not exist([["a"]], "ab")
